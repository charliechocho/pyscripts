# -*- coding: utf-8 -*-
answ_li = []
answ = ''
print 'Enter your name or exit to stop: '
while answ != 'exit':
	answ = raw_input("What's ya name? ")
	if answ == 'exit':
		break
	else:
		answ_li.append(answ)

#sort(answ_li)
name_db = open('names.db', 'a+')

for line in sorted(answ_li):
	name_db.write('%s\n' % line)

name_db.close()

