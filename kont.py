import sqlite3 as sqlite
import os
from verifyeKont import otantifye


def enskripsyon():
    print("--ENSKRIPSYON--\n\n")
    print('Mete enfomasyon kont ou an\n')

    non = input('Mete non w : ')
    prenon = input('Mete prenon w : ')
    laj = input('Mete laj ou : ')
    if (non.isalpha() and prenon.isalpha()) and (len(non) >= 3 and len(prenon) >= 3) and (
            laj.isdigit() and int(laj) >= 18):
        adres = input('Mete adres ou : ')
        nimewo = input('Mete nimewo kont ou pa ekzanp: 31000011\n')
        if not otantifye(nimewo):
            balans = 0

            itilizate = (non, prenon, laj, adres, nimewo, balans)

            # koneksyon avek BD sqlite3
            koneksyonDB = sqlite.connect("kont.db")
            pwente = koneksyonDB.cursor()

            # kreyasyon tab kont itilizate
            tab = '''create table IF NOT EXISTS kont
                (non text, prenon text, laj integer, adres text, nimewo text primary key, balans integer)'''
            pwente.execute(tab)

            reket = "insert into kont(non, prenon, laj, adres, nimewo, balans) values(?, ?, ?, ?, ?, ?)"
            pwente.execute(reket, itilizate)

            koneksyonDB.commit()
            koneksyonDB.close()

            os.system("cls")
            print("kont ou an kreye ak sikse !")
        else:
            os.system("cls")
            print(f"Kont sa anrejistre deja nan sistem nan oubyen nimewo a pa korek")
    elif not non.isalpha():
        print("Non ou mete a pa korek")
    elif not prenon.isalpha():
        print("prenon ou mete a pa korek")
    elif len(non) < 3:
        print("Non ou mete tro kout")
    elif len(prenon) < 3:
        print("prenon ou mete a tro kout")
    elif not laj.isdigit():
        print("Laj ou mete a pa korek")
    elif int(laj) < 18:
        print("fok ou maje pou ou kapab kreye yon kont")
    else:
        print("enfomasyon enkorek")
