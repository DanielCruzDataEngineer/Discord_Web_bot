import git

# inicializa o repositório git
repo = git.Repo('..\Discord_Web_bot')

# faz o add dos arquivos modificados
repo.git.add(update=True)

# cria um commit com a mensagem informando qual comando foi executado
commit_message = "Adicionando arquivos modificados"
repo.index.commit(commit_message)