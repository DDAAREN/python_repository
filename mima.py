def volid(pwd):
    a = any(map(str.isupper, pwd))
    b = any(map(str.islower, pwd))
    c = any(map(str.isdigit, pwd))
    d = not all(map(str.isalnum, pwd))
    return all([a,b,c,d])
    
#验证密码是否符合条件（只由字母和数字组成，且大小写字母都有）