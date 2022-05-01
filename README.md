# mixr

basic flask app that stores data from html table to sqlalchemy DB <br>
front end sucks and is not done, table needs more fields 

### basic usage:
  (from mixr dir) <br>
  virtualenv env <br>
  source env/bin/activate <br>
  python3 app.py <br>
  runs at localhost:5000 <br>
  
### docker usage:
  (from mixr dir) <br>
  virtualenv env <br>
  source env/bin/activate <br>
  docker build --tag desired_image_name <br>
  docker run --name desired_container_name -d -p desired_external_port:5000 whatever_you_named_the_image <br>
  then docker ps to see it running, docker logs -f container_name to see live logs <br>
