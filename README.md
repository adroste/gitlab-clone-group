# gitlab-clone-group

Python script to clone all GitLab repos of a group and their subgroups while keeping the tree structure.

Tested with GitLab API v4.

## Usage

1. Download the gitlab-clone-group.py
2. Generate a private access token with *read_api* and *read_repository* rights
3. Get your group ID (displayed in light gray on below your group name)
4. Run the script

### Example:
```
python3 gitlab-clone-group.py --token glabc-D-e-llaaabbbbcccccdd 12345678 .
```
*Clones the group 12345678 (and subgroups) into the current working directory, keeping the tree structure.*

### Help:
```
usage: gitlab-clone-group.py [-h] [--token TOKEN] [--gitlab-domain GITLAB_DOMAIN] group_id directory

positional arguments:
  group_id              id of group to clone (including subgroups)
  directory             directory to clone repos into

options:
  -h, --help            show this help message and exit
  --token TOKEN         Gitlab private access token with read_api and read_repository rights
  --gitlab-domain GITLAB_DOMAIN
                        Domain of Gitlab instance to use, defaults to: gitlab.com
```
