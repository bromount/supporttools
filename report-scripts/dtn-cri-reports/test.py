import csv
ifile  = open('team.csv', "rb")
reader = csv.reader(ifile)


for row in reader:
        
        username = row[0]
	print username
