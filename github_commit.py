import os

def github_commit():
    GITHUB_REPO = "https://github.com/FeymanMCSQ/linkedin-python.git"
    COMMIT_MESSAGE = "Added new Article"

    # Ensure we are on the main branch (create it if it doesn't exist)
    os.system("git checkout main || git checkout -b main")

    # Pull latest changes and auto-merge (to prevent non-fast-forward errors)
    # os.system("git pull --rebase --autostash origin main || git reset --hard origin/main")

    # Add changes and commit
    os.system("git add .")
    os.system(f'git commit -m "{COMMIT_MESSAGE}"')

    # Force push to override any conflicts
    os.system("git push origin main")

    print("Commit changes added successfully!")

