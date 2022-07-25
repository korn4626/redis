import redis
import time
import random

r_pool = redis.ConnectionPool(host="localhost", port=6379, db=0, max_connections=10)

r = redis.Redis(connection_pool=r_pool)

li = {}

for i in range(10000):
    if len(li) < 1000:#round(random.randrange(1,4)) != 1:
        key = "tran_{0}".format(random.randrange(1,10000))
        li[key] = key
        print("add:{1}:{2}".format(i, key, len(li)))
        r.set(key,i)
    elif len(li) == 1000 and round(random.randrange(1,4)) != 1:
        key = "tran_{0}".format(random.randrange(1,10000))
        li[key] = key
        print("add:{1}:{2}".format(i, key, len(li)))
        r.set(key,i)
    else:
        if len(li) > 0:
            key = list(li.keys()).pop(0)
            del li[key]
            r.delete(key)
            print("del:{1}:{2}".format(i, key, len(li)))
#     time.sleep(0.00001)
    
print("Done!!")
a = input("PressKey")
print("Delete!!")
for key in li:
#     key = "tran_{0}".format(i)
    print(key)
#     time.sleep(0.01)
    r.delete(key)
