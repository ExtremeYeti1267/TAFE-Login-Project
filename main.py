#   Ethan Todd.
#   29/10/2025.
#   Login program for integration into other applications.

#   Importing fuctions created in other python files.
from programRegister import registerUser
from programLogin import login
from programLoginsView import loginsView

#   Login status variable.
loggedOn = False

#   Loop to keep program running until the user specifies.
while True:

    #   Reset user input.
    userInput = 'INVALID'

    #   If and else statement displays user navigation options based on the loggedOn variable state.
    if loggedOn == False:
        print('\nEnter command to proceed:     \"Register\"     \"Login\"     \"Exit\"\n')

    else:
        print('\nEnter command to proceed:     \"Logoff\"     \"List Users\"     \"Exit\"\n')
    
    #   Assigns user keyboard input to userInput variable.
    userInput = input()

    #   Converts users keyboard input to uppercase removing the need for case sensitivity for navigation.
    userInput = userInput.upper()

    #   The below if and elif statements check user input against valid navigation commands and executes related functions.
    if userInput == 'REGISTER' and loggedOn == False:
        registerUser()

    elif userInput == 'LOGIN' and loggedOn == False:
        loggedOn = login()
    
    elif userInput == 'LOGIN' and loggedOn == True:
        print("\n Already logged in.")

    elif userInput == 'LIST USERS' and loggedOn == True or userInput == 'LISTUSERS' and loggedOn == True:
        loginsView()

    elif userInput == 'LIST USERS' and loggedOn == False or userInput == 'LISTUSERS' and loggedOn == False:
        print('\nYou are currently logged out.  Please login to access this feature.')

    elif userInput == 'LOGOFF' and loggedOn == True:
        loggedOn = False

    elif userInput == 'LOGOFF' and loggedOn == False:
        print('\nNot currently logged in.  Type \"exit\" to quit')

    elif userInput == 'EXIT':
        break

    #inform the user that the input command was invalid.
    else:
        print("\nInvalid command.  Please try again.")
