from sympy.crypto.crypto import encipher_bifid6, decipher_bifid6
key = "encryptingit"
pt = "A very good book will be released in 2015"
encipher_bifid6(pt, key)
ct = "AENUIUKGHECNOIY27XVFPXR52XOXSPI0Q"
decipher_bifid6(ct, key)

