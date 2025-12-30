
        if menu_function == 1:
        print("Phonebook")
        phonebook_menu = """
        PHONEBOOK
        Press 1 For Search
        Press 2 For Service Number
        Press 3 For Add name
        Press 4 For Erase
        Press 5 For Edit
        Press 6 For Assign tone
        Press 7 For Send b'card
        Press 8 For Options
        Press 9 For Speed dials
        Press 10 For Voice tags
        """
        print(phonebook_menu)
        choice = int(input("Choose: "))
        if choice == 1:
            print("Search")
        elif choice == 2:
            print("Service number")
        elif choice == 3:
            print("Add name")
        elif choice == 4:
            print("Erase")
        elif choice == 5:
            print("Edit")
        elif choice == 6:
            print("Assign tone")
        elif choice == 7:
            print("Send b'card")
        elif choice == 8:
            print("Options")
            options_menu = """
            Press 1 For Type of view
            Press 2 For Memory Status
            """
            print(options_menu)
            opt_choice = int(input("Choose: "))
            if opt_choice == 1:
                print("Type of view")
            elif opt_choice == 2:
                print("Memory status")
        elif choice == 9:
            print("Speed dials")
        elif choice == 10:
            print("Voice tags")

    elif menu_function == 2:
        print("Messages")
        messages_menu = """
        MESSAGES
        Press 1 For Write messages
        Press 2 For Inbox
        Press 3 For Outbox
        Press 4 For Picture messages
        Press 5 For Templates
        Press 6 For Smileys
        Press 7 For Send b'card
        Press 8 For Info service
        Press 9 For Voice mailbox number
        Press 10 For Service command editor
        """
        print(messages_menu)
        choice = int(input("Choose: "))
        if choice == 1:
            print("Write messages")
        elif choice == 2:
            print("Inbox")
        elif choice == 3:
            print("Outbox")
        elif choice == 4:
            print("Picture messages")
        elif choice == 5:
            print("Templates")
        elif choice == 6:
            print("Smileys")
        elif choice == 7:
            print("Send b'card")
        elif choice == 8:
            print("Info Services")
        elif choice == 9:
            print("Voice mailbox")
        elif choice == 10:
            print("Service Command editor")

    elif menu_function == 3:
        print("Chat")
    elif menu_function == 4:
        print("Call Register")
    elif menu_function == 5:
        print("Tones")
    elif menu_function == 6:
        print("Settings")
    elif menu_function == 7:
        print("Call divert")
    elif menu_function == 8:
        print("Games")
    elif menu_function == 9:
        print("Calculator")
    elif menu_function == 10:
        print("Remainders")
    elif menu_function == 11:
        print("Clock")
    elif menu_function == 12:
        print("Profile")
    elif menu_function == 13:
        print("SIM services")
    else:
        print("Invalid choice!")




