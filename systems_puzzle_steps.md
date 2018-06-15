# Steps

## Error 1

1. After attempting the build instructions and noticing that I was getting a 502 gateway error, I decided to look at the nginx container log through:

`sudo docker logs -t systems-puzzle_nginx_1`

2. I noticed from the previous step that nginx was not able to hit port 5001 on the flaskapp container. Thus, I ran the app locally to check if flaskapp runs on 5001, and I found out it actually ran on 5000.

3. I modified the flaskapp.conf file which has the configuration for nginx interacting with the flaskapp server. I changed http://flaskapp:5001 to http://flaskapp:5000. Then I reloaded the configuration through `nginx -s reload` inside the bash shell for the nginx docker container. then I hit the web page again on my browser and found that I could see the form. This also makes sense because the default port that flask app starts on in 5000.

4. Reverted back to port 5001 after making flaskapp run on port 5001.

## Error 2

1. Changed the environment to development by adding `FLASK_ENV=development` in `env_file`

2. Followed logs for python flask application in a command line interface. docker logs -f flaskapp_name

3. Created a few entries and then ran Postgres bash. After running postgres bash, checked to see if entries were being put into db correctly
  using psql command line interface.

4. Entries were being put correctly. So looked through function querying data. noticed that objects were being returned in query but data was not retrieved because we were returning the object list. By iterating through results, unpacked data from each object into string and displayed it on return.

5. Return results as json list.

## Further TODOs

~1. Understand why query.all() didn't work where as iterating through model list did.~
  * Because \_\_repr\_\_ function is not defined appropriately in the items class and that is what is used when printing a list. Defined to     instead to return object.

~2. Return results as json list.~

2. Understand flask and sqlalchemy a bit more.

~3. Understand why port 5001 doesn't need to be changed to 5000 for the .yml file and dockerfile.~
  * While I am not sure I am comfortable with every detail just yet, but EXPOSE is supposed to make a container listen to connections on a certain port. I realized I could change the flask app to run on port 5001 instead of port 5000 and revert the nginx configuration file back to its original state. The intent of the original author seems to put the docker application on port 5001 and thus I have made this modification.
