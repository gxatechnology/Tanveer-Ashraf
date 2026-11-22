txt = open('assets/js/app.js', encoding='utf-8').read()
idx = txt.find('function syllabus(')
if idx != -1:
    print(txt[idx:idx+1500])
