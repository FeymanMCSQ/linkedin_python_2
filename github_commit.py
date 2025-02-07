import os

def github_commit():
    GITHUB_REPO = "https://github.com/FeymanMCSQ/linkedin_python_2.git"
    COMMIT_MESSAGE = "Added new Article"

    os.system(f"git remote add origin {GITHUB_REPO}")
    # Ensure we are on the main branch (create it if it doesn't exist)
    os.system("git checkout main || git checkout -b main")


    # Add changes and commit
    os.system("git add .")
    os.system(f'git commit -m "{COMMIT_MESSAGE}"')

    # Force push to override any conflicts
    os.system("git push origin main")

    print("Commit changes added successfully!")

