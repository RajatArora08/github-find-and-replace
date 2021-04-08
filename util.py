from github import Github
import json


class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email


def get_github(hostname, token):
    if hostname == 'github.com':
        return Github(token)

    else:
        return Github(base_url=f'https://{hostname}/api/v3', login_or_token=token)


def get_config(file):
    with open(file) as config_file:
        return json.load(config_file)
