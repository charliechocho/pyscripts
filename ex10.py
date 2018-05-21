# -*- coding: utf-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t\t* Cat Food
\t* Fishises
\t* Catnip\n\t* Grass
'''

print tabby_cat.expandtabs(16)
print persian_cat
print backslash_cat
print fat_cat.expandtabs(20)
