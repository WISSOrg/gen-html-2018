# coding: utf-8

# (PaperID (public), SubmissionID (internal))
pairs = [
    (u"01", u"14"),
    (u"02", u"11"),
    (u"03", u"20"),
    (u"04", u"32"),
    (u"05", u"22"),
    (u"06", u"9"),
    (u"07", u"25"),
    (u"08", u"21"),
    (u"09", u"28"),
    (u"10", u"24"),
    (u"11", u"4"),
    (u"12", u"6"),
    (u"13", u"29"),
    (u"14", u"17"),
    (u"15", u"3"),
    (u"16", u"7")
]

for public_id, file_id in pairs:
    input_file_name = "raw/" + file_id + ".txt"
    output_file_name = public_id + ".html"
    html = u""
    html += u'<!DOCTYPE html><html lang="ja"><head><meta charset="utf-8" /><title>査読コメント (ID: ' + public_id + u')</title><link rel="stylesheet" href="../style.css" /></head><body class="review"><header><a href="../">論文一覧に戻る</a></header>'
    text = open(input_file_name).read().decode('utf-8')
    text = text.replace(u'-----------------------------\r\nreview comment 1\r\n-----------------------------', u'<h2>査読者 1</h2>')
    text = text.replace(u'■ 採否理由', u'<h3>採否理由</h3><pre>')
    text = text.replace(u'■ この研究をよくするためのコメント', u'</pre><h3>この研究をよくするためのコメント</h3><pre>')
    text = text.replace(u'■ 採録判定時のコメント', u'</pre><h3>採録判定時のコメント</h3><pre>')
    text = text.replace(u'■ レビューサマリ', u'</pre><h3>レビューサマリ</h3><pre>')
    text = text.replace(u'■ その他コメント', u'</pre><h3>その他コメント</h3><pre>')
    text = text.replace(u'-----------------------------\r\nreview comment 2\r\n-----------------------------', u'</pre><h2>査読者 2</h2>')
    text = text.replace(u'-----------------------------\r\nreview comment 3\r\n-----------------------------', u'</pre><h2>査読者 3</h2>')
    text = text.replace(u'-----------------------------\r\nreview comment 4\r\n-----------------------------', u'</pre><h2>査読者 4</h2>')
    text = text.replace(u'-----------------------------\r\nreview comment 5\r\n-----------------------------', u'</pre><h2>査読者 5</h2>')
    text = text.replace(u'■ 総合点', u'<h3>総合点</h3>')
    text = text.replace(u'■ 確信度', u'<h3>確信度</h3>')
    html += text
    html += '</pre></body></html>'
    open(output_file_name, 'w').write(html.encode('utf8'))
