def volid(pwd):
    a = any(map(str.isupper, pwd))
    b = any(map(str.islower, pwd))
    c = any(map(str.isdigit, pwd))
    d = not all(map(str.isalnum, pwd))
    return all([a,b,c,d])

#判断密码是否是全部是数和或字母组成，且大小写都有
