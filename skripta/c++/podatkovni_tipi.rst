Podatkovni tipi
===============





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
