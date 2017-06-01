# Frequent Words Counter by MohamadKh75
# 2017-06-01
# ********************

import re
import codecs
from pathlib import Path


# Defining Variables
old_dic = {}
quantity = 10

# Defining Paths
source_path = Path("Hafez.txt").resolve()
results_path = Path("Results.txt").resolve()


# Open the file and read it!
document_text = codecs.open(source_path, 'r', 'utf-8')
text_string = document_text.read()

# Using Regular Expression to find the words with more than 3 characters
temp = re.findall(r'\b[^ ]{3,15}\b', text_string)

# Counting the words' repetition
for word in temp:
    count = old_dic.get(word, 0)
    old_dic[word] = count + 1

# Convert the string to a Dictionary
dict(old_dic)

# Delete the items with the quantity of less than X
new_dic = dict((k, v) for k, v in old_dic.items() if v >= quantity)


# And finally, write it to a txt file!
fw = codecs.open(results_path, 'w', 'utf-8')

for k, v in new_dic.items():
    fw.write(str(k) + " : " + str(v) + "\n\n")

fw.close()
