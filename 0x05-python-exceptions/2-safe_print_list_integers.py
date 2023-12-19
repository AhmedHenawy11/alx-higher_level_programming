#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for n in range(0, x):
        try:
            print(f"{my_list[n]}", end="")
            length += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (length)
