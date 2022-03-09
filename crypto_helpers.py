import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoHelpers:
    @staticmethod
    def generate_fernet_key(literal_password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'=D\xba\xb7DgN\xa0\xf2Nr\xd0!\x8f\xde\x9b',
            iterations=390000
        )
        return base64.urlsafe_b64encode(kdf.derive(literal_password.encode("UTF-8")))

    @staticmethod
    def encrypt_password(key, decrypted_password):
        if key is None:
            return None
        try:
            return Fernet(key).encrypt(decrypted_password.encode("UTF-8")).decode()
        except:
            print("Error while trying to encrypt password. Fernet key wrong ?")
            return None

    @staticmethod
    def decrypt_password(key, crypted_password):
        if key is None:
            return None
        return Fernet(key).decrypt(crypted_password.encode("UTF-8")).decode()
