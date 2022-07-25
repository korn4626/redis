import redis
import time
import ast

r_pool = redis.ConnectionPool(host="localhost", port=6379, db=2, max_connections=10)

r = redis.Redis(connection_pool=r_pool)

p = r.pubsub()
# p.subscribe('__keyspace@2__:CurC')
p.subscribe('__keyspace@2__:TRList')
PAUSE = True 
maxc = r.get("MaxC").decode()
while PAUSE: 
    # Checks for message 
    message = p.get_message() 
    if message: 
#         print(message)
        # Get data from message 
        command = message['data']
        if command == b'set':
#             print("Set")
            t1 = r.get("CurC")
            t = t1.decode()
#             if int(t) > int(maxc):
            print(t)
#             data = ast.literal_eval(t)
#             if len(data) > 0:
#                 print(data[0])
        elif command == b'del':
            print("Delete!!")
