## About

This allows a quick way to retrieve the code submitted as a pull request in a forked repository where the upstream is configured.
This script takes the repository path and PR number and creates a new branch of that PR number and then switches to the branch.

## How to use

Enter the PR number and auto fetch PR branch from repo. Then switch to the branch.

Steps:
- ensure upstream is configured in local repo
- run python script
- enter directory where repo is located
- enter PR number 

Result:
- The script will create and switch to a new branch containing PR
- Example: if the PR number is `123` a branch will be created called `pr-123`

