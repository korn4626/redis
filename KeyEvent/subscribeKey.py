import redis
import time

r_pool = redis.ConnectionPool(host="localhost", port=6379, db=0, max_connections=10)

r = redis.Redis(connection_pool=r_pool)

r1 = redis.StrictRedis(host='localhost', port=6379, db=2)

p = r.pubsub()
p.psubscribe('__keyspace@0__:*')
PAUSE = True 
cnt = r.dbsize()
# cnt=0
no = 0
li = {}
maxC = int(r1.get("MaxC"))
print(maxC)
while PAUSE: 
    # Checks for message 
    message = p.get_message() 
    if message: 
        # Get data from message 
        command = message['data']
        cha = message['channel'].decode().split(":")
#         print(message)
        if command == b"set":
            no += 1
#             cnt += 1
            li[cha[1]]=None
            if len(li) > maxC:
                r1.set("TRList", str(list(li.keys())[:maxC]))
            print("set-[{0}]key size:{1}".format(no, len(li)))
            r1.set("CurC", len(li))
        elif command == b"del":
            no += 1
#             cnt -= 1
            del(li[cha[1]])
            print("del-[{0}]key size:{1}".format(no, len(li)))
            r1.set("CurC", len(li))
            if len(li) < maxC:
#                 r1.set("TRList", "[]")
                r1.delete("TRList")
            r1.set("CurC", len(li))            
