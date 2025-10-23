def registerUser():

    import csv

    inputCredentials = []
    credentials = []
    lineCount = 0
    confirmPassword = ''
    
    with open('accounts.txt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            credentials.append(row)

        for row in credentials:
            if len(row) > 1 and len(row[1]) >= 10:
                lineCount += 1

    while True:
        i = 0
        Taken = False

        if inputCredentials:
            inputCredentials = []
            print('Invalid password.  Please try again.')

        while True:
            print('Enter Username:')
            inputCredentials.append(input())
            print('Enter Password:')
            inputCredentials.append(input())
            print('Please Confirm Password')
            confirmPassword = input()

            if inputCredentials[1] != confirmPassword:
                print('Passwords do not match.  Please try again.')
            
            else:
                break

        for each in credentials:
            if credentials[i][0] == inputCredentials[0]:
                Taken = True
                break
            i += 1

            if i == lineCount:
                break
        
        if Taken == False and len(inputCredentials[1]) >= 10:
            
            
            with open('accounts.txt', mode='r', newline='') as file:
                lines = list(csv.reader(file))

            lines.insert(lineCount, inputCredentials)

            with open('accounts.txt', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(lines)

            print('User Created Successfully')
            return True