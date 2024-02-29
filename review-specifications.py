# coding: utf-8

import os

from specificationsreviewer import SpecificationsReviewer


def work():
    prompt_path = os.environ.get('SPECIFICATIONS_REVIEWER_PROMPT_PATH')

    atlassian_domain = os.environ.get('ATLASSIAN_DOMAIN')
    jira_api_login_email = os.environ.get('JIRA_API_LOGIN_EMAIL')
    jira_api_token = os.environ.get('JIRA_API_TOKEN')

    with open(prompt_path, encoding='utf-8') as f:
        reviewer_prompt = f.read()

    confluence_page_id = input('Please input the Confluence page ID: ')

    reviewer = SpecificationsReviewer(
        prompt=reviewer_prompt,
        atlassian_domain=atlassian_domain,
        jira_api_login_email=jira_api_login_email,
        jira_api_token=jira_api_token,
        confluence_page_id=confluence_page_id,
    )

    reviewer.work()


if __name__ == "__main__":
    work()
