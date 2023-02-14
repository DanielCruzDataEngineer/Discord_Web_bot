import os
import git

# obtém a URL do repositório a partir da variável de ambiente GITHUB_REPOSITORY
repo_url = f"https://github.com/DanielCruzDataEngineer/Discord_Web_bot.git"

# inicializa o repositório git
repo = git.Repo(os.getcwd())

# cria um commit com a mensagem informando qual comando foi executado
commit_message = "Adicionando arquivos modificados"
repo.index.commit(commit_message)
