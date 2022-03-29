from helpers import *
import time
import stdiomask

def main():
    while True:

        # Ask master password and get fernet key
        user_input = stdiomask.getpass(prompt="Enter master password: ", mask='*')
        if "stop" in user_input or "quit" in user_input:
            return
        else:
            # Create Password Manager instance
            pm = PasswordManager(master_password=user_input)
            time.sleep(0.2)
            print(f"Your Fernet key is {pm.key}")
            time.sleep(0.5)

        # Main loop
        while True:

            has_valid_password_file = pm.has_valid_password_file()

            # Infos
            print_info(pm, has_valid_password_file)

            # Input
            user_input = input("> ")

            # Commands
            if user_input == "1" or user_input == "create":  # Create new password file
                try_create_password_file(pm)
            elif user_input == "2" or user_input == "load":  # Load existing password file
                try_load_password_file(pm)
            elif user_input == "3" or user_input == "files": # Get the list of password files
                password_files_list = str(pm.get_password_files_list()).replace("[", "").replace("]", "")
                print(f"Password files detected: {password_files_list}")
            elif (has_valid_password_file and user_input == "4") or user_input == "change":  # Change PasswordFile key
                try_changing_password_file_key(pm)

            elif (has_valid_password_file and user_input == "5") or user_input == "add":  # Add a new password
                try_add_password(pm)
            elif (has_valid_password_file and user_input == "6") or "remove" in user_input:  # Remove a password
                try_remove_password(pm)
            elif (has_valid_password_file and user_input == "7") or user_input == "edit":  # Edit a password
                try_edit_password(pm)
            elif (has_valid_password_file and user_input == "8") or user_input == "rename":  # Rename a site
                try_rename_site(pm)
            elif (has_valid_password_file and user_input == "9") or user_input == "get":  # Get a password
                try_get_password(pm)
            elif (has_valid_password_file and user_input == "10") or user_input == "list":  # Get the list
                try_get_sites_name(pm)

            elif user_input == "p":  # Change master password / fernet key
                clear_console()
                break
            elif user_input == "c":  # Clear console
                clear_console()
            elif user_input == "q":  # Quit
                print(green_text("Bye ^^"))
                time.sleep(0.6)
                return None
            else:
                print("Invalid input")

            time.sleep(0.8)


if __name__ == '__main__':
    main()
