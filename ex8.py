formatter = "%r %r %r %r"
#Define formatter first (four in a row), and then can simply use it in statements afterwards
print formatter % (1, 2, 3, 4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#If there is single quote mark used in a sentence, the sentence will be shown in double quotes
