import os
from crypto_helpers import CryptoHelpers

class PasswordFile:
    def __init__(self, key, path):
        if not os.path.exists(path):
            raise Exception("Path invalid for the instantiation of PasswordFile")
        # Store path
        self.path = path
        # Fill lines
        self.lines = []
        self.get_lines()
        # Fill passwords dictionary
        self.password_dict = {}
        self.update_password_dict(key)

    # Lines
    def get_lines(self):
        with open(self.path, "r") as f:
            self.lines = f.read().splitlines()
        return self.lines
    def apply_lines(self):
        with open(self.path, "w") as f:
            f.write(self.create_text_from_list(self.lines))
    def create_text_from_list(self, list):
        result = ""
        for element in list:
            result += element + "\n"
        return result

    # Passwords dictionary gestion
    def update_password_dict(self, key):
        self.password_dict.clear()
        for line in self.lines:
            site, crypted_password = line.split(':')
            self.password_dict[site] = CryptoHelpers.decrypt_password(key, crypted_password)

    # Get info functions
    def contains(self, site):
        return site in self.password_dict
    def get_password(self, site):
        if not self.contains(site):
            return None
        return self.password_dict[site]
    def get_sites_list(self):
        result = []
        for site, decrypted_password in self.password_dict.items():
            result.append(site)
        result.sort()
        return result

    # Add / Remove / Edit / Rename
    def add_password(self, key, site, password_to_add):
        if self.contains(site):
            print(f"PasswordFile already contains {site}")
            return False

        self.lines.append(f"{site}:{CryptoHelpers.encrypt_password(key, password_to_add)}")

        self.apply_lines()
        self.update_password_dict(key)
        return True
    def remove_password(self, key, site):
        if not self.contains(site):
            print(f"PasswordFile does not contain {site}")
            return False

        for i in range(0, len(self.lines)):
            if site in self.lines[i]:
                self.lines.remove(self.lines[i])
                self.apply_lines()
                self.update_password_dict(key)
                return True
        return False
    def edit_password(self, key, site, new_password):
        if not self.contains(site):
            print(f"PasswordFile does not contain {site}")
            return False
        return self.remove_password(key, site) and self.add_password(key, site, new_password)
    def rename_site(self, key, site, new_site):
        if not self.contains(site):
            return False
        decrypted_site_password = self.get_password(site)
        return self.remove_password(key, site) and self.add_password(key, new_site, decrypted_site_password)
    def clear(self):
        with open(self.path, "w") as f:
            f.write("")
        self.lines = []
        self.password_dict.clear()

    # Destroy
    def destroy(self):
        self.clear()
        os.remove(self.path)
