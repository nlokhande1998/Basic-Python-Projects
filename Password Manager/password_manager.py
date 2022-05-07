from cryptography.fernet import Fernet  # module used to encrypt text using a key


'''def write_key():
    key = Fernet.generate_key()
    with open("D:\Python Projects\key.key", "wb") as key_file:
        key_file.write(key)
write_key()
Key generates is in bytes
This function is required only once to generate a key, hence commented out
'''

def load_key():
    file = open("D:\Python Projects\key.key", "rb")   # read bytes
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('D:\Python Projects\password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()                                # rstrip() is used to strip extra line that gets printed due to print() reading \n
            user, passw = data.split()                          # split() uses delimiter(space) to seperate elements and returns a list, First element gets assigned to first variable and so on...
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('D:\Python Projects\password.txt', 'a') as f:
        f.write(name + " " + fer.encrypt(pwd.encode()).decode() + "\n")  # encoding is used to convert string to bytes as key is in bytes format and later entire thing is decoded


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
