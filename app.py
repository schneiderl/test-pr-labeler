import os
import requests


from flask import Flask, request
from github import Github, GithubIntegration
from connection import get_connection
from release import Release
from pull_request import PR
from branch import Branch
from action import Action
import json
from db import db

app = Flask(__name__)
# MAKE SURE TO CHANGE TO YOUR APP NUMBER!!!!!




def create_new_branch_with_diffs(repo, base_branch, head_branch, release_branch_name):
    commit_diff = compare_branches(repo, base_branch, head_branch).commits
    release_branch = repo.get_branch(release_branch_name)
    new_branch = repo.create_git_ref(ref='refs/heads/' + head_branch + "_downport", sha=release_branch.commit.sha)
    

def create_pr_for_release_branch(current_pr, repo, title, head_branch, base_branch):
    new_branch_name = create_new_branch_with_diffs(repo, head_branch, base_branch, get_latest_major_release_branch())
    new_pr = repo.create_pull(title=title + " - VP CHERRY-PICK", body="", head=head_branch, base=base_branch)
    current_pr.create_comment("Created new PR for the release branch " + new_pr.html_url)




@app.route("/", methods=['POST'])
def bot():
    # Get the event payload
    payload = request.json
    json_payload = request.get_json()
    json_formatted_str = json.dumps(json_payload, indent=2)
    print(json_formatted_str)
    action = Action(payload)
    owner = payload['repository']['owner']['login']
    repo_name = payload['repository']['name']
    git_connection = get_connection(owner, repo_name)
    repo = git_connection.get_repo(f"{owner}/{repo_name}")
    
    # repo.create_check_run("test", "758b828ad5fd11bf71acae281d2025762fecf492", status="completed", conclusion="success")
    # print("created check run")
    if action.is_action_pr_opened():
        print("New PR open. Tagging it.")
        issue = repo.get_issue(number=payload['pull_request']['number'])
        PR.create_tag_for_latest_major_release(issue, Release.get_latest_major_release_branch())
    elif action.is_action_pr_labeled():
        print("PR was labeled. Creating a new PR for the release branch")
        issue = repo.get_issue(number=payload['pull_request']['number'])
        PR.create_pr_for_release_branch(repo, payload['label']['name'], payload['pull_request']['base']['ref'], payload['pull_request']['head']['ref'], payload['pull_request']['title'], issue)
    elif action.is_action_pr_unlabeled():
        print("Label deleted. Rolling back the opened PR.")
        Branch.delete_downport_branch_from_label(repo, payload['pull_request']['number'], payload['label']['name'])
    elif action.is_action_sync():
        print("Source branch was changed. Syncing the downport branches.")
        

    
    # if payload['action'] == 'labeled' and 'pull_request' in list(payload.keys()):
    #     print("Creating PR")
    #     # print(payload['label'])
    #     
    #     create_pr_for_release_branch(issue, repo, payload['pull_request']['title'],  payload['pull_request']['head']['ref'], payload['label']['name'])
        
    #     create_pr_for_branch(issue)
    # # if payload.


    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=5000)