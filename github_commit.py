import os

# Set up Git repo
def github_commit():
    GITHUB_REPO = "https://github.com/FeymanMCSQ/linkedin-python.git"
    COMMIT_MESSAGE = "Added new Article"

    os.system("git init")  # Initialize Git if not already
    os.system(f"git remote add origin {GITHUB_REPO}")  # Add remote
    os.system("git pull origin main --rebase")
    os.system("git add .")  # Add all changes
    os.system(f'git commit -m "{COMMIT_MESSAGE}"')  # Commit changes
    os.system("git branch -M main")  # Set branch to main (if needed)
    os.system("git push origin main")  # Push to GitHub
    print("Commit changes added")