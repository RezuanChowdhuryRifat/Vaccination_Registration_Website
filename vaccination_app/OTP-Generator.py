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

key = gen_key() #TODO: Put in Database
print(key)
uri = gen_url(key)
print(uri)

# Generates a timed otp code:
code = generate_code(key)
print(code)
time.sleep(10)

# Generates a normal otp code:
code0 = generate_code(key)
print(code0)

print(verify_code(key, code))
print(verify_code(key, code0))

