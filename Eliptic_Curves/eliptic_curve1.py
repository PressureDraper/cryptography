from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())

public_key = private_key.public_key()

data = b'hola mundo'

signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))

try:
    public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
    print('La firma es válida')
except:
    print('La firma no es válida')