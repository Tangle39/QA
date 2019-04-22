# 8 random string
import random
import string

ran_str = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 8))
# join connencts string
print ran_str
