TNAH 2022 : devoir collectif d'EAD
==================================

# Contenu du dépôt
- [referentiels/](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/main/referentiels) : Ce dossier **référentiels** contient les référentiels utilisés pour l’indexation
- [schemas/](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/main/schemas) : Ce dossier contient les schémas utilisés pour l'instrument de recherche en EAD et la notice en EAC-CPF
- [consignes.docx](https://github.com/sbiay/DM-EAD-TNAH-2022/blob/main/consignes.docx) : Le document **consignes.docx**consignes générales du devoir
- [documentation.md](https://github.com/sbiay/DM-EAD-TNAH-2022/blob/main/documentation.md) : Le document **documentation.md** contient la documentation de l'encodage de l'instrument de recherche en Markdown
- [encodage.xml](https://github.com/sbiay/DM-EAD-TNAH-2022/blob/main/encodage.xml) : Le fichier **encodage.xml** contient le premier encodage XML-EAD de l'instrument de recherche instr-rech-20110282_CRMHIDF.odt
- [encodage2.xml](https://github.com/sbiay/DM-EAD-TNAH-2022/blob/main/encodage2.xml) : Le fichier **encodage2.xml** contient la deuxième version de l'encodage de l'instrument de recherche, suite à la transformation avec XSLT.
- [instr-rech-20110282_CRMHIDF.odt](https://github.com/sbiay/DM-EAD-TNAH-2022/blob/main/instr-rech-20110282_CRMHIDF.odt) : Le document **instr-rech-20110282_CRMHIDF.odt** contient instrument de recherche archivistique à convertir en EAD
- [notice-prod-FRAN_NP_005412.xml](https://github.com/sbiay/DM-EAD-TNAH-2022/blob/main/notice-prod-FRAN_NP_005412.xml) : Le fichier **notice-prod-FRAN_NP_005412.xml** contient la notice de producteur enrichie selon le schéma [EAC-CPF](./schemas/cpf.xsd)

# Branches

Chaque groupe a déposé son travail sur une branche distincte, nommée les branches sur le modèle suivant : `groupeN`, le "N" correspondant au numéro de groupe.

**Les nombreuses fusions des branches ont entraîné de conflits, le travail de certains groupes n'a pas pu être ajouté dans son intégralité lors de leur intégration dans l'encodage général. Les travaux sont cependant bien présents et consultables sur les branches. Il n'est pas impossible qu'il manque certains éléments dans le fichier de regroupement de encodages (première version) qui sont cependant bien présents dans les productions des groupes.**

Pour accéder à leurs travaux plus rapidement:
- Le groupe 7 (EAC-CPF) : [groupe7](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe7)
- Le groupe 6 (encodage) : [groupe6](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe6)
- Le groupe 6 (encodage) : [groupe5](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe5)
- Le groupe 6 (encodage) : [groupe4](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe4)
- Le groupe 6 (encodage) : [groupe3](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe3)
- Le groupe 2 (archdesc et indexation) : [groupe2](https://github.com/virgile-reignier/DM-EAD-TNAH-2022/tree/groupe2)
- Le groupe 1 (header, gestion des groupes et de l'encodage) : [groupe1](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe1-Zoe)et [groupe1-xsl](https://github.com/sbiay/DM-EAD-TNAH-2022/tree/groupe1-xsl)


# Fonctionnement de l'encodage en groupe

Suite à un accord sur la façon d'encoder l'instrument de recherche, celui-ci a été traité à l'aide d'un script Python afin d'en créer la structure de base, en particulier dans le cas des *séries* et *sous-séries*. Cela a permis de simplifier la répartition du travail entre les groupes et de réduire le nombre de conflits lors de la fusion de toutes les contributions.

Lors de l'avancée des travaux, l'encodage général initialement prévu posé des difficultés lors de cas particuliers (structures complexes). C'est pourquoi il a été décidé, une fois les travaux des groupes ajoutés, de transformer l'encodage à l'aide de XSLT afin d'affiner la structuration de l'ensemble, et d'enrichir l'instrument de recherche. Cette transformation automatique n'aurait pu être réalisée sans le travail régulier des groupes.

# Issues

Certaines questions d'encodage ont été discutées dans la partie (Issues)[https://github.com/sbiay/DM-EAD-TNAH-2022/issues] du dépôt Github, il est donc possible de suivre une partie des réflexions des groupes à cet endroit. 