import os
choice_li = ['%', '%', '%', '%', '%', '%', '%', '%', '%', '%']

def prn_brd():
    os.system('clear')
    print '*' * 9

    print '* %s|%s|%s *' % (choice_li[0], choice_li[1], choice_li[2])
    print '* %s|%s|%s *' % (choice_li[3], choice_li[4], choice_li[5])
    print '* %s|%s|%s *' % (choice_li[6], choice_li[7], choice_li[8])

    print '*' * 9

def go_home():
    exit()


def gamer_init(crkl, cross):
    crkl = raw_input('Gamer Circle, enter your name!: ')
    cros = raw_input('Gamer Cross, enter your name!: ')
    return crkl, cros




print 'Hello %s! Do you want to play a game' % (os.getenv('USER'))
answ = raw_input('(y/n)   :')

if answ == 'y':
    prn_brd()
    crkl, cros = gamer_init('a', 'b')
    print crkl
    print cros
else:
    go_home()
