import os
import sys
import json
import uuid
import threading
import inspect
import logging

from kafka import KafkaConsumer


import engine

#logging.basicConfig(level=logging.DEBUG)


class Consumer:
    def __init__(self, topic="eyyg", host="localhost", port=9093) -> None:
        self.topic = topic
        self.host =  host
        self.port = port

        self.bootstrap_servers = [f'{self.host}:{self.port}']
        self.__consumer = None


    def __poll(self):
        self.__consumer = KafkaConsumer(bootstrap_servers=self.bootstrap_servers, auto_offset_reset="earliest")
        self.__consumer.subscribe(self.topic)

        print("Consumer is being initialized for polling...")

        try:
            self.__consumer.poll(timeout_ms=5000)
            print("Consumer is being polled now from: ", self.topic)
        except Exception as e:
            raise Exception("Polling process is failed")

        while True:
            for message in self.__consumer:
                print("[RECEIVED] - ", str(message.value, 'utf-8'))
                try:
                    self.__listener(message)
                except Exception as e:
                    print(e)
                    return


    def __listener(self, message):
        decoded_message = json.loads(str(message.value, encoding="utf-8"))
        engine.run(decoded_message)

    def run(self):
        threading.Thread(target=self.__poll).start()
        print("[INFO] Consumer is running on background")



def main():
    consumer = Consumer()
    consumer.run()

if __name__ == "__main__":
    main()
