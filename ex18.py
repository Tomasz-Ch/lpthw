def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("Ja nie mam nic.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("Pierwszy!")
print_none()
