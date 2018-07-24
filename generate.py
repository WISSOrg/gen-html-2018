import csv

csv_file = open('./data.csv', 'r')
member_list = csv.reader(csv_file, delimiter=',')

html = '<div class="member-container">\n'

for row in member_list:
	item_html = ''
	item_html += '<div class="item">'
	item_html += '<img src="http://www.wiss.org/WISS2018/wp-content/uploads/' + row[5] + '-300x300.jpg" class="portrait aligncenter size-medium" />'
	item_html += '<p class="member-name">' + row[0] + '<a target="_blank" href="' + row[3] + '">[icon name="external-link" unprefixed_class="member-name-icon"]</i></a><a href="https://twitter.com/' + row[4] + '" target="_blank">[icon name="twitter" unprefixed_class="member-name-icon"]</a></p>'
	item_html += '<p>'
	item_html += '<b>所属：</b>' + row[1]
	item_html += '<br />'
	item_html += '<b>専門：</b>' + row[2]
	item_html += '</p>'
	item_html += '</div>'
	html += item_html + '\n'

html += '</div>'

csv_file.close()

print(html)
