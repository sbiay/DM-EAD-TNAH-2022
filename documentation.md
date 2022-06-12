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

`<unttitle>` et `<unitdate>`: reprise du type et des dates

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


L'élément `<dsc>` (description des sous-composants) contient les éléments `<c>` (composant) qui servent à retranscrire la hiérarchie du plan de classement.

Chaque élément `<c>` a un attribut `@type` qui précise le niveau de l'élément. 

- Le plan de classement du fonds est divisé en deux grandes parties: la "Programmation" et la "Conduite de travaux."" Il a donc été décidé de reprendre cette structure sous la forme de séries organiques, selon la définition du [*Dictionnaire de terminologie archivistique*](https://francearchives.fr/file/4575c619ab1e1e738d81d2249ff8dd4115a3d8cb/ARCHIVES_DE_FRANCE_Dictionnaire_de_terminologie_archivistique.pdf):

> Série organique : Division organique du *fonds*, identifiée par *l'archiviste* lors de son *classement*, qui constitue un ensemble de *dossiers* maintenus groupés parce qu'ils résultent d'une même activité, se rapportent à une même fonction ou à un même sujet, ou revêtent une même forme.

Ainsi, les deux éléments à la racine du `<dsc>` sont des `<c level="series>` qui décrivent les deux séries organiques du plan de classement (Programmation et Conduite de travaux).

- Les composants `<c level="subseries">` servent à décrire ce qui correspond à des sous-séries dans le plan de classement, c'est-à-dire les regroupements par lieux

> Sous-série organique : Subdivision de la série organique
>> *Dictionnaire de terminologie archivistique*

- `<c level="file">` = dossier = boîtes. Si la boîte correspond à un seul édifice, on se contente d'un composant de ce type. S'il y a plusieurs édifices dans une boîte, on créera de nouveaux `<c level="file">` dans ledit composant afin de créer des sous-dossiers (il n'y pas d'attribut `@type` qui y corresponde.)
**Possibilité d'utiliser un level="subgroup" pour un sous-groupe de documents ? ou est-ce que subgroup est en lien avec recordgroup ?**

> Dossier : Ensemble de *documents* constitués, soit organiquement par le *producteur d'archives* pour la conduite ou le traitement d'une affaire, soit par regroupement logique lors du *classement* dans le *service d'archives*.
>> *Dictionnaire de terminologie archivistique*

- `<c level="item">` = article = pièces (item) dans les articles des dossiers

> Article : Ensemble de *pièces* de même *provenance*, se rapportant à un même *objet* ou à une même affaire et dont l'importance matérielle n'excède pas la capacité d'une *unité matérielle de conditionnement*. L'article  constitue tout à la fois une *unité (intellectuelle) de description* et l'*unité ((matérielle)* pour la *cotation*, le *rangement* et la *communication* des *documents d'archives*. 
> Pièce : La plus petite *unité de description* indivisible à la fois matériellement et intellectuellement (feuillet simple ou double, plusieurs feuillets agrafés, cahier, registre...)
>> *Dictionnaire de terminologie archivistique*


- did unitid unittitle unitdate etc


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
				<unitid>20110282/15</unitid>
				<unittitle>Archives nationales</unittitle>
			</did>
			<c level="file">
				<did>
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
