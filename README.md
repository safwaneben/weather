# weather

Pour lancer apicaller avec docker faire :

- cd apicaller
- docker image build -t apicaller .
- docker run -it -p 5000:5000 apicaller

Pour lancer toute l'appli avec docker compose faire à la racine :

- docker compose build
- docker compose up