TNAH 2022 : devoir collectif d'EAD
==================================

# Contenu du dépôt
- **consignes.docx** : consignes générales du devoir
- **encodage.xml** : encodage XML-EAD de l'instrument de recherche instr-rech-20110282_CRMHIDF.odt
- **instr-rech-20110282_CRMHIDF.odt** : instrument de recherche archivistique à convertir en EAD
- **notice-prod-FRAN_NP_005412.xml** : notice de producteur à enrichir selon le schéma [EAC-CPF](./schemas/cpf.xsd)
- **referentiels/** : référentiels à utiliser pour l’indexation

# Branches

Le fonctionnement des branches se fera de la façon suivante: chaque groupe aura une branche sur laquelle il pourra déposer son travail, ce qui permettra une meilleure gestion des différents travaux. Libre à vous de vous organiser comme vous le souhaitez pour avancer au mieux au sein de votre groupe !

Merci de nommer les branches sur le modèle suivant : `groupeN`, le "N" correspondant à votre numéro de groupe.

=> Ex: `groupe2`, `groupe3` ...

# Fonctionnement de l'encodage en groupe
- L'encodage en EAD sera à faire entièrement dans le document **encodage.xml** afin d'éviter d'avoir trop de fichiers à gérer (sauf pour l'EAC-CPF). Le fait qu'on travaille tous sur des parties différentes devrait éviter les conflits. S'il y a trop de problèmes, on envisagera une autre solution.
- Pour le groupe 2: il pourra bientôt se lancer dans l'encodage du `<archdesc>`, en se focalisant en particulier sur l'indexation.
- Pour les groupes 3 à 6 : Le groupe 1 travaille actuellement à la mise en place de la structure du plan de classement dans le `<dsc>` avec les `<c>` qui sembleront appropriés. Une fois la structure mise en place, les groupes 3 à 6 pourront ensuite y travailler à l'encodage des parties qui les concernent.
- Pour le groupe 7: il peut dès à présent commencer l'encodage de la notice EAC-CPF, étant donné qu'il est le seul groupe à travailler dessus.