docker stop suzy-bot
docker rm suzy-bot
docker build -t suzybot-v.0.0.1 .
docker run --name suzy-bot suzybot-v.0.0.1