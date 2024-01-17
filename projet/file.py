# récupère les librairies contenu dans un fichier texte et les stocke
def libr_file(file):
    with open(file, "r", encoding="utf_8") as f:
        l = f.read().split("\n")
    return l

