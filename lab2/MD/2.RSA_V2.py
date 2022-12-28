#Private Key 
def private_key():
    private_key = 1
    while public_key_e * private_key % phi_num_n !=1:
        private_key += 1
    return private_key


#Encryption Section
def encrypt(message):
    encrypted_message = []
    for i in message:
        int_message = ord(i)
        encrypt_charachter = (int_message ** public_key_e) % num_n
        encrypted_message.append(encrypt_charachter)           
    return encrypted_message


#Decryption Section
def decrypt(message):
    message = message.split(',')
    decrypted_message = ""
    for i in message:
        charachter = chr((int(i) ** private_key_d) % num_n)
        decrypted_message += charachter
    return decrypted_message


#Constant Section
prime_num_p = 151
prime_num_q = 157
public_key_e = 23701
num_n = prime_num_p * prime_num_q
phi_num_n = (prime_num_p-1)*(prime_num_q-1)
private_key_d = private_key()


#Input Section
print("RSA Algorithm if you wanna decrypt, separate the numbers by comma (,)")
message = input("Enter your message: ")
action = input("Press (1) for encryption and (2) for decryption:")

if action == "1":
    encrypted_message =  encrypt(message)
    print("The message encrypted is: ", encrypted_message)
elif action == "2":
    decrypted_message = decrypt(message)
    print("The message Decrypted is: ", decrypted_message)
else:
    print("Please learn to read, choose 1 or 2")