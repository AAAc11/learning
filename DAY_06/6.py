def appending_note(note):
    with open("dziennik.txt","a",encoding="utf-8") as f:
        f.write(note+"\n")

def printing_note():
    with open("dziennik.txt","r",encoding="utf-8") as f:
        print(f"Content of your note: \n{f.read()}")

def main():
    try:
        while True:
            decision = int(input("What do you want to do?\n"
                             "1. Add note\n"
                             "2. Read notes\n"
                             "3. End\n\n"
                             "Your answer: "))
            match decision:
                case 1:
                    note=input("Enter the note: ")
                    appending_note(note)
                case 2:
                    printing_note()
                case 3:
                    break

    except ValueError:
        print("Incorrect answer!")

if __name__ == '__main__':
    main()
