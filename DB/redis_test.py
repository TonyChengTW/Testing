import redis

tony_pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
tony_redis = redis.Redis(connection_pool = tony_pool)
tony_redis.setnx('name', 'tony')
print(tony_redis['name'])
print(tony_redis.get('name'))
print(tony_redis.type('name'))
tony_redis.setnx("fw:address:id", 123)
print(tony_redis.get("fw:policy:id"))

# Add Record1
address_hash = "address:{0}".format('234')
address_value = {"name": 'address234', "addrtype": 'ipmask'}

# Check is address hash is exists , True is existing
if not tony_redis.exists(address_hash):
    print("Redis: add key: %s, value: %s") % (address_hash, address_value)
    try:
        result1 = tony_redis.hmset(address_hash, address_value)
        # result2 = tony_redis.lpush('policy_hashlist', policy_hash)
    except:
        print("something wrong...")
        tony_redis.delete(address_hash)
        # tony_redis.lrem('policy_hashlist', policy_hash, 0)
        raise
else:
    print("This address name is exist")

# result_lrange = tony_redis.lrange('policy_hashlist', 0, -1)
result_hgetall1 = tony_redis.hgetall('address:234')
pass


