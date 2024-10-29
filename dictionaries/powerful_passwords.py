from hashlib import sha256

def login(email, stored_logins, password_to_check):
    if stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_logins = {
        "bestlife@gmail.com": "52884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "life_line_forever@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1518a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
    print(login("bestlife@gmail.com", stored_logins, "word"))
    print(login("bestlife@gmail.com", stored_logins, "password"))

    print(login("life_line_forever@cip.org", stored_logins, "Karel"))
    print(login("life_line_forever@cip.org", stored_logins, "karel"))

    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "123!456?789"))

if __name__ == '__main__':
    main()
