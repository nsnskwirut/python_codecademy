#!/opt/ute/python/bin/python


import re


def count_words(string):
	words = re.findall('\w+', string)
	count_repetitions = {}
	for word in words:
		if word.lower() not in count_repetitions:
			count_repetitions.update({word.lower(): 1})
		else:
			count_repetitions[word.lower()] += 1
	return count_repetitions


wierszyk = "Drodzy Rodacy, \
Mieszkancy Warszawy i Goscie \
oraz Ci, ktorzy przebywaja poza Ojczyzna w poszukiwaniu chleba, \
Czcigodny Ojcze Dyrektorze ze wszystkimi, \
ktorzy tworza Telewizje TRWAM, \
Przedstawiciele wladz panstwowych i samorzadowych, \
Czlonkowie Parlamentu,\
Przedstawiciele swiata kultury, nauki i sztuki oraz oswiaty i sluzby zdrowia,\
Czlonkowie Solidarnosci i innych zwiazkow zawodowych,\
Drodzy Rolnicy,\
Kochani Dziennikarze,\
Szanowni przedstawiciele sluzb mundurowych:\
wojska, policji, strazy granicznej, strazy pozarnych, urzedow celnych,\
Drodzy Bracia w kaplanstwie i zyciu konsekrowanym,\
Siostry zakonne,\
Kochana mlodziezy uczaca sie, pracujaca i poszukujaca pracy!"
print count_words(wierszyk)
