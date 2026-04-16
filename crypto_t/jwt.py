import json
import base64
import hmac
import hashlib


header = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "username": "Alice",
    "role": "admin"
}

secret = "secret123"

def b64_encode(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b'=').decode()

def b64_decode(data):
    return json.loads(base64.urlsafe_b64decode(data + '=='))

# ---------- ENCODE ----------
h_enc = b64_encode(header)
p_enc = b64_encode(payload)

message = h_enc + "." + p_enc

signature = hmac.new(
    secret.encode(),
    message.encode(),
    hashlib.sha256
).digest()

sig_enc = base64.urlsafe_b64encode(signature).rstrip(b'=').decode()

token = message + "." + sig_enc

print("----- JWT TOKEN -----")
print(token)

# ---------- DECODE ----------
parts = token.split('.')

decoded_header = b64_decode(parts[0])
decoded_payload = b64_decode(parts[1])

print("\n----- DECODED -----")
print("Header:", decoded_header)
print("Payload:", decoded_payload)

# ---------- VERIFY ----------
new_sig = hmac.new(
    secret.encode(),
    (parts[0] + "." + parts[1]).encode(),
    hashlib.sha256
).digest()

new_sig_enc = base64.urlsafe_b64encode(new_sig).rstrip(b'=').decode()

print("\n----- VERIFICATION -----")
if new_sig_enc == parts[2]:
    print("Signature Valid")
else:
    print("Invalid Token")