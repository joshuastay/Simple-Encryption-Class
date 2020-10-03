# Simple-Encryption-Class

This Encryption class can be used in code to encrypt a string of characters. It uses a dictionary of all ASCII characters as keys and assigns a random 4 digit string to each character. It also reverses the key, value pairs for decryption.

To use the code:

-import enrcypter.py

-construct the encrypter object by calling HiddenInfo class. [objectname = HiddenInfo()]

-when object is initialized as dictionary is randomly generated, call the encrypt method with the string to be encrypted as the only argument. [objectname = objectname.encrypt(new_message)]

-the encrypted string is returned, message can now be decrypted by calling the decrypt method.

-the key used in encrypytion can be saved by calling the key_download method, then reinserted by the key_upload method.

-key_gen method can be used to generate a new random dictionary as well. IF THIS METHOD IS CALLED ANY DICTIONARY CURRENTLY GENERATED WILL BE LOST, DICTIONARY SHOULD BE DOWNLOADED BEFORE USING KEY_GEN METHOD.

