# levenshtein
Python script that imports the python Levenshtein library, reads a csv file, appends string distance and similarity ratio to rows, and writes to an output csv.

# Execution
- Import the python Levenshtein library (https://pypi.org/project/python-Levenshtein/)
- Extract main.py into an empty directory
- Save csv file with string data in same directory
- Update main.py "readFile" line to be consistent with the csv's file name
- Navigate to directory via command line and execute "python main.py"

# CSV Read File Structure
- The current script requies the csv file to have a specific structure:
  - Column 1 = unique identifier (if none exists, just label 1 - XXX)
  - Column 2 = first string for comparison
  - Column 3 = second string for comparison
