
def encode(message, key):
    new_message = ''

    for i in range(len(message)):
        ascii_val = ord(message[i])
        val = ascii_val + key
        if val >122:
            k = (122-val)
            k = k % 26
            new_message += chr(96 + k)
             
        else:
            new_message += chr(val)
    return new_message

def decode(message, key):
    return encode(message, -key)


message = 'hai'
key = 3

mess = encode(message, key)
print(mess)
# print(decode(mess, -key))