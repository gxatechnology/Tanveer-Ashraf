txt = open('assets/js/app.js', encoding='utf-8').read()
idx = txt.find('exportProgress')
if idx != -1:
    print(txt[idx-100:idx+800])
else:
    print("exportProgress not in app.js")
    idx2 = txt.find('backup')
    print("backup search:", idx2)
