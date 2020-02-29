docker stop suzy-bot
docker rm suzy-bot
docker build -t masterms/suzyBot .
docker run --name suzy-bot suzy-bot --env-file .env


