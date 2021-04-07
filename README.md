# github-find-and-replace

This code allows you to find and replace text across repositories and create pull requests.

## Configuration

All configurations can be edited in [config.json](config.json).

| Property    | Type        | Description |
| ----------- | ----------- | ----------- |
| repositories | list | List of repositories. Should be specified in `<org>/<repo-name>` format. |
| find_and_replace_list | list | List of text to search and text to replace. |
| files | list | File paths to files. These should not be absolute paths |
| token | str | GitHub personal access token. See [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) on how to generate a personal access token. |
| ssh_key | str | Path to SSH Key. See [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) on how to generate ssh keys.  |
| branch_name | str | Your branch name. |
| host_name | str | Github hostname. Defaults to `github.com`. |
| commit_message | str | Commit message. |
| pull_request_body | str | Body for Pull Request. Defaults to `commit_message`. |
| base_branch | str | Base branch. Defaults to `main`. |
| remote_name | str | Remote name. Defaults to `origin`. |
| local_clone_path | str | Local path where repositories can be cloned. Defaults to `temp_repositories/`. |
| author_name | str | Author name for commit. |
| author_email | str | Author email for commit. |

## How to run?

Step 1: Clone repository

```bash
git clone git@github.com:RajatArora08/github-find-and-replace.git
```

Step 2: Edit configurations in [config.json](config.json)

Step 3: Install requirements

```bash
pip install -r requirements.txt
```

Step 3: Run script using Python 3.x+

```bash
python main.py
```
