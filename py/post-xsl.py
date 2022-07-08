# On ouvre le résultat de la trasnfo XSL
with open("./encodage-transf.xml") as xmlf:
    contenu = xmlf.read()
    contenu = contenu.split("\n")
    
# On ouvre le fichier de sortie
with open("./encodage-transf-net.xml", mode="w") as xmlnet:
    # On boucle sur chaque ligne
    for index, l in enumerate(contenu):
        if "<scopecontent>" in l:
            # Contrôler la date
            if "unitdate" in contenu[index - 2]:
                unitdate = contenu[index - 2]
                unitdate = unitdate.split(">")
                # S'il y a un unitdate vide
                if "</unitdate" in unitdate[1]:
                    # On l'efface
                    unitdate = unitdate[1].replace("</unitdate", "")
                else:
                    unitdate = None
            else:
                unitdate = None
            
            p = contenu[index + 1]
            # Si le contenu comporte une parenthèse suivie d'une virgule (c'est une liste à diviser)
            if "), " in p:
                liste = []
                string = p.replace("<p>", "").replace("</p>", "").replace(".", "")
                string = string.split("), ")
                for index, item in enumerate(string):
                    if item[0] == " ":
                        item = item[1:]
                    if index != len(string) - 1:
                        liste.append(item + ")")
                    else:
                        liste.append(item)
                xmlnet.write("<scopecontent>\n<list>\n")
                # On écrit la liste
                for item in liste:
                    # On place une majuscule au début et un point à la fin
                    initiale = item[0].title()
                    xmlnet.write(f"<item>{initiale}{item[1:]}</item>\n")
                xmlnet.write("</list>\n")
            # Si le contenu ne comporte pas de parenthèse suivie d'une virgule (pas considéré comme une liste)
            else:
                if unitdate:
                    # On supprime l'info de date (déjà inscrite dans le unitdate) et le point final
                    p = p.replace(f" ({unitdate})", "").replace(".", "")
                    # On place une majuscule au début et un point à la fin
                    initiale = p[3].title()
                    p = p[:3] + initiale + p[4:-4] + ".</p>"
                xmlnet.write(f"<scopecontent>\n{p}\n")
        
        elif "<scopecontent>" not in contenu[index - 1]:
            xmlnet.write(l + "\n")
            
        # Contrôler la l. 2272