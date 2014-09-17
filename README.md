# Programerski krožek na Gimnaziji Vič

V tem repozitoriju se nahaja dokumentacija za programerski krožek na Gimnaziji
Vič.

# Namestitev

Za namestitev potrebujete nameščen `python3` in za njega pakete `pip` in
`virtualenv`. Nato potrebujete le zagnati:

    make install

kar ustvari virtualenv in namesti vse potrebne pakete (ki se nahajajo v
`requirements.txt`).

# Git submoduli

Ta repozitorij vsebuje dodatni subrepozitorij. Da dobite vse potrebne datoteke,
morate namesto 'navadnega' `git clone` zagnati `git clone --recursive`. Če ste
to pozabili in ste repozitorij že prenesli, pojdite v njega in zaženite:

    git submodule update --init --recursive
