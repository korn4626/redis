import redis


class custom_redis(redis.Redis):
    #rename-command hget a8
    def hget(self, name, key):
        return self.execute_command('hget변경된명령어', name, key)
        #return self.execute_command('a8', name, key)
    #rename-command get a9
    def hset(self, name):
        #return self.execute_command('a9', name)
        return self.execute_command('get변경된명령어', name)
        
        
  
redis_info = custom_redis(host="localhost", port=port, db=dbno, decode_responses=True)
t = redis_info.hget("test", "test2")
