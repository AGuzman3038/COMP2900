
def age():
    global currentYear
    global birthYear
    
    currentAge = currentYear - birthYear
    print(f"You age is {currentAge}")
    
currentYear = int(input("Current Year: "))
birthYear = int(input("Birth year: "))

age()
