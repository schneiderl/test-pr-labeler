from git import Repo
from utils import *
import shutil

def cherry_pick_commits(repo, commits, branch):
    tmp_folder = "/tmp/clone/" + generate_random_string()
    cloned_repo = Repo.clone_from(repo.clone_url, tmp_folder)
    cloned_repo.git.checkout(branch)
    for commit in commits:
        cloned_repo.git.cherry_pick(commit.sha)
    cloned_repo.git.push("origin", branch)
    shutil.rmtree(tmp_folder, ignore_errors=True)
    
    