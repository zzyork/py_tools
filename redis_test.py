import redis
#创建连接池
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,decode_responses=True)
#创建链接对象
r=redis.Redis(connection_pool=pool)
r.set('test','dddddddddddd',ex=3,nx=True)
print(r.get('test'))