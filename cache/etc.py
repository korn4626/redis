import redis, ast
from django.conf import settings


def get_redis_cache(dbindex, key, **kwargs):
    result = None
    redis_cache = redis.Redis(connection_pool=redis_pool[dbindex])
    if kwargs.get('type', '') == "hget":
        sub_key = kwargs.get('sub_key', '')
        result = redis_cache.hget(key, sub_key)
    else:
        result = redis_cache.get(key)

    if kwargs.get('type_change', False) == True:
        if result:
            result = ast.literal_eval(result)  # .replace("'", '"')
    return result


def delete_redis_cache(dbindex, key, **kwargs):
    result = None
    redis_cache = redis.Redis(connection_pool=redis_pool[dbindex])
    if kwargs.get('type', '') == "hdel":
         sub_key = kwargs.get('sub_key', '')
         result = redis_cache.hdel(key, sub_key)
    elif kwargs.get('type', '') == "pattern":
        for key0 in redis_cache.scan_iter(key):
            result = redis_cache.delete(key0)
    else:
        result = redis_cache.delete(key)
    return result


def set_redis_cache(dbindex, key, value, **kwargs):
    result = None
    redis_cache = redis.Redis(connection_pool=redis_pool[dbindex])
    ttl = kwargs.get('ttl', 0)
    if ttl and not redis_cache.exists(key):
        if kwargs.get('type', '') == "hset":
            sub_key = kwargs.get('sub_key', '')
            result = redis_cache.hset(key, sub_key, value)
        else:
            result = redis_cache.set(key, value)
        redis_cache.expire(key, time=ttl)
    else:
        if kwargs.get('type', '') == "hset":
            sub_key = kwargs.get('sub_key', '')
            result = redis_cache.hset(key, sub_key, value)
        else:
            result = redis_cache.set(key, value)
    return result

