#  Funtion with output

def format_name(fname ,lname):
    a=fname.title()
    b=lname.title()
    # return a+ " "+b
    return f"{a} {b}"
    

f_name=input("enter your first name")
l_name=input("enter your last name")

print(format_name(f_name,l_name))