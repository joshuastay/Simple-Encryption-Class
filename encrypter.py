import random
import string


def dict_copy(orig_dictionary):
    tmp_dict = dict()
    for each in orig_dictionary:
        tmp_dict[each] = orig_dictionary[each]
    return tmp_dict


class HiddenInfo:
    """
    Class to encrypt a message with a set of random digits for each letter separated by '#'
    to aid in decryption
    """

    def __init__(self):
        self.characters = string.printable
        self.encrypt_dict = dict()
        self.decrypt_dict = dict()
        self.key_value = ""
        self.key_gen()

    # Use key_upload to insert the key used for a particular encoded message
    def key_upload(self, encrypt_key, decrypt_key):
        self.decrypt_dict.clear()
        self.encrypt_dict.clear()
        self.decrypt_dict = decrypt_key
        self.encrypt_dict = encrypt_key

    # Use key_download to save the key used for a message for later use
    def key_download(self):
        encrypt_dict_out = dict_copy(self.encrypt_dict)
        decrypt_dict_out = dict_copy(self.decrypt_dict)
        return encrypt_dict_out, decrypt_dict_out

    # key_gen creates the key used in encryption, can be ran multiple times to create new keys
    def key_gen(self):
        self.encrypt_dict.clear()
        self.decrypt_dict.clear()
        for each in self.characters:
            value_list = self.encrypt_dict.values()
            while True:
                self.key_value = str(random.randint(1000, 9999)) + "#"
                if self.key_value in value_list:
                    continue
                else:
                    break
            self.encrypt_dict[each] = self.key_value
        temp_dict = self.encrypt_dict.items()
        for x, y in temp_dict:
            self.decrypt_dict[y] = x

    # Encrypt your message
    def encrypt(self, encode_msg):
        encrypted = encode_msg
        for each in encode_msg:
            encrypted = encrypted.replace(each, self.encrypt_dict[each])
        return encrypted

    # Decrypt your message, returns string when the wrong key is loaded
    def decrypt(self, decode_msg):
        temp_decrypt = decode_msg.split("#")
        if "" in temp_decrypt:
            temp_decrypt.remove("")
        decrypted = ""
        try:
            for key in temp_decrypt:
                decrypted += self.decrypt_dict[key + "#"]
            return decrypted
        except:
            return "Incompatible Key Loaded!"
