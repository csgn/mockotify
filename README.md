# mockotify

Spotify Music Recommendation

```bash
# start kafka
$ cd kafka
$ docker-compose up

# install & start cassandra
$ docker pull cassandra:latest
$ docker run --rm -d --name cassandra

# create keyspace
$ docker exec -it cassandra cqlsh
cqlsh> CREATE KEYSPACE IF NOT EXISTS store
		 WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };


# create venv
$ virtualenv venv -p python3.10
$ source ./venv/bin/activate
$ pip install -r requirements.txt

# start consumer
$ python consumer.py

# start api
$ python api.py


```
