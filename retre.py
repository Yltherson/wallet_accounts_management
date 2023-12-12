import sqlite3 as sqlite
import os
from verifyeKont import otantifye
from verifyeMontant import teskob

p = print


def retrekont():
    nimewo = input("antre nimewo telefon wap fe retre a : \n")
    os.system("cls")

    koneksyonDB = sqlite.connect("kont.db")
    pwente = koneksyonDB.cursor()

    if otantifye(nimewo):

        reket = "select * from kont where nimewo = (?)"
        res = pwente.execute(reket, (nimewo,))

        kobRetre = input("Mete kantike kob wap retire a : \n")

        for kliyan in res:
            p(f"{kliyan[0]} {kliyan[1]}")
            balans = kliyan[-1]

        if teskob(kobRetre) and (balans >= int(kobRetre)):
            balans -= int(kobRetre)

            rek2 = "UPDATE kont SET balans = (?) where nimewo = (?)"

            pwente.execute(rek2, (balans, nimewo))
            koneksyonDB.commit()
            koneksyonDB.close()
            p(f'ou fe retre {kobRetre} goud sou kont ou ak sikse')
        elif balans < int(kobRetre):
            p('Balans ou pa sifi pou ou fe retre sa\n')
        else:
            os.system("cls")
            p(f"montan retre a enkorek")
    else:
        os.system("cls")
        p(f"Kont sa poko anrejistre nan sistem nan")
