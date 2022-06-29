import bcrypt
import hashlib

from loguru import logger

def hash_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
    

def check_password(password: str, password_hashed):
    endcode_pass = password.encode('utf-8')
    logger.info(f'password endcode: {endcode_pass}')
    logger.info(f'password hashed: {password_hashed}')
    if bcrypt.checkpw(password.encode('utf-8'), password_hashed):
        return True
    else:
        return False

def has_pas(pw:str):
    return hashlib.sha3_512(pw.encode('utf-8')).hexdigest()

def ck_pas(pw:str, hpw):
    h_pw =  hashlib.sha3_512(pw.encode('utf-8')).hexdigest()
    if h_pw == hpw:
        print('giong')
    else: 
        print('khong giong')

if __name__=="__main__":
    r1 = hash_password("Ohio2222")
    print(r1)
    print("match" if check_password("Ohio2222", r1) else "not match")

    r2 = has_pas('ohio2022'+"8dc49ce3-7970-431f-a705-be37973edb66")
    print(r2)
    ck_pas('Ohio2022', r2)