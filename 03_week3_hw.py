#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Add code to print a line of hyphens the same length as the Belgium string, followed by:

print('-' * len(Belgium))

# The string with the comma separators replaced by colons ':'. followed by:

print(Belgium.replace(',', ':'))

# The population of Belgium (the second field) plus the population of the capital city (the fourth field). The answer should be 11183818

split_string = Belgium.split(',')
# print(split_string)
combined_population = f"The combined population of Belgium and the capital city of Brussels is {int(split_string[1]) + int(split_string[3])}"
print(combined_population)
