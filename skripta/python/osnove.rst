Osnove
======

V tem poglavju si bomo ogledali osnove programiranja, s katerimi lahko
vzpostavimo osnovno komunikacijo z računalnikom in naredimo zelo enostavne
programe.

Spremenljivke
-------------

Spremenljivke so prostori v spominu z določenim imenom, v katere lahko spravimo
neko vrednost. Tako lahko npr. pod ime ``leta`` spravimo vrednost ``5``. V
osnovi ločimo tri tipe spremenljivk - ``float`` (realna števila), ``int`` (cela
števila) in ``string`` (nize znakov). Začetek in konec ``stringa`` je označen z
dvojnim ali enojnim narekovajem (``"`` ali ``'``). Python tipe spremenljivk
določa samodejno.

Spremenljivke se definira na naslednji način::

  x = 2
  y = 5
  ime = "Andreja"
  leta = x + y

.. HINT::
  Znak = v programiranju nima istega pomena kot v matematiki. = pravzaprav
  pomeni "vrednost na desni zapiši v spremenljivko na levi". Torej bo ukaz x =
  x + 2 dejansko pomenil "x povečaj za 2".

Komentarji
----------

Komentarji so programerjeve opombe v kodi, namenjene bralcu -- sebi ali nekomu
drugemu, ki bo to bral za njim. Interpreter jih ignorira. V Pythonu so
komentarji enovrstični in že začnejo z znakom ``#``. Vsi znaki v vrstici od
znaka ``#`` so ignorirani. Komentarje se ponavadi napiše pred manj razumljiv del
kode, da obrazložimo njeno delovanje, ali pa če želimo kakšen del kode trenutno
umakniti iz programa, ne da bi ga izbrisali. Komentarji pogosto tudi obrazložijo
in dokumentirajo kodo in narekujejo njeno uporabo.

Primer::

  ime = "Janez"  # ime naj bo brez presledkov in naj se začne z veliko začetnico
  # v absx shranimo absolutno vrednost x
  x = -8
  if x < 0:
      absx = -x
  else:
      absx = x

Input in output
---------------

Input in output pomeni branje uporabnikovega vpisa in izpisovanje na zaslon.
Uporabili smo funkcije ``input``, ``int``, ``print``, ``format``.

.. py:function:: input(niz_znakov)

  Izpiše niz znakov in vrne to, kar je uporabnik vtipkal.

.. py:function:: int(niz_znakov)

  Niz znakov spremeni v dejansko celo število, s katerim znamo računati. Če je
  parameter že celo število, ne pride do sprememb.

.. py:function:: print(niz_znakov)

  Izpiše niz znakov niz_znakov.

.. py:class:: str

  .. py:method:: format(p1, p2, p3, ...)

    Na mesto označeno z {0} vstavi p1, na {1} vstavi p2, ...

Primer:

.. literalinclude:: /tutorialsPythonBasic/verybasic/input/input3.py
  :linenos:

If stavki
---------

``If stavek`` se uporablja vsakič, kadar hočemo, da se naš program obnaša
drugače pod drugačnimi pogoji. Če je pogojev več, lahko za ``if`` uporabimo še
``elif`` (else if), ki doda dodatne pogoje. Za konec pa lahko damo še ``else``,
ki se izvede takrat, ko ni bil izpolnjen noben od pogojov v ``if`` in ``elif``
stavkih. ``elif`` in ``else`` deli niso obvezni.

Sintaksa if stavkov je naslednja (pazljivi moramo biti na zamik po if stavku -
dobimo ga tako, da pritisnemo tabulator, ki se nahaja nad caps lock tipko na
tipkovnici)::

  if pogoj:
      Koda, ki se izvede, če je izpolnjen pogoj
  elif pogoj2:
      Koda, ki se izvede, če je izpolnjen pogoj2
  else:
      Koda, ki se izvede, če ni izpolnjen noben od zgornjih pogojev


Pogoji
~~~~~~

Pogoji so lahko enostavni ali sestavljeni. Enostavni pogoji so npr. primerjanje
enakosti (je enako ``==``, ni enako ``!=``), primerjanje vrednosti (večje
``>``, večje ali enako ``>=``, manjše ``>``, manjše ali enako ``<=``),
sestavljeni pa so narejeni iz kombinacije enostavnih z uporabo matematičnih
operacij ``NOT``, ``AND``, ``OR``, ``XOR`` itd.

Primer::

    x = int(input("Vpisite stevilo: "))
    if x > 0:
        if x > 100:
            print("x je vecji od 100")
        else:
            print("x je pozitiven")
    elif x == -5:
        print("x je -5")
    else:
        print("x je negativen")

Zanke
-----

Zanke se uporablja takrat, ko moramo neko stvar ponoviti večkrat. Če moramo
npr. izpisati vsa števila med 1 in 100 uporabimo zanko. Če hočemo isto stvar
ponoviti 3x, uporabimo zanko. Če bi radi, da se nekaj dogaja, dokler ni
izpolnjen nek pogoj (npr. vtipkavaj geslo, dokler ne vtipkaš pravilnega),
uporabimo zanko.

While zanka
~~~~~~~~~~~

::

  while pogoj:
      Koda, ki se izvaja dokler je pogoj izpolnjen

``while`` zanko uporabimo takrat, ko se mora nekaj izvajati dokler je pogoj
izpolnjen. Pri while zanki moramo biti zelo pozorni na neskončne zanke.
Neskončna zanka se zgodi takrat, ko je pogojvedno izpolnjen, program pa bo
tekel v neskončnost. Če se nam to slučajno zgodi, pritisnemo kombinacijo tipk
``ctrl+c``, s čimer program prekinemo.

::

  """Uporabnik vpisuje geslo. Če 5x zaporedoma vpiše napačno geslo je izključen
  iz sistema (za to poskrbi spremenljivka števec) """
  geslo = 123
  stevec = 0
  x = int(input("Vpisi geslo: "))
  while x != geslo:
      stevec = stevec + 1
      if stevec > 4:
          break
      x = int(input("Ponovno vpisi: "))
  if x != geslo:
      print("Preveckrat si poskusil, zakljenjen si iz sistema!")
  else:
      print("Bravo!")

For zanka
~~~~~~~~~

::

  for spremenljivka in zbirka:
      Koda, ki se izvaja dokler spremenljivka ne preteče vseh elementov zbirke.

``for`` zanko uporabimo takrat, ko želimo, da naša spremenljivka preteče vse
elemente neke zbirke. Zbirka je lahko seznam, niz znakov, slovar, iterator ali
kaj podobnega, bolj podrobno si bomo to pogledali pozneje. Zaenkrat bomo for
zanko večinoma uporabljali skupaj s funkcijo ``range(x)``, ki vrne vse elemente
od ``0`` do ``x-1`` (torej ``range(5)`` vrne ``[0, 1, 2, 3, 4]``).

Primer:

.. literalinclude:: /tutorialsPythonBasic/verybasic/loops/for.py
  :linenos:

Break
~~~~~

Če kjerkoli v zanki napišemo ukaz ``break``, bo zanka takrat prekinjena. Občasno
se programira tudi tako, da zanalašč naredimo neskončno zanko, in potem ob
določenih pogojih pokličemo ``break``.

Ukaz break prekine le 'najbližjo' zanko -- če imamo gnezdenih več zank (npr. for
zanka znotraj while zanke) se bo prekinila le notranja zanka (v našem primeru
for zanka).

Continue
~~~~~~~~

Continue je podoben stavku ``break``, le da ne prekine najbolj notranje zanke,
ampak preskoči vse do konca trenutne iteracije in takoj začne izvajanje
naslednje. To je uporabno na primer za filtriranje neveljavnih podatkov::

  a = "sajkdfs adfjkhasdf jkasdkfjas dfkjhasd fasdlfkjsa dflkjsadf"
  veljavno = "aeiou"
  for i in a:
      if a not in veljavno:
          continue
      # tukaj zelo veliko kode, ki procesira veljavne podatke

Kot ste morda opazili se da continue vedno nadomestiti z ustreznim ``if``
``else`` stavkom, a je to lahko veliko bolj neberljivo.

.. vim: spell spelllang=sl
