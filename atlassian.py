# coding: utf-8


import json

import requests
from requests.auth import HTTPBasicAuth


class GetJiraIssue:
    definition = {
        "name": 'GetJiraIssue',
        "description": "Returns the details for an issue.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    }

    def __init__(self, domain: str, key: str, api_login_email: str, api_token: str) -> None:
        self._domain = domain
        self._key = key
        self._email = api_login_email
        self._token = api_token

    def execute_and_generate_message(self, args) -> str:
        path = f'/rest/api/3/issue/{self._key}'
        url = f'https://{self._domain}{path}'

        auth = HTTPBasicAuth(self._email, self._token)

        accept = 'application/json'
        headers = {
            'Accept': accept,
        }

        response = requests.get(url=url, headers=headers, auth=auth)

        json_response = response.json()

        summary = json_response['fields']['summary']
        description = json_response['fields']['description']

        summary_json = {
            "summary": summary,
            "description": description
        }
        json_text = json.dumps(summary_json, ensure_ascii=False)

        return json_text

class GetConfluencePage:
    definition = {
        "name": 'GetConfluencePage',
        "description": "Returns a specific page.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    }

    def __init__(self, domain: str, id: str, api_login_email: str, api_token: str) -> None:
        self._domain = domain
        self._id = id
        self._email = api_login_email
        self._token = api_token

    def execute_and_generate_message(self, args) -> str:
        path = f'/wiki/api/v2/pages/{self._id}?body-format=storage'
        url = f'https://{self._domain}{path}'

        auth = HTTPBasicAuth(self._email, self._token)

        accept = 'application/json'
        headers = {
            'Accept': accept,
        }

        response = requests.get(url=url, headers=headers, auth=auth)

        json_response = response.json()

        title = json_response['title']
        body = json_response['body']['storage']['value']

        summary_json = {
            "title": title,
            "body": body
        }
        json_text = json.dumps(summary_json, ensure_ascii=False)

        return json_text
