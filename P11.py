def emailCheck(email):
    try:
        if '@' not in email:
            raise ValueError("@ must be present in the email.")
        
        if email.count('@') != 1:
            raise ValueError("Only one '@' must be present in the email.")
        
        at_index = email.find('@')
        if at_index == 0:
            raise ValueError("There must be something before '@'.")

        dot_index = email.rfind('.')
        if dot_index == -1 or dot_index < at_index:
            raise ValueError("There must be a '.' after '@' to indicate a domain.")

        if dot_index - at_index <= 1:
            raise ValueError("There must be at least one character between '@' and '.'.")

        if dot_index == len(email) - 1:
            raise ValueError("Domain must contain characters after '.'.")

        print("Email is valid.")
    
    except ValueError as e:
        print(e)

while True:
    string = input("Enter Email: ")
    emailCheck(string)
