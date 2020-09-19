# Tutorial to play with redis pub sub

```bash
docker network ls
```

```bash
docker network create pubsub-network
```

```bash
docker network rm pubsub-network
```

docker run -e REDIS_HOST=redis-host -e REDIS_PORT=4667 -e REDIS_CHANNEL=the_channel --network pubsub-network redis_pub_sub_worker

```bash
docker run --name redis-host -d --rm --network pubsub-network redis:alpine3.10 redis-server --port 4667
```

```bash
docker exec -it redis-host env

> HOSTNAME=redis-host
> REDIS_VERSION=5.0.7

docker exec -it redis-host /bin/sh
redis-cli -p 4667

publish the_channel "hello world"
```

