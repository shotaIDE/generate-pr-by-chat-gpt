# coding: utf-8

from ai import chat_with_function_calling_loop
from atlassian import GetConfluencePage


class SpecificationsReviewer:
    _actor_name = 'Reviewer'

    def __init__(
            self,
            prompt: str,
            atlassian_domain: str,
            jira_api_login_email: str,
            jira_api_token: str,
            confluence_page_id: str,
    ):
        self.prompt = prompt

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

        confluence_page = self._get_confluence_page.execute_and_generate_message({})
        user_message = (
            'Specifications:\n'
            f'{confluence_page}'
        )

        comment = chat_with_function_calling_loop(
            system_message=system_message,
            user_message=user_message,
            actor_name=self._actor_name,
        )

        print(f'{self._actor_name}: {comment}')
        return comment
