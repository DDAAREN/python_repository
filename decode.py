#!/usr/bin/env python
# _*_ coding: UTF-8 _*_


_keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

def fromCharCode(a, *b):
    return unichr(a%65536)+''.join([unichr(i%65536) for i in b])

def listGetChar(s, index):
    try:
        return s[index]
    except:
        return ""

def listGetCharCode(s, index):
    try:
        return ord(s[index])
    except:
        #return np.nan
        return 0

def _utf8_decode(c):
    a = ""
    b = 0
    c1, c2 = 0 ,0
    for b in range(len(c)):
        d = ord(c[b])
        
        if d < 128:
            a = a + fromCharCode(d)
            b = b + 1
        else:
            if d > 191 and d < 224:
                c2 = listGetCharCode(c, (b+1))
                a = a + fromCharCode((d&31)<<6|c2 & 63)
                b = b + 2
            else:
                c2 = listGetCharCode(c, (b+1))
                c3 = listGetCharCode(c, (b+2))
                a = a + fromCharCode((int(d) & 15) << 12 | (int(c2) & 63) << 6 | int(c3) & 63)
                b = b + 3
    return a
                
def decode(c):
    a = ""
    b, d, h, f, g, e = 0, 0, 0, 0, 0, 0
    c = c.replace(r'[^A-Za-z0-9\+\/\=]', "")
    while e < len(c):
        b = _keyStr.find(listGetChar(c,e))
        e += 1
        d = _keyStr.find(listGetChar(c,e))
        e += 1
        f = _keyStr.find(listGetChar(c,e))
        e += 1
        g = _keyStr.find(listGetChar(c,e))
        e += 1
        b = b << 2 | d >> 4 
        d = (d & 15) << 4 | f >> 2
        h = (f & 3) << 6 | g 
        a += fromCharCode(b)
        if f != 64:
            a += fromCharCode(d)
        if g != 64:
            a += fromCharCode(h)

    return _utf8_decode(a)


if __name__ == '__main__':
    with open('data.txt','rb+') as f:
        for data in f:
            # output json
            print decode(data[1:-2])
