from redis import Redis
import os
import logging
import time


logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

if __name__ == "__main__":
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