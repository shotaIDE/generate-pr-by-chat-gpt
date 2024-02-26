# coding: utf-8

import os

from reviewer2 import Reviewer2


def work():
    github_owner = os.environ.get('GITHUB_OWNER')
    github_repository = os.environ.get('GITHUB_REPOSITORY')
    github_token = os.environ.get('GITHUB_TOKEN')

    github_pull_request_number_string = input('Please input the pull request number: ')
    github_pull_request_number = int(github_pull_request_number_string)

    reviewer = Reviewer2(
        github_owner=github_owner,
        github_repository=github_repository,
        github_number=github_pull_request_number,
        github_token=github_token,
    )

    reviewer.work()


if __name__ == "__main__":
    work()
