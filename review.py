# coding: utf-8


from reviewer import Reviewer2


def work():
    reviewer = Reviewer2(prompt='prompt')

    reviewer_comment = reviewer.work()


if __name__ == "__main__":
    work()
