import os
import requests

def create_branch_and_pr(issue_number, issue_title):
    # Define branch name based on issue number and title
    branch_name = f"issue-{issue_number}-{issue_title.replace(' ', '-')}"

    # Create branch
    headers = {
        'Authorization': f'token {os.environ["GITHUB_TOKEN"]}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'ref': branch_name,
        'sha': 'main'  # Change this if your default branch is not main
    }
    response = requests.post(f'https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/git/refs', json=data, headers=headers)
    response.raise_for_status()

    # Create pull request
    pr_data = {
        'title': f'Auto-generated PR for issue #{issue_number}',
        'head': branch_name,
        'base': 'main',  # Change this if your default branch is not main
        'body': f'This PR was automatically created in response to issue #{issue_number}.'
    }
    pr_response = requests.post(f'https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/pulls', json=pr_data, headers=headers)
    pr_response.raise_for_status()

if __name__ == "__main__":
    import sys
    issue_number = sys.argv[1]
    issue_title = sys.argv[2]
    create_branch_and_pr(issue_number, issue_title)
