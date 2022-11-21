#!/usr/bin/env python3
import os
import re
import requests
import posixpath
import argparse
from git import Repo

parser = argparse.ArgumentParser('gitlab-clone-group.py')
parser.add_argument('group_id', help='id of group to clone (including subgroups)')
parser.add_argument('directory', help='directory to clone repos into')
parser.add_argument('--token', help='Gitlab private access token with read_api and read_repository rights')
parser.add_argument('--gitlab-domain', help='Domain of Gitlab instance to use, defaults to: gitlab.com', default='gitlab.com')

args = parser.parse_args()

api_url = 'https://' + posixpath.join(args.gitlab_domain, 'api/v4/groups/', args.group_id, 'projects') + '?per_page=9999&page=1&include_subgroups=true'

headers = {'PRIVATE-TOKEN': args.token}
res = requests.get(api_url, headers=headers)
projects = res.json()

base_ns = os.path.commonprefix([p['namespace']['full_path'] for p in projects])
print('Found %d projects in: %s' % (len(projects), base_ns))

abs_dir = os.path.abspath(args.directory)
os.makedirs(abs_dir,exist_ok=True)

def get_rel_path(path):
    subpath = path[len(base_ns):]
    if (subpath.startswith('/')):
        subpath = subpath[1:]
    return posixpath.join(args.directory, subpath)

for p in projects:
    clone_dir = get_rel_path(p['namespace']['full_path'])
    project_path = get_rel_path(p['path_with_namespace'])
    print('Cloning project: %s' % project_path) 
    if os.path.exists(project_path):
        print("\tProject folder already exists, skipping")
    else:
        print("\tGit url: %s" % p['ssh_url_to_repo'])
        os.makedirs(clone_dir, exist_ok=True)
        Repo.clone_from(p['ssh_url_to_repo'], project_path)

