import csv

csv_file = open('./data.csv', 'r')
paper_list = csv.reader(csv_file, delimiter=',')

def gen_title_html(title, talk_id, is_long, postpone):
	html = '<div class="title"><span>[' + str(talk_id) + ']</span>&nbsp;<span>'
	html += title if not postpone else '(TBA)'
	html += '</span>&nbsp;<span>['
	html += 'Long' if is_long else 'Short'
	html += ']</span></div>'
	return html

def gen_authors_html(authors):
	return '<div class="authors">' + authors + '</div>'

def gen_abstract_html(abstract, postpone):
	html = '<div class="abstract abstract-item"><b>要旨：</b>'
	html += abstract if (len(abstract) != 0) and (not postpone) else '(TBA)'
	html += '</div>'
	return html

def gen_review_comment_html(review_comment, postpone):
	html = '<div class="review-comment review-comment-item"><b>採録時コメント：</b>'
	html += review_comment if (len(review_comment) != 0) and (not postpone) else '(TBA)'
	html += '</div>'
	return html

def gen_image_html(file_name, postpone):
	html = '<div class="image-item"><img class="thumb" src="'
	url = 'https://www.wiss.org/WISS2018/wp-content/uploads/' + (file_name if (len(file_name) != 0) and (not postpone) else 'talk-placeholder.png')
	html += url
	html += '" /></div>'
	return html

def gen_container_html(file_name, abstract, review_comment, postpone):
	html = '<div class="paper-container">'
	html += gen_image_html(file_name, postpone)
	html += gen_abstract_html(abstract, postpone)
	html += gen_review_comment_html(review_comment, postpone)
	html += '</div>'
	return html

html = ''

for row in paper_list:
	item_html = '<div class="talk">'
	item_html += gen_title_html(row[3], row[0], len(row[7]) != 0, len(row[8]) != 0)
	item_html += gen_authors_html(row[4])
	item_html += gen_container_html(row[9], row[5], row[6], len(row[8]) != 0)
	item_html += '</div>'
	html += item_html + '\n<hr />\n'

csv_file.close()

print(html)
