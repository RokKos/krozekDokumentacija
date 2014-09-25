Podatkovni tipi
===============

Podatkovni tipi so zelo pomemben koncept v C++-u. Vsaka spremenljivka ima svoj
tip in ena najpogostejših napak pri compilanju je, da se tipi ne ujemajo. Morda
je potrebno nekaj truda, da se na tipe navadimo, ampak pri velikih projektih
lahko tipi zelo pomagajo pri jasnosti kode in pri boljšem razumevanju kaj
počnemo, saj ne moremo npr. ponesreči podati funkciji napačnih parametrov.

Uvod
----

Tipe delimo na primitivne in neprimitivne. Neprimitivni so tipi, ki so
definirani kot razredi, vendar ta razlika nima posebnega vpliva. Primitivni so
vsi številski in logični tipi. 

Števila
------------

Številski tipi se razlikujejo glede na to ali predstavljajo cela ali decimalna
števila in po velikosti. Celoštevilski tipi so ``short``, ``int``, ``long`` in
``long long``, decimalni pa ``float``, ``double`` in ``long double``. Med
celoštevilske tipe lahko štejemo tudi ``char``, ki predstavlja en znak, a je v
resnici številka (koda znaka v ASCII tabeli). Tipi podpirajo standardne aritmetične in bitne operacije.
Primer:

.. code-block:: cpp

  int a = 9;
  char c = 'a';
  short b = a + c + '1'; // b = 155
  double g = -12.44;
  float r = 1.1e15;

Omejitve
~~~~~~~~

============ =============== ============================
ime          velikost [#f1]_  približen razpon
============ =============== ============================
char         8 bit           :math:`\pm 127`
short        16 bit          :math:`\pm 32\,767` 
int          32 bit          :math:`\pm 2.14 \cdot 10^9` 
long         native          
long long    64 bit          :math:`\pm 9.22 \cdot 10^{19}`
float        32 bit          :math:`\pm 3.4 \cdot 10^{\pm 38}`, 7 decimalk  
double       64 bit          :math:`\pm 3.4 \cdot 10^{\pm 308}`, 15 decimalk 
long double  80 bit          :math:`\pm 1.1 \cdot 10^{\pm 4932}`, 18 decimalk
============ =============== ============================

.. [#f1] Velikost je odvisna od operaicjskega sistema in računalnika. Native
  pomeni  64 ali 32 biten, zopet odvisno od računalnika. V tablei so naštete
  najbolj pogoste velikosi. ``unsigned`` verzije imajo enak razpon, samo da je
  ce na pozitivnem delu osi. Več `tukaj
  <http://en.cppreference.com/w/cpp/language/types#Properties>`_.

Mnogo bolj podrobno in pravilno tabelo najdete `tukaj
<http://en.cppreference.com/w/cpp/language/types#Range_of_values>`_.

Naj vas to ne prestraši, pametno je poznati omejitve, a mi bomo ponavadi za
cela števila uporabljali kar ``int`` in za decimalna ``double``. (Float je pres
precej nenatančen, kar je na tekmovanjih, v resnici pa še toliko bolj, lahko
problematično. Ali kot je dejal nekoč moj kolega "Kdor uporablja floate je pa
res čevl." Pred celoštevilske tipe lahko vtaknemo tudi ``unsigned``, ki razpon
števila premakne na pozitivno os. Če število povečamo čez razsežnost tipa, se
ne zgodi na videz nič, številka se samo navije okrog spodnje meje. Torej, če
rečemo ``char a = 130;`` bo ``a`` v resnici enak ``-126``. 

Decimalna števila zaokrožujejo in zaradi tega se pojavljajo napake. Obstaja
zelo močna veja matematike, ki se ukvarja s preučevanjem in odpravljanjem teh
napak, ampak za nas bo dovolj, da se samo zavedamo, da obstajajo. Če na primer
10 krat seštejete 0.1, to ni nujno enako celemu številu 1 (``if`` stavek se
lahko recimo ne izvede, če je kaj takega v pogoju). Dveh decimalnih števil
nikoli ni pametno direktno preverjati, ali sta enaki, ponavadi se za mero
enakosti vzame kaj podobnega kot ``abs(a - b) < -1e9``. Decimalna števila imajo
omejitve tudi glede tega, kako blizu 0 lahko pridejo (vsa lahko predstavijo
točno 0). Podobne omejitve za decimalna števila veljajo tudi v Pythonu in
ostalih programskih jezikih.

Pretvorbe
~~~~~~~~~
Med tipi lahko med pretvarjamo, poznami implicitne in eksplicitne pretvorbe.
Compiler bo avtomatsko naredil pretvorbe, ki ne škodujejo "kvaliteti" tipa, pri
pretvorbi iz npr. ``double`` v ``int`` pa bo posvaril vsaj z opozorilom. Tako
pretvorbo lahko sami naredimo na več načinov (ki so glede na rezultat ekvivalentni):

.. code-block:: cpp

  int a = static_cast<int>(12.34);
  int b = int(12.34);
  int c = (int) 12.34;

Če uporabimo ``static_cast``, to compilerju da informacijo in lahko s tem
naprej bolje analizira kodo, medtem ko ostali tega ne naredijo, zato je
priporočen.

Logične vrednosti
-----------------

Logični vrednosti sta ``true`` in ``false``. Z logičnimi vrednostmi lahko
računamo kot vedno, z operatorji ``&&``, ``||`` in ``!``. Kot številski
vrednosti predstavljata 0 in 1. Logične spremenljivke imajo tip ``bool``.
Vrsti red operatorjev je enak kot v matematiki, a je priporočljivo uporabljati
oklepaje. Primer: 

.. code-block:: cpp

  bool a = false;
  bool c = 4 < 2.3;
  bool m = a && c || !c;

Seznami
-------

Nizi znakov
-----------

Asociativni seznami
-------------------

Množice
-------

Dodatek o vseh zbirkah
----------------------


.. _range-for:


Range for zanka
~~~~~~~~~~~~~~~

Za vsako zbirko, ki definira ``.begin()`` in ``.end()`` iteratorja, ki
podpirata ``++it``, ``*it`` in ``!=``, se lahko uporablja ``range for`` zanko.

Torej lahko za vektor ``v``, če nas indeksi njegovih elementov ne zanimajo, ali
pa morda naša zbirka sploh ne podpira dostopa po indeksih, namesto:

.. code-block:: cpp

  for (vector<int>::iterator it = v.begin(); it != v.end(); ++it) {
      // pocni nekaj z *it
  }

napišemo:

.. code-block:: cpp

  for (int x : v) {
      // pocni nekaj z x
  }

Paziti je potrebno, da se v tem primeru ustvari kopija ``x``, in da če ``x``
spremenimo, to nima vpliva na ``v``. A je tudi to rešljivo. Zgornja verzija v
nobenem primeru ni optimalna, če vrednosti ne želimo spreminjati, napišemo

.. code-block:: cpp
  
  for (const int& x : v) {
      // pocni nekaj z x
  }

kar prepreči kopiranje ``x``, saj je ``x`` dejanski objekt iz ``v``. Če
``const`` izpustimo, lahko ``x`` tudi spreminjamo, kar bo spremenilo tudi
elemente ``v``. Več o referencah (to so tisti & znaki) v poglavju
:ref:`funckije-cpp`. Tip ``int`` lahko nadomestimo tudi z ``auto``, da nam ni
potrebno pisati zelo dolgih tipov, pri čemer še vedno popolnoma veljavno
uporabljamo npr. ``auto& x`` z enakim pomenom kot prej.


.. vim: spell spelllang=sl
