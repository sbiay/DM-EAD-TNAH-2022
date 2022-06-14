# Documentation de l'encodage : le fichier EAD

*En cours de rédaction*

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

Il comprend un premier élément `<creation>`, dans lequel est présenté le contexte de création de l'instrument de recherche en XML-EAD, ainsi que ses auteurs. **pour les auteurs: on met le nom de la promotion comme dans l'encodage actuel ou on met les noms de chaque élève ?**

On y trouve aussi l'élément `<langusage>`, dans lequel on précise la langue utilisée pour l'encodage de l'instrument de recherche dans un (ou des) élément(s) `<language>`. Cet élément doit prendre pour attribut `@langcode` le code (en trois caractères) de langue utilisée selon la norme ISO639-2b.

L'élément `<descrules>` est utilisé pour présentater les normes et règles suivies pour l'encodage de l'instrument de recherche.


### Le revisiondesc : Suivi des versions

L'élément `<revisiondesc>` sert à suivre les différentes modifications qui peuvent être effectuées sur l'instrument de recherche encodé en XML-EAD après sa première publication, ce qui permet un meilleur suivi de ses différentes versions. Dans le cas du présent travail d'encodage, il n'est pas utilisé car l'instrument de recherche est en cours de rédaction, mais il y est placé en prévision des futures modifications qu'il subira.

Chaque modification devra y être indiquée dans un élément `<change>`, dans lequel on en indiquera la date dans un élément `<date>`, et son objet dans un élément `<item>`.

## Le archdesc :  description de l'ensemble documentaire

L'élément `<archdesc>` sert à décrire le fonds dans son ensemble. Il prend un attribut `@level` (obligatoire) qui permet de préciser le niveau description du fonds: dans le cas de la présente édition, le niveau choisi est celui des séries organiques d'après la structure du plan de classement, qui correspond à la définition qu'en donne l'*Abrégé d'archivistique*:
	> La **série organique** est une division organique, constituée par un ensemble de dossiers ou de documents (pièces) réunis ensemble et maintenus groupés parce qu'ils résultent d'une même activité, se rapportent à une même fonction ou à un même sujet ou revêtent une même forme. 

Il comprend en premier lieu un élément `<did>` dans lequel se trouvent les principales informations de description du fonds:

- L'élément `<unitid>` dans lequel sont indiquées les cotes extrêmes des unités documentaires du fonds. Son attribut `@type` permet de donner une indication supplémentaire sur le type de cote dont il s'agit.

- L'élément`<unttitle>` sert à indiquer l'intitulé du fonds.

- L'élément `<unitdate>` sert à indiquer les dates du fonds, ou la période qui le concerne, avec les dates extrêmes dans un attribut `@normal`, dans leur forme normalisée.

- Dans un élément `<origination>`, on décrit le producteur. Celui du fonds étant une organisation et non une personne physique, c'est l'élément `<corpname>` qui a été utilisé pour le décrire.

- Dans le `<physdesc>`, on décrit les documents physiques et leur conditionnement: dans le cas présent, on utilise un élément `<extent>` pour donner des informations sur l'importance matérielle du fonds, et un élément `<dimensions>` pour en préciser les dimensions en mètres linéaires. 

Après le `<did>`, un élément `<accessrestrict>` est utilisé pour préciser les conditions d'accès et de communicabilité aux documents du fonds, qui sont renseignées dans un élément `<p>` (paragraphe).

Les conditions d'utilisations sont ensuite précisées dans un autre élément `<userestrict>`, au sein d'éléments `<p>`.

L'élément `<acqinfo>` sert à décrire l'historique des versements du fonds aux Archives nationales. Chaque versement y est indiqué dans un élément `<p>` distinct s'il y a besoin d'en indiqué plusieurs, et les dates de versements sont indiquées dans des éléments `<date>`.

L'élément `<bioghist>` sert à donner des renseignements sur l'histoire du producteur. Le texte y est structuré en un ou plusieurs paragraphes `<p>` au sein de cet élément.

L'élément `<custodhist>` sert à retracer l'historique de la conservation des documents avant leur versement aux Archives nationales. Chaque étape est indiquée dans un `<p>` distinct.

L'élément `<arrangement>` sert à donner des informations sur la façon dont les archives sont organisées selon le plan de classement. Les différentes explications sont données dans un élément englobant `<list>`, avec un élément `<item>` pour chaque explication.

Les différents types de versements liés au fonds décrit dans l'instrument de recherche sont répartis dans deux types d'éléments:
- Le premier est l'élément `<separatedmaterial>` : il concerne les autres versements liés au fonds décrit qui ont le même producteur.

- Le second est l'élément `<relatedmaterial>` : il concerne les autres versements liés au fonds décrit, mais avec un producteur différent.

Enfin, l'élément`<processinfo>` permet de donner des informations sur le traitement des archives physiques, par exemple sur des éliminations ou des opérations de tri. Chaque type d'information est donné dans un `<p>` distinct.

## Le dsc


L'élément `<dsc>` (description des sous-composants) contient les éléments `<c>` (composant) qui servent à retranscrire la hiérarchie du plan de classement.

### Les composants

Chaque élément `<c>` a un attribut `@type` qui précise le niveau de l'élément. 

- Le plan de classement du fonds est divisé en deux grandes parties: la "Programmation" et la "Conduite de travaux. Il a donc été décidé de reprendre cette structure sous la forme de **séries organiques**, selon la définition du [*Dictionnaire de terminologie archivistique*](https://francearchives.fr/file/4575c619ab1e1e738d81d2249ff8dd4115a3d8cb/ARCHIVES_DE_FRANCE_Dictionnaire_de_terminologie_archivistique.pdf):

	> Série organique : Division organique du *fonds*, identifiée par *l'archiviste* lors de son *classement*, qui constitue un ensemble de *dossiers* maintenus groupés parce qu'ils résultent d'une même activité, se rapportent à une même fonction ou à un même sujet, ou revêtent une même forme (*DTA*).	

Ainsi, les deux éléments à la racine du `<dsc>` sont des `<c level="series>` qui décrivent les deux séries organiques du plan de classement (Programmation et Conduite de travaux).

- Les composants `<c level="subseries">` servent à décrire ce qui correspond à des **sous-séries** dans le plan de classement, c'est-à-dire les regroupements par lieux (Paris, Yvelines, Val-d'Oise...). C'est à l'intérieur de ces sous-séries que l'on trouvera les dossiers et les articles. 

	> Sous-série organique : Subdivision de la série organique (*DTA*).

- Les composants `<c level="file">` servent à décrire les dossiers des **dossiers**, qui correspondent aux édifices dans le plan de classement. Par exemple, pour Paris, on pourra trouver un dossier pour l'Arc de Triomphe, un autre pour les Archives nationales... 
	
	- S'il n'y a pas de dossier correspondant à un édifice particulier, on passera directement à la description par **item**.
	
	- Si le dossier correspond à un seul édifice, on se contente d'un composant de ce type.
	
	- S'il y a plusieurs édifices dans un lieu, on créera de nouveaux `<c level="file">` dans ledit composant afin de créer des sous-dossiers.  

	> Dossier : Ensemble de *documents* constitués, soit organiquement par le *producteur d'archives* pour la conduite ou le traitement d'une affaire, soit par regroupement logique lors du *classement* dans le *service d'archives* (*DTA*).

- Les composants `<c level="item">` servent à décrire les articles (les pièces) qui composent un dossier, ce qui correspond au plus petit niveau de description du plan de classement à encoder. Ce sont des éléments tels que "Dorure de la grille principale (1982)" ou "Réféction des couvertures, versant nord (1981-1982)"

	> Article : Ensemble de *pièces* de même *provenance*, se rapportant à un même *objet* ou à une même affaire et dont l'importance matérielle n'excède pas la capacité d'une *unité matérielle de conditionnement*. L'article  constitue tout à la fois une *unité (intellectuelle) de description* et l'*unité (matérielle)* pour la *cotation*, le *rangement* et la *communication* des *documents d'archives*. 
	> Pièce : La plus petite *unité de description* indivisible à la fois matériellement et intellectuellement (feuillet simple ou double, plusieurs feuillets agrafés, cahier, registre...) (*DTA*).


**Exemples:**

*Les exemples seront enrichis avec les productions des groupes*

Structure de dossier simple:

```XML
<c level="series">
	<did>
		<unittitle>Conduite de travaux</unittitle>
	</did>
	<c level="subseries">
		<did>
			<unittitle>Paris</unittitle>
		</did>
		<c level="file">
			<did>
				<unitid>20110282/14</unitid>
				<unittitle>Arc de Triomphe</unittitle>
			</did>
			<c level="item">
				<did>
					<unittitle>Crypte Kléber....</unittitle>
				</did>
			</c>
			<c level="item">
				<did>
					<unittitle>Plaque commémorative...</unittitle>
				</did>
			</c>
		</c>
	</c>
</c>
```
Structure de dossier complexe:


```XML
<c level="series">
	<did>
		<unittitle>Conduite de travaux</unittitle>
	</did>
	<c level="subseries">
		<did>
			<unittitle>Paris</unittitle>
		</did>
		<c level="file">
			<did>
				<unitid>20110282/15-20110282/21</unitid>
				<unittitle>Archives nationales</unittitle>
			</did>
			<c level="file">
				<did>
					<unitid>20110282/15</unitid>
					<unittitle>Hotel de Rohan</unittitle>
				</did>
				<c level="item">
					<did>
						<unittitle>Dorure de la grille principale...</unittitle>
					</did>
				</c>
				<c level="item">
					<did>
						<unittitle>Réfection du parquet des salons...</unittitle>
					</did>
				</c>
			</c>
			<c level="file">
				<did>
					<unitid>20110282/15</unitid>
					<unittitle>Hotel de Soubise</unittitle>
				</did>
				<c level="item">
					<did>
						<unittitle>Réfection des couvertures...</unittitle>
					</did>
				</c>
				<c level="item">
					<did>
						<unittitle>Réfection des chéneaux...</unittitle>
					</did>
				</c>
			</c>
		</c>
	</c>
</c>
```

### La description des composants

Il est important d'éviter la redondance des informations, ainsi on préfèrera préciser un maximum de choses au plus haut niveau (composant) possible, sans les répéter - sauf si c'est nécessaire - dans ses composants internes. 

La description des composants `<c>` se fait principalement dans l'élément `<did>` (identification et description), qui s'y place en première position. Il contient obligatoirement au moins un élément `<unitid>` ou un élément `<unittitle>`.

- L'élément `<unitid>` contient une cote, ou identifiant. On peut y renseigner les cotes extrêmes d'un regroupement de dossiers par exemple, ou la cote d'un dossier dans lequel on trouvera plusieurs items.

- L'élément `<unittitle>` sert à renseigner l'intitulé de l'élément décrit. Par exemple, dans le cas de "Dorure de la grille principale (1982)", l'intitulé sera: "Dorure de la grille principale", et la date sera placée dans un élément `<unitdate>`
- L'élément `<unitdate>` correspond à une date (pour un item sur une date précise par exemple), ou à des dates extrêmes (par exemple sur toute l'étendue d'un dossier). Il est à utiliser une seule fois par composant. Les dates sont aussi à préciser dans son attribut `@normal` selon la norme ISO 8601 (par exemple AAAA-MM-JJ pour un jour particulier ou AAAA/AAAA pour un intervalle de dates).
- D'autres éléments peuvent aussi y être utilisés si nécessaire: `<langmaterial>` (langue des unités documentaires), `<materialspec>` (particularités de certains types de documents), `<origination>` (origine des documents, comme un producteur), `<physdesc>` (description physique des documents), `<physloc>` (localisation physique des documents), `<repository>` (organisme responsable de l'accès intellectuel).

Après le `<did>`, il est possible, si nécessaire, d'ajouter des informations complémentaires dans les éléments suivants : `<accessrestrict>` (restrictions d'accès), `<accruals>` (accroissements), `<acqinfo>` (informations sur les modalités d'entrée), `<altformavail>` (documents de susbtitution), `<appraisal>` (informations sur l'évaluation des documents), `<arrangement>` (classement), `<bibliography>` (bibliographie), `<bioghist>` (biographie ou histoire), `<controlaccess>` (vedettes et accès contrôlés), `<custodhist>` (historique de la conservation), `<originalsloc>` (existence et lieu de conservation des documents originaux), `<otherfindaid>` (autre instrument de recherche), `<phystech>` (caractéristiques matérielles et contraintes techniques), `<processinfo>` (informations sur le traitement), `<relatedmaterial>` (documents en relation),`<scopecontent>` (présentation du contenu),  `<separatedmaterial>` (documents séparés), `<userestrict>` (restrictions d'utilisation). L'encodage doit cependant rester le plus léger possible : dans la plupart des cas, ces éléments ne sont pas utilisés car ces informations sont renseignées à un plus haut niveau. En cas d'information complémentaire, il est souvent plus simple de se contenter d'un `<scopecontent>`.

Les composants `<c>` sont à imbriquer à la suite du `<did>`, ainsi que des informations complémentaires s'il y en a.

# Documentation de l'encodage : le fichier EAC-CPF
