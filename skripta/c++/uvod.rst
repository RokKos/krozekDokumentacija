Uvod
====

C++ je zelo uporabljen in močen jezik, v katerem, ali v njegovem predhodniku
C-ju, so sprogramirani najbolj zahtevni, hitri in znani programi, med drugim vsi
glavni operacijski sistemi, veliko igric, Microsoft Office in sploh večina
stvari, ki vam jih pade na pamet, pa niso na telefonu (razen seveda Android
operacijskega sistema, ki je zopet v C-ju).

C++ je, z razliko od Pythona *prevajan* jezik, kar pomeni, da je kodo najprej
potrebno prevesti v strojno kodo, ki jo potem računalnik izvede. Zaradi tega
vmesnega koraka je tudi za kakšen red velikosti hitrejši od npr. Pythona.

Druga razlika je, da je *statično tipiziran*, kar pomeni, da moramo vsaki
spremenljivki v naprej določiti tip, ki ga potem ne moremo več spreminjati, kar
omogoča veliko bolj efektivno planiranje porabe spomina in boljšo pretvorbo v
strojno kodo, sam ima prevajalnik (compiler) veliko več podatkov.

Na začetku se zdijo to mogoče hude omejitve in je potrebno nekaj truda, da se
človek navadi na "malo manj svobode" in "neke čudne napake", vendar te omejitve
lahko vodijo v kodo z manj napakami in kodo z boljšim dizajnom. Program, ko je
enkrat preveden v strojno kodo, je samostojna aplikacija, ki so lahko zaženemo
tudi na drugih računalnikih (z določenimi omejitvami, na primer OS), ne da bi
imeli tam programsko kodo.

C++ je ravno zaradi teh lastnosti zelo uporabljen in zelo močan jezik, ki se ga
zagotovo splača znati. Je sicer eden izmed težjih, toda iz njega sledi veliko
boljše razumevanje delovanja računalnika in programiranja, pa udi druge jezike
se je potem lažje učiti.

Od programske do strojne kode
-----------------------------
Primer programske kode:

.. code-block:: c++

  #include <cstdio>

  int main() {
      printf("Hello world!");
      return 0;
  }

Prevajanje v strojno kodo poteka v več korakih
(verjetno obstajajo sloveski izrazi, a se ne bom niti trudil, pa tudi napake ki
jih boste dobivali bodo v angleščini):

Preprocessor
  V naši kodi prebere ``#`` direktive in jih izvede, to vključuje vsebovanje
  header file-ov, makrote, header guarde... (več o tem kasneje)

Compiler
  Kodo, ki jo je izpljunil preprocessor prevede v assembler (zbirni jezik), ki
  je zadnji nivo pred strojno kodo. Na tem koraku program izpiše morebitne
  napake v sintaksi vaše kode, neujemanje tipov, itd... Tem napakam se reče
  "compiler errors" in so daleč najbolj pogoste.

Assembler
  Kodo, ki jo je naredil kompiler spremeni v object datoteke (``.o``), ki so
  že zeli blizu strojni kodi. Tu naj ne bi bilo napak, saj je sicer nekaj
  verjetno narobe s compilerjem, ne pa z vašim programom.

Linker
  Poveže object datoteke v eno zaključeno celoto, tako da računalniku pove, v
  katerih knjižnicah so kakšne funkcije ipd. Tu lahko dobite "linker error", ti
  so ponavadi rezultat tega, da se pozabili prilinkati zraven kakšno zunanjo
  knjižnico ali pa ste napisali in klicali funkcijo brez telesa.

Na koncu je rezultat nekaj, kar razume računalnik, mi pa ne, in se lahko
razlikuje od računalnika do računalnika::

  ELF>�@@@ @@@@@@�@@@@�� ��`�``h
  ��`�@@DDP�tdtt@t@44Q�td/lib64/ld-linux-x86-64.so.2GNU GNU[^��.�2?#��9��W��� �3
  O libstdc++.so.6__gmon_start___Jv_RegisterClasses_ITM_deregisterTMCloneTable_
  ITM_registerTMCloneTablelibm.so.6libgcc_s.so.1libc.so.6printf__libc_start_main
  GLIBC_2.2.5�u▒i ��      `�      `�      `�      `H�H�E H��t�3H���52 �%4 @�%2
  h������%* h������%" h�����1�I��^H��H���PTI��P@H���@H���@������fD� `\textit{HU
  `H��H��vH��t]� `��f�]�fffff.�� `UH�� `H��H��H��H��?H�H��t�H��t ]� `��]�fD�=y
  uUH���n���]�f ��@��`H�?u���H��t�UH����]�z���UH���d@�������]�AWAVA��AUATL�%�
  UH�-�
  SI��I��1�L)�H�H���U���H��t�L��L��D��A��H��H9�u�H�[]A\A]A^A_�ff.���H�H��Hello
  world!0���|\���LR����l�������� zRx ���*zRx $����@F▒J U �?▒;*3$"D����▒A�C
  Dd����eB�B▒�E �B(�H0�H8�O@p8A0A(B B▒B������@�@is� T@�▒����o`@(@�@
  h@ � ▒�     `H ▒ ▒���o�@���o���o�@�`�@�@�@GCC: (GNU) 4.9.0 20140507
  (prerelease)GCC: (GNU)
  4.9.1.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.
  dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.text.fini.
  rodata.eh_frame_hdr.eh_frame.init_array.fini_array.jcr.dynamic.got.got.plt.
  data.bss.comment#@ 1<@<$D���o`@N �@�▒V(@(�^���o�@�k���o�@�▒� @ H
  ▒�h@h▒��@�@��@���T@T �`@`�t@t4��@���������`��        `�   �� `�     ��
  `�     � ` �0 88 �H▒ >@@<@`@�@(@��@  @ @ h@ �@T@`@t@�@�`�`�`�`�     `�
  `▒�     ` �@^�����` �@X g {T@�� �`@� �▒�    `�▒`�`�`" ▒�    `-A `�▒�    ` �@e
  ' `,▒ �@▒8
  h@init.ccrtstuff.c__JCR_LIST__deregister_tm_clonesregister_tm_clones__do_
  global_dtors_auxcompleted.6617__do_global_dtors_aux_fini_array_entryframe_
  dummy__frame_dummy_init_array_entrya.cpp__FRAME_END____JCR_END___GLOBAL_
  OFFSET_TABLE___init_array_end__init_array_start_DYNAMICdata_startprintf@@
  GLIBC_2.2.5__libc_csu_fini_start__gmon_start___Jv_RegisterClasses_fini__
  libc_start_main@@GLIBC_2.2.5_ITM_deregisterTMCloneTable_IO_stdin_used_ITM_
  registerTMCloneTable__data_start__TMC_END____dso_handle__libc_csu_init__
  bss_start_end_edatamain_init

Nekaj podobnega dobite, če odprete katerikoli ``.exe`` file v beležnici.

.. vim: spell spelllang=sl
