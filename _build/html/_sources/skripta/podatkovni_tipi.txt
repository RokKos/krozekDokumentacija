Podatkovni tipi
===============

V tem poglavju bomo predstavili podatkovne tipe, kaj so in zakaj so pomembni,
kako jih uporabljamo in kateri obstajajo. Nekatere si bomo tudi podrobneje
ogledali.

Uvod
----

Program za svoje delovanje potrebuje podatke, števila, besede, slike, tabele,
... Take in drugačne tipe podatkov računalnik hrani v pomnilniku, v programu pa
imamo podatke na voljo kot spremenljivke. Python ima veliko podatkovnih tipov,
na kratko smo si že pogledali števila in nize znakov. Različni tipi podpirajo
različne operacije in so primerni za različne priložnosti, zato jih je potrebno
poznati, da jih znamo pravilno izbirati.

Števila
-------

Python podpira (na grobo) dve vrsti števil -- cela števila in decimalna
števila. Za cela števila ni omejitve na dolžino, decimalna števila pa imajo
standardne omejitve, a so za naše računanje dovolj dobra. Veljavne vrednosti
decimalnih števila sta tudi obe neskončnosti in ``nan``, ki pomeni "Not a
number". Cela števila dobimo iz drugih tipov s funkcijo ``int``, decimalna pa s
funkcijo ``float``.

Primer::

  a = 238743234
  b = 123.5324
  c = a + b    # rezultat je decimalno število
  k = -13
  r = -123.3223e12
  z = 0xdead   # z je sedaj 57005
  inf = float('inf')

S števili lahko računamo (duh), tip rezultata je odvisen od tipov operandov. Če
je eden izmed njiju decimalno število, potem je rezultat decimalen, Rezultat
operacije dveh celih števil je celo število. Izjema je deljenje, ki vedno vrne
decimalno število. Če želimo dobiti celoštevilsko deljenje, ki zaokrožuje proti
0, uporabimo operator ``//``.

Logične vrednosti
-----------------

.. todo::

  Dodaj section logične vrednosti

Seznami
-------

Največji problem enostavnih spremenljivk je v tem, da lahko vsebujejo le en
podatek. Tako moramo npr.  če hočemo od uporabnika dobiti 10 stvari, za to
narediti tudi 10 spremenljivk. Kaj pa, če hočemo stvari dobiti 1000? Ali pa
100.000?

Tu v poštev pridejo seznami. Sezname prav tako kot spremenljivko spravimo pod
neko ime, označujejo pa jih oglati oklepaji ``[`` in ``]``. Med oglatimi
oklepaji lahko navedemo poljubno število spremenljivk, ki bodo vse vsebovane v
seznamu::

  seznam = [1, 5, "abc", 66.12]

Kot vidimo, lahko seznam vsebuje mešane tipe spremenljivk - vsebuje lahko nekaj
celih števil, nekaj decimalnih števil in nekaj nizov znakov. Sezname iz drugih
tipov dobimo s funkcijo ``list``.

Dostopanje elementov seznama
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dostopanje do elementov seznama je malce drugačno kot pri navadnih
spremenljivkah. Če namreč vpišemo samo ime seznama, bomo seveda dobili vse
elemente -- v seznamu. Če pa hočemo dostopati do elementov, moramo za imenom
seznama v oglatih oklepajih napisati njegovo mesto. Pozor, računalnik ponovno
šteje od 0 naprej (torej je prvo mesto označeno z nič, drugo z 1, ...). Če
poskusimo dostopati "prepozen" element (npr. št. 12 v seznamu s štirimi
elementi) dobimo napako. V številko elementa pa lahko vpišemo tudi negativno
število, kjer -1 pomeni zadnji element, -2 predzadnji itd.::

  >>> seznam [1, 5, 'abc', 66.12]
  >>> seznam[0]
  1
  >>> seznam[3]
  66.12
  >>> seznam[12]
  Traceback (most recent call last): File "<pyshell#6>", line 1, in <module> seznam[12]
      IndexError: list index out of range >>> seznam[-1] 66.12

Dodajanje in odvzemanje elementov seznama
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V seznam seveda lahko dodajamo in iz njega odvzemamo elemente. Za te (in ostale
operacije na seznamih) uporabljamo metode. Do metod dostopamo tako, da po imenu
seznama napišemo ``.``, za njo pa ime metode (seznam.metoda()). Najbolj
uporabljane metode so naslednje:

.. py:class:: list

  .. py:method:: append(vrednost)

    V seznam na koncu doda element z vrednostjo ``vrednost``.

  .. py:method:: insert(index, vrednost)

    V seznam pred ``index``-to mesto doda element z vrednostjo ``vrednost``.

  .. py:method:: pop(index)

    Iz seznama pobriše ``index``-ti element in vrne njegovo vrednost.

  .. py:method:: remove(vrednost)

    Iz seznama pobriše prvi element z vrednostjo ``vrednost``.

Še primeri uporabe metod::

  >>> seznam = [1, 5, 'abc', 66.12]
  >>> seznam.append(16)
  >>> seznam
  [1, 5, 'abc', 66.12, 16]
  >>> seznam.insert(2, "Hello World!")
  >>> seznam
  [1, 5, 'Hello World!', 'abc', 66.12, 16]
  >>> seznam.pop(0)
  1
  >>> seznam
  [5, 'Hello World!', 'abc', 66.12, 16]
  >>> seznam.pop(-2)
  66.12
  >>> seznam
  [5, 'Hello World!', 'abc', 16]
  >>> seznam.remove(5)
  >>> seznam
  ['Hello World!', 'abc', 16]

Nizi znakov
----------------------

Niz zankov (string) v pythonu naredimo tako da, damo besedilo v enojne ali
dvojne narekovaje. Mogoči so tudi trojni narekovaji, ki segajo čez več vrstic.
Niz pa lahko uzstvarimo tudi iz kateregakoli drugega tipa s klicanjem funkcije
``str``. Primer::

  ime = "Janez"
  priimek = 'Novak'
  kratek_zivljenjepis = """
    Rodil: 1934
    Živel na Primorkem.
    Umrl: 2001
  """
  stevilka_ampak_ne_cisto = str(12)
  stevilka_ampak_spet_ne_cisto = '134'


Niz znakov ``"abcd"`` sli lahko nekako predstavljamo kot seznam ``['a', 'b',
'c', 'd']``. Primerjava v Pythonu ni čisto popolna, saj elementov niza znakov
ne moremo spreminjati, pri branju elementov pa se obnaša popolnoma enako. Tako
npr. ``niz[2]`` pomeni tretji element niza znakov (torej tretja črka oz. znak).

Torej -- nize znakov beremo na isti način kot sezname, spreminjati njihovih
elementov pa ne moremo::

  >>> niz = "Dober dan!"
  >>> niz[2] 'b'
  >>> niz[-1] '!'
  >>> niz[12]
  Traceback (most recent call last):
      File "<pyshell#3>", line 1, in <module> niz[12]
          IndexError: string index out of range
  >>> niz[1] = 'c'
  Traceback (most recent call last):
      File "<pyshell#4>", line 1, in <module> niz[1] = 'c'
          TypeError: 'str' object does not support item assignment

Brisanje in dodajanje v niz znakov
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Za razliko od seznamov nizi znakov nimajo metod ``.append``, ``.pop`` in
podobno. Znamo pa nize znakov "seštevati" (znak + dva niza zlepi skupaj). Torej
lahko dodajanje znakov na konec dobimo s prištevanjem na konec, dodajanje
znakov na začetek pa s prištevanjem na začetek. Seveda s tem originalnega niza
v resnici ne spremenimo na mestu, saj moramo vrednost spet dodeliti neki (lahko
isti) spremenljivki::

  >>> niz
  'Dober dan!'
  >>> niz = niz + " Kako se imate?"
  >>> niz 'Dober dan! Kako se imate?'
  >>> niz = "Lep pozdrav in " + niz
  >>> niz
  'Lep pozdrav in Dober dan! Kako se imate?'

Spreminjanje elementov niza znakov
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ker elementov ne moremo spremeniti direktno z ukazom ``niz[x] = 'a'`` ali
podobno, jih spreminjamo tako, da naredimo nov prazen niz, nato pa potujemo po
starem nizu in prepisujemo črko po črko v nov niz. Vsakič ko srečamo znak, ki
ga nočemo, ga preprosto ne prepišemo. Če pa srečamo znak, ki bi ga radi
zamenjali, ga preprosto zamenjamo. Spodaj primer programa, ki v našem nizu vse
samoglasnike nadomesti z zvezdico.

::

  niz = "Lep pozdrav in Dober dan! Kako se imate?"
  nov_niz = ""
  samoglasniki = "aeiou"
  for i in niz:
      if i in samoglasniki:
          nov_niz = nov_niz + "*"
      else:
          nov_niz = nov_niz + i
  print(nov_niz)
  >>>
  L*p p*zdr*v *n D*b*r d*n! K*k* s* *m*t*?

Zadnji dve vrstici sta kopija tega, kar se pojavi, ko program izvedemo.

Slovarji
--------

.. todo::

  Dodaj section Slovarji

Množice, nabori
---------------

.. todo::

  Dodaj section Množice, nabori

.. vim: spell spelllang=sl
