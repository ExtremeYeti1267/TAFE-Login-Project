#   Ethan Todd.
#   29/10/2025.
#   Logic used to display all the users in the "accounts.txt" CSV file.

#   Definses a new function called loginsView for use elsewhere in the program.
def loginsView():
    
    #   Importing library for CSV handling.
    import csv

    #   Defines a credentials list to store CSV file user data, a userCount variable to store the amount of user credentials in the CSV list, and an iterator variable.
    credentials = []
    userCount = 0
    i = 0

    #   Reading CSV login info into the "credentials" list.
    with open('accounts.txt', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            credentials.append(row)
 
    #   Counts the number of users read into the "credentials" list.
    while userCount < len(credentials):
        if len(credentials[userCount]) == 2:
            userCount += 1

    #   Shows the user the number of listed users.
    print(f"\nTotal Users = {userCount}\n")

    #   Displays all the users and passwords stored in the "credentials" list to the user.
    for each in credentials:
        if i <= userCount -1:
            print(f"Username:  {credentials[i][0]}  Password:  {credentials[i][1]}")
        i += 1 