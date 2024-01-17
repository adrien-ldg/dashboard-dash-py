**DASHBOARD: évolution des stratégies énergétiques de l'Union Européenne**


Présentation du sujet:

Au cours de ce projet, nous nous sommes penchés sur l'évolution des stratégies énergétiques des pays membres de l'Union Européenne. Dans le but de répondre à cette question cruciale, nous avons entrepris des recherches pour identifier un ensemble de données pertinent sur Kaggle qui soit en adéquation avec notre problématique.

Nos recherches nous a conduit à la découverte d'un ensemble de données adapté à notre sujet : le jeu de données intitulé "Global Data on Sustainable Energy (2000-2020)" disponible sur la plateforme Kaggle. Ce jeu de données est une source riche d'informations, couvrant la période allant de l'an 2000 à 2020, et il englobe une variété de données pertinentes liées à la durabilité énergétique à l'échelle mondiale.

En utilisant ce jeu de données, nous avons pu mener une analyse approfondie pour évaluer l'évolution des politiques et des tendances énergétiques dans les pays de l'Union Européenne sur cette période. Nous avons examiné divers indicateurs, statistiques et métriques pour tirer des conclusions et obtenir des informations précieuses concernant les choix stratégiques en matière d'énergie adoptés par les pays européens.

Ce jeu de données a servi de base à notre projet, nous permettant d'explorer et de visualiser les données pour mieux comprendre comment les stratégies énergétiques ont évolué au fil du temps au sein de l'Union Européenne. Notre analyse repose sur une démarche rigoureuse, et nous avons utilisé des outils et des techniques appropriés pour présenter clairement les résultats de notre étude.



User Guide:


L'ensemble de notre projet se trouve dans le fichier rendu.
Pour récupérer l'entiéreté des fichiers du projet sur sa machine, il faut le cloner grâce à la commande:


avec une clé ssh:
$ git clone git@git.esiee.fr:lindebea/projet_py.git

avec https:
$ git clone https://git.esiee.fr/lindebea/projet_py.git

Le dashboard sera lancé avec la commande:

$ python main.py


Developper Guide:

Une fois le projet récupéré, vous obtiendrez un code avec l'architecture suivant:

![Architecture du projet](images/architecture.png)

Comme illustré dans ce graphique, notre projet commence par le processus d'acquisition de données à partir de la plateforme Kaggle. La récupération des données est automatisée grâce à un ensemble de scripts Python situés dans le répertoire "download". Ces scripts permettent de télécharger le dataset de manière dynamique, c'est-à-dire que le programme Python effectue cette tâche de manière autonome.

Plus précisément, le répertoire "download" contient quatre fichiers Python dédiés à la récupération et au stockage du dataset. Ces fichiers se chargent de gérer le téléchargement et de placer les données dans le répertoire "dataset" de notre projet.

L'étape suivante est le prétraitement des données. Ce processus de prétraitement est essentiel pour nettoyer les données en éliminant les valeurs manquantes, ainsi que pour supprimer les échantillons ou les colonnes qui ne sont pas pertinentes pour notre analyse. Les fichiers Python situés dans le répertoire "dataset" se chargent de cette phase de nettoyage et de transformation des données.

Vous trouverez aussi un fichier nommé "requirements.txt" dans notre projet. Ce fichier répertorie les bibliothèques Python nécessaires au bon fonctionnement de notre dashboard. Le fichier "file.py" récupère les bibliothèques listées dans "requirements.txt" et les stocke dans une liste. Ensuite, le fichier "import_py.py" vérifie si ces bibliothèques sont installées et les installe automatiquement si elles ne le sont pas.

Passons ensuite à la création de notre dashboard interactif. Notre dashboard est divisé en trois composantes distinctes :

- Le répertoire "pages" : Ce répertoire contient les mises en page (layouts) de notre dashboard. Nous avons créé quatre mises en page distinctes pour notre projet, chacune ayant son propre fichier Python.

- Les composants : Dans notre dashboard, nous utilisons un composant crucial, une barre de navigation, qui permet aux utilisateurs de passer d'une mise en page à une autre.

- "main.py" : Ce fichier est le point central de notre application. Il est responsable de la création, de la configuration et du lancement de notre dashboard. Il relie tous les éléments mentionnés précédemment et permet aux utilisateurs d'accéder au dashboard final.

Enfin, pour lancer et déployer notre application, nous utilisons le fichier "main.py" comme point d'entrée. Il fait le lien entre tous les composants, configurations et données, offrant ainsi aux utilisateurs l'accès au dashboard interactif final. 


Analyse:

La qualité et la quantité des données disponibles dans notre jeu de données nous permettent de poser une problématique pertinente : Y a-t-il une tendance énergétique dans les pays d'Europe au cours des 20 dernières années ? Celle-ci a-t-elle une quelconque corrélation avec le nombre d'habitants de ces pays, ainsi que leur PIB ou encore leurs émissions de CO2 ?
Nous avons réalisé plusieurs graphiques dans notre tableau de bord (dashboard) qui nous permettent d'établir des conclusions pour répondre à cette problématique.

Notre bar chart nous permet de visualiser, pour une année précise entre 2000 et 2020, la quantité des données que l'on définit en ordonnée pour tous les pays d'Europe. Par exemple, on remarque que, au cours des 20 dernières années, les seuls vrais producteurs d'énergie fossile sont l'Allemagne, l'Espagne, l'Italie et la Pologne. En ce qui concerne le nucléaire, seul la France en produit énormément, avec l'Allemagne loin derrière, et donc la production a nettement baissé au cours des dernières années. Pour ce qui est des énergies renouvelables, de nombreux pays se démarquent, mais on remarque une forte hausse dans toute l'Europe de la production de cette nouvelle forme d'énergie.

Sur un autre onglet, notre scatter plot nous permet d'observer plus clairement la formation de tendances au fil du temps. En effet, on remarque que les émissions de CO2 en Europe sont en quasi-constante baisse depuis 2005. On observe également que c'est à partir de cette époque que le PIB par habitant a commencé à croître de manière significative (malgré une croissance du PIB relativement stable) et que l'intensité énergétique a commencé à baisser.

Par ailleurs, sur notre onglet intitulé "Courbe de tendance", on peut réaliser des observations en examinant spécifiquement la corrélation entre deux variables. Ce graphique nous permet, entre autres, de voir l'importance du PIB par habitant dans l'optique d'une potentielle transition énergétique, car bien que plus responsable pour la planète, les nouvelles technologies et sources d'énergie sont bien plus coûteuses que les sources plus traditionnelles.

Notre jeu de données met donc en avant ici que la situation économique globale des habitants d'Europe s'améliorant au cours des deux dernières décennies tandis que les énergies renouvelables commencent à se populariser aussi de plus en plus tandis que le nucléaire et les énergies fossiles continuent lentement mais sûrement à être mises de côté.

