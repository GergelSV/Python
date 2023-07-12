try:
    apples = int(input("Enter the amount of apples you have: "))
    if apples < 0:
        raise Exception("You can’t have  " + str(apples) + "  apples\n")
    parts_number = int(input("Enter the number    of parts: "))
    parts_amount = apples / parts_number
    print("You have", apples, "apples \n")
    print("Each of " + str(parts_number) + " parts consists of " + str(parts_amount) + " apples")
except (ZeroDivisionError, ValueError):
    print("Improper value was obtained")
except Exception as ex:
    print(ex)
except:
    print("Hmm... Something went wrong")
finally:
    print("The program has finished")


