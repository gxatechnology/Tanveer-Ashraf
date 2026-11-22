with open('scripts/build_mcqs_ch06_to_ch08.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace known unescaped double quotes inside strings
text = text.replace('"the State"', '\\"the State\\"')
text = text.replace('"force"', '\\"force\\"')

with open('scripts/build_mcqs_ch06_to_ch08.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed quotes in build_mcqs_ch06_to_ch08.py.")
