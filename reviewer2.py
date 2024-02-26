# coding: utf-8

from ai import chat_with_function_calling_loop
from github import ListPullRequestFiles
from jira import GetJiraIssue


class Reviewer2:
    _actor_name = 'Reviewer'

    def __init__(
            self,
            prompt: str,
            github_owner: str,
            github_repository: str, 
            github_number: str, 
            github_token: str,
            atlassian_domain: str,
            jira_key: str,
            jira_api_login_email: str,
            jira_api_token: str,
    ):
        self.prompt = prompt

        self._list_pull_request_files = ListPullRequestFiles(
            owner=github_owner,
            repository=github_repository,
            number=github_number,
            token=github_token,
        )

        self._get_jira_issue = GetJiraIssue(
            domain=atlassian_domain,
            key=jira_key,
            api_login_email=jira_api_login_email,
            api_token=jira_api_token,
        )


    def work(self) -> str:
        print('---------------------------------')
        print(f'{self._actor_name}: start to work')

        system_message = self.prompt

        comment = chat_with_function_calling_loop(
            messages=system_message,
            functions=[
                self._list_pull_request_files,
                self._get_jira_issue,
            ],
            actor_name=self._actor_name,
        )

        print(f'{self._actor_name}: {comment}')
        return comment
