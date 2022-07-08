import click


def arbo(fichier):
    """Cette fonction prend comme argument un chemin de fichier au format .md
    et imprime son arborescence de titres"""
    with open(fichier) as f:
        contenu = f.read()
    contenu = contenu.split("\n")
    h1 = 0
    h2 = 0
    h3 = 0
    h4 = 0
    plan = ""
    for ligne in contenu:
        if "#" and not "<span" in ligne:
            if ligne[:2] == "# ":
                h1 += 1
                h2 = 0
                h3 = 0
                h4 = 0
                plan += str(str(h1) + ". " + ligne[2:]) + "\n"
            elif ligne[:3] == "## ":
                h2 += 1
                h3 = 0
                h4 = 0
                plan += str("\t" + str(h2) + ". " + ligne[3:]) + "\n"
            elif ligne[:4] == "### ":
                h3 += 1
                h4 = 0
                plan += str("\t\t" + str(h3) + ". " + ligne[4:]) + "\n"
            elif ligne[:5] == "#### ":
                h4 += 1
                plan += str("\t\t\t" + str(h4) + ". " + ligne[5:]) + "\n"
        elif "#" and "<span" in ligne:
            if ligne[:2] == "# ":
                h1 += 1
                h2 = 0
                h3 = 0
                h4 = 0
                plan += str(str(h1) + ". " + ligne[48:-7]) + "\n"
            elif ligne[:3] == "## ":
                h2 += 1
                h3 = 0
                h4 = 0
                plan += str("\t" + str(h2) + ". " + ligne[49:-7]) + "\n"
            elif ligne[:4] == "### ":
                h3 += 1
                h4 = 0
                plan += str("\t\t" + str(h3) + ". " + ligne[50:-7]) + "\n"
            elif ligne[:5] == "#### ":
                h4 += 1
                plan += str("\t\t\t" + str(h4) + ". " + ligne[51:-7]) + \
                        "\n"
    return plan


@click.command()
@click.argument("fichier")
def run(fichier):
    # On récupère le contenu du fichier md
    with open(fichier) as f:
        contenu = f.read()
    corps = contenu.split("\n")

    h1 = 0
    niveauCourant = 1
    comp = "<!--compléter-->"

    # On ouvre le fichier où l'on écrit l'élément dsc
    with open("./dsc.xml", mode="w") as g:
        g.write('''<?xml version="1.0" encoding="UTF-8"?>\n''')
        g.write('''<dsc>\n''')

        for ligne in corps:
            if ligne[:2] == "# ":
                # Programmation
                if h1 == 0:
                    g.write('''<c level="series">\n''')
                    g.write('''<did>\n''')
                    g.write(f'''<unitid type="identifiant">{comp}</unitid>\n''')
                    g.write(f'''<unittitle>{ligne[2:]}</unittitle>\n''')
                    g.write(f'''<unitdate normal="">{comp}</unitdate>\n''')
                    g.write('''</did>\n''')
                    h1 += 1
                # Dossiers de travaux
                else:
                    # On écrit le code
                    if niveauCourant == 2:
                        g.write('''</c>\n''')
                        g.write('''</c>\n''')
                    elif niveauCourant == 3:
                        g.write('''</c>\n''')
                        g.write('''</c>\n''')
                        g.write('''</c>\n''')
                    g.write('''<c level="series">\n''')
                    g.write('''<did>\n''')
                    g.write(f'''<unitid type="identifiant">{comp}</unitid>\n''')
                    g.write(f'''<unittitle>{ligne[2:]}</unittitle>\n''')
                    g.write(f'''<unitdate normal="">{comp}</unitdate>\n''')
                    g.write('''</did>\n''')
                
                niveauCourant = 1

            elif ligne[:3] == "## ":
                if niveauCourant == 2:
                    g.write('''</c>\n''')
                elif niveauCourant == 3:
                    g.write('''</c>\n''')
                    g.write('''</c>\n''')
                elif niveauCourant == 4:
                    g.write('''</c>\n''')
                    g.write('''</c>\n''')
                    g.write('''</c>\n''')
                g.write('''<c level="subseries">\n''')
                g.write('''<did>\n''')
                g.write(f'''<unitid type="identifiant">{comp}</unitid>\n''')
                g.write(f'''<unittitle>{ligne[3:]}</unittitle>\n''')
                g.write(f'''<unitdate normal="">{comp}</unitdate>\n''')
                g.write('''</did>\n''')
                
                niveauCourant = 2

            elif ligne[:4] == "### ":
                if niveauCourant == 3:
                    g.write('''</c>\n''')
                elif niveauCourant == 4:
                    g.write('''</c>\n''')
                    g.write('''</c>\n''')
                g.write('''<c level="file">\n''')
                g.write('''<did>\n''')
                g.write(f'''<unitid type="identifiant">{comp}</unitid>\n''')
                g.write(f'''<unittitle>{ligne[4:]}</unittitle>\n''')
                g.write(f'''<unitdate normal="">{comp}</unitdate>\n''')
                g.write('''</did>\n''')
    
                niveauCourant = 3

            elif ligne[:5] == "#### ":
                if niveauCourant == 4:
                    g.write('''</c>\n''')
                g.write('''<c level="item">\n''')
                g.write('''<did>\n''')
                g.write(f'''<unitid type="identifiant">{comp}</unitid>\n''')
                g.write(f'''<unittitle>{ligne[5:]}</unittitle>\n''')
                g.write(f'''<unitdate normal="">{comp}</unitdate>\n''')
                g.write('''</did>\n''')
    
                niveauCourant = 4

        g.write('''</c>\n''')
        g.write('''</c>\n''')
        g.write('''</c>\n''')
        g.write('''</dsc>\n''')


if __name__ == "__main__":
    run()
