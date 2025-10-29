#   Ethan Todd.
#   29/10/2025.
#   Logic used to register a new login that is compliant with password requirements for use in the program.

#   Definses a new function called regiserUser for use elsewhere in the program.
def registerUser():

    #   Importing library for CSV handling.
    import csv

    #   Declaration of list to store CSV credentials as well as a line counter variable and variables for a username, password and password confirmation.
    credentials = []
    lineCount = 0
    username = ''
    password = ''
    confirmPassword = ''
    
    #   Reading CSV login info into the "credentials" list.
    with open('accounts.txt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            credentials.append(row)

        #   Counting number of valid passwords in the credentials list.
        for row in credentials:
            if len(row) > 1 and len(row[1]) >= 10:
                lineCount += 1

    #   Loop for user registration logic.  Loop will exit when a username and password is added to the "accounts.txt" CSV file.
    while True:

        #   Variables for registration logic.
        i = 0
        Taken = False

        #   Sets the username, password and confirmPassword variables to empty if any of them are populated.
        if username or password or confirmPassword:
            username = ''
            password = ''
            confirmPassword = ''
            print('\nInvalid username or password.  Please try again.')

        #   Asks for username, password and password confirmation and saves it to the username, password and confirmPassword variables.
        while True:
            print('\nEnter Username:')
            username = input()
            print('\nEnter Password:')
            password = input()
            print('\nPlease Confirm Password')
            confirmPassword = input()

            #   Checks if the passwords typed by the user match.
            if password != confirmPassword:
                print('\nPasswords do not match.  Please try again.')
            
            else:
                break

        #   Checks to make sure the username does not already exist.
        for each in credentials:
            if credentials[i][0] == username:
                Taken = True
                break
            i += 1

            if i == lineCount:
                break
        
        #   Checks to ensure username and password validity before writing to the "accounts.txt" CSV file.
        if Taken == False and len(password) >= 10:
            
            #   Write input credentials to "accounts.txt" CSV file.
            with open('accounts.txt', mode='r', newline='') as file:
                lines = list(csv.reader(file))

            lines.insert(lineCount, [username, password])

            with open('accounts.txt', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            #   Inform the user of the successful creation of the account.
            print('\nUser Created Successfully')
            break