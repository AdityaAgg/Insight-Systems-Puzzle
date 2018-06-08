# Steps

## Error 1

1. After attempting the build instructions and noticing that I was getting a 502 gateway error, I decided to look at the nginx container log through:

`sudo docker logs -t systems-puzzle_nginx_1`

2. I noticed from the previous step that nginx was not able to hit port 5001 on the flaskapp container. Thus, I ran the app locally to check if flaskapp runs on 5001, and I found out it actually ran on 5000.

3. I modified the flaskapp.conf file which has the configuration for nginx interacting with the flaskapp server. I changed http://flaskapp:5001 to http://flaskapp:5000. Then I reloaded the configuration through `nginx -s reload` inside the bash shell for the nginx docker container. then I hit the web page again on my browser and found that I could see the form. This also makes sense because the default port that flask app starts on in 5000.

## Error 2

1. Changed the environment to development by adding `FLASK_ENV=development` in `env_file`

2. Followed logs for python flask application in a command line interface. docker logs -f flaskapp_name

3. Created a few entries and then ran Postgres bash. After running postgres bash, checked to see if entries were being put into db correctly
  using psql command line interface
