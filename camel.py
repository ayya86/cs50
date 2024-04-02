def main():
    #get input camel case
    camelcase=input("camelcase: ")

    #call the function snake_case
    snakecase=snake_case(camelcase)

    #result
    print("Snake_case: ",snakecase)

def snake_case(camelcase):
    scase=''
    for c in camelcase:
        if c.isupper():
            scase += '_' + c.lower()
        else:
            scase += c

    if scase.startswith('_'):
        scase=scase[1:]
    return scase

main()
