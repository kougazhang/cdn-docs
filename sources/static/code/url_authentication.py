# token 防盗链， CDN 客户生成 token 的 demo


import hashlib,time

URI = input("Input URL:")
key = input('Input the secret key:')
times = int(input('Input the validity period (the unit is second):'))

etime = int(time.time()) + times
sign = key + '&' + str(etime) + '&' + URI
print("the sign is: ",sign)
print("the expiration is:", etime)
def calc_md5(sign):
    md5 = hashlib.md5()
    md5.update(sign.encode('utf-8'))
    return md5.hexdigest()

print("the md5 of the sign: ", calc_md5(sign))
print('the 8 digits of the sign: ',calc_md5(sign)[12:20])
token = calc_md5(sign)[12:20] + str(etime)
print('the final token:',token)
URL = URI + '?_upt=' + token
print('the url with the token:',URL)