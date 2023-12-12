import os

# delete the DATA FILE of users

if os.path.isfile("kont.db"):
    os.remove("kont.db")
    print("DATAFILE dropped")
