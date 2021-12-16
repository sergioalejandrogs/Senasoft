from git import Repo 
import os
from func import run_app

local_repo_directory = "../repositorio"
branch = "master"

def clone_repo():
    if os.path.exists(local_repo_directory):
        print("Directory exists, pulling changes from master branch")
        repo = Repo(local_repo_directory)
        origin = repo.remotes.origin
        origin.pull(branch)
    else: 
        print("Directory does not exists, cloning repository")
        Repo.clone_from('https://github.com/sergioalejandrogs/repositorio.git', local_repo_directory, branch=branch)

def main():
    clone_repo()
    run_app()
    repo = Repo(local_repo_directory)
    repo.git.add(all=True)
    repo.git.commit('-m', 'Uploaded organized files', author='sergioalejandrogs@gmail.com')
    repo.git.push('origin', branch)

main()