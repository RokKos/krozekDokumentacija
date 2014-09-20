Funckije in objekti
===================

Funckije in objekti so zelo uporabljene strukture v programiranju. Zaradi
splošnosti in lepih načinov za dodajanje novih funkcionalnosti in zato, ker naredijo
kodo mnogo bolj berljivo in uporabno so eden najpomembnejših konceptov, ki se
je zelo razvit in zelo pomemben v resnem programiranju.

Funkcije
--------

Velikokrat se nam zgodi, da imamo v programu zelo podobno kodo, ki dela zelo
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
      pc *= i
  print(pa)
  print(pb)
  print(pc)

.. code-block:: python

  """Program preveri ali je število, ki ga vnese uporabnik popolno."""
  while True:
      a = int(input("Vpisi stevilo: "))
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

V prvem primeru je problem zelo ponavljajoča koda, v drugem pa je težko
berljiva in zelo gnezdena. V tem primeru pridejo na pomoč funkcije, ki so
primerne ravno za take probleme: določene pomensko neodvisne izseke kode ločijo
in jih naredijo primerne za večkratno uporabo.

Funkcijo si lahko predstavljamo kot neko črno škatlo, ki ji nekaj damo, funkcija
pa potem s tem nekaj naredi in/ali nam nekaj vrne. Velika prednost funkcij je
to, da ni potrebno vedeti, kako točno deluje (lahko nam kakšno funkcijo npr.
napiše kdo drug, jo skopiramo iz interneta itd.). Poleg tega funkcije naredijo
kodo lažje za vzdrževanje, saj omogočajo preprosto popravljanje in spreminjanje.
Če namreč v funkciji pride do kakšne napake, lahko napako popravimo le v
definiciji, namesto da bi jo morali popraviti povsod, kjer funkcijo uporabimo.

Sintaksa
~~~~~~~~
Funkcijo vedno začnemo z besedo ``def``, nato pride ime funkcije (kot ime
spremenljivke mora biti nujno iz ene besede) in v oklepaju poljubno število
parametrov. Telo funkcije je potrebno zamakniti.

.. code-block:: python

  def imeFunkcije(parameter1, parameter2):
      Koda, ki se izvede, ko pokličemo funkcijo


Vračanje rezultatov
~~~~~~~~~~~~~~~~~~~

Če hočemo, da funkcija kaj vrne, to povemo z ukazom ``return``. Ko funkcija nekaj
vrne, lahko to ujamemo in s tem nekaj naredimo (npr. shranimo v spremenljivko,
izpišemo itd.) ali pa ne naredimo ničesar -- s tem bo stvar, ki jo je funkcija
vrnila, izgubljena. Poglejmo si primer, ki preveri, ali je dano število popolno,
in vrne ``True`` če je, sicer pa ``False``.

.. code-block:: python

  def popolno(n):
      vsota_deliteljev = 0
      for i in range(1, n):
          if n % i == 0:
              vsota_deliteljev += i
      if vsota_deliteljev == n:
          return True
      else:
          return False

.. warning::

  Ko se v funkciji izvede ``return`` ukaz, se funkcija konča, tudi če je
  pod stavkom še kaj kode. Če ukaza ``return`` ni, potem funkcija na koncu vrne
  ``None``.

Klicanje funkcij
~~~~~~~~~~~~~~~~

Ko izvedemo program, ki vsebuje samo definicije funkcij, se ne zgodi nič. 
Funkcijo je treba namreč še poklicati. Naše funkcije kličemo popolnoma enako kot
že vdelane funkcije (npr. print(), range(), ...)

Oglejmo si primer programov iz uvoda, samo da tokrat uporabljata definirane
funkcije. Za vsakim programom je tudi njegov možen izpis.

.. code-block:: python

  def zmnozi(seznam):
      prod = 1
      for i in seznam:
          prod *= i
      return prod

  a = [1, 2, 3, 4, 5]
  b = [14, 15, 0, 2]
  c = [-1, -1, -1, -1]
  print(zmnozi(a))
  print(zmnozi(b))
  print(zmnozi(c))

::

  120
  0
  1

.. code-block:: python

  """Program preveri ali je število, ki ga vnese uporabnik popolno."""
  while True:
      a = int(input("Vpisi stevilo: "))
      if a == 0:
          break
      if popolno(a):
          print("Stevilo", a, "je popolno.")
      else:
          print("Stevilo", a, "ni popolno.")

::

  Vpisi stevilo: 13
  Stevilo 13 ni popolno.
  Vpisi stevilo: 6
  Stevilo 6 je popolno.
  Vpisi stevilo: 2
  Stevilo 2 ni popolno.
  Vpisi stevilo: 28
  Stevilo 28 je popolno.
  Vpisi stevilo: 0

Objekti
-------

.. todo::
  Dodaj objekte.

.. _konstruktorji:

Konstruktorji in destruktorji
-----------------------------

.. vim: spell spelllang=sl
