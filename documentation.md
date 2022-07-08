# Tableau de répartition des personnes par groupe

|Groupe|Tâche|Composition des groupes|
|------|-----|-----------------------|
|Groupe 1|Fichier EAD : production de l’en-tête du fichier (élément <eadheader>) ; contrôle de cohérence et de qualité du fichier EAD ; rédaction d’un fichier externe de documentation explicitant les choix faits|Zoé Cappe, Sébastien Biay, Victor Boby|
|Groupe 2|Fichier EAD : encodage des informations de description globale du versement (pages 2-4) ; indexation du fichier|Maxime Humeau, Virgile Reignier, Valentin De Craene|
|Groupe 3|Fichier EAD : encodage de la description des dossiers conservés sous les cotes 20110282/1 à 20110282/21 inclus (p. 6-12)|Elsa Falcoz, Ariane Menu, Kelly Christensen|
|Groupe 4|Fichier EAD : encodage de la description des dossiers conservés sous les cotes 20110282/22 à 20110828/40 inclus (p.12-18)|Baudoin Davoury, Esteban Sánchez Oeconomo, Teresa Knapowska|
|Groupe 5|Fichier EAD : encodage de la description des dossiers conservés sous les cotes 20110282/41 à 20110282/59 inclus (p. 18-26)|Soline Doat, Margaux Faure, Anaïs Mazoué|
|Groupe 6|Fichier EAD : encodage de la description des dossiers conservés sous les cotes 20110282/60 à 20110282/74 inclus (p. 26-33)|Anahi Haedo, Paul Kervegan, Kristina Konstantinova|
|Groupe 7|Fichier EAC-CPF : enrichissement de la notice du producteur FRAN_NP_005412.xml|Lien Ceard, Fanny Lebreton, Cécile Sajdak|

# Documentation de l'encodage : le fichier EAD

La documentation de l'encodage de l'instrument de recherche en XML-EAD et EAC-CPF selon les normes ISAD(G) et ISAAR(CPF) se base sur l'*Abrégé d'archivistique. Principes et pratiques du métier d'archiviste*, 4e édition, refondue et augmentée, Association des archivistes français, Paris, 2020, et l'[*Encoded Archival Description Tag Library*](https://francearchives.fr/file/0def64f5a10f3f1ae03fdea59399a3e0755ef157/static_1066.pdf), version 2002, Society of American Archivists, 2004

## Le eadheader

L'élément `<eadid>`, en tête de fichier, est obligatoire: il sert à indiquer l'identifiant unique de l'instrument de recherche encodé.

### Le filedesc : Description de l'instrument de recherche d'origine

L'élément `<filedesc>` sert à donner des renseignements sur l'instrument de recherche d'origine, qui est encodé en XML-EAD.

- Au sein de cet élément, on retrouve l'élément `<titlestmt>`. Il englobe l'élément `<titleproper>` (obligatoire), il contient le titre complet de l'instrument de recherche; ainsi que l'élément `<subtitle>`, qui est utilisé pour donner des informations complémentaires sur le type d'instrument de recherche qui est encodé (dans notre cas : "Répertoire numérique"). On y trouve aussi l'élément `<author>` qui sert à décrire les auteurs de l'instrument de recherche d'origine : selon la DTD SIA, ils sont tous regroupés dans un seul élément.

- Vient ensuite l'élément `<editionstmt>` dans lequel se trouve `<edition>`: facultatif, il permet de donner des informations sur la forme de l'instrument de recherche encodé (dans notre cas, une première édition électronique).

- Le `<publicationstmt>` donne des informations sur la publication ou la diffusion de l'instrument de recherche. Il contient l'élément `<publisher>`, qui donne le nom du responsable de publication, son adresse dans un élément `<address>`, et la date de publication dans un élément `<date>`, qui est enrichi d'un attribut `@normal` dans lequel on trouve ladite date sous sa forme normalisée.


### Le profiledesc : Description de l'instrument de recherche encodé en XML-EAD

L'élément `<profiledesc>` sert à donner des renseignements sur l'instrument de recherche encodé en XML-EAD à partir de sa première forme (dans notre cas, donc, une première édition éléctronique).

Il comprend un premier élément `<creation>`, dans lequel est présenté le contexte de création de l'instrument de recherche en XML-EAD, ainsi que ses auteurs.

On y trouve aussi l'élément `<langusage>`, dans lequel on précise la langue utilisée pour l'encodage de l'instrument de recherche dans un (ou des) élément(s) `<language>`. Cet élément doit prendre pour attribut `@langcode` le code (en trois caractères) de langue utilisée selon la norme ISO639-2b.

L'élément `<descrules>` est utilisé pour présentater les normes et règles suivies pour l'encodage de l'instrument de recherche.


### Le revisiondesc : Suivi des versions

L'élément `<revisiondesc>` sert à suivre les différentes modifications qui peuvent être effectuées sur l'instrument de recherche encodé en XML-EAD après sa première publication, ce qui permet un meilleur suivi de ses différentes versions. Dans le cas du présent travail d'encodage, il n'est pas utilisé car l'instrument de recherche est en cours de rédaction, mais il y est placé en prévision des futures modifications qu'il subira.

Chaque modification devra y être indiquée dans un élément `<change>`, dans lequel on en indiquera la date dans un élément `<date>`, et son objet dans un élément `<item>`.

## Le archdesc :  description de l'ensemble documentaire

L'élément `<archdesc>` sert à décrire le fonds dans son ensemble. Il prend un attribut `@level` (obligatoire) qui permet de préciser le niveau description : dans le cas de la présente édition, il s'agit d'une description au niveau du fonds. L'élément se présente donc ainsi : `<archdesc level="fonds">`.

Il comprend en premier lieu un élément `<did>` dans lequel se trouvent les principales informations de description du fonds:

- L'élément `<unitid>` dans lequel sont indiquées les cotes extrêmes des unités documentaires du fonds. Son attribut `@type` permet de donner une indication supplémentaire sur le type de cote dont il s'agit.

- L'élément`<unttitle>` sert à indiquer l'intitulé du fonds.

- L'élément `<unitdate>` sert à indiquer les dates du fonds, ou la période qui le concerne, avec les dates extrêmes, dont la forme normalisée est donnée par l'attribut `@normal`.

- Dans un élément `<origination>`, on décrit le producteur. Celui du présent fonds étant une organisation et non une personne physique, c'est l'élément `<corpname>` qui a été utilisé pour le décrire. Il prend un attribut `@authfilenumber` qui permet de le lier à la notice EAC-CPF du producteur : ici `<corpname authfilenumber="FRAN_NP_005412">Conservation régionale des monuments historiques d'Île-de-France</corpname>`

- Dans le `<physdesc>`, on décrit les documents physiques et leur conditionnement: dans le cas présent, on utilise un élément `<extent>` pour donner des informations sur l'importance matérielle du fonds, et un élément `<dimensions>` pour en préciser les dimensions en mètres linéaires. 

Après le `<did>`, un élément `<accessrestrict>` est utilisé pour préciser les conditions d'accès et de communicabilité aux documents du fonds, qui sont renseignées dans un élément `<p>` (paragraphe).

Les conditions d'utilisations sont ensuite précisées dans un autre élément `<userestrict>`, au sein d'éléments `<p>`.

L'élément `<acqinfo>` sert à décrire l'historique des versements du fonds aux Archives nationales. Chaque versement y est indiqué dans un élément `<p>` distinct s'il y a besoin d'en indiquer plusieurs, et les dates de versements sont indiquées dans des éléments `<date>`.

L'élément `<bioghist>` sert à donner des renseignements sur l'histoire du producteur. Le texte y est structuré en un ou plusieurs paragraphes `<p>` au sein de cet élément. Il peut sembler redondant avec la notice EAC-CPF qui décrit aussi le producteur : cette question a fait l'objet de discussions entre les groupes, et il a été décidé de conserver le `<bioghist>` en plus de la notice en EAC-CPF. En effet, un utilisateur peut ne consulter que l'instrument de recherche et non la notice sur le producteur, ces informations peuvent donc lui être utiles. De même, il est utile de fournir ces informations aussi dans la notice EAC-CPF, car un utilisateur peut la consulter sans nécessairement chercher des informations dans cet instrument de recherche en particulier.

L'élément `<custodhist>` sert à retracer l'historique de la conservation des documents avant leur versement aux Archives nationales. Chaque étape est indiquée dans un `<p>` distinct.

L'élément `<arrangement>` sert à donner des informations sur la façon dont les archives sont organisées selon le plan de classement. Les différentes explications sont données dans un élément englobant `<list>`, avec un élément `<item>` pour chaque explication.

Les différents types de versements liés au fonds décrit dans l'instrument de recherche sont répartis dans deux types d'éléments:

- Le premier est l'élément `<separatedmaterial>` : il concerne les autres versements liés au fonds décrit qui ont le même producteur.

- Le second est l'élément `<relatedmaterial>` : il concerne les autres versements liés au fonds décrit, mais avec un producteur différent.

- L'élément`<processinfo>` permet de donner des informations sur le traitement des archives physiques, par exemple sur des éliminations ou des opérations de tri. Chaque type d'information est donné dans un `<p>` distinct.


## Le dsc

L'élément `<dsc>` (description des sous-composants) contient les éléments `<c>` (composant) qui servent à retranscrire la hiérarchie du plan de classement.

### Les composants : avant la transformation avec XSLT

Chaque élément `<c>` a un attribut `@type` qui précise le niveau de l'élément. 

- Le plan de classement du fonds est divisé en deux grandes parties: la "Programmation" et la "Conduite de travaux". Il a donc été décidé de reprendre cette structure sous la forme de **séries organiques**, selon la définition du [*Dictionnaire de terminologie archivistique*](https://francearchives.fr/file/4575c619ab1e1e738d81d2249ff8dd4115a3d8cb/ARCHIVES_DE_FRANCE_Dictionnaire_de_terminologie_archivistique.pdf):

	> Série organique : Division organique du *fonds*, identifiée par *l'archiviste* lors de son *classement*, qui constitue un ensemble de *dossiers* maintenus groupés parce qu'ils résultent d'une même activité, se rapportent à une même fonction ou à un même sujet, ou revêtent une même forme (*DTA*).	

	Ainsi, les deux éléments à la racine du `<dsc>` sont des `<c level="series>` qui décrivent les deux séries organiques du plan de classement (Programmation et Conduite de travaux).

- Les composants `<c level="subseries">` servent à décrire ce qui correspond à des **sous-séries** dans le plan de classement, c'est-à-dire les regroupements par lieux (Paris, Yvelines, Val-d'Oise...). C'est à l'intérieur de ces sous-séries que l'on trouvera les dossiers et les articles. 

	> Sous-série organique : Subdivision de la série organique (*DTA*).

- Les composants `<c level="file">` servent à décrire les **dossiers**, qui correspondent aux édifices dans le plan de classement. Par exemple, pour Paris, on pourra trouver un dossier pour l'Arc de Triomphe, un autre pour les Archives nationales... 
	
	- S'il y a des édifices dans un lieu, on crée un dossier pour chacun d'entre eux.

	- S'il n'y a pas de dossier correspondant à un édifice particulier, on passera directement à la description par **recordgrp**.

	> Dossier : Ensemble de *documents* constitués, soit organiquement par le *producteur d'archives* pour la conduite ou le traitement d'une affaire, soit par regroupement logique lors du *classement* dans le *service d'archives* (*DTA*).

- Les composants `<c level="recordgrp">` s'insèrent ou dans les **subseries**, ou dans les **dossiers** selon le niveau de description. Ils servent à décrire les groupes de documents, qui ne correspondent ni à des dossiers, ni à des pièces. Leur contenu sera renseigné dans un élément `<scopecontent>`, qui contiendra une `<list>` de tous ses `<items>`.

- Des sous-dossiers peuvent exister dans les `<c level="recordgrp">` (par exemple une sous-division concernant le parc et le château d'un même édifice), dans ce cas des `<c level="subgrp">` seront créés.

- *Les composants `<c level="item">` ne sont pas utilisés ici car ils servent à décrire les articles (les pièces) qui composent un dossier, ce qui correspond au plus petit niveau de description du plan de classement à encoder. Le niveau de description du fonds de l'instrument de recherche ne va pas jusqu'à la pièce, et s'arrête à des groupes de documents.*

	> Article : Ensemble de *pièces* de même *provenance*, se rapportant à un même *objet* ou à une même affaire et dont l'importance matérielle n'excède pas la capacité d'une *unité matérielle de conditionnement*. L'article  constitue tout à la fois une *unité (intellectuelle) de description* et l'*unité (matérielle)* pour la *cotation*, le *rangement* et la *communication* des *documents d'archives*. 
	> Pièce : La plus petite *unité de description* indivisible à la fois matériellement et intellectuellement (feuillet simple ou double, plusieurs feuillets agrafés, cahier, registre...) (*DTA*).


### Exemples : avant la transformation avec XSLT

#### Structure de dossier pour la série Programmation

```XML
<c level="series">
        <did>
          <unitid type="identifiant">20110282/1-20110282/13</unitid>
          <unittitle>Programmation</unittitle>
          <unitdate normal="1956/1991">1956-1991</unitdate>
        </did>
        <c level="subseries">
          <did>
            <unitid type="identifiant">20110282/1-20110282/8</unitid>
            <unittitle>Paris</unittitle>
            <unitdate normal="1966/1989">1966-1989</unitdate>
          </did>
          <c level="recordgrp">
            <did>
              <unitid type="cote-de-consultation">20110282/1</unitid>
              <unittitle></unittitle>
              <unitdate normal="1967/1987">1967-1987</unitdate>
            </did>
            <scopecontent>
              <list>
                <item>Arc de triomphe (1968-1987)</item>
                <item>Archives nationales (1968-1987)</item>
                <item>Bibliothèque nationale (1970-1985)</item>
                <item>Chapelle expiatoire (1983-1986)</item>
                <item>Collège de France (1967-1984)</item>
                <item>Colonne d'Austerlitz, place Vendôme (1969-1981)</item>
                <item>Colonne de Juillet, place de la Bastille (1971-1986)</item>
              </list>
            </scopecontent>
          </c>
          <c level="recordgrp">
            <did>
              <unitid type="cote-de-consultation">20110282/2</unitid>
              <unittitle></unittitle>
              <unitdate normal="1968/1988">1968-1988</unitdate>
            </did>
            <scopecontent>
              <list>
                <item>Conservatoire national supérieur de musique (1970-1986)</item>
                <item>Conservatoire national des arts et métiers (photographies) (1970-1981)</item>
                <item>Conservatoire national supérieur d'art dramatique (1968-1985)</item>
                <item>Cour des comptes (1968-1977)</item>
                <item>Ecole nationale supérieure des arts décoratifs (ENSAD) (1969-1986)</item>
                <item>Ecole nationale supérieure des Beaux-Arts, porte du château d'Anet et vestiges de l'Hôtel de la Trémoille (1969-1988)</item>
              </list>
            </scopecontent>
          </c>
        </c>  
</c>
```

#### Structure de dossier pour la série Dossiers de travaux

##### Quand un dossier ne comporte qu'un édifice

```xml
		<c level="subseries">
          <did>
            <unitid type="identifiant">20110282/14-20110282/59</unitid>
            <unittitle>Paris</unittitle>
            <unitdate normal="1970/1994">1970-1998</unitdate>
          </did>
          <c level="file">
            <did>
              <unitid type="cote-de-consultation">20110282/14</unitid>
              <unittitle>Arc de Triomphe</unittitle>
              <unitdate normal="1970/1989">1970-1989</unitdate>
            </did>
            <scopecontent>
              <list>
                <item>Crypte Kléber, comptoir de vente et rénovation des circulations (1972)</item>
                <item>Plaque commémorative pour les militaires morts en Afrique du Nord (1972)</item>
                <item>Protection anti-suicide (1970-1974)</item>
                <item>Pavage de l'esplanade (1984)</item>
                <item>Restauration des grilles et chéneaux en pierre de la terrasse (1986-1987)</item>
                <item>Remise en état des fosses à fleurs (1987)</item>
                <item>Etudes destinées à assurer la stabilité et à permettre la restauration de l’édifice (1987-1988)</item>
                <item>Ravalement et restauration des façades et des voûtes (1987-1988)</item>
                <item>Etudes préparatoires à la restauration de l’édifice : étude géotechnique, investigations topographiques, mesures de vibration, mesures altimétriques, auscultation, procès-verbaux d’essais (1987-1989)</item>
              </list>
            </scopecontent>
          </c>
        </c>
```

##### Quand un dossier comporte plusieurs édifices

```XML
	<c level="series">
        <did>
          <unitid type="identifiant">20110282/14-20110282/74</unitid>
          <unittitle>Dossiers de travaux</unittitle>
          <unitdate normal="1962/1993">1962-1998</unitdate>
        </did>
        <c level="subseries">
          <did>
            <unitid type="identifiant">20110282/14-20110282/59</unitid>
            <unittitle>Paris</unittitle>
            <unitdate normal="1970/1994">1970-1998</unitdate>
          </did>
          <c level="file">
            <did>
              <unitid type="identifiant">20110282/15-20110282/21</unitid>
              <unittitle>Archives nationales</unittitle>
              <unitdate normal="1974/1998">1974-1998</unitdate>
            </did>
            <c level="recordgrp">
              <did>
                <unitid type="cote-de-consultation">20110282/15</unitid>
                <unittitle>Hôtel de Rohan</unittitle>
                <unitdate normal="1982/1988">1982-1988</unitdate>
              </did>
              <scopecontent>
                <list>
                  <item>Dorure de la grille principale (1982)</item>
                  <item>Réfection du parquet des salons (1982)</item>
                  <!-- ... -->
                </list>
              </scopecontent>
            </c>
            <c level="recordgrp">
              <did>
                <unitid type="cote-de-consultation">20110282/15</unitid>
                <unittitle>Hôtel de Soubise </unittitle>
                <unitdate normal="1981/1990">1981-1990</unitdate>
              </did>
              <scopecontent>
                <list>
                  <item>Réfection des couvertures, versant nord (1981-1982)</item>
                  <item>Réfection des chéneaux et brisis à l’aplomb des appartements de la princesse, versant sud et ouest sur chéneau encaissé côté cour de Clisson. (1981-1985)</item>
                  <!-- ... -->
                </list>
              </scopecontent>
            </c>
          </c>
        </c>
    </c>
```


### La description des composants : avant la transformation avec XSLT
#### Le did
Il est important d'éviter la redondance des informations, ainsi on préfèrera préciser un maximum de choses au plus haut niveau (composant) possible, sans les répéter - sauf si c'est nécessaire - dans ses composants internes. 

La description des composants `<c>` se fait principalement dans l'élément `<did>` (identification et description), qui s'y place en première position. Il contient obligatoirement au moins un élément `<unitid>` ou un élément `<unittitle>`.

- L'élément `<unitid>` contient une cote, ou identifiant. On peut y renseigner les cotes extrêmes d'un regroupement de dossiers par exemple, ou la cote d'un dossier dans lequel on trouvera plusieurs items. S'il s'agit d'un intervalle de cotes (par exemple : "20110282/15-20110282/21"), on ajoutera un attribut `@type="identifiant` à l'`<unitid>`. S'il s'agit d'une cote simple (par exemple : "20110282/15"), on ajoutera un attribut `@type="cote-de-consultation"`.

- L'élément `<unittitle>` sert à renseigner l'intitulé de l'élément décrit. Par exemple, dans le cas des Archives nationales à Paris, l'intitulé sera: "Archives nationales".

- L'élément `<unitdate>` correspond à une date (pour un item sur une date précise par exemple), ou à des dates extrêmes (par exemple sur toute l'étendue d'un dossier). Il est à utiliser une seule fois par composant. Les dates sont aussi à préciser dans son attribut `@normal` selon la norme [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601#La_notation_abr%C3%A9g%C3%A9e) (par exemple AAAA-MM-JJ pour un jour particulier ou AAAA/AAAA pour un intervalle de dates).

- D'autres éléments peuvent aussi y être utilisés si nécessaire: `<langmaterial>` (langue des unités documentaires), `<materialspec>` (particularités de certains types de documents), `<origination>` (origine des documents, comme un producteur), `<physdesc>` (description physique des documents), `<physloc>` (localisation physique des documents), `<repository>` (organisme responsable de l'accès intellectuel).

#### Après le did

Après le `<did>`, il est possible, si nécessaire, d'ajouter des informations complémentaires dans les éléments suivants : `<accessrestrict>` (restrictions d'accès), `<accruals>` (accroissements), `<acqinfo>` (informations sur les modalités d'entrée), `<altformavail>` (documents de susbtitution), `<appraisal>` (informations sur l'évaluation des documents), `<arrangement>` (classement), `<bibliography>` (bibliographie), `<bioghist>` (biographie ou histoire), `<controlaccess>` (vedettes et accès contrôlés), `<custodhist>` (historique de la conservation), `<originalsloc>` (existence et lieu de conservation des documents originaux), `<otherfindaid>` (autre instrument de recherche), `<phystech>` (caractéristiques matérielles et contraintes techniques), `<processinfo>` (informations sur le traitement), `<relatedmaterial>` (documents en relation),`<scopecontent>` (présentation du contenu),  `<separatedmaterial>` (documents séparés), `<userestrict>` (restrictions d'utilisation). L'encodage doit cependant rester le plus léger possible : dans la plupart des cas, ces éléments ne sont pas utilisés car ces informations sont renseignées à un plus haut niveau. En cas d'information complémentaire, il est souvent plus simple de se contenter d'un `<scopecontent>`.

Les composants `<c>` sont à imbriquer à la suite du `<did>`, ainsi que des informations complémentaires s'il y en a.

Les sous-dossiers et articles faisant partie des dossiers (dans les longs parapgraphes sous forme d'énumération d'items) sont à renseigner dans une `<list>` dans un `<scopecontent>` au sein du composant concerné. Chaque élément distinct correspond à un `<item>`. *Pour illustration, voir les exemples ci-dessus.*



### Les composants et la description des composants : après la transformation avec XSLT

Les choix d'encodage qui ont été faits et appliqués sur l'instrument de recherche ont fait l'objet de nombreuses discussions, en particulier le `<scopecontent>` contenant les listes d'items qui semblait peu adapté aux exigences de l'ISAD(G) et de l'EAD. Le choix a donc été fait de transformer automatiquement avec XSLT les productions des groupes en une version encodée de l'instrument de recherche qui paraissait plus adaptée.

En effet, ces listes d'items (correspondant aux paragraphes dans l'instrument de recherche) correspondaient à des sous-niveaux qui pouvaient être structurés plus finement en EAD à l'aide de `<c level="subgroup">`. Ils se présente sous une forme régulière ("Nom de lieu" suivi de ":", et listes d'items régulières grâce au travail des groupes) qui permet leur traitement de façon automatisée. Ainsi, les longues listes de lieux et dossiers deviennent des composants plus précis, avec une description plus fine qui leur est propre (notamment grâce aux `<unitdate>` qui peuvent maintenant être renseignés). Ce travail avait été commencé dans les productions des groupes (voir pour cela l'issue #10), mais des contraintes de temps nous ont imposé de préférer l'automatisation de la transformation.

Le nouvel encodage se structure :

- Les composants de niveau *série* (`<c level="series>`) et *sous-série* (`<c level="subseries">`) ont conservé le même rôle que dans l'ancien encodage : ils correspondent respectivement aux deux séries du plan de classement (Programmation et Conduite de travaux), et aux divisions par lieux. 
- Les `<c level="file">` correspondant aux divisions par édifices ou institutions.
- Les `<c level="recordgrp">` sont les divisions au sein des dossiers édifices, correspondant soit à une division par édifice ou type de documents, soit par cote quand la séparation des items est marquée par un changement d'identifiant.
- Dans l'encodage initial, les listes d'items présentes dans les différentes divisions étaient renseignées dans un élément `<scopecontent>`, qui contenait une `<list>` et un ou plusieurs `<item>`. La structure des items était pourtant complexe, certains items pouvant eux-mêmes être sous-divisés en un dossier correspondant à un édifice, contenant lui-même plusieurs sous-divisions. C'est pourquoi nous avons créé des `<c level="subgrp">` pour chacun de ces éléments.
- Ces derniers sont complétés par un `<scopecontent>` contenant une liste d'`<item>` dans les cas où il contient une ou plusieurs sous-disions. 

Ces modifications précisent la structuration des dossiers entre eux, et ainsi le risque de perte d'informations est moins important.Elles nous ont aussi permis d'ajouter les notes de bas de page dans des éléments `<scopecontent>` avec des paragraphes `<p>`.

### Exemples : après la transformation avec XSLT


#### Structure de dossier pour la série Programmation

```XML
<c level="series">
                <did>
                    <unitid type="identifiant">20110282/1-20110282/13</unitid>
                    <unittitle>Programmation</unittitle>
                    <unitdate normal="1956/1991" calendar="gregorian" era="ce">1956-1991</unitdate>
                </did>
                <c level="subseries">
                    <did>
                        <unitid type="identifiant">20110282/1-20110282/8</unitid>
                        <unittitle>Paris</unittitle>
                        <unitdate normal="1966/1989" calendar="gregorian" era="ce">1966-1989</unitdate>
                    </did>
                    <c level="recordgrp">
                        <did>
                            <unitid type="cote-de-consultation">20110282/1</unitid>
                            <unittitle/>
                            <unitdate normal="1967/1987" calendar="gregorian" era="ce">1967-1987</unitdate>
                        </did>
                        <c level="subgrp">
                            <did>
                                <unittitle>Arc de triomphe</unittitle>
                                <unitdate normal="1968/1987">1968-1987</unitdate>
                            </did>
                        </c>
                        <!-- ... -->
                        <c level="subgrp">
                            <did>
                                <unittitle>Colonne de Juillet, place de la Bastille</unittitle>
                                <unitdate normal="1971/1986">1971-1986</unitdate>
                            </did>
                            <scopecontent>
                                <p>Photographies [1983] conservées à la photothèque de 
                                    l'Opérateur du patrimoine et des projets immobiliers de la Culture.</p>
                            </scopecontent>
                        </c>
                    </c>
                    <c level="recordgrp">
                        <did>
                            <unitid type="cote-de-consultation">20110282/2</unitid>
                            <unittitle/>
                            <unitdate normal="1968/1988" calendar="gregorian" era="ce">1968-1988</unitdate>
                        </did>
                        <c level="subgrp">
                            <did>
                                <unittitle>Conservatoire national supérieur de musique</unittitle>
                                <unitdate normal="1970/1986">1970-1986</unitdate>
                            </did>
                        </c>
                        <c level="subgrp">
                            <did>
                                <unittitle>Conservatoire national des arts et métiers (photographies)</unittitle>
                                <unitdate normal="1970/1981">1970-1981</unitdate>
                            </did>
                        </c>
                        <!-- ... -->
                        <c level="subgrp">
                            <did>
                                <unittitle>Ecole nationale supérieure des Beaux-Arts, porte du château d'Anet et vestiges de l'Hôtel de la Trémoille</unittitle>
                                <unitdate normal="1969/1988">1969-1988</unitdate>
                            </did>
                        </c>
                    </c>
```

#### Structure de dossier pour la série Dossiers de travaux

##### Quand un dossier ne comporte qu'un édifice

```xml
                <c level="subseries">
                    <did>
                        <unitid type="identifiant">20110282/14-20110282/59</unitid>
                        <unittitle>Paris</unittitle>
                        <unitdate normal="1970/1994" calendar="gregorian" era="ce">1970-1998</unitdate>
                    </did>
                    <c level="file">
                        <did>
                            <unitid type="cote-de-consultation">20110282/14</unitid>
                            <unittitle>Arc de Triomphe</unittitle>
                            <unitdate normal="1970/1989" calendar="gregorian" era="ce">1970-1989</unitdate>
                        </did>
                        <c level="subgrp">
                            <did>
                                <unittitle>Crypte Kléber, comptoir de vente et rénovation des circulations</unittitle>
                                <unitdate normal="1972">1972</unitdate>
                            </did>
                        </c>
                        <!-- ... -->
                        <c level="subgrp">
                            <did>
                                <unittitle>Etudes préparatoires à la restauration de l’édifice</unittitle>
                                <unitdate normal="1987/1989">1987-1989</unitdate>
                            </did>
                            <scopecontent>
                                <p>Étude géotechnique, investigations topographiques, mesures de vibration, mesures altimétriques, auscultation, procès-verbaux d’essais.</p>
                            </scopecontent>
                        </c>
                    </c>
                </c>
```

##### Quand un dossier comporte plusieurs édifices

```XML
            <c level="series">
                <did>
                    <unitid type="identifiant">20110282/14-20110282/74</unitid>
                    <unittitle>Dossiers de travaux</unittitle>
                    <unitdate normal="1962/1993" calendar="gregorian" era="ce">1962-1998</unitdate>
                </did>
                <c level="subseries">
                    <did>
                        <unitid type="identifiant">20110282/14-20110282/59</unitid>
                        <unittitle>Paris</unittitle>
                        <unitdate normal="1970/1994" calendar="gregorian" era="ce">1970-1998</unitdate>
                    </did>
                    <!-- ... -->
                    <c level="file">
                        <did>
                            <unitid type="identifiant">20110282/15-20110282/21</unitid>
                            <unittitle>Archives nationales</unittitle>
                            <unitdate normal="1974/1998" calendar="gregorian" era="ce">1974-1998</unitdate>
                        </did>
                        <c level="recordgrp">
                            <did>
                                <unitid type="cote-de-consultation">20110282/15</unitid>
                                <unittitle>Hôtel de Rohan</unittitle>
                                <unitdate normal="1982/1988" calendar="gregorian" era="ce">1982-1988</unitdate>
                            </did>
                            <c level="subgrp">
                                <did>
                                    <unittitle>Dorure de la grille principale</unittitle>
                                    <unitdate normal="1982">1982</unitdate>
                                </did>
                            </c>
                            <c level="subgrp">
                                <did>
                                    <unittitle>Réfection du parquet des salons</unittitle>
                                    <unitdate normal="1982">1982</unitdate>
                                </did>
                            </c>
                            <!-- ... -->
                        </c>
                        <c level="recordgrp">
                            <did>
                                <unitid type="cote-de-consultation">20110282/15</unitid>
                                <unittitle>Hôtel de Soubise </unittitle>
                                <unitdate normal="1981/1990" calendar="gregorian" era="ce">1981-1990</unitdate>
                            </did>
                            <c level="subgrp">
                                <did>
                                    <unittitle>Réfection des couvertures, versant nord</unittitle>
                                    <unitdate normal="1981/1982">1981-1982</unitdate>
                                </did>
                            </c>
                            <c level="subgrp">
                                <did>
                                    <unittitle>Réfection des chéneaux et brisis à l’aplomb des appartements de la princesse, versant sud et ouest sur chéneau encaissé côté cour de Clisson.</unittitle>
                                    <unitdate normal="1981/1985">1981-1985</unitdate>
                                </did>
                            </c>
                        </c>
                    </c>
                </c>
            </c>        
```


# Documentation de l'encodage : le fichier EAC-CPF
Nous avons souhaité décrire les ajouts et les modifications apportés à la notice d’autorité d’origine consacrée à la Conservation régionale des monuments historiques d’Île-de-France. 

- `<sources>` : cet élément contient des éléments `<source>`, qui représentent chacun une ressource dont on a tiré des informations utiles à l'élaboration de la notice. Chaque élément `<source>` est porteur d'un attribut `@xmlns:xlink` permettant le rattachement au namespace [xlink](https://www.w3.org/1999/xlink), ainsi qu'un attribut `@xlink:href` dont la valeur est l'URL de la ressource en question. Chaque élément `<source>` contient un élément `<sourceEntry>` contenant l'intitulé de la source et sa date de consultation, ainsi qu'un élément `<descriptiveNote>` qui permet de préciser sommairement, en texte libre structuré par un ou des éléments `<p>`, quelles informations ont été trouvées grâce à cette source.

- `<conventionDeclaration>` :  Dans des éléments `<conventionDeclaration>` distincts, on renseigne les normes et les référentiels qui ont permis d’établir la notice d’autorité. Chaque élément `<conventionDeclaration>` contient un élément `<abbreviation>` et un élément `<citation>`. Dans l’élément `<abbreviation>`, on précise la forme abrégée du nom de la norme. Dans l’élément `<citation>`, on précise la forme développée du nom de la norme. Pour les référentiels, nous n'avons pas mis d'élément `<abbreviation>`. 

- `<nameEntry>` : Le premier `<nameEntry>` contient la forme autorisée du nom, ce que l'on précise grâce à l'attribut `@localType` de valeur "autorisée". La forme autorisée a été établie à partir de la notice d’autorité [*Région. Conservation régionale des monuments historiques*](https://aaf.ica-atom.org/region-conservation-regionale-des-monuments-historiques) du référentiel AToM (Référentiel pour l’administration locale). Cette notice suit la norme NF Z 44-060 relative à la forme et à la structure des vedettes des collectivités, ce qui a motivé notre choix. Les autres éléments `<nameEntry>` contiennent les formes alternatives du nom. On indique les dates d’existence correspondantes étant donné que Puisque la notice d’autorité porte sur un producteur qui a changé de nom au fur et à mesure de son existence, on pourra indiquer, le cas échéant, les dates d'existence du producteur sous tel ou tel nom. Pour ce faire, on utilise un élément `<useDates>` contenant un élément `<dateRange>`. Ce dernier contient un élément `<fromDate>` et un élément `<toDate>`, qui permettent respectivement d'indiquer le début et la fin de la période concernée. Ces deux derniers éléments sont porteurs d'un attribut `@standardDate` dont la valeur est la date au format standard, tel que définit par la norme ISO 8601. Les différents `<nameEntry>` constituent des points d'accès à la notice d’autorité qui pourront notamment être mobilisés pour effectuer une recherche avancée. 

- `<biogHist>` : En plus de l'élément `<biogHist>` de la notice d’autorité, un historique du producteur est présent dans l'instrument de recherche, au sein de l’élément `<bioghist>`. Dans la salle des inventaires virtuels, un usager n’ira pas forcément lire, dans un premier temps, la notice d’autorité. C’est pourquoi conserver un historique du producteur est nécessaire pour que l’usager puisse pleinement comprendre l’instrument de recherche. Toutefois, dans la notice d’autorité, l’historique du producteur est plus complet.

- `<cpfRelation>` : Deux relations d’identité sont présentes. Elles permettent d’aligner les données des Archives nationales sur des référentiels extérieurs produits par d'autres institutions patrimoniales, par exemple la Bibliothèque nationale de France. Ainsi, les usagers peuvent avoir une vision globale du producteur des archives, non limitée aux activités et fonctions dont sont issus les fonds d’archives. Dans la mesure du possible, les formes autorisées du nom et les dates d’existence proviennent des référentiels extérieurs à ceux des Archives nationales. Dans la cas où ces informations sont inconnues, les informations de la notice d’autorité des Archives nationales ont été utilisées. 

- Par ailleurs, nous avons essayé de compléter du mieux possible les informations de datation.