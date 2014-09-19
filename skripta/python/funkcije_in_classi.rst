Funckije in objekti
===================
To sta zelo pomembna in zelo uporabljena koncepta.

Funkcije
--------

Velikrat se nam zgodi, da imamo v programu zelo podobno kodo, ki dela zelo
podobno reč, napisano večkrat. Recimo, da želimo izračunati produkt elementov v
seznamu, v našem programu pa imamo 3 sezname, ali pa še huje, imamo zelo veliko
seznamov, ki nam jih je podal uporabnik. Lahko pa koda postane tudi zelo
zapletena, saj znotraj ene zanke preverjamo, kaj drugega z drugo zanko in tako
naprej...

Primera takih programov:

.. code-block:: python

  a = [1, 2, 3, 4, 5]
  b = [14, 15, 0, 2]
  c = [-1, -1, -1, -1]
  pa = 1
  for i in a:
      pa *= i
  for i in b:
      pb *= i
  for i in c:
      pb *= i
  print(pa)
  print(pb)
  print(pc)

.. code-block:: python

  """Program preveri ali je število, ki ga vnese uporabnik popolno."""
  while True:
      a = int(input())
      if a == 0:
          break
      vsota_deliteljev = 0
      for i in range(1, a):
          if a % i == 0:
              vsota_deliteljev += i
      if vsota_deliteljev == a:
          print("Stevilo", a, "je popolno.")
      else:
          print("Stevilo", a, "ni popolno.")

V prvem primeru je problem zelo ponavaljajoča koda
todo

Funkcijo si lahko predstavljamo kot neko črno škatlo, ki ji nekaj damo, funkcija
pa potem s tem nekaj naredi in/ali nam nekaj vrne. Velika prednost funkcij je
to, da ni potrebno vedeti, kako točno deluje (lahko nam kakšno funkcijo npr.
napiše kdo drug, jo skopiramo iz interneta itd.) in preprosto popravljanje. Če
namreč v funkciji pride do kakšne napake, lahko napako popravimo le v
definiciji, namesto da bi jo morali popraviti povsod, kjer funkcijo uporabimo
Sintaksa
def imeFunkcije(parameter1, parameter2): Koda, ki se izvede ko pokličemo
funkcijo

Funkcijo vedno začnemo z besedo "def", nato pride ime funkcije (kot ime
spremenljivke mora biti nujno iz ene besede) in v oklepaju poljubno število
parametrov.
Vračanje funkcij
def sestej(x,y): return(x+y)

Če hočemo, da funkcija kaj vrne, to povemo z ukazom "return". Ko funkcija nekaj
vrne, lahko to ujamemo in s tem nekaj naredimo (npr. shranimo v spremenljivko,
izpišemo itd.) ali pa ne naredimo ničesar - s tem bo stvar, ki jo je funkcija
vrnila, izgubljena. V primeru vidimo funkcijo, ki za parameter dobi dve števili
(poimenovani x in y) ter vrne njun seštevek.
OPOZORILO: Ko se v funkciji izvede "return" ukaz, se funkcija konča, tudi če je
pod njo še kaj kode.
Klicanje funkcij

Ko izvedemo program, ki vsebuje definicije funkcij, se ne zgodi nič. Funkcijo je
treba namreč še poklicati. Naše funkcije kličemo popolnoma enako kot že vdelane
funkcije (npr. print(), range() itd.).
sestej(12,15)
Primer

Kot primer funkcije si poglejmo funkcijo prastevilo(x), ki nam za dano število x
vrne True (je praštevilo) ali False (ni praštevilo).
""" Funkcija vrne True, če je x praštevilo, in False, če x ni praštevilo """ def
prastevilo(x): #Če je x <= 1, potem ni praštevilo - vrnemo False in s tem
končamo if(x <= 1): return(False) #Preverimo, če je katerokoli število med 2 in
x delitelj števila x #Če ga najdemo, povemo da x ni praštevilo - vrnemo False
for i in range(2, x): #x%i == 0 pomeni "ali i deli x" oz "ali je i delitelj x"
if(x%i == 0): return(False) #Če smo prišli do sem, potem x nima nobenega
delitelja med 2 in x #in iz tega sledi da je x praštevilo return(True)

Preverimo, če funkcija deluje (v Python Shell bomo napisali zanko, ki bo za
števila od 0 do 25 izpisala število, zraven pa True oz. False).
>>> for i in range(26): print(i, prastevilo(i)) 0 False 1 False 2 True 3 True 4
False 5 True 6 False 7 True 8 False 9 False 10 False 11 True 12 False 13 True 14
False 15 False 16 False 17 True 18 False 19 True 20 False 21 False 22 False 23
True 24 False 25 False


Objekti
-------

.. todo::
  Dodaj objekte.

.. vim: spell spelllang=sl
