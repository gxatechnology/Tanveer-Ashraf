txt = open('syllabus.html', encoding='utf-8').read()
idx = txt.find('id="content"')
if idx != -1:
    print(txt[idx:idx+1000])
else:
    print("content id not found, looking for <main")
    m_idx = txt.find('<main')
    print(txt[m_idx:m_idx+1000])
