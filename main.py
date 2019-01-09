import csv          # library required for csv read write
import Levenshtein  # pip install python-Levenshtein
                    #https://pypi.org/project/python-Levenshtein/#documentation 

readFile = open("FILE_NAME.csv", "r")
writeFile = open("output.csv", "w")

with readFile:
    reader = csv.reader(readFile)
    writer = csv.writer(writeFile)
    for row in reader:
        row.append(Levenshtein.distance(row[1],row[2])) # num of edits to match strings
        row.append(Levenshtein.ratio(row[1],row[2])) # Similarity between two strings
        writer.writerow(row) # write appended row to ouput.csv

readFile.close()
writeFile.close()
