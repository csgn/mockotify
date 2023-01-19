import os
import sys
import json
import uuid
import threading

from kafka import KafkaProducer

import logging
#logging.basicConfig(level=logging.DEBUG)


class Producer:
    def __init__(self, topic="eyyg", host="localhost", port=9093) -> None:
        self.topic = topic
        self.host = host
        self.port = port

        self.bootstrap_servers = [f'{self.host}:{self.port}']

        self.__producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, 
                                        value_serializer=lambda v: json.dumps(v,
                                                                   indent=4,
                                                                   default=str) \
                                                                .encode('utf-8'))

    def send(self, value, key=str(uuid.uuid4())):
        self.__producer.send(topic=self.topic, value=value, key=bytes(key, encoding='utf-8'))

