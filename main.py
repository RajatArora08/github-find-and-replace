import git
import os
import shutil
import util
from util import Author


def main(config):
    commit_message = config['commit_message']
    local_clone_path = config.get('local_clone_path', 'temp_repositories/')
    pr_body = config.get('pull_request_body', config['commit_message'])
    base_branch = config.get('base_branch', 'main')
    branch_name = config['branch_name']
    hostname = config.get('host_name', 'github.com')

    author = Author(name=config['author_name'], email=config['author_email'])
    g = util.get_github(hostname, config['token'])

    for repository in config['repositories']:
        path_to_repository = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          local_clone_path + repository)

        cloned_repository = git.Repo.clone_from(f'git@{hostname}:{repository}.git', path_to_repository,
                                                branch=base_branch,
                                                env={"GIT_SSH_COMMAND": 'ssh -i ' + config['ssh_key']})

        new_branch = cloned_repository.create_head(branch_name)
        new_branch.checkout()

        for file in config['files']:
            path_to_repository_file = os.path.join(path_to_repository, file)
            is_file = os.path.isfile(path_to_repository_file)

            for texts in config['find_and_replace_list']:
                text_to_find = texts[0]
                text_to_replace = texts[1]

                if is_file:
                    file = open(path_to_repository_file, 'r')
                    current_file_data = file.read()
                    file.close()

                    new_file_data = current_file_data.replace(text_to_find, text_to_replace)

                    file = open(path_to_repository_file, 'w')
                    file.write(new_file_data)
                    file.close()

            if is_file:
                cloned_repository.index.add(path_to_repository_file)

        cloned_repository.index.commit(commit_message, author=author)
        origin = cloned_repository.remote(name=config.get('remote_name', 'origin'))
        origin.push(new_branch)

        repo = g.get_repo(repository)
        pr = repo.create_pull(title=commit_message, body=pr_body, head=branch_name, base=base_branch)
        print(pr.html_url)

    if os.path.exists(local_clone_path):
        shutil.rmtree(local_clone_path)


if __name__ == '__main__':
    main(util.get_config('config.json'))
