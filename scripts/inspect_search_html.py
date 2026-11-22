txt = open('search.html', encoding='utf-8').read()
idx = txt.find('<script')
print(txt[idx:])
