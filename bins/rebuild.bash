docker stop suzy-bot
docker rm suzy-bot
if [[$1 == '-f']]
then
  docker build -t suzybot -v.0.0.1 $2
else
  docker build -t suzybot -v.0.0.1 https://github.com/MasterMs/suzyBot.git
fi
docker run --name suzy-bot suzybot-v.0.0.1


