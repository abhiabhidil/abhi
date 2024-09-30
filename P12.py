import re
def checkPhoneNumber(num):
    try:
        pattern=r'\D'
        if re.search(pattern,num):
            raise ValueError("Phone Number Should Only contain numbers")

        pattern=r'^\d*$'
        if re.match(pattern,num):
            """if len(num) !=10:
                raise ValueError("Phone Number must be of ten digits")"""
            if len(num)<10:
                raise ValueError(f"Number is shorter by {10-len(num)} digits")
            elif len(num)>10:
                raise ValueError(f"Number is longer by {len(num)-10} digits")
    except ValueError as e:
        print(e)
    else:
        print("Correct")




pn=input("Enter Phone Number: ")
checkPhoneNumber(pn)
