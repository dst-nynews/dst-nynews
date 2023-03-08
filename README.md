# DataScientest NY News

> Repo principal du projet

## Structure du projet

Ce repo rassemblent tous les éléments du projet et chaque composant a un dossier dédié à la racine du repo.

### les composants du projet 

Chacun des composants de l'architecture (`api`, `db`, ...) du projet a un dossier distinct qui est géré comme si c'était un repo en soi. C'est là qu'on développe les features du projet.

Quand on travaille dans ces dossiers:

  - on ne commit pas sur la branche `main` 
    - on crée une branche pour développer une feature
  - on ne fait pas d'auto-merge:
    - on fait une pull request pour valider les modifications avec les collègues
    - on passe par la branche `staging` avant d'incorporer les modificationss dans la branche `main`. 

### les dossiers de développement

Certains dossiers ne sont pas des composants du projets et servent à ranger des fichiers qui nous aide pour le développement du projet.

- `assets`: pour les fichiers statiques qui nous servent à documenter le projet (images, pdf, ...)
- `data`: si on veut stocker des petits jeux de données bruts (csv, json, ...) pour tester les features qu'on développe
- `notebooks`: pour les Jupyter Notebooks

On n'est pas obligé de passer par une branche ou de faire valider nos modifications quand on travaille sur ces dossiers de développement et sur la documentation du projet.

## Pour démarrer le projet

- clonez ce repo
- installez les librairies Python requises en lançant cette commande dans votre terminal:

  ```shell
  pip install -r requirements-dev.txt 
  ```


