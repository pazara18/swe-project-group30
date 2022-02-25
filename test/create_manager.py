import sys

sys.path.insert(1, "./../src/")

import database
from passlib.hash import sha256_crypt

def create_manager(national_id, name, surname, password):
    manager = database.Manager(national_id, name, surname, sha256_crypt.hash(password))
    ret = database.add_manager(manager)
    if not ret:
        print("Could not add manager")

national_id = "66142382132"
name = "Hakan"
surname = "Öztürk"
password = "manager"

create_manager(national_id, name, surname, password)