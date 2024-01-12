import unittest
from unittest.mock import patch, MagicMock
import os, sys
import json
# This should point to the directory containing the 'utils' module
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_dir)

import utils

class TestGptChatAndExecuteFunctionBank(unittest.TestCase):
    """
    A class for testing the `gpt_chat_and_execute_function_bank` function.

    Methods:
    --------
    test_gpt_chat_and_execute_function_bank_no_function_call: Test case where the function call is not present in the response.
    test_gpt_chat_and_execute_function_bank_with_function_call: Test case where the function call is present in the response.
    test_gpt_chat_and_execute_function_bank_api_error: Test case where the API returns an error.
    """
    @patch('requests.post')
    def test_gpt_chat_and_execute_function_bank_no_function_call(self, mock_post):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {"message": {"role": "assistant", "content": "Hello, how can I assist you today?"}}
            ]
        }
        mock_post.return_value = mock_response

        question = "Hello, AI!"
        context = None
        model = "gpt-3.5-turbo-0613"
        function_call = 'auto'

        response, context = utils.gpt_chat_and_execute_function_bank(question, context, model, function_call)

        self.assertEqual(response, "Hello, how can I assist you today?")
        self.assertEqual(len(context), 1)

    @patch('requests.post')
    def test_gpt_chat_and_execute_function_bank_with_function_call(self, mock_post):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {"message": {"role": "assistant", "content": "Hello, how can I assist you today?", "function_call": {"name": "test_function", "arguments": "{}"}}}
            ]
        }
        mock_post.return_value = mock_response

        question = "Hello, AI!"
        context = None
        model = "gpt-3.5-turbo-0613"
        function_call = 'auto'

        with self.assertRaises(ValueError):
            utils.gpt_chat_and_execute_function_bank(question, context, model, function_call)

    @patch('requests.post')
    def test_gpt_chat_and_execute_function_bank_api_error(self, mock_post):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.json.side_effect = Exception("API Error")
        mock_post.return_value = mock_response

        question = "Hello, AI!"
        context = None
        model = "gpt-3.5-turbo-0613"
        function_call = 'auto'

        response, context = utils.gpt_chat_and_execute_function_bank(question, context, model, function_call)

        self.assertEqual(response, None)
        self.assertEqual(len(context), 1)

if __name__ == '__main__':
    unittest.main()