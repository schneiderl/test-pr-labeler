
from branch import Branch
from comment import Comment
from db import db

class PR():
    def __init__(self):
        pass
    
    @staticmethod
    def create_tag_for_latest_major_release(issue, label_name):
        issue.add_to_labels(label_name)
        
    @staticmethod
    def create_pr_for_release_branch(repo, label_name, original_pr_base, original_pr_head, original_pr_title, current_pr):
        new_branch_name = Branch.create_downport_branch(repo, original_pr_base, original_pr_head, label_name)
        new_pr = repo.create_pull(title=original_pr_title + " - cherry-picking-vp", body="", head=new_branch_name, base=label_name)
        db.insert_pr(current_pr.number, label_name, new_pr.number, 'pending', new_branch_name)
        Comment.pr_create_comment(current_pr, new_pr.html_url)
        # pr_base.commit.
        # issue.add_to_labels(label_name)
        # repo.create_pull(title=title, head=head, base="release/sdk/v3.x"
    
    # staticmethod()
    # def delete_branch_from_deleted_label(repo, label):
        
        
                
        
# g = Github("user", "pass")
# repoName = "apiTest"
# source_branch = 'master'
# target_branch = 'newfeature'

# repo = g.get_user().get_repo(repoName)
# sb = repo.get_branch(source_branch)
# repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)