import git_cli
from release import Release
from db import db
class Branch():
    def __init__(self, name, commit):
        self.name = name
        self.commit = commit
    
    @staticmethod
    def compare_branches(repo, base, head):
        return repo.compare(base, head)
    
    @staticmethod
    def create_downport_branch(repo, original_pr_base, original_pr_head, label_name):
        commit_diff = Branch.compare_branches(repo, original_pr_base, original_pr_head).commits
        new_pr_base = repo.get_branch(label_name)
        downport_branch_name = 'bot/' + original_pr_head + "/" + Release.extract_tag_from_label(label_name)
        repo.create_git_ref(ref='refs/heads/' + downport_branch_name, sha=new_pr_base.commit.sha)
        git_cli.cherry_pick_commits(repo, commit_diff, downport_branch_name)
        return downport_branch_name
    
    def delete_downport_branch_from_label(repo, original_pr_number, label_name):
        #downport_branch_name = 'bot/' + original_pr_head + "/" + Release.extract_tag_from_label(label_name)
        branch_name = db.get_branch_from_original_pr_and_label(original_pr_number, label_name)
        repo.get_git_ref('heads/' + branch_name).delete()
        db.get_branch_from_original_pr_and_label(original_pr_number, label_name)
        
    # def get_downport_branches(repo, original_pr_head):
    #     downport_branches = []
    #     for branch in repo.get_branches():
    #         if branch.name.startswith('bot/' + original_pr_head):
    #             downport_branches.append(branch)
    #     return downport_branches