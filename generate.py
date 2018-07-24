import csv

csv_file = open('./data.csv', 'r')
member_list = csv.reader(csv_file, delimiter=',')

html = ''

for row in member_list:
	item_html = '<div class="item"></div>'
	html += item_html + '\n'

csv_file.close()

print(html)
