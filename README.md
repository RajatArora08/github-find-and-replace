# github-find-and-replace
[![Build](https://github.com/RajatArora08/github-find-and-replace/actions/workflows/main.yml/badge.svg)](https://github.com/RajatArora08/github-find-and-replace/actions/workflows/main.yml)
[![Docker](https://img.shields.io/docker/pulls/rajatar08/github-find-and-replace.svg)](https://hub.docker.com/r/rajatar08/github-find-and-replace)

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
| log_level | str | The levels, in increasing order of severity, are DEBUG, INFO, WARNING, ERROR, and CRITICAL. Defaults to INFO. |

## How to run?


### Option 1: Using docker (Recommended)

Step 1: Edit configurations in [config.json](config.json)

Step 2: Run docker container

```bash
docker run -it -v $(pwd)/config.json:/app/config.json -v ~/.ssh/id_ed25519:/root/.ssh/id_ed25519 rajatar08/github-find-and-replace:latest
```

### Option 2: Build and run on local

Step 1: git clone

```bash
git clone git@github.com:RajatArora08/github-find-and-replace.git
```

Step 2: Edit configurations in [config.json](config.json)

Step 3: Install requirements

```bash
pip install -r requirements.txt
```

Step 4: Run script using Python 3.x+

```bash
python main.py
```

NOTE: All pull requests are logged to `pull_requests.log` for ease of sharing.
