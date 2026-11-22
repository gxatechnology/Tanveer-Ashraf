import glob

pages = sorted(glob.glob('*.html'))
for p in pages:
    txt = open(p, encoding='utf-8').read()
    has_nav = 'class="nav"' in txt or "class='nav'" in txt
    has_acad = 'learning-academy.html' in txt
    print(f"{p:25} | has_nav: {str(has_nav):5} | has_acad: {str(has_acad):5}")
