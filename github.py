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
        self.owner = owner
        self.repository = repository
        self.number = number
        self.token = token

    def execute_and_generate_message(self, args) -> str:
        url = f'{__GITHUB_API_ORIGIN}/repos/{self.owner}/{self.repository}/pulls/{self.number}/files'
        accept = 'application/vnd.github.diff'

        headers = {
            'Accept': accept,
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.get(url, headers=headers)

        return response.text
