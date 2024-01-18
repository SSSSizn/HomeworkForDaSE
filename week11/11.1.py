from github import Github

g = Github("xxx")

user = g.get_user()

following_repos = {}

for following in user.get_following():
    repos = following.get_repos()
    following_repos[following.login] = [repo.name for repo in repos]

with open("result.txt", "w") as file:
    for username, repos in following_repos.items():
        file.write(f"{username}'s Repositories: {', '.join(repos)}\n")
