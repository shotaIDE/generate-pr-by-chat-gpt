# coding: utf-8

import json
import os

import openai


def chat_with_function_calling_loop(system_message, user_message, functions=None, actor_name: str=None):
    openai.organization = os.environ.get('OPENAI_ORGANIZATION')
    openai.api_key = os.environ.get('OPENAI_TOKEN')
    model_name = os.environ.get('OPENAI_MODEL_NAME')

    iteration = 0

    messages = []
    if system_message is not None:
        messages.append({
            "role": "system",
            "content": system_message,
        })
    if user_message is not None:
        messages.append({
            "role": "user",
            "content": user_message,
        })

    function_definitions = [function.definition for function in functions] if functions is not None else None
    function_call = 'auto' if functions is not None else None

    while iteration < 30:
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=messages,
            functions=function_definitions,
            function_call=function_call,
        )

        response_message = response["choices"][0]["message"]

        if response_message.get("function_call"):
            function_call = response_message["function_call"]
            function_name = function_call["name"]
            function = [
                function
                for function in functions
                if function.definition['name'] == function_name
            ][0]
            function_arguments = json.loads(function_call["arguments"])

            print(f'System requires function call: "{function_name}" with arguments: {function_arguments}')

            function_response = function.execute_and_generate_message(
                args=function_arguments
            )
            
            print('Function response\n')
            print(function_response)

            messages.append(response_message)

            messages.append({
                "role": "function",
                "name": function_name,
                "content": function_response,
            })

        else:
            break

        iteration += 1

    content = response_message.get('content')
    return content
