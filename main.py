import git
import os
import shutil
import util
from util import Author
import logging


def main(config):
    logging.basicConfig(level=config.get('log_level', 'INFO').upper())

    commit_message = config['commit_message']
    local_clone_path = config.get('local_clone_path', 'temp_repositories/')
    pr_body = config.get('pull_request_body', config['commit_message'])
    remote = config.get('remote_name', 'origin')
    base_branch = config.get('base_branch', 'main')
    branch_name = config['branch_name']
    hostname = config.get('host_name', 'github.com')

    author = Author(name=config['author_name'], email=config['author_email'])
    g = util.get_github(hostname, config['token'])

    log_file = open('pull_requests.log', 'a')

    for repository in config['repositories']:
        path_to_repository = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          local_clone_path + repository)

        clone_url = f'git@{hostname}:{repository}.git'
        cloned_repository = git.Repo.clone_from(clone_url, path_to_repository,
                                                branch=base_branch,
                                                env={"GIT_SSH_COMMAND": 'ssh -i ' + config['ssh_key']})

        logging.info(f'git clone {clone_url}')

        new_branch = cloned_repository.create_head(branch_name)
        new_branch.checkout()
        logging.info(f'git checkout -b {new_branch}')

        for file in config['files']:
            path_to_repository_file = os.path.join(path_to_repository, file)

            if os.path.isfile(path_to_repository_file):
                for texts in config['find_and_replace_list']:
                    text_to_find = texts[0]
                    text_to_replace = texts[1]

                    file = open(path_to_repository_file, 'r')
                    current_file_data = file.read()
                    file.close()

                    new_file_data = current_file_data.replace(text_to_find, text_to_replace)

                    file = open(path_to_repository_file, 'w')
                    file.write(new_file_data)
                    file.close()

                cloned_repository.index.add(path_to_repository_file)
                logging.info(f'git add {path_to_repository_file}')

        cloned_repository.index.commit(commit_message, author=author)
        origin = cloned_repository.remote(name=remote)
        origin.push(new_branch)
        logging.info(f'git push {remote} {branch_name}')

        repo = g.get_repo(repository)
        pr = repo.create_pull(title=commit_message, body=pr_body, head=branch_name, base=base_branch)
        logging.info(f'Pull request created: {pr.html_url}')
        log_file.write(f'{pr.html_url}\n')

    if os.path.exists(local_clone_path):
        shutil.rmtree(local_clone_path)

    log_file.close()


if __name__ == '__main__':
    main(util.get_config('config.json'))
