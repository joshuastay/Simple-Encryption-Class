import random
import string


def dict_copy(orig_dictionary):
    tmp_dict = dict()
    for each in orig_dictionary:
        tmp_dict[each] = orig_dictionary[each]
    return tmp_dict


class HiddenInfo:
    def __init__(self):
        self.letters = string.ascii_letters + " "
        for each in range(10):
            self.letters += str(each)
        self.encrypt_dict = dict()
        self.decrypt_dict = dict()
        self.key_value = ""
        self.key_gen()

    def key_upload(self, encrypt_key, decrypt_key):
        self.decrypt_dict.clear()
        self.encrypt_dict.clear()
        self.decrypt_dict = decrypt_key
        self.encrypt_dict = encrypt_key

    def key_download(self):
        encrypt_dict_out = dict_copy(self.encrypt_dict)
        decrypt_dict_out = dict_copy(self.decrypt_dict)
        return encrypt_dict_out, decrypt_dict_out

    def key_gen(self):
        self.encrypt_dict.clear()
        self.decrypt_dict.clear()
        for each in self.letters:
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

    def encrypt(self, encode_msg):
        encrypted = encode_msg
        for each in encode_msg:
            encrypted = encrypted.replace(each, self.encrypt_dict[each])
        return encrypted

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
