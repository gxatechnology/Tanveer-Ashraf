with open('scripts/data_jurisprudence_mcqs_3.py', 'r', encoding='utf-8') as f:
    text = f.read()

fixed_text = text.replace('"id": "mcq-jur-06-010"', '"id": "mcq-jur-11-010"')
with open('scripts/data_jurisprudence_mcqs_3.py', 'w', encoding='utf-8') as f:
    f.write(fixed_text)
print('Fixed mcq-jur-11-010 in scripts/data_jurisprudence_mcqs_3.py')
