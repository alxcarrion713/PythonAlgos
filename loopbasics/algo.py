# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given “ there’s no free lunch - gotta pay yer way. “, return “TNFL-GPYW”. Given “Live from New York, it’s Saturday Night!”, return “LFNYISN”
# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

text= "National Basketball Association"
print(text)

acronym=""
for c in text:
    if c.isupper():
        acronym+= c

print(acronym)

