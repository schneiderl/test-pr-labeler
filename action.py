

class Action():
    def __init__(self, payload):
        self.payload = payload
        
    def is_action_pr_opened(self):
        return self.payload['action'] == 'opened' and'pull_request' in list(self.payload.keys()) and self.payload['pull_request']['user']['login'] != 'cherry-picking-vp[bot]'

    def is_action_pr_labeled(self):
        return self.payload['action'] == 'labeled' and 'pull_request' in list(self.payload.keys())
    
    def is_action_pr_unlabeled(self):
        return self.payload['action'] == 'unlabeled' and 'pull_request' in list(self.payload.keys())
    
    def is_action_sync(self):
        return self.payload['action'] == 'synchronize' and 'pull_request' in list(self.payload.keys())