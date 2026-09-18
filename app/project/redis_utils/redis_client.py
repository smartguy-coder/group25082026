import redis
import config
import datetime

redis_client = redis.Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    decode_responses=True,
    username=config.REDIS_USERNAME,
    password=config.REDIS_PASSWORD,
)

# Write - CREATE
# strings
# success = redis_client.set('foo', 'bar333333333333333')
# print(success)
# redis_client.set('myKeyTTL', 'secret data', ex=15)
# redis_client.set('promo:2', 'promocode', exat=datetime.datetime(year=2027, month=3, day=8))

# list
# redis_client.lpush('list-key', 'value init')
# redis_client.lpush('list-key', 'value1')
# redis_client.rpush('list-key', 'value2')
# redis_client.rpush('list-key', 'value3', 'value4')
# redis_client.expire('list-key', 10666)

# dicts
# redis_client.hset('user:123', mapping={'name': 'Alise', 'age': '26'})
# redis_client.hset('user:123', mapping={'name': 'Alex', 'city': 'Odesa'})
# redis_client.expire('user:123', 10666)

# counter
# redis_client.incr('views', -11)
# redis_client.incrby('views', 5555555)
