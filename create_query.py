import csv
with open('df_trat_3.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print('('+', '.join(row)+'),')

