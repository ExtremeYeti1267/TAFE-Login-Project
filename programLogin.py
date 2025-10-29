#   Ethan Todd.
#   29/10/2025.
#   Login logic for use in login program.  Checks usernames and passwords from the "accounts.txt" csv file.

#   Definses a new function called Login for use elsewhere in the program.
def login():

    #   Importing library for CSV handling.
    import csv

    #   Lists and variable used to keep track of user's input credentials and saved CSV credentials as well as login attempts.
    inputCredentials = []
    credentials = []
    loginAttempts = 0

    #   Reading CSV login info into the "credentials" list.
    with open('accounts.txt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            credentials.append(row)

    #   Loop for login logic.  Loop will exit when a return statement is reached.
    while True:
        
        #   Iteration variable to check array content with.
        i = 0

        #   Increment loggin attempt count.
        loginAttempts += 1

        #   Returns false if the username and or password is incorrect too many times.
        if loginAttempts >= 4:
            print("Login Failed")
            return False

        #   Resets the inputCredentials list to be empty.
        if inputCredentials:
            inputCredentials = []
            print('\nInvalid Username or Password')

        #   Request and store user input to the inputCredentials list.
        print('\nEnter Username:')
        inputCredentials.append(input())
        print('\nEnter Password:')
        inputCredentials.append(input())

        #   Checks for the input username against the stored CSV credentials to see if it exists.  If it does exist then the loop will exit leaving the i variable equal to the position of the valid login in the 
        #   credentials list.  If it does not exist then i will be a value outside of the array bounds meaning the if statement at the end of the program will not run.  I will be reset at the beginning of the loop 
        #   and the user will be prompted to try login again.
        for each in credentials:
            if credentials[i][0] == inputCredentials[0]:
                break
            i += 1

        #   Checks that its not trying to compare the user input credentials to a nonexistent part of the credentials list.  It also checks if the input username and password is found in the CSV file info stored in 
        #   the credentials list.  If all these conditions are true it will let the user know the login was successfull and return true.
        if len(credentials) != i and credentials[i][0] == inputCredentials[0] and credentials[i][1] == inputCredentials[1]:
            print('\nLogin Success')
            return True