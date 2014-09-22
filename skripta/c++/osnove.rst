Osnove
======

V tem poglavju si bomo ogledali osnove programiranja, s katerimi lahko
vzpostavimo osnovno komunikacijo z računalnikom in naredimo zelo enostavne
programe, pogledali si bomo predpisano strukturo programa in nekaj osnovnih
ukazov.

Osnovna struktura programa
--------------------------
Osnovni "Hello world" program zgleda tako:

.. code-block:: cpp

  #include <iostream>

  int main() {
      std::cout << "Hello world!" << std::endl;
      return 0;
  }

Na začetku so vedno ``#include`` direktive, ki so podobne Pythonovim
``import``-om, ki vključujejo različne knjižnice. V našem primeru vključujemo
knjižnico za input in output (input output stream).

Program izvede vse in samo to, kar se nahaja v funkciji ``main``. Ta funkcija
lahko seveda kliče druge funkcije. Funkcija mora vrniti število, ki pomeni "exit
status" programa in mora biti 0, če je program zaključil uspešno. Vsi naši
programi bodo imeli na koncu return 0.

Vsak stavek se mora končati s podpičjem. Presledki v kodi niso obvezni, tako kot
v Pythonu, zamikanje je samo zaradi berljivosti. Toda koda kot na primer ``int
main(){std::cout<<"Hello world!"<<std::endl;return 0;}`` je sicer veljavna, a
se je izogibajte kot določenih profesorjev.

C vs. C++ vs. C++11
-------------------
C++ je nadgradnja C-ja, zaradi tega podpira veliko večino C stvari, hkrati pa
nudi svojo novo funkcionalnost. C++ je imel tudi večjo posodobitev leta 2011,
ki je prinesla veliko novosti, ki jih bomo mi z veseljem uporabljali in jih
tudi večina compilerjev že podpira. V splošnem bomo uporabljali bolj C++
funkcije namesto starih C funkcij. Če si boste doma instalirali kakšen
predpotopni compiler, lahko da kakšnih novosti ne bo podpiral, a to ne bi smel
biti hud problem.

Vse funkcije, ki jih podpira standarda knjižnica C++ so v *namespace*-u
``std``. Tako je treba, kot zgoraj v primeru, pred vsako uporabo stvari iz
standardne knjižnice pisati ``std::``. Temu se lahko izognemo, tako da na
začetku programa (za ``#include``-i in pred uporabo funkcij) napišemo ``using
namespace std;``. To sicer ni najbolj higienično v velikih programih saj lahko
povzroči poplavo imen, vendar v naših programih to verjetno ne bo problem.

Obstajajo C-jevske funckije za stdio, random, sezname, vendar bomo uporabljali
C++-ovske, pogosto celo C++11.

Spremenljivke
-------------

Spremeljivke so prostori v spominu, ki hranijo določeno vrednost in jih lahko
tekom programa spreminjamo. Vsako spremenljivko moramo deklarirati z njenim
tipom, nato pa ji lahko pripišemo vrednost. 

.. code-block:: cpp

  int a;
  a = 8;
  a = 7;
  int b = 9;
  int b;      // compiler error - dvakrat definirana spremenljivka
  c = 6;      //  compiler error - nedefinirana spremenljivka

Če spremenljivki vrednosti ne pripišemo, bo njena vrednost pogosto neko sranje,
ki je ravno takrat v ramu, tako da je vse spremenljivke zelo priporočljivo
inicializirati.

Osnovni tipi so ``int`` za števila, ``double`` za decimalna števila, ``bool``
za logične vrednosti in ``char`` za znake.

Komentarji
----------
Komentarji so enovrstični z ``//`` in več vrstični s parom ``/*  */``.

Input in output
---------------
Za manipulacijo standardnega vhoda in izhoda uporabljamo knjižnico
``iostream``, ki definira objekta ``cin`` in ``cout``, s katerima pišemo in
beremo v stdio. Pri nizih to prebere vse do prvega whitespace-a. Če želimo
prebrati celo vrstico uporabimo funkcijo ``getline``.

.. code-block:: cpp

  #include <iostream>

  using namespace std;

  int main() {
      int a;
      cout << "Vpiši število: ";
      cin >> a;
      cout << "Vpisali ste število " << a << endl;
  }

.. note::

  Obstajajo ljudje, ki bodo trdili, da je potrbno uporabljati C-jevski verziji
  ``scanf`` in ``printf``, saj sta mnogo hitrejši. To ni nujno res, pri uporabi
  ``cin`` in ``cout`` se je samo potrebno izgoniti ``endl``, ki neporebno
  flusha in nastaviti ``cin.sync_with_stdio(false)``, da nove verzije pozabijo na
  C funckije in delujejo samostojno. Za kakršnekoli resne programe je časovna
  razlika nepomembna, veliko več prednosti prinese ekstenzibilnost in
  type-safety.

If stavki
---------
If stavki v C++-u so strukture, ki izvedejo blok kode, samo če je izpolnjen
določen pogoj. *Blok* kode je definiran kot en stavek ali več stavkov znotraj
``{`` in ``}``. Običajna sintaksa ``if`` stavkov:

.. code-block:: cpp

  if (pogoj) {
      koda ...
  } else if (pogoj) {
      koda ...
  } else {
      koda ...
  }

Pogoji so sestavljeni (ponavadi) iz logičnih (``&&``, ``||``, ``!``) in
primerjalnih operatorjev (``==``, ``<``, ``>=``, ...).

Primer:

.. code-block:: cpp

  // program preveri ali je a sodo število
  if (a % 2 == 0) {
      cout << "sodo" << endl;
  } else {
      cout << "liho" << endl;
  }

.. warning::

  Če je v ``if`` stavku en sam stavek, potem lahko oklepaje izpustimo, saj je
  stavek že sam od sebe blok. Zgornjo kodo lahko napišemo tudi tako:

  .. code-block:: cpp
    
    if (a % 2 == 0)
        cout << "sodo" << endl;
    else 
        cout << "liho" << endl;
  
  To lahko vodi v buge, ko dodamo še en stavek, 

  .. code-block:: cpp
    
    if (a % 2 == 0)
        cout << "sodo" << endl;
    else 
        cout << "liho" << endl;
        cout << "vedno" << endl;
 
  Stavek ``vedno`` se izvede vedno, čeprav indentacija namiguje dugače, kajti
  ``else`` "zagrabi" le en naslednji stavek. 
  
.. danger::

  V C++ je veljavno imeti v ``if`` stavku operator ``=``, ki **nastavi**
  spremenljivke. Torej, človek se zmoti in namesto ``==`` napiše ``=``, kar
  je lahko katastrofalno. Primer:

  .. code-block:: cpp
   
    if (password_valid = true) {
        // omogoči dostop do bančnih računov in slečenih slik
    } else {
        cout << "Invalid password" << endl;
    }

    Zgornja koda je enaka, ko če bi kar direktno omogočili ves dostop,
    ``password_valid`` se namreč **nastavi** na ``true``, kar tudi vrne 
    vrednost ``true`` in je pogoj v ``if`` stavku vedno pravilen.

Obstaja tudi stavek ``switch``, ki se ga ponavadi uporablja kot lepši ``if``,
``else if``. Primer uporabe:

.. code-block:: cpp
  
  switch (vrednost) {
      case 1:
          // koda
          break;
      case 2:
          //koda
          break;
      case 13:
          //koda
          break;
      default:
          //koda
          break;
  }

Vrednosti pri ``case``-ih morajo biti konstantne in stavek glede na vrednost
spremenljivke ``vrednost`` izvede primerno kodo, če dane vrednosti ni naštete,
potem izvede kodo pod ``default``.

Zanke
-----


.. vim: spell spelllang=sl
