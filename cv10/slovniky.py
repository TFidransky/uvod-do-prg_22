from collections import defaultdict
# Slovník jako překladový slovník
den2cislo = {
	"pondělí": 0,
	"úterý": 1,
	"sobota": 5,
	"neděle" : 6
}

print(den2cislo)
print(den2cislo["úterý"])
den2cislo["středa"] = 2
del den2cislo["neděle"]
print(den2cislo)

# ve výchozím stavu iteruji přes klíče
for klic in den2cislo:
	print(f"{klic} = {den2cislo[klic]}")

# pomocí .values() iteruji přes hodnoty
for hodnota in den2cislo.values():
	print(hodnota)

# pomocí .items() iteruji přes dvojice klíč,hodnota
for (klic,hodnota) in den2cislo.items():
	print(f"{klic} = {hodnota}")

# je klíč ve slovníku
if "neděle" in den2cislo:
	print("Neděle tam je")
else:
	print("Neděle tam není")

# Příklad 1:
# Proveďte frekvenční analýzu zadaného textu. Tedy vypište, který znak se v
# zadaném textu kolikrát vyskytoval.
# Vstup: "ahoj hugo"
# Výstup: a: 1, h: 2, o: 2, j: 1, u:1, g:1,  :1 
letters = {}
text = input("Zadej text:")
for ch in text:
	if ch in letters:
		letters[ch] += 1
	else:
		letters[ch] = 1
str_letters = str(letters)
str_letters = str_letters.replace("'","")
print(str_letters)

default_letters = defaultdict(int)
#text = input("Zadej text:")
for ch in text:
	default_letters[ch] += 1
for (key,val) in default_letters.items():
	print(f"{key}: {val}, ",end="")
print()

letters2 = {}
for ch in text:
	letters2[ch] = letters2.get(ch,0) + 1
print(letters2)
	

# Slovník jako datová struktura
parkoviste = {
	"jmeno": "P+R Zličín",
	"kapacita": {
		"obycejne": 340,
		"ztp": 6,
		"elektromobily": 10
	},
	"pr": True,
	"zaplnenost": 320,
	"seznam": [1,2,3]
}