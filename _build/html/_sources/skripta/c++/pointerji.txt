Pointerji in reference
======================

Pointerje v C++ si lahko predstavljamo kot naslove do spremeljivk. Če bi to
hoteli prikazati to z pratičnim primerom bi bil pointer naslov do hiše(Tržaška
cesta 72) spremenljivka pa bi bila hiša.

Uvod
----
Če na pointerje pogledamo iz bolj iz računalniškega vidika moramo najprej poznati
ozadje delovanja računalnikov, kako so podatki shranjeni v računalniku in kako
program dostopa do podatkov. Spomin računalnika je razdeljen na spominjske celice
(ang. memory cells) vsaka je velika 1 byte in vsaka imajo svojo unikaten naslov.
Med našim izvajanjem programa, ko mi deklariramo novo spremenljivko nam
operacijski sistem določi en delček spomina. Problem je v tem, ker mi sami ne
moremo določiti kam bo shranili to spremeljivko, zato si je včasih uporabno
shraniti naslov do nje, kot bomo kasneje videli.

Sintaksa
--------

Definicija pointerja v C++ ima naslednjo sintkaso:
.. code-block:: cpp

    type * ime_pointerja

Nastavljanje pointerjev(& operator)
-----------------------------------

Če hočemo pointerju nastaviti naslov na katerega bo kazal to naredimo s
operatorjem ``&``. Primer nastavitve pointerja na naslov funkcije.

.. code-block:: cpp

    int variable = 5;
    int * pointer = &variable;  // Vrednost naslova 0x7ffeacbf64ec

Dostopanje do vrednosti(* operator)

Sedaj ko smo dobili naslov vrednosti jo seveda hočemo uporabiti. To naredimo
z operatorjem ``*``, ki ga damo pred imenom pointerja.

.. code-block:: cpp

    cout << *pointer + 5 << endl;  // Izpiše nam 10

Poleg dostopanja lahko vrednost tudi spreminjamo, saj imamo seveda naslov, kjer
je shranjena spremenljivka.

.. code-block:: cpp

    *pointer += 10;
    cout << variable << endl;  // Izpiše nam 15

.. warning::

    Paziti moramo na zvezdica pred imenom pointerja saj je to ključno za
    delovanje pointerja. Saj če jo pozabimo zvezdico ali jo izpustimo je to
    velika razlika. Poglejmo na primeru:

    .. code-block:: cpp


        *pointer++;  // Povečamo vrednost spremenljivke

        pointer++;  // Spremenimo naslov pointerja... sedaj pointer kaže na radom vrednost v spominu
