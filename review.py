# coding: utf-8

import os

from reviewer2 import Reviewer2


def work():
    prompt_path = os.environ.get('REVIEWER_PROMPT_PATH')

    github_owner = os.environ.get('GITHUB_OWNER')
    github_repository = os.environ.get('GITHUB_REPOSITORY')
    github_token = os.environ.get('GITHUB_TOKEN')

    atlassian_domain = os.environ.get('ATLASSIAN_DOMAIN')
    jira_api_login_email = os.environ.get('JIRA_API_LOGIN_EMAIL')
    jira_api_token = os.environ.get('JIRA_API_TOKEN')

    with open(prompt_path, encoding='utf-8') as f:
        reviewer_prompt = f.read()

    github_pull_request_number_string = input('Please input the pull request number: ')
    github_pull_request_number = int(github_pull_request_number_string)

    jira_issue_key = input('Please input the Jira issue key: ')

    confluence_page_id = input('Please input the Confluence page ID: ')

    reviewer = Reviewer2(
        prompt=reviewer_prompt,
        github_owner=github_owner,
        github_repository=github_repository,
        github_number=github_pull_request_number,
        github_token=github_token,
        atlassian_domain=atlassian_domain,
        jira_key=jira_issue_key,
        jira_api_login_email=jira_api_login_email,
        jira_api_token=jira_api_token,
        confluence_page_id=confluence_page_id,
    )

    reviewer.work()


if __name__ == "__main__":
    work()
