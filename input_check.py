def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Integers only, try again")
            continue

        if len(str(value)) > 4:
            print("Too large of number, keep under 1000")
            continue
        else:
            break
    return value
