#setup
import pandas as pd
football_data = pd.read_csv("cfb.csv")

#making dictionary for wins, as well as lists to analyze in the future if statements
categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "fewer than 6 wins": []
}
teams = football_data["Team"].tolist()
wins = football_data["Win"].tolist()
seasons = football_data["Season"].tolist()

#ask the user which season they would like to analyze
season = int(input("Enter a season to analyze: "))
print(f"College Football Results for {season}")

#getting the data
if season in seasons:
    for i in range(len(seasons)):
        if seasons[i] == season:
            if wins[i] >= 10:
                categories["10 or more wins"].append(teams[i])
            elif wins[i] >= 8:
                categories["8-9 wins"].append(teams[i])
            elif wins[i] >= 6:
                categories["6-7 wins"].append(teams[i])
            elif wins[i] < 6:
                categories["fewer than 6 wins"].append(teams[i])
    print("\n10 or more wins: ")
    for team in categories["10 or more wins"]:
        print(team)
    print("\n8-9 wins: ")
    for team in categories["8-9 wins"]:
        print(team)
    print("\n6-7 wins: ")
    for team in categories["6-7 wins"]:
        print(team)
    print("\nFewer than 6 wins: ")
    for team in categories["fewer than 6 wins"]:
        print(team)
elif season not in seasons:
    print("The requested season is not found.")
    
