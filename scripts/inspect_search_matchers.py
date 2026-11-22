txt = open('assets/js/legal-search.js', encoding='utf-8').read()
idx = txt.find('matchVocab')
print(txt[idx-100:idx+600])
