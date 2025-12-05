# ========================= WASABI GAME STORE =========================
# A simple command-line application to manage a game store's inventory.
# Users can add, update, delete, and sell games, as well as browse the catalog.

# ========================= GAME DATA =========================

# List of games stored as dictionaries in a list
# Each game contains: Id, Name, Category, Genre, Stock, and Price
games = [{"Id" : "GN001",
          "Name" : "Pokemon Legends Arceus",
          "Category" : "Nintendo",
          "Genre" : "Action RPG",
          "Stock" : "25", 
          "Price" : "650000"},
          {"Id" : "GP001",
          "Name" : "Uncharted 4",
          "Category" : "Playstation",
          "Genre" : "Adventure",
          "Stock" : "15", 
          "Price" : "680000"},
          {"Id" : "GX001",
          "Name" : "Forza Horizon 5",
          "Category" : "Xbox",
          "Genre" : "Racing",
          "Stock" : "10", 
          "Price" : "640000"}
]

# Valid categories of games
listCategory = ["Nintendo", "Playstation", "Xbox"]

# ========================= MAIN MENU =========================

def mainDashboard():
    # Display the main dashboard menu
    print("\n==== WASABI GAME ====")
    print("1. Add Game")
    print("2. Game Catalog")
    print("3. Update Game")
    print("4. Delete Game")
    print("5. Sell Game")
    print("6. Exit\n")
    print("Choose Menu [1-6]")

def inputMenu():
    # Input user menu choice
    global choose
    choose = input("Input Menu: ")

def inputNotValid():
    # Show message for invalid input
    print('Input Invalid!')

def inputValid(x):
    # Show message for successful action
    print(f"\nGame has been {x}")

# ========================= ADD GAME =========================

def dashboard1():
    # Display submenu for adding games
    print("\n=== Data Addition Menu ===")
    print("1. Add Game")
    print("2. Back to Main Menu")
    print("Choose Menu [1-2]")

def subDashboard1():
    # Display submenu for adding games
    while True:
        dashboard1()
        inputMenu()
        if choose == "1":
            addGame()
            continue
        elif choose == "2":
            break
        else:
            inputNotValid()

def addGame():
    # Add a new game with user input validation
    # Ensures no duplicate IDs and correct formatting for all fields   
    while True:
        print("Game Id input format must be 2 Alphabets and 3 Numbers! Ex: XX000")
        gameId = input("Input Game Id: ")
        if any(game["Id"] == gameId.upper() for game in games):
            print("\n--- Game Id already exists! ---")
            return
        elif not (len(gameId) == 5 and gameId[:2].isalpha() and gameId[2:].isdigit()):
            inputNotValid()
            continue
        else:
            break
    while True:   
        gameName = input("Input Game Name: ")
        if not gameName.strip():
            inputNotValid()
            continue
        else:
            break
    while True:
        gameCategory = input("Input Game Category [Nintendo/Playstation/Xbox]: ")
        if gameCategory.capitalize() not in listCategory:
            inputNotValid()
            continue
        else:
            break
    while True:
        gameGenre = input("Input Game Genre [Genre can't be Numbers]: ")
        if not gameGenre.isalpha() or gameGenre.isspace():
            inputNotValid()
            continue
        else:
            break
    while True:
        gameStock = (input("Input Game Stock [Stock must be Numbers and can't be minus]: "))
        if not gameStock.isdigit():
            inputNotValid()
            continue
        else:
            break
    while True:
        gamePrice = (input("Input Game Price [Price must be Numbers and can't 0 or minus]: "))
        if not gamePrice.isdigit() or gamePrice == "0":
            inputNotValid()
            continue
        else:
            break
    while True:
        saveGame = input("Will the Data be saved? [Yes/No]: ")
        if saveGame.capitalize() == "Yes":
            newGame = {"Id" : gameId.upper(),
                       "Name" : gameName.title(),
                       "Category" : gameCategory.capitalize(),
                       "Genre" : gameGenre.title(),
                       "Stock" : gameStock,
                       "Price" : gamePrice} 
            games.append(newGame)
            inputValid("added!")
            listGame()
            break
        elif saveGame.capitalize() == "No":
            print("\n--- Data addition has been canceled! ---")
            break
        else:
            inputNotValid()

# ========================= VIEW GAME CATALOG =========================

def dashboard2():
    # Display submenu for game catalog
    print("\n=== Game Catalog ===")
    print("1. Game's List")
    print("2. Choose Game by Id")
    print("3. Game's by Category")
    print("4. Back to Main Menu")
    print("Choose Menu [1-3]")

def subDashboard2():
    # Navigate game catalog submenu
    while True:
        dashboard2()
        inputMenu()
        if choose == "1":
            listGame()
            continue
        elif choose == "2":
            gameById()
            continue
        elif choose == "3":
            gameByCategory()
            continue
        elif choose == "4":
            break
        else:
            inputNotValid()

def listGame():
    # Display all games
    print("\nList of Games")
    print("=" * 90)
    print(f"{'Id':<6} | {'Name':<25} | {'Category':<12} | {'Genre':<12} | {'Stock':>5} | {'Price':>8}")
    print("-" * 90)
    for game in games:
        print(f"{game['Id']:<6} | {game['Name'].title():<25} | {game['Category'].capitalize():<12} | {game['Genre'].title():<12} | {game['Stock']:>5} | {game['Price']:>8}")
    print("=" * 90)
    
def gameById():
    # Display certain game by Id
    print("\nChoose Game by Id")
    while True:
        inputId = input("\nInput Game Id: ")
        if not any(i["Id"] == inputId.upper() for i in games):
            print("\n--- Game not exist! ---")
            return
        else:
            print("=" * 90)
            print(f"{'Id':<6} | {'Name':<25} | {'Category':<12} | {'Genre':<12} | {'Stock':>5} | {'Price':>8}")
            print("-" * 90)
            for i in games:
                if i["Id"] == inputId.upper():
                    print(f"{i['Id']:<6} | {i['Name'].title():<25} | {i['Category']:<12} | {i['Genre'].title():<12} | {i['Stock']:>5} | {i['Price']:>8}")
                    print("=" * 90) 
            break

def gameByCategory():
    # Display game by category
    print("\nList of Games by Category")
    while True:
        inputCategory = input("Input Category [Nintendo/Playstation/Xbox]: ")
        if inputCategory.capitalize() not in listCategory:
            inputNotValid()
            return
        else:
            print("\nList of Games by Category")
            print("=" * 90)
            print(f"{'Id':<6} | {'Name':<25} | {'Category':<12} | {'Genre':<12} | {'Stock':>5} | {'Price':>8}")
            print("-" * 90)
            for i in games:
                if i["Category"] == inputCategory.capitalize():
                    print(f"{i['Id']:<6} | {i['Name'].title():<25} | {i['Category']:<12} | {i['Genre'].title():<12} | {i['Stock']:>5} | {i['Price']:>8}")
                    print("=" * 90) 
            break

# ========================= UPDATE GAME =========================

def dashboard3():
    # Display submenu for udpating games
    print("\n=== Update Game Data ===")
    print("1. Update Game")
    print("2. Back to Main Menu")
    print("Choose Menu [1-2]")

def subDashboard3():
    # Navigate update game submenu
    while True:
        dashboard3()
        inputMenu()
        if choose == "1":
            updateGame()
            continue
        elif choose == "2":
            break
        else:
            inputNotValid()

def updateGame():
    # Display submenu for updating games
    print("\nUpdate Game by Id")
    while True:
        inputId = input("\nInput Game Id: ")
        if not any(i["Id"] == inputId.upper() for i in games):
            print("\n--- Game not exist! ---")
            return
        else:
            print("=" * 90)
            print(f"{'Id':<6} | {'Name':<25} | {'Category':<12} | {'Genre':<12} | {'Stock':>5} | {'Price':>8}")
            print("-" * 90)
            for i in games:
                if i["Id"] == inputId.upper():
                    index = i
                    print(f"{i['Id']:<6} | {i['Name']:<25} | {i['Category']:<12} | {i['Genre']:<12} | {i['Stock']:>5} | {i['Price']:>8}")
                    print("=" * 90) 
            break
    while True:
        editGame = input("Will the Data be updated? [Yes/No]: ")
        if editGame.capitalize() == "Yes":
            while True:
                inputColumn = input("Specify the column to edit: ")
                # Prevent update if input is not a valid column
                if inputColumn.capitalize() not in games[0].keys():
                    inputNotValid()
                    continue
                elif inputColumn.capitalize() == 'Id':
                    print("Id is a Primary Key. Cannot be changed!")
                    continue
                else:
                    break
            # Handle specific validation for each column
            if inputColumn.title() == "Name":
                while True:
                    newValue = input(f"Input new {inputColumn.title()}: ")
                    if not newValue.strip():
                        inputNotValid()
                        continue
                    else:
                        break
            elif inputColumn.title() == "Category":
                while True:
                    newValue = input(f"Input new {inputColumn.title()}: ")
                    if newValue.capitalize() not in listCategory:
                        inputNotValid()
                        print("Category can only be Nintendo/PlayStation/Xbox!")
                        continue
                    else:
                        break
            elif inputColumn.title() == "Genre":
                while True:
                    newValue = input(f"Input new {inputColumn.title()}: ")
                    if not newValue.isalpha() or newValue.isspace():
                        inputNotValid()
                        print("Genre can't be Numbers!")
                        continue
                    else:
                        break
            elif inputColumn.title() == "Stock":
                while True:
                    newValue = input(f"Input new {inputColumn.title()}: ")
                    if not newValue.isdigit():
                        inputNotValid()
                        print("Stock must be a Number!")
                        continue
                    else:
                        break
            elif inputColumn.title() == "Price":
                while True:
                    newValue = input(f"Input new {inputColumn.title()}: ")
                    if not newValue.isdigit() or newValue == "0":
                        inputNotValid()
                        print("Price must be Numbers and can't 0 or minus!")
                        continue
                    else:
                        break
            while True:
                confirmationEdit = input("Are you sure want to update into new data? [Yes/No]: ")
                if confirmationEdit.capitalize() == "Yes":
                    index[inputColumn.title()] = newValue
                    print(f"Game {inputColumn.capitalize()} successfully updated to {newValue.title()}!")
                    listGame()
                    break
                elif confirmationEdit.capitalize() == "No":
                    print("\n--- Game Data Update has been canceled! ---")
                    break
                else:
                    inputNotValid()
                    continue
            break
        elif editGame.capitalize() == 'No':
            print("\n--- Game Data Update has been canceled! ---")
            break
        else:
            inputNotValid()
            continue

# ========================= DELETE GAME =========================

def dashboard4():
    # Display submenu for deleting games
    print("\n=== Delete Game Data ===")
    print("1. Delete Game")
    print("2. Back to Main Menu")
    print("Choose Menu [1-2]")

def subDashboard4():
    # Navigate delete game submenu
    while True:
        dashboard4()
        inputMenu()
        if choose == "1":
            deleteGame()
            continue
        elif choose == "2":
            break
        else:
            inputNotValid()

def deleteGame():
    # Delete a game by its Id
    print("\nDelete Game by Id")
    while True:
        inputId = input("Input Game Id: ")
        if not any(i["Id"] == inputId.upper() for i in games):
            print("\n--- Game not exist! ---")
            return
        else:
            print("=" * 90)
            print(f"{'Id':<6} | {'Name':<25} | {'Category':<12} | {'Genre':<12} | {'Stock':>5} | {'Price':>8}")
            print("-" * 90)
            for i in games:
                if i["Id"] == inputId.upper():
                    index = i
                    print(f"{i['Id']:<6} | {i['Name']:<25} | {i['Category']:<12} | {i['Genre']:<12} | {i['Stock']:>5} | {i['Price']:>8}")
                    print("=" * 90) 
            break
    while True:
        deleteGame = input("Data will be deleted? [Yes/No]: ")
        if deleteGame.capitalize() == "Yes":
            games.remove(index)
            inputValid("deleted!")
            listGame()
            return
        elif deleteGame.capitalize() == "No":
            inputValid("not deleted!")
            break
        else:
            inputNotValid()

# ========================= SELL GAME =========================

def dashboard5():
    # Display submenu for selling games
    print("\n=== Sell Game ===")
    print("1. Sell Game")
    print("2. Back to Main Menu")
    print("Choose Menu [1-2]")

def subDashboard5():
    # Navigate sell game submenu
    while True:
        dashboard5()
        inputMenu()
        if choose == "1":
            sellGame()
            continue
        elif choose == "2":
            break
        else:
            inputNotValid()

def sellGame():
    # Sell a game and reduce stock
    print("\nSell Game")
    listGame()
    while True:
        inputId = input("Input Game Id to Sell: ")
        if not any(i["Id"] == inputId.upper() for i in games):
            print("\n--- Game not exist! ---")
            return
        else:
            print("=" * 90)
            print(f"{'Id':<6} | {'Name':<25} | {'Category':<12} | {'Genre':<12} | {'Stock':>5} | {'Price':>8}")
            print("-" * 90)
            for i in games:
                if i["Id"] == inputId.upper():
                    index = i
                    print(f"{i['Id']:<6} | {i['Name']:<25} | {i['Category']:<12} | {i['Genre']:<12} | {i['Stock']:>5} | {i['Price']:>8}")
                    print("=" * 90)
            break
    while True:
        inputStock = input("Input Stock to Sell [Stock must be numbers]: ")
        if not inputStock.isdigit():
            inputNotValid()
            continue
        inputStock = int(inputStock)
        if inputStock <= 0:
            print("Stock must be more than 0!")
            continue
        if inputStock > int(index["Stock"]):
            print("Not enough stock available!")
            return
        break
    total = int(index["Price"]) * inputStock
    while True:
        confirm = input(f"Confirm sale of {inputStock} pcs for Rp{total}? [Yes/No]: ")
        if confirm.capitalize() == "Yes":
            index["Stock"] = str(int(index["Stock"]) - inputStock)
            print(f"Transaction recorded! Amount received: {total}")
            print(f"\n{index["Name"]} -- Remaining stock: {index["Stock"]}")
            break
        elif confirm.capitalize() == "No":
            print("\nTransaction canceled.")
            break
        else:
            inputNotValid()

def startMenu():
    # Main program loop to display and interact with dashboard
    while True:
        mainDashboard()
        inputMenu()
        if choose == "1":
            subDashboard1()
            continue
        elif choose == "2":
            subDashboard2()
            continue
        elif choose == "3":
            subDashboard3()
            continue
        elif choose == "4":
            subDashboard4()
            continue
        elif choose == "5":
            subDashboard5()
            continue
        elif choose == "6":
            print("Thank you, see you again!")
            break
        else:
            inputNotValid()
            continue
startMenu()
