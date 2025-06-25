# WorkPlannerAgent
Work Planner Agent using Hugging Face SmolAgents 

# Generate Hugging Face Token
1. Go to Hugging Face Website
Open your browser and go to:
🔗 https://huggingface.co

2. Login or Sign Up
If you already have an account, click Log in (top right) and enter your credentials.
If not, click Sign Up and create a free account.
Go to Access Tokens Page
After logging in, navigate to:
🔗 https://huggingface.co/settings/tokens

3. Alternatively:
Click your profile picture (top-right corner).
Go to Settings → Access Tokens (in the sidebar).
Create New Token
Click "New token".
Enter a name for your token (e.g., my-project).

4. Look into this carefully Set the Role:
Read: Only needed for downloading models/datasets (most common).
Write: Only if you plan to upload or manage repos.

5.Click "Generate token".
Copy the Token
Once created, copy the token and store it securely – you won't be able to see it again.

# For SSL issues and fixes
Go to hugging face website --> connection is secure --> check if certificate is valid --> details --> export
Then paste it in your file and it'll work.
