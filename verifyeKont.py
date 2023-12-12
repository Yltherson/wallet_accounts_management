import sqlite3 as sqlite

koneksyonDB = sqlite.connect("kont.db")
pwente = koneksyonDB.cursor()

# kreyasyon tab kont itilizate
tab = '''create table IF NOT EXISTS kont
(non text, prenon text, laj integer, adres text, nimewo text primary key, balans integer)'''
pwente.execute(tab)


def otantifye(nimewo):

    reket = "select nimewo from kont where nimewo = (?)"
    res = pwente.execute(reket, (nimewo,))
    if res.fetchone() and (len(nimewo) < 8):
        return True
    else:
        return False
