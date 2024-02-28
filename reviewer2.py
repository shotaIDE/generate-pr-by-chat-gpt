# coding: utf-8

from ai import chat_with_function_calling_loop
from atlassian import GetConfluencePage, GetJiraIssue
from github import ListPullRequestFiles


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
            confluence_page_id: str,
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

        self._get_confluence_page = GetConfluencePage(
            domain=atlassian_domain,
            id=confluence_page_id,
            api_login_email=jira_api_login_email,
            api_token=jira_api_token,
        )


    def work(self) -> str:
        print('---------------------------------')
        print(f'{self._actor_name}: start to work')

        system_message = self.prompt

        pull_request_files = self._list_pull_request_files.execute_and_generate_message({})
        jira_issue = self._get_jira_issue.execute_and_generate_message({})
        confluence_page = self._get_confluence_page.execute_and_generate_message({})
        user_message = (
            'GitHub diff:\n'
            f'{pull_request_files}\n'
            '-\n'
            'Jira details:\n'
            f'{jira_issue}\n'
            '-\n'
            'Confluence page:\n'
            f'{confluence_page}'
        )

        comment = chat_with_function_calling_loop(
            system_message=system_message,
            user_message=user_message,
            actor_name=self._actor_name,
        )

        print(f'{self._actor_name}: {comment}')
        return comment
