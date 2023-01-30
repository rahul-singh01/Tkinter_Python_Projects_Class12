# Encryption and Decryption of a text

import random

# alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&0123456789 '

# print(len(alphabet))

# msg = input("enter the message = ")


# bita = 'abcdefghijklmnopqrstuvwxyz'

# numeric_assign = '!#$%&*~@*49JGU&989#*dkskHG%$#$kxjnvj$7172'

# key  = 5
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'

with open('passw.txt','r') as t:
    key = t.read()

def decode(code):
    final = ''
    key_index = 0
    alternate = 0


    for j, i in enumerate(code):

        if j != 0 and j == int(key[0]) + key_index*int(key[0]) + key_index:
            key_index += 1
            continue

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue

        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==1):
            change = 'A'
        else:
            if alternate%2==1:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final

def encode(code, key):
    final = ''
    key_index = 0
    alternate = 0

    for j, i in enumerate(code): # j= indexing of a  i= value of a

        if j != 0 and j%int(key[0]) == 0:
            final += key[key_index%len(key)] # IMPORTANT ALGORITHEM...(it's like looping some range of integer.)
            key_index += 1

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue
        
        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==0):
            change = 'A'
        else:
            if alternate%2==0:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final




msg = input("enter msg")
msg = encode(msg, key)

num = random.randint(1000000,9999999)
num = encode(str(num), key)

final = msg+num
print(final)

msg1 = input("decode msg")
key1 = msg1[len(msg1)-len(num):]
msg = msg1[:len(msg1)-len(num)]

print(msg)
print(key1)

print(encode(msg, key1)+num)
# num_encrypt = ''
# encrypt = '' 
# num = random.randint(1000000,9999999)
# q = encode(str(num), key)
# print(q)

# for i in msg:
#     position = alphabet.find(i)
#     newposition  = (position + num ) % 44
#     encrypt += alphabet[newposition]
# r= encrypt

# print('encrypted ', r+q)

# new = input('Enter the message')

# decrypt1 = ''
# q1 = input('Enter the message')
# y = new[::-1]
# l = y[0:7]
# c = l[::-1]
# numeric = c[0:7]
# num1 = decode(numeric)
# print(num1)
# for i in q1:
#     position = alphabet.find(i)
#     newposition  = (position - int(num1) ) % 44
#     decrypt1 += alphabet[newposition]
# print('decrypted message= ',decrypt1)

# q = input('Enter the Encrypted message: ')
# w = q[::-1]
# e = w[0:7]
# r = e[::-1]
# decryption_key = r[0:7]
# print(decryption_key)

# num_decrypt = ''
# for i  in str(decryption_key):
#     luck = numeric_assign.find(i)
#     luck_position = (luck - 5) % 43
#     num_decrypt += numeric_assign[luck_position]
# print(num_decrypt)

# b = int(num_decrypt)

# decrypt = ''
# for i in q:
#     position = alphabet.find(i)
#     newposition  = (position - b) % 43
#     decrypt += alphabet[newposition]
# print(decrypt)
