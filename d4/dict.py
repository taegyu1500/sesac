from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    USER = "user"

users = {
    "adm": {
        "password": "adddd",
        "role": "admin",
    },
    "test1": {
        "password": "test",
        "role": "user",
    }
}
def profile_update():
    new_password = input("PW: ")
    new_role = input("Role: ")

    users[id]["password"] = new_password
    users[id]["role"] = new_role
    print("Profile updated successfully.")

def profile_view():
    for key, value in users[id].items():
        print(f"{key}: {value}")


id = input("ID: ")
password = input("PW: ")

if id in users:
    if password == users[id]["password"]:
        print(f"login successful")
        print(f"welcome {id}")
        profile_view()
        profile_update()
        profile_view()
        exit()
    print("password fail")
    exit()
print("id fail")
exit()
