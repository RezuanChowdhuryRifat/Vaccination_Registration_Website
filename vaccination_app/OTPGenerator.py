# install pyotp:
import pyotp
import time



def gen_key():
    return pyotp.random_base32()

def gen_url(key: str):
    return pyotp.totp.TOTP(key).provisioning_uri(name='Yash',issuer_name='2FA Verification')

def generate_code(key: str):
    totp = pyotp.TOTP(key)
    return totp.now()

def verify_code(key: str, code: str):
    totp = pyotp.TOTP(key)
    return totp.verify(code)




