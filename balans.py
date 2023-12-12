import sqlite3 as sqlite
import os
from verifyeKont import otantifye

p = print


def balanskliyan():
    nimewo = input("antre nimewo telefon ou : \n")
    os.system("cls")

    if otantifye(nimewo):
        koneksyonDB = sqlite.connect("kont.db")
        pwente = koneksyonDB.cursor()

        reket = "select non, prenon, balans from kont where nimewo = (?)"
        res = pwente.execute(reket, (nimewo,))

        for kliyan in res:
            p(f"{kliyan[0]} {kliyan[1]} Balans kont ou se : {kliyan[-1]}goud")

        koneksyonDB.close()

    elif (len(nimewo) != 8) or (not nimewo.isnumeric()):
        p("Nimewo ou antre a pa bon, nimewo a sipoze gen 8 chif san karaktè")
    else:
        p("nimewo kont sa poko anrejistre")
