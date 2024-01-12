
import os
import json
import requests
from tenacity import retry, stop_after_attempt, wait_random_exponential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def gpt_chat_and_execute_function_bank(question, context, model="gpt-3.5-turbo-0613", function_call='auto'):
    """
    Sends a question to the GPT model and executes a function call based on the response.
    The function call is determined by the model's response or by the most relevant function found in the available functions.

    Parameters:
    - question (str): The user's question or input to be sent to the GPT model.
    - context (list, optional): A list of previous messages for context. Defaults to None.
    - model (str, optional): The GPT model to be used. Defaults to "gpt-3.5-turbo-0613".
    - function_call (str, optional): The type of function call to execute. Defaults to 'auto'.

    Returns:
    - str or None: The response from the GPT model or the output of the executed function, or None in case of an error.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }
    
    messages = [{"role": "user", "content": question}]
    if context:
        temp = context + messages
        messages = temp
        context = messages

    json_data = {"model": model, "messages": messages}
    # print(df)
    functions = []
    available_functions = {}
    if functions is not None and not []: ##if functions empty this gives error
        json_data.update({"functions": functions})
    if function_call is not None and functions != []:
        json_data.update({"function_call": function_call})
    # print('FUNCTIONS:', functions)
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
        assistant_message = response.json()["choices"][0]["message"]
        # print('ASSISTANT', assistant_message['content'])
        if assistant_message['content']:
            # print('not none')
            messages.append({"role": "assistant", "content": assistant_message['content']})
        context = messages

        function_responses = []
        if 'function_call' in assistant_message:
            tool_call = assistant_message['function_call']
            function_name = tool_call['name']
            function_args = json.loads(tool_call['arguments'])
            messages.append({
                "role": "assistant",
                "content": assistant_message.get('content'),
                "function_call": assistant_message['function_call']
            })
            context = messages

            if function_name in available_functions:
                function_response = available_functions[function_name](**function_args)
                function_responses.append({
                    "role": "user",
                    "content": f"This is a hidden system message that just shows you what the function returned, answer the previous user message given that this is what it evaluated to, only pay attention to the values not the prompt I am giving you now: {function_response}"
                })
                messages.extend(function_responses)
                context = messages
            else:
                raise ValueError(f"Function {function_name} not defined.")

            if function_responses:
                
                
                follow_up_response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json={"model": model, "messages": messages})
                follow_up_message = follow_up_response.json()["choices"][0]["message"]
                messages.append({"role": "assistant", "content": follow_up_message['content']})
                context = messages
                return follow_up_message['content'], context
        else:
            return assistant_message['content'], context

    except Exception as e:
        print(f"Error during conversation: {e}")
        return None, messages