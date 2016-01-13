"""
Changes a character at specific position on every line in Input.txt, saves the new version at Output.txt
"""

with open("Input.txt", "r") as infile, open("Output.txt", "w") as outfile:
    next(infile)
    for line in infile:
        line = line[:52] + "1" + line[53:]
        outfile.write(line)
