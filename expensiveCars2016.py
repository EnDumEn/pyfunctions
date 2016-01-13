"""
Picks out the most expensive car, printing the name and price.

Example input from Skatteverket.se

16PE001	108 3D ACCESS PureTech 68	89900
16PE002	108 5D ACTIVE PureTech 68	99900
16PE003	108 5D TOP! PureTech 68	124900
16BM001	116d 5d LCI	245500
16BM002	116d 5d LCI Advantage Editon	219900
16BM003	116d EfficientDynamics 5d LCI	247000
16BM004	116d EfficientDynamics 5d LCI Advantage Edition	219900
16BM005	118d 5d LCI	255000
16BM006	118d 5d LCI Advantage Editon	250900
16BM007	118d xDrive 5d LCI	275000
16BM008	118d xDrive 5d LCI Advantage Editon	269900
16BM009	118i 5d	231000
16BM010	118i 5d LCI Advantage Edition	209900
16BM011	120d 5d LCI	283000
16BM012	120d 5d LCI Advantage Editon	277900
16BM013	120d xDrive 5d LCI	322000
16BM014	120d xDrive 5d LCI Advantage Editon	314900
16BM015	120i 5d LCI	270000
16BM016	125d 5d LCI	346000
16BM017	125i 5d LCI	286000
16PE004	2008 ACCESS PureTech 82	129900

Answer from full list:
16MB279	Mercedes-AMG G 65 Station Wagon Lång	2575000
"""

import re
name = []
number = []
with open("Input.txt", "r") as infile:
    for line in infile:
        lst = re.split(r"\t+", line)
        name.append(lst[1])
        number.append(lst[2])

number = map(str.strip, number)
number = map(int, number)
print name[number.index(max(number))] + " " + str(max(number))
