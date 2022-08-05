import mysql.connector as sql
import maskpass #Masks password

#Variable Data Arrays
myOrderItems = []
myOrderCost = []

#Global Variables
nextOrder = True
total = 0

#SQL Database Connection and Cursor Creation (insert your password here)
db = sql.connect(host = "localhost", user = "root", passwd = "", database = "p1")
cur = db.cursor()

#Log-In Function
def login() :
    username = input("Username: ")
    password = maskpass.askpass(prompt="Password: ", mask="*")
    cur = db.cursor()
    statement = f"SELECT username from Users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
        login()
    else:
        print("Success...\n")
    
    if username == "root":
        print("\nWELCOME ADMIN\n")
        isAdmin()

def isAdmin():
    adminChoice = input("Select 1 to add users\n2 to remove users\n3 to continue to store\n>>> ")
    if adminChoice == "1":
        newUser()
    elif adminChoice == "2":
        cur = db.cursor()
        sql = "DELETE FROM Users WHERE username = %s;"
        kill = input("Enter username you wish to remove >>> ")
        kill = (kill, )
        cur.execute(sql, kill)
        print("\nKILL CONFIRMED\nReturning to Sign-In...")
        db.commit()
    else:
        pass

#Create New User Function
def newUser():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    user_type = "user"
    sql = "INSERT INTO Users(username, password, user_type) VALUES (%s, %s, %s)"
    val = (username, password, user_type)
    cur.execute(sql, val)
    db.commit()
    print("Account created. Please sign in...\n")
    login()

#Opening 'Wanna Buy' Question
def Opening():
    first_variable = input("Welcome Back!\nWant some SICK MERCH? Yes/No >>> ")
    if len(first_variable) < 1: #Prevents crash if nothing is entered
        print("\nWHOOPS!\n")
        Opening()
    if first_variable.lower()[0] == "n":
        print("\nFine then...")
        cur.close()
        db.close()
        exit()
    else:
        print("\nFantastic!!!\n")

#The Menu List
def orderMenu():
    print("*************************\nHere's what we're offering:\n")
    print("1. Media\ndesc: Our debut album, 'We Just Killed Bambi'\n ")
    print("2. Shirts\ndesc: They're cool, trust us. No you can't see them before ordering.\n ")
    print("3. Hats\ndesc: Not the funny kind.\n ")
    print("4. Other\ndesc: Peek into the mystery box\n*************************")

#Item Selection Function
def itemSelect(theOrder):
    global total #Allows the function to access global variable
    if (theOrder.lower()[0] == "m" or theOrder == "1"):
        print("Type?\n1 for CD ($10)\n2 for Vinyl ($25)\n3 for Digital ($9)")
        Type = input(">>> ")
        if Type == "1":
            #Pulling the String Value from Database
            statement = "select item_name from Items where item_name = 'CD';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            #Pulling the Integer Value from Database
            statement = "select price from Items where item_name = 'CD';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)
                
        elif Type == "2":
            statement = "select item_name from Items where item_name = 'Vinyl';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Vinyl';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        elif Type == "3":
            statement = "select item_name from Items where item_name = 'Digital';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Digital';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)
        else:
            print("NO DICE PAL. PUT A NUMBER IN")

    elif (theOrder.lower()[0] == "s" or theOrder == "2"):
        print("Type?\n1 for T-Shirt ($20)\n2 for Long Sleeve ($25)\n3 for Hoodie ($40)")
        Type = input(">>> ")
        if Type == "1":
            #Direct append used because of difficulty manipulating strings with special characters
            myOrderItems.append("T-Shirt")

            statement = f"select price from Items where item_name = 'T-Shirt';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        elif Type == "2":
            #Direct append used because of difficulty manipulating strings with special characters
            myOrderItems.append("Long Sleeve")

            statement = "select price from Items where item_name = 'Long Sleeve';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        elif Type == "3":
            statement = "select item_name from Items where item_name = 'Hoodie';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Hoodie';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)
        else:
            print("NO DICE PAL. PUT A NUMBER IN")

    elif (theOrder.lower()[0] == "h" or theOrder == "3"):
        print("Type?\n1 for Snapback ($30)\n2 for Beanie ($20)\n3 for Golden Sombrero ($100)")
        Type = input(">>> ")
        if Type == "1":
            statement = "select item_name from Items where item_name = 'Snapback';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Snapback';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        elif Type == "2":
            statement = "select item_name from Items where item_name = 'Beanie';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Beanie';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        elif Type == "3":
            statement = "select item_name from Items where item_name = 'Golden Sombrero';"
            #Direct append used because of difficulty manipulating strings with special characters
            myOrderItems.append("Golden Sombrero")

            statement = "select price from Items where item_name = 'Golden Sombrero';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)
        else:
            print("NO DICE PAL. PUT A NUMBER IN")

    elif (theOrder.lower()[0] == "o" or theOrder == "4"):
        print("Type?\n1 for Pins ($10)\n2 for Stickers ($3)")
        Type = input(">>> ")
        if Type == "1":
            statement = "select item_name from Items where item_name = 'Pins';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Pins';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        elif Type == "2":
            statement = "select item_name from Items where item_name = 'Stickers';"
            cur.execute(statement)
            string = cur.fetchone()
            res = ""
            for row in string:
                if row.isalpha():
                    res = "".join([res, row])
            myOrderItems.append(str(res))

            statement = "select price from Items where item_name = 'Stickers';"
            cur.execute(statement)
            charge = cur.fetchone()
            for row in charge:
                total += row
                myOrderCost.append(row)

        else:
            print("NO DICE PAL. PUT A NUMBER IN")

    else:
        print("NO DICE PAL. YOU GOTTA BUY SOMETHING NOW.")

    return total

def receipt(total):
    global username
    print("\n**********")
    for each in range(len(myOrderItems)):
        print(myOrderItems[each], ":", "$", myOrderCost[each])
    print("**********")
    print("\nTotal: $" + str(round(total, 2)))

def confirm():
    print("Re-enter your user credentials to confirm:")
    username = input("Username: ")
    password = maskpass.askpass(prompt="Password: ", mask="*")
    statement = f"SELECT PersonID from Users WHERE username='{username}' AND Password = '{password}';"
    cur.execute(statement)
    id = cur.fetchone()
    for row in id:
        id = row

    sql = "INSERT INTO Orders(customer_id, total) VALUES (%s, %s)"
    val = (id, total)
    cur.execute(sql, val)
    db.commit()
    cur.close()
    db.close()
    print("\nYour order has been placed...\nWe already know your credit card #...\nLater, chump.")

    quit()


#PROGRAM START
print("**********\nWelcome to the (Un)Official Store of\nABRIDGE ABUTMENT")
print("Pioneers of Ska-Punk Deathcore\n**********")

while __name__ == "__main__":
    if total == 0:
        userQ = input("New User? Yes/No >>> ")
        if userQ.lower() == "y":
                newUser()
        login()
        Opening()
    orderMenu()
    theOrder = input("\nEnter the item name or number here >>> ")
    itemSelect(theOrder)
    finished = input("Item added.\n\nFinished? Yes/No >>> ")
    if finished.lower() == "y":
        receipt(total)
        confirm()
