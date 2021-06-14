from Crypto.Cipher import Salsa20

key = b'0123456789012345'
cipher = Salsa20.new(key)
ciphertext = cipher.encrypt(b'The secret I want to send.')
ciphertext1 = cipher.decrypt(ciphertext)
print(ciphertext1)
print(cipher.nonce)  # A byte string you must send to the receiver too