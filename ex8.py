# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"
#formatter = "%s %s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing",
        "That your could type up right.",
        "But it did not sing.",
        "So I said goodnight."
#        "Bä Bä räksmörgås"

)
