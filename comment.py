import re

parse_tests = """test

<!--for the bot internal consumption, do not modify{'release/sdk/v3.x': 50}-->"""

result = re.search('<!--for the bot internal consumption, do not modify(.*)-->', parse_tests)
print(result.group(1))

class Comment:
    def __init__(self):
        pass
    
    @staticmethod
    def pr_create_comment(current_pr, new_pr_url):
        current_pr.create_comment("Created new PR for the release branch " + new_pr_url)
