# coding: utf-8


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
        url = f'{self._domain}{path}'

        auth = HTTPBasicAuth(self._email, self._token)

        accept = 'application/json'
        headers = {
            'Accept': accept,
        }

        response = requests.get(url=url, headers=headers, auth=auth)

        return response.text
