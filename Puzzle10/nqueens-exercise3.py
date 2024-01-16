def check(stracture):
    for i in range(len(stracture)):
        if stracture[i] != stracture[-(i+1)]:
            print("this str isn't palindrome.")
            return 
    print("this str is palindrome.")

def check_2(stracture, current):
    if current >= len(stracture)/2:
        print("this str is palindrome.")
        return
    # print(stracture[current], stracture[-current - 1])
    if stracture[current] != stracture[-current - 1]:
        print("this str isn't palindrome.")
        return
    check_2(stracture, current + 1)

stracture = input("plese input str:")
check(stracture)
check_2(stracture, 0)

