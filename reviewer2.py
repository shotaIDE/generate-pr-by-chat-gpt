# coding: utf-8

from ai import chat_with_function_calling_loop
from github import ListPullRequestFiles


class Reviewer2:
    _actor_name = 'Reviewer'

    def __init__(
            self,
            github_owner: str,
            github_repository: str, 
            github_number: str, 
            github_token: str
    ):
        self._list_pull_request_files = ListPullRequestFiles(
            owner=github_owner,
            repository=github_repository,
            number=github_number,
            token=github_token,
        )


    def work(self) -> str:
        print('---------------------------------')
        print(f'{self._actor_name}: start to work')

        system_message = (
            "You are an excellent Python program reviewer. \n" +
            "We review and thoroughly check the modifications made by programmers in response to requests from engineer leader, " +
            "and identify any points that require additional attention and point them out to programmers in japanese.\n" +
            "Once all checks have been completed and there are no issues found, ensure you execute the RecordLGTM function.\n" +
            "When reviewing, please pay particular attention to the following points:\n" +
            "- The revised code should have a natural design, with readable code that utilizes appropriate and understandable variable names.\n" +
            "The request from the engineer leader is as follows.\n\n" + self._leader_comment
        )

        comment = chat_with_function_calling_loop(
            messages=system_message,
            functions=[
                self._list_pull_request_files,
            ],
            actor_name=self._actor_name,
        )

        print(f'{self._actor_name}: {comment}')
        return comment
