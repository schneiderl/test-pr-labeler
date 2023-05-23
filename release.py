import re

class Release:
    def __init__():
        pass
    
    @staticmethod
    def get_latest_major_release_branch():
        return "release/sdk/v2.x"
    
    @staticmethod
    def extract_tag_from_label(label):
        pattern = r'v[0-9]+(\.[0-9]+)?\.x'
        match = re.search(pattern, label)
        if match is not None:
            return match.group(0)
        else:
            return None