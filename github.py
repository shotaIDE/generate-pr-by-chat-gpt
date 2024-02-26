# coding: utf-8


import requests

__GITHUB_API_ORIGIN = 'https://api.github.com'


class ListPullRequestFiles:
    definition = {
        "name": 'ListPullRequestFiles',
        "description": "Lists the files in a specified pull request.",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    }

    def __init__(self, owner: str, repository: str, number: str, token: str) -> None:
        self._owner = owner
        self._repository = repository
        self._number = number
        self._token = token

    def execute_and_generate_message(self, args) -> str:
        path = f'/repos/{self._owner}/{self._repository}/pulls/{self._number}/files'
        url = f'{__GITHUB_API_ORIGIN}{path}'
        accept = 'application/vnd.github.diff'

        headers = {
            'Accept': accept,
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.get(url, headers=headers)

        return response.text
