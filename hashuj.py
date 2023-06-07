from hashlib import sha1

text = 'admin1'

my_hash = sha1(text.encode('utf-8'))
print(my_hash.hexdigest())
