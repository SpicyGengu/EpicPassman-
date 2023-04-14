import random


def generate_password(length=7):
    asciiRange = 122-33

    generated_password = ""
    for i in range(int(length)):
        generated_password += chr(33 +
                                  random.randrange(asciiRange))
    return generated_password


print(generate_password())
