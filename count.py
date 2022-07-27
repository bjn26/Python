from tkinter import filedialog
name = filedialog.askopenfilename()
print(name)
text = open(name)

counts = dict()
for line in text:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
