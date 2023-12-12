import sqlite3 as sqlite
import os
from verifyeKont import otantifye
from verifyeMontant import teskob

p = print


def depokont():
    nimewo = input("antre nimewo telefon wap fe depo a : \n")
    os.system("cls")

    koneksyonDB = sqlite.connect("kont.db")
    pwente = koneksyonDB.cursor()

    # kreyasyon tab kont itilizate
    tab = '''create table IF NOT EXISTS kont
    (non text, prenon text, laj integer, adres text, nimewo text primary key, balans integer)'''
    pwente.execute(tab)

    if otantifye(nimewo):
        kobDepo = input("Mete kantike kob wap depoze a : \n")
        reket = "select * from kont where nimewo = (?)"
        res = pwente.execute(reket, (nimewo,))

        os.system("cls")
        for kliyan in res:
            p(f"{kliyan[0]} {kliyan[1]}")
            balans = kliyan[-1]

        if teskob(kobDepo):
            balans += int(kobDepo)

            rek2 = "UPDATE kont SET balans = (?) where nimewo = (?)"

            pwente.execute(rek2, (balans, nimewo))
            koneksyonDB.commit()
            koneksyonDB.close()
            p(f'ou fe depo {kobDepo} goud sou kont ou ak sikse')
        elif int(kobDepo) < 20:
            print('pi piti kob ou ka fe depo se 20goud')
        else:
            print('Kanttite kob ou antre a pa korèk')
    else:
        os.system("cls")
        p(f"Kont sa poko anrejistre nan sistem nan")
