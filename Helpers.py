import os
from Colors import *

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'): # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def hidden_text(text):
    return '*'*len(text)

def try_create_password_file(pm):
    path = input("Enter the new file name: ")
    if pm.create_password_file(path):
        print(green_text(f"Successfully created and loaded a password file at path: {path}"))
    else:
        print(red_text(f"Something went wrong when creating or loading a file at path: {path}"))

def try_load_password_file(pm):
    path = input("Enter the path of the file: ")
    if os.path.isfile(path):
        if pm.set_password_file(path):
            print(green_text(f"Successfully loading password file at path: {path}"))
        else:
            print(red_text(f"Couldn't load password file at path: {path}"))
    else:
        print(red_text("No file exists at this path"))

def try_add_password(pm):
    # Ask site and password
    site = input("Enter the site: ")
    password = input("Enter the password: ")
    # Add password
    if pm.add_password(site, password):
        print(green_text(f"Successfully added {hidden_text(password)} for {site}"))
    else:
        print(red_text(f"Couldn't add {hidden_text(password)} for {site}"))

def try_remove_password(pm):
    # Ask site
    site = input("Give site: ")
    # Remove password
    if pm.remove_password(site):
        print(green_text(f"Successfully removed the password of {site}"))
    else:
        print(red_text(f"Couldn't remove the password of {site}"))


def try_edit_password(pm):
    # Ask site and new password
    site = input("Edit the password of which site: ")
    new_password = input("What is the new password: ")
    # Edit password
    if pm.edit_password(site, new_password):
        print(green_text(f"Successfully edited the password of {site} to {hidden_text(new_password)}"))
    else:
        print(red_text(f"Couldn't edit the password of {site}"))

def try_rename_site(pm):
    # Ask old site name
    site_name = input("Which site should be renamed: ")
    # Verify its existence
    if pm.password_file.contains(site_name):
        # Ask new name for this site
        new_name = input("How should it be named: ")
        # Apply
        if pm.rename_site(site_name, new_name):
            print(green_text(f"Successfully renamed '{site_name}' to '{new_name}'"))
        else:
            print(red_text(f"Couldn't rename '{site_name} into '{new_name}'"))
    else:
        print(red_text(f"Selected passwords file does not contains the site named {site_name}. Operation cancelled"))


def try_get_password(pm):
    # Ask site
    site = input("Get the password of which site: ")
    # Found and display if found
    found_password = pm.password_file.get_password(site)
    print(
        f"The password of {site} is {bold_text(found_password)}"
        if found_password is not None else f"No password found for {site}"
    )


def try_get_sites_name(pm):
    # Get sites array, cast it to a string
    sites_name = str(pm.password_file.get_sites_list())
    # Remove the brackets
    sites_name = sites_name[1:len(sites_name) - 1]
    # Display
    print(f"This file contains the passwords of: {bold_text(sites_name)}")


def print_info(pm, has_valid_password_file):
    selected_password_file_helper = f"(password file selected is '{pm.password_file.path}')" \
        if has_valid_password_file else "(No selected password file)"
    print(bold_text(f"\nWhat do you want to do?\t\t") + selected_password_file_helper)

    # Passwords files gestion
    print_bold("Passwords files:")
    print_dark("(1) Create new password file\n(2) Load existing password file")
    # Passwords gestion
    if has_valid_password_file:
        print_bold("\nPasswords:")
        print_dark(
            "(3) Add a new password\n(4) Remove a password\n" +
            "(5) Edit a password\n(6) Rename a site\n(7) Get a password\n" +
            "(8) List the sites")
    # Others
    print_bold("\nOthers:")
    print_dark("(p) Change Master password/Fernet key\n(c) Clear console\n(q) Quit\n")