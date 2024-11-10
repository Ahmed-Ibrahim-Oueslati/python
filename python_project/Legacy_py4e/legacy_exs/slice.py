text = "X-DSPAM-Confidence:    0.8475"
p = text.find(' ')
p1 = float(text[p:])
print(p1)