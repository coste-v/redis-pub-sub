from redis import Redis
import os
import logging
import time


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

def pubsub_example():
    """
        Here, if a message is send to REDIS_CHANNEL,
        all the worker listening to this channel will receive
        the message
    """
    redis = Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        decode_responses=True
    )

    pubsub = redis.pubsub()
    pubsub.subscribe(os.getenv("REDIS_CHANNEL"))

    while True:
        message = pubsub.get_message()
        if message:
            logger.info(message["data"])
        time.sleep(0.01)

def queue_example():
    redis = Redis(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        decode_responses=True
    )

    while True:
        message = redis.rpop(os.getenv("REDIS_CHANNEL"))
        if message:
            logger.info(message)
        time.sleep(0.01)


if __name__ == "__main__":
    queue_example()