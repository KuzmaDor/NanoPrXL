from string import ascii_letters
def loginScreen():
        nameCheck = ascii_letters + " "
        passCheck = ascii_letters + "1234567890_"
        print("│ Sup, stranger. Want to enter my store? Well then, time to make an account.")
        name = input("│ Enter your name: ")

        #getting player's name
        while True:
            if not all(i in nameCheck for i in list(name)):
                name = input("\n│ You're either creating a name by smashing your face \
on the keyboard \
\n│ or using a language that i don't speak. \
\n\n│ Please try again: ")
            elif name == " " or name == "":
                name = "No name Nancy"
                break
            else:
                name = name[0].upper() + name[1:]
                break

        #making the utterly useless and annoying password    
        months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        print(f"\n│ Ok {name}, time to make a password")

        #a lot of checks
        while True:
            password = input("\n│ Your password: ")
            if password.casefold() == "shut up im a dev":
                break
            if password == "":
                print("│ At least try")
                continue
            if not all(i in passCheck for i in list(password)):
                print("│ Only letters and numbers are allowed. Maybe an underscore if im in a good mood")
                continue
            elif not any(chr.isdigit() for chr in password): 
                print("│ Your password must contain a number")
                continue
            elif not any(chr.isalpha() for chr in password):
                print("│ Your password must contain at least one letter")
                continue
            flag = 0
            for month in months:
                if month in password.casefold():
                    flag = 1
                    break
            if not flag:
                print("│ Your password must contain at least one month of the year")
                continue
            passNumbers = 0
            for character in password:
                if character in "1234567890":
                    passNumbers += int(character)
            if passNumbers != 25:
                print("│ The numbers in your password must add up to 25")
                continue
            flaggers = 0
            for character in password.casefold():
                if character.casefold() == "u" or character.casefold() == "r":
                    print("│ yoUR passwoRd Uses one of two letteRs that i don't like. make a diffeRent one")
                    flaggers = 1
                    break
            if flaggers:
                continue
            flaggyboi = 0
            for char in password:
                if char == "9":
                    print("│ EEEEEEEEEEEEEEW, is that a 9? I hate that number! REMOVE IT!")
                    flaggyboi = 1
                    break
            if flaggyboi:
                continue
            if len(password) >= 10:
                print("│ Your password is too long, not gon tell you the limit tho")
                continue

            else:
                break
        print("│ Just kidding, none of it matters, come on in\n")
        return name