cd $1
docker stop suzy-bot
docker rm suzy-bot
docker build -t suzy-bot . 
docker run --name suzy-bot suzy-bot

