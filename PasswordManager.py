import os
from MyCrypto import MyCrypto
from PasswordFile import PasswordFile

class PasswordManager:
    def __init__(self, master_password):
        self.key = MyCrypto.generate_fernet_key(master_password)
        self.password_file = None

    # PasswordFile gestion
    def set_password_file(self, path):
        try:
            self.password_file = PasswordFile(self.key, path)
            return True
        except:
            return False
    def create_password_file(self, path):
        if os.path.exists(path):
            print("File at this path already exists. Operation cancelled")
            return False
        new_file = open(path, "w")
        new_file.close()
        return self.set_password_file(path)
    def has_valid_password_file(self):
        return self.password_file is not None

    # Add / Remove / Password / Rename
    def add_password(self, site, password_to_add):
        if not self.has_valid_password_file():
            print("No password file selected. Operation cancelled")
            return False
        return self.password_file.add_password(self.key, site, password_to_add)
    def remove_password(self, site):
        if not self.has_valid_password_file():
            return
        return self.password_file.remove_password(self.key, site)
    def edit_password(self, site, new_password):
        if not self.has_valid_password_file():
            return False
        return self.password_file.edit_password(self.key, site, new_password)
    def rename_site(self, site, new_site_name):
        if not self.has_valid_password_file():
            return False
        return self.password_file.rename_site(self.key, site, new_site_name)
