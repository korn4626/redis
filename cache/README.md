# django에서 cache로 redis 사용
> settings.py에 cache설정
```python
CACHES = {
    "cache_name": { #cache_name라는 이름의 cache
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:password@ip:port/database_no",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}
```
>사용예제
```python
from django.core.cache import caches

#읽어오기
result = caches["cache_name"].get(key)

#저장하기
caches["cache_name"].set(key, value, 60*60*24) #ttl저장

#삭제하기
cache = caches['cache_name'].delete(key)
```

> cache로 사용할 경우 redis의 key값에 version prefix 항목이 붙음.(ex. :1:redis_key)
> 
> cache로 사용할 경우 redis의 value를 hash사용하는 방법 못찾음.

# python redis library 이용
> redis connection
```python
redis.StrictRedis(host=ip, port=port, db=database_no, password='password')
```
> redis connectionpool 이용
```python
#connection pool 생성
cp = redis.ConnectionPool(host=ip, port=port, db=database_no, password='password', decode_responses=True)

#connection pool 이용
redis = redis.Redis(connection_pool=cp)
```
