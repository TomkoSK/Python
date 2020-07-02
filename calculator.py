from colorama import Fore, Back, Style
try:
    exit = False
    print(Fore.BLUE +"------------------------------------------ \n               Calculator \n------------------------------------------ " + Style.RESET_ALL)
    print(Fore.BLUE + "Do you want to multiply, divide, add up or subtract? (Write the number next to the option, not the name of it)")
    optionIsInt = 0
    while optionIsInt == 0:
        print(Fore.GREEN +"1 Multiply\n2 Divide\n3 Add up\n4 Subtract")
        option = (input(Fore.BLUE + ":"))
        if option == "1":
            optionIsInt = 1
            print(Fore.GREEN + "Write the first factor")
            firstNumber = float(input(Fore.BLUE + ":"))
            print(Fore.GREEN + "Write the second factor")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = firstNumber * secondNumber
            print(Fore.BLUE + "The result is " +Fore.RED +  str(result) +Fore.BLUE + ". What do you want to do with the result?")
        elif option == "2":
            optionIsInt = 1
            print("Write the dividend")
            firstNumber = float(input(Fore.BLUE + ":"))
            print("Write the divisor")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = firstNumber / secondNumber
            print("The result is " +Fore.RED +  str(result)+Fore.BLUE + ". What do you want to do with the result?")
        elif option == "3":
            optionIsInt = 1
            print("Write the first addend")
            firstNumber = float(input(Fore.BLUE + ":"))
            print("Write the second addend")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = firstNumber + secondNumber
            print("The result is " +Fore.RED +  str(result)+Fore.BLUE + ". What do you want to do with the result?")
        elif option == "4":
            optionIsInt = 1
            print("Write the minuend")
            firstNumber = float(input(Fore.BLUE + ":"))
            print("Write the subtrahend")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = firstNumber - secondNumber
            print("The result is " +Fore.RED +  str(result)+Fore.BLUE + ". What do you want to do with the result?")
        else:
            print("Write the number next to the option, not the name of it")

    while exit == False:
        print(Fore.GREEN + "1 Multiply\n2 Divide\n3 Add up\n4 Subtract\n5 Turn off the calculator")
        option = (input(Fore.BLUE + ":"))
        if option == "1":
            print(Fore.GREEN + "Write the factor")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = result * secondNumber
            print("The result is " + Fore.RED + str(result)+Fore.BLUE + ". What do you want to do with the result?")
        elif option == "2":
            print(Fore.GREEN + "Write the divisor")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = result / secondNumber
            print("The result is " + Fore.RED + str(result)+Fore.BLUE + ". What do you want to do with the result?")
        elif option == "3":
            print(Fore.GREEN + "Write the addend")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = result + secondNumber
            print("The result is " + Fore.RED + str(result)+Fore.BLUE + ". What do you want to do with the result?")
        elif option == "4":
            print(Fore.GREEN + "Write the subtrahend")
            secondNumber = float(input(Fore.BLUE + ":"))
            result = result - secondNumber
            print("The result is " + Fore.RED +  str(result)+Fore.BLUE + ". What do you want to do with the result?")
        elif option == "5":
            print(Fore.RED + "Turning off the calculator...")
            quit()
        else:
            print("Write the number next to the option, not the name of it")
except ValueError:
    print(Fore.RED + "Only write numbers, not words. If you don't want to write integers, write \"0.5\" not \"0,5\"")
except KeyboardInterrupt:
    print(Fore.RED + "Turning off the calculator...")