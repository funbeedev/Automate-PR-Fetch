## About

This allows a quick way to retrieve the code submitted as a pull request in a forked repository. The local repository must be configured with the remote repository upstream.
This script takes the repository path and PR number as inputs, then creates a new branch containing the PR code then switches to the branch.

## How to use

Enter the PR number and auto fetch PR branch from repo. Then switch to the branch.

Steps:
- ensure upstream is configured in local repo
- run python script
- enter directory where repo is located
- enter PR number 

Result:
- The script will create and switch to a new branch containing PR code
- Example: if the PR number is `123` a branch will be created called `pr-123` containing the code submitted for PR 123

