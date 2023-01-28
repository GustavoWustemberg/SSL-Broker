import os
import chardet

folder_path = input("Insira o caminho da pasta: ")
files_to_modify = ["geral.php", "footer.php", "robots.txt", "sitemap.xml", ".htaccess", "gerador-htaccess.php"]

for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name in files_to_modify:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'rb') as f:
                result = chardet.detect(f.read())
            with open(file_path, 'r', encoding=result['encoding']) as file:
                file_content = file.read()
                file_content = file_content.replace("http://", "https://")
            with open(file_path, 'w', encoding=result['encoding']) as file:
                file.write(file_content)
                print(f"O arquivo {file_name} foi modificado")

# Verifica se o arquivo ".gitignore" já existe
if not os.path.exists(os.path.join(folder_path, ".gitignore")):
    open(os.path.join(folder_path, ".gitignore"), "w").close()

# Abre o arquivo .gitignore e verifica se já contém a palavra .htaccess
with open(os.path.join(folder_path, ".gitignore"), "r") as gitignore:
    content = gitignore.read()
    if ".htaccess" in content:
        print("A palavra '.htaccess' já existe no arquivo .gitignore")
    else:
        gitignore.close()
        # Adiciona a palavra ".htaccess" ao arquivo .gitignore
        with open(os.path.join(folder_path, ".gitignore"), "a") as gitignore:
            gitignore.write("\n.htaccess")
            print("Palavra '.htaccess' adicionada com sucesso ao arquivo .gitignore!")