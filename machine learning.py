from asyncore import read
import time
from pyexpat import model
from re import X
print("sto elaborando i dati a disposizione")
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier
giocatori = read_csv(r"C:\Users\alessandrini\Documents\coding\learning machine\giocatori.csv") #definire dove è il programma
X = giocatori.drop(columns=['videogame'])   #dire che le alre informazioni si trovano nelle altre colonne eccetto quella videogame
y = giocatori['videogame']  #indicare im quale colonna exel si trovano giocatori

modello = DecisionTreeClassifier()
modello.fit(X.values, y.values) #analliza i dati
genere = input("inserire genere persona: ")
if genere == "maschio": #se l'imput è mascio
    genere = 1  #inserisce variabile x su 1 (maschio)
else:
    genere = 0  #se è donna inserisce variabile x su 0  (donna)
anni = input("inserire anni persona: ") #chiede gli anni
previsione = modello.predict([[genere,anni]])   #impostare variabile sulla previsione
print(previsione)   #dice la previsione
time.sleep(10)