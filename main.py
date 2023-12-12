import os

from kont import enskripsyon
from depo import depokont
from retre import retrekont
from balans import balanskliyan
from screenCleaner import clear


p = print

# main loop
def __main__():
    while True:
        p('\t1-ENSKRIPSYON')
        p('\t2-DEPO')
        p('\t3-RETRE')
        p('\t4-BALANS')
        p('\t5-KITE\n')

        chwa = input('Peze yon chif nan meni avan pou ou fe yon operasyon : \n')
        # function allow to clear the screen
        clear()

        match chwa:
            case '1':
                enskripsyon()
            case '2':
                depokont()
            case '3':
                retrekont()
            case '4':
                balanskliyan()
            case '5':
                p('Bye...')
                exit()
            case default:
                p('Chwa ou fe a pa valide\n')
        # wait for pressed key
        os.system("pause")

__main__()
