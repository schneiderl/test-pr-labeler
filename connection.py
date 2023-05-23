
from github import Github, GithubIntegration
import os

def get_connection(owner, repo_name):
    app_id=335683
    # Read the bot certificate
    with open(
            os.path.normpath(os.path.expanduser('./test-pr-labeler.2023-05-18.private-key.pom')),
            'r'
    ) as cert_file:
        app_key = cert_file.read()

    git_integration = GithubIntegration(
        app_id,
        app_key,
    )

    git_connection = Github(
        login_or_token=git_integration.get_access_token(
            git_integration.get_installation(owner, repo_name).id
        ).token
    )
    
    return git_connection