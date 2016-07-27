from sympy.crypto.crypto import rsa_private_key, rsa_public_key, encipher_rsa, decipher_rsa
a, b, c = 11, 13, 17
rsa_private_key(a, b, c)
publickey = rsa_public_key(a, b, c)
pt = 8
encipher_rsa(pt, publickey)

privatekey = rsa_private_key(a, b, c)
ct = 112
decipher_rsa(ct, privatekey)

