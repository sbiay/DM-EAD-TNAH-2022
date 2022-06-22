from bs4 import BeautifulSoup
import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(chemin_actuel, "index.xml")
result = os.path.join(chemin_actuel, "index_enrichi.xml")
referentiel_hors_Paris = os.path.join(chemin_actuel, "DM-EAD-TNAH-2022", "referentiels", "XML_SIA", "FRAN_RI_026.xml")

with open(file, 'r', encoding="ISO-8859-1") as f:
    xml_doc = f.read()
soupe = BeautifulSoup(xml_doc, features="xml")
mh_parisien = soupe.find("commune").find_all("mh")

with open(referentiel_hors_Paris, 'r', encoding="ISO-8859-1") as f:
    xml_doc = f.read()
soup = BeautifulSoup(xml_doc, features="xml")
ref_com = soup.find_all("terme")

for mh in mh_parisien:
    if "id" not in mh.attrs:
        nom_mh = mh.get_text()
        if " de " in nom_mh:
            nom_mh = nom_mh.split(" de ")
            nom_mh = nom_mh[1] + " (" + nom_mh[0]
        for ref in ref_com:
            if ref.get_text().startswith(nom_mh):
                mh['id'] = ref.parent['id']


with open(result, "w", encoding="ISO-8859-1") as f:
    f.write(str(soupe))