def main():
    value =input("Welcome to the bank: ")
    bank(value)

def bank(val):
    v=val.lower().strip()
    if v.startswith("hello"):
        print("$0")
    elif v.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
