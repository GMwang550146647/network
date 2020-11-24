import hashlib
import hmac

def confirm_func_hash(rand,secret_key):
    sha = hashlib.sha1(secret_key)
    sha.update(rand)
    res = sha.hexdigest()
    res=res.encode()
    return res

def confirm_func_hmac(rand,secret_key):
    h=hmac.new(secret_key,rand)
    res=h.digest()
    return res