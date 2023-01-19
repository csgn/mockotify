# mockotify

Spotify Music Recommendation

```bash
# start kafka
$ cd kafka
$ docker-compose up

# create kafka topic
$ docker exec -it <KAFKA_CONTAINER_ID> bash
$ kafka-topics.sh --create --topic eyyg --bootstrap-server localhost:9092

# install & start cassandra
$ docker pull cassandra:latest
$ docker run --rm --name cass_cluster -p 9042:9042 cassandra:latest

# create keyspace
$ docker exec -it cass_cluster cqlsh
cqlsh> CREATE KEYSPACE IF NOT EXISTS store WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };


# create venv
$ virtualenv venv -p python3.10
$ source ./venv/bin/activate
$ pip install -r requirements.txt

# start consumer
$ python consumer.py

# start api
$ python api.py


```
