import unittest
from unittest.mock import patch, MagicMock
import os
import json
from .. import utils

class TestGptChatAndExecuteFunctionBank(unittest.TestCase):
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