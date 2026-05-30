from validator_collection import validators,errors

address = input("What's your email address? ")

try:
    email_address = validators.email(address)
    print("Valid")
except (errors.EmptyValueError,errors.InvalidEmailError):
    print("Invalid")

