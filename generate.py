import csv

csv_file = open("./data.csv", "r")
member_list = csv.reader(csv_file, delimiter=",")

for row in member_list:
    print(row)
