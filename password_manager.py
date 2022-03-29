import os
from crypto_helpers import CryptoHelpers
from password_file import PasswordFile

class PasswordManager:
    def __init__(self, master_password=None, fernet_key=None):
        if fernet_key is None:
            if master_password is None:
                raise Exception("Need master_password to initialize PasswordManager")
            else:
                self.key = CryptoHelpers.generate_fernet_key(master_password)
        else:
            self.key = fernet_key

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
    def get_password_files_list(self):
        elements = os.listdir(os.getcwd())
        password_files = []
        for element in elements:
            element_path = os.getcwd() + "\\" + element
            if os.path.isfile(element_path) and (not element.startswith(".")):
                file_name, file_extension = os.path.splitext(element)
                if file_extension == "":
                    password_files.append(element)
        return password_files

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
