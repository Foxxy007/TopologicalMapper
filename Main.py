import csv

jsonPATH = "config.json"
csvPATH = "out.csv"
 
# initializing the titles and rows list
titles = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
 
    # extracting field names through first row
    titles = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))
 
# printing the field names
print('Field names are:' + ', '.join(field for field in titles))
# print(rows)
values = {}
for row in rows:
    values[row[0]]=row[1:-1]
print(values)
# printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     # parsing each column of a row
#     for col in row:
#         print("%10s" % col, end=" "),
#     print('\n')