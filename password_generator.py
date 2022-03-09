import random

class PasswordGenerator:
    ascii_min = 33
    ascii_max = 126
    ascii_exceptions = [
        34, 39, 40, 41, 42,
        44, 46, 47, 58,
        59, 60, 61, 62,
        91, 92, 93, 94,
        96, 123, 124,
        125, 126, 127
        ]

    @staticmethod
    def generate(length, generation_number=1):
        if generation_number == 1:
            password = ""
            for i in range(0, length):
                ascii_code = random.randint(PasswordGenerator.ascii_min, PasswordGenerator.ascii_max + 1)
                while ascii_code in PasswordGenerator.ascii_exceptions:
                    ascii_code = random.randint(PasswordGenerator.ascii_min, PasswordGenerator.ascii_max + 1)
                password += chr(ascii_code)
            return password
        else:
            passwords = []
            for i in range(0, generation_number):
                passwords.append(PasswordGenerator.generate(length=length))
            return passwords
