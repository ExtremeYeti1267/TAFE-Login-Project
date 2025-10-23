def login():

    import csv

    inputCredentials = []
    credentials = []
    loginAttempts = -1

    with open('accounts.txt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            credentials.append(row)

    while True:
        i = 0
        loginAttempts += 1

        if loginAttempts >= 3:
            print("Login Failed")
            return False

        if inputCredentials:
            inputCredentials = []
            print('Invalid Username or Password')

        print('Enter Username:')
        inputCredentials.append(input())
        print('Enter Password:')
        inputCredentials.append(input())

        for each in credentials:
            if credentials[i][0] == inputCredentials[0]:
                break
            i += 1

        if len(credentials) != i and credentials[i][0] == inputCredentials[0] and credentials[i][1] == inputCredentials[1]:
            print('Login Success')
            return True