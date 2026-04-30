## Dockerize streamlit app

1. Open streamlit app folder
2. Create a dockerfile
3. Build docker image `docker build -t image_name` from the app folder path in terminal to 
4. Run docker the image in a docker container using `docker run --env_file .env --name container_name -p8501:8501 container_name` to check if the docker container runs properly

## Push Image to Docker Hub

1. Create a public repository `image_name` in dockerhub.
2. Now in local terminal, run `docker tag image_name repository_name` to tag the image
3. Login to docker, run `docker login`
4. Push the image to docker hub, run `docker push repository_name` 

## Create EC2 instance in AWS
1. Launch new instance
-   