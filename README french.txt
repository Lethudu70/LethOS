LethOS - README

Description:
LethOS est un système d'exploitation simulé conçu pour offrir une expérience interactive via une ligne de commande. Ce programme permet de simuler diverses fonctionnalités telles que la conversion de température, l'exploration de fichiers, la gestion d'un disque virtuel, et plus encore.

Fonctionnalités principales :
1. **Conversion de température**: Convertissez la température dans différentes unités (Celsius, Fahrenheit, Kelvin) vers l'unité personnalisée °W.
2. **Disque virtuel**: Créez un disque virtuel et copiez des fichiers exécutables dans ce disque.
3. **Son de démarrage et d'arrêt**: Lors du démarrage, un son de démarrage Windows XP est joué. Idem pour l'arrêt.
4. **Écran de démarrage**: Affichage d'une barre de progression lors du démarrage du système.
5. **Options de gestion du système**: Vous pouvez éteindre, redémarrer ou retourner au shell via un menu interactif.
6. **Affichage de la date et de l'heure**: Commandes pour afficher la date du jour et l'heure actuelle en temps réel.
7. **Faits aléatoires**: Une commande pour afficher des faits intéressants et aléatoires à chaque appel.
8. **Horloge en temps réel**: Affiche l'heure actuelle avec mise à jour en temps réel sur la console.
9. **Equipé du dernier Leth Exploro**: Un explorateur propre au programme.
Commandes disponibles :
- **help**: Affiche la liste des commandes disponibles.
- **clear**: Efface l'écran.
- **echo [texte]**: Affiche le texte spécifié.
- **ls**: Liste les fichiers et dossiers du répertoire actuel.
- **shutdown**: Ouvre les options d'arrêt (Éteindre, Redémarrer, Retourner au Shell).
- **explorer**: Ouvre l'explorateur de fichiers.
- **wedo_converter**: Lance le convertisseur de température vers l'unité °W.
- **info**: Affiche des informations système.
- **play**: Joue un fichier son ou vidéo.
- **date**: Affiche la date du jour.
- **random_fact**: Affiche un fait aléatoire.
- **clock**: Affiche l'heure actuelle en temps réel.
- **joke**: Affiche une blague aléatoire.
- **calculator**: Lance une calculatrice simple.

Instructions d'installation :
1. Assurez-vous que Python 3.x est installé sur votre machine.
2. Placez ce programme dans un répertoire de votre choix.
3. Placez les fichiers sonores nécessaires (Windows XP Startup, Shutdown et Error) dans le répertoire `C:\sound for LethOS\` pour que les sons soient joués correctement.
4. Lancez le programme via la commande `python lethos.py` ou `python3 lethos.py` dans votre terminal.

Avertissements :
- Ce programme est conçu pour fonctionner uniquement sur des systèmes Windows en raison de l'utilisation des chemins de fichiers spécifiques et de la bibliothèque `winsound` pour la gestion des sons.
- Les sons et les autres fichiers nécessaires doivent être présents dans les chemins spécifiés pour éviter les erreurs lors de l'exécution.

Auteur :
- Développé par Leth.

License :
- Ce programme est fourni sous la licence MIT.
