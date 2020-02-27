docker stop $1
docker rm $1 
docker build -t $1 . 
docker run --name $1 $1
