# Hosting a streamlit app in AWS with HTTPS

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
- OS: `Ubuntu`
- Instance Type: `t3.small or more`
- Storage: 16GB

Proceed without key pair or create a key pair.

2. Add inbound rules

- Type: `SSH`, Protocol:`TCP`, Port Range: `22`, Source:"Anywhere IPv4/custom"
- Type: `HTTP`, Protocol:`TCP`, Port Range: `80`, Source:"Anywhere IPv4/custom"
- Type: `HTTPS`, Protocol:`TCP`, Port Range: `443`, Source:"Anywhere IPv4/custom" 


## Connect to EC2 Instance

Run the following commands

1. Install Docker on EC2
- `sudo apt update`
- `sudo apt install docker.io -y`
- `sudo systemctl start docker`

2. Check if the docker is running: `ps -aux | grep dock`. Go to the url specified and paste the code to login.

3. Give permissions

- `sudo usermod -aG docker $USER`
- `newgrp docker`
- `nano .env` - paste the local env files used here
- `cat .env` - to check if the file is written and saved

4. Install nginx and certbot

- Install nginx: `sudo apt-get install nginx -y`
- Install the certbot: `sudo apt install certbot -y`
- Stop Nginx so the certbot can run: `sudo service nginx stop`
- Create a certificate for your domain: `sudo certbot certonly --standalone -d website_domain`. Obtain a domain (currently using duckdns), registered to the public IPv4 of the EC2 instance.
- Start nginx again: `sudo service nginx start`
- Clear the current configuration of nginx: `sudo sh -c 'echo -n > /etc/nginx/sites-available/default'`
- Open the nginx config file: `sudo vi /etc/nginx/sites-available/default`.

Paste the following code

```
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}
upstream backend {
    server 127.0.0.1:8501;
    keepalive 64;
}
server {
    listen 80;
    server_name [website_domain](website_url);
    location / {
        return 301 https://$host$request_uri;
    }
}
server {
    listen 443 ssl;
    server_name [website_domain](website_url);
    ssl_certificate /etc/letsencrypt/live/website_domain/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/website_domain/privkey.pem;
    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```
Example: website_domain: garbageclassifier.duckdns.org, website_url: http://garbageclassifier.duckdns.org

- Verify nginx config is valid `sudo nginx -t`
- Restart your nginx server `sudo service nginx restart`
- Check nginx is actually running and listening on 443 `sudo ss -tlnp | grep ':443'`

5. Run Docker Container

- `docker run --env-file .env -d -p 8501:8501 --name container_name repository_name`

6. Dagshub Authentication (if used)

After running the docker container,

- Obtain Container ID `docker ps`
- Get the logs of docker to get the authentication link `docker logs Container ID`
- Incase of link not showing up, try changing pages or reloading and run the previous cmd again. The authentication url can show up.

If the authentication fails due to API, then try getting a new password token and update the .env file.