from programRegister import registerUser
from programLogin import login
from programLoginsView import loginsView

loggedOn = False

while True:
    userInput = 'INVALID'

    if loggedOn == False:
        print('\nEnter command to proceed:     \"Register\"     \"Login\"     \"Exit\"\n')

    else:
        print('\nEnter command to proceed:     \"Logoff\"     \"List Users\"     \"Exit\"\n')
    
    userInput = input()
    userInput = userInput.upper()

    if userInput == 'REGISTER' and loggedOn == False:
        registerUser()

    elif userInput == 'LOGIN' and loggedOn == False:
        loggedOn = login()

    elif userInput == 'LIST USERS' and loggedOn == True or userInput == 'LISTUSERS' and loggedOn == True:
        loginsView()

    elif userInput == 'LOGOFF' and loggedOn == True:
        loggedOn = False

    elif userInput == 'EXIT':
        break

    else:
        print("Invalid command.  Please try again.")
