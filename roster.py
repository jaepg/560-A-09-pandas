import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau", "Claude", "Brown", "Tyson"
                        ,"Davis","Trimble","Powell","Jackson"],
          "First Name": ["Armando", "RJ", "Elliot", "Ty", "James", "Cade",
                         "Elijah","Seth","Drake","Ian"],
          "height": [83,72,73,79,82,79,75,75,78,76],
          "weight": [240,180,180,230,215,200,215,195,195,190]
          }

data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters squared and round to two decimal points
data["bmi"] = round((data["weight"]/2.205)/((data["height"]/39.37)**2), 2)

print(data)

data.to_csv("bmi.csv")