import subprocess

# Set a default directory to use if input is blank
default_directory = "TeachMePythonLikeIm5/"


def pull_pr_review():

    directory = input("Enter repo path: ")

    if(directory == ""):
        directory = default_directory

    pr_num = input("Enter PR number to fetch in repo [%s]: " % directory)

    pr_path = "pull/" + pr_num + "/head:pr-" + pr_num

    print(pr_path)
    print(directory)

    subprocess.run(["git", "fetch", "upstream", pr_path], cwd=directory)  # e.g. git fetch upstream pull/1234/head:pr-123
    # subprocess.run(["git", "fetch", "origin", pr_path], cwd=directory)

    pr_switch = "pr-" + pr_num
    print("Switching to branch %s" % pr_switch)

    subprocess.run(["git", "checkout", pr_switch], cwd=directory)  # e.g. git checkout pr-123


if __name__ == "__main__":
    print("--- Start ---")
    pull_pr_review()
