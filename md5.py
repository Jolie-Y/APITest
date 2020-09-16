# -*- coding: utf-8 -*-
import hashlib
 

def md5Encode(strr):
    m = hashlib.md5()
    m.update(strr)
    return m.hexdigest()

