import hashlib
def hash256(s):
    # Two rounds sha256
    if isinstance(s, str):
        s = s.encode('utf-8')
    first_round = hashlib.sha256(s).digest()
    second_round = hashlib.sha256(first_round).hexdigest()
    return second_round