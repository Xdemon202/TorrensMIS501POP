import re

def signup():
    full_name = input("Enter your full name: ")
    contact_number = input("Enter your contact number: ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    password = input("Enter your password: ")
    password_confirmation = input("Enter your password confirmation: ")

    # Check if the mobile number is valid
    if not re.match("0[1-9]{9}", contact_number):
        print("Invalid mobile number. Please enter a 10-digit mobile number starting with 0.")
        return

    # Check if the password is valid
    if not re.match("^[a-zA-Z]+[@&][0-9]+$", password):
        print("Invalid password. The password must start with an alphabet, followed by either @ or &, and end with a numeric.")
        return

    # Check if the password confirmation matches the initial password
    if password != password_confirmation:
        print("Password confirmation does not match the initial password. Please enter the same password again.")
        return

    # Check if the user is at least 16 years old
    year = int(dob[-4:])
    if year < 2007:
        print("You must be at least 16 years old to sign up.")
        return

    # Check if the DOB is in the correct format
    try:
        day, month, year = map(int, dob.split("/"))
    except ValueError:
        print("Invalid date of birth. Please enter your date of birth in the format DD/MM/YYYY.")
        return

    # Save the user data
    user_data = {
        "full_name": full_name,
        "contact_number": contact_number,
        "dob": dob,
        "password": password,
    }

    print("Signup successful!")

    # Save the user data in a list
    user_list = []
    user_list.append(user_data)

    return user_list

if __name__ == "__main__":
    user_list = signup()
    print(user_list)