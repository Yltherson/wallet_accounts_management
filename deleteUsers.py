import sqlite3 as sqlite

koneksyonDB = sqlite.connect("kont.db")
pwente = koneksyonDB.cursor()

request = "DELETE FROM KONT"

pwente.execute(request)

koneksyonDB.commit()
koneksyonDB.close()

print("all users have been dropped")