# Documentation de l'encodage

*En cours de rédaction*

**IR = instrument de recherche**

## Le eadheader
### Le filedesc : IR d'origine

`<eadid>` : identifiant de l'IR

`<titleproper>` : titre complet de l'IR

`<subtitle>` : précision sur le type d'IR

`<author>` : auteurs de l'IR d'origine (en docx), tous dans un seul élément selon la DTD SIA

`<editionstmt>` : première édition éléctronique vu qu'on parle du fichier d'origine et non de l'édition en EAD, à vérifier

`<publisher>` : AN, car ce sont eux qui ont produit le doc suite au versement et pas le producteur

`<address>` : à vérifier, probablement plutôt celle de l'IR (Paris), et celle de Fontainebleau serait dans un `<physloc>` car correspond à la localisation des archives physiques

`<date>` : date de rédaction du premier IR

### Le profiledesc : IR en EAD

`<creation>` : présentation du contexte de création en EAD, pour les auteurs: on met le nom de la promotion comme dans l'encodage actuel ou on met les noms de chaque élève ?

`<langusage>` : encodage & IR en français

`<descrules>` : présentation des normes et règles suivies

`<revisiondesc>` : étant donné que nous sommes en création de l'IR, nous n'utiliserons probablement pas cette partie, qui sert au suivi des modifications qui ont lieu après la création

## Le archdesc

`<unitid>` : choix u type de cote

`<unttitle>` et <unitdate>: reprise du type et des dates

`<origination>`, `<corpname>`: producteur, "N1 = 5181 ?"

`<physdesc>` description du conditionnement des documents physiques

`<accessrestrict>` et `<userestrict>` : conditions d'accès et d'utilisation

`<acqinfo>` : histoire du fonds liée aux versements aux AN

`<bioghist>` : histoire du producteur

`<custodhist>` : historique de la conservation (avant versement)

`<arrangement>` : informations sur la façon dont les archives sont classées

`<separatedmaterial>` : autres versements en lien avec le fonds mais avec le même producteur

`<relatedmaterial>` : autres versements en lien avec le fonds mais avec un producteur différent

`<processinfo>` : informations sur le traitement des archives physiques, correspondrait à "Évaluation, tris et éliminations"

## Le dsc

Structure de l'instrument de recherche, à définir (`<c>` et @types de `<c>`) 
