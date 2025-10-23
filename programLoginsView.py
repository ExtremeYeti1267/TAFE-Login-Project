def loginsView():
    
    import csv

    credentials = []
    userCount = 0
    i = 0

    with open('accounts.txt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            credentials.append(row)
 

    while True:
        if len(credentials[userCount]) == 2:
            userCount += 1
        elif userCount == len(credentials):
            break
        else:
            break

    print(f"\n{userCount} Users Listed.\n")

    for each in credentials:
        if i <= userCount -1:
            print(f"Username:  {credentials[i][0]}  Password:  {credentials[i][1]}")
        i += 1