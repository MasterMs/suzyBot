docker stop suzy-bot
docker rm suzy-bot
docker build -t https://github.com/MasterMs/suzyBot.git .
docker run --name suzy-bot suzy-bot --env-file .env


