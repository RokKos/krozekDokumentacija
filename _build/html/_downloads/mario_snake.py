import pygame

SIRINA_EKRANA = 600
VISINA_EKRANA = 400


class KosKace(pygame.sprite.Sprite):
    """ En kvadrat, ki je del kace """
    def __init__(self, x=0, y=0, vx=0, vy=0):
        super().__init__()
        # velikost enega kosa kace
        self.sirina = self.visina = 20
        # Naredimo njeno sliko in jo pobarvajmo
        self.image = pygame.Surface((self.sirina, self.visina))
        self.rect = self.image.get_rect()
        self.image.fill((0, 200, 0))
        # Nastavimo ji pravilno velikost in hotrost
        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        # Naj se premakne
        self.rect.x += self.vx
        self.rect.y += self.vy
        # Naj bo rob ekrana prepusten
        self.rect.x %= SIRINA_EKRANA
        self.rect.y %= VISINA_EKRANA


class Kaca(object):
    """ Celotna kača """
    def __init__(self, x=0, y=0, velikost=5):
        # Velikost hitrosti
        self.hitrost = 1
        # Začetna hitrost/hitrost glave
        self.vx = self.hitrost
        self.vy = 0
        # Naredimo posode, kamor bomo shranili vse kose
        self.moji_kosi = pygame.sprite.Group()
        self.urejeni_kosi = []
        # Naredimo glavo in jo shranimo
        glava = KosKace(x, y, self.vx, self.vy)
        self.urejeni_kosi.append(glava)
        self.moji_kosi.add(glava)
        # Dodajmo vse ostale kose
        self.dodaj_kos(velikost-1)
        # Dodajmo stevec, ki nam bo povedal, kdaj moramo spreminjati hitrosti
        self.stevec = 0
        # Za koliko kosov se moramo podaljsati v naslednjem koraku
        self.buffer = 0

    def dodaj_kos(self, n=1):
        # Dodaj n kosov s hitrostjo 0 na rep kace
        rep = self.urejeni_kosi[-1]
        for i in range(n):
            nov_kos = KosKace(rep.rect.x, rep.rect.y)
            self.urejeni_kosi.append(nov_kos)
            self.moji_kosi.add(nov_kos)

    def update(self):
        # Naj se vsi kosi kace premaknejo
        self.moji_kosi.update()
        # Poglej ce je cas, da se zamenjajo hitrosti
        self.stevec += 1
        if self.stevec > self.urejeni_kosi[0].sirina / self.hitrost:
            # Resetiraj stevec
            self.stevec = 0
            # Premakni hitrosti kosov na kos, ki je pred njim
            for i in range(len(self.moji_kosi)-1, 0, -1):
                self.urejeni_kosi[i].vx = self.urejeni_kosi[i-1].vx
                self.urejeni_kosi[i].vy = self.urejeni_kosi[i-1].vy
            # Nastavi hitrost glave na trenutno hitrost
            self.urejeni_kosi[0].vx = self.vx
            self.urejeni_kosi[0].vy = self.vy
            # Podaljsaj kaco toliko kot je potrebno
            self.dodaj_kos(self.buffer)
            self.buffer = 0

    # Funkcije za premikanje kace
    def pojdi_levo(self):
        self.vx = -self.hitrost
        self.vy = 0

    def pojdi_desno(self):
        self.vx = self.hitrost
        self.vy = 0

    def pojdi_gor(self):
        self.vx = 0
        self.vy = -self.hitrost

    def pojdi_dol(self):
        self.vx = 0
        self.vy = self.hitrost

    def povecaj_se(self):
        self.buffer += 1


class Mario(pygame.sprite.Sprite):
    """ Gospod Mario """
    def __init__(self, ovire=None):
        super().__init__()
        self.ovire = ovire

        sirina = 40
        visina = 60

        self.image = pygame.Surface((sirina, visina))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.hitrost_x = 0
        self.hitrost_y = 0

        self.max_skokov = 1
        self.st_skokov = self.max_skokov

    def update(self):
        # Smer X
        self.rect.x += self.hitrost_x
        self.rect.x %= SIRINA_EKRANA
        if self.ovire:
            trki = pygame.sprite.spritecollide(self, self.ovire, False)
            for ovira in trki:
                if self.hitrost_x < 0:
                    self.rect.left = ovira.rect.right
                if self.hitrost_x > 0:
                    self.rect.right = ovira.rect.left
        # Smer Y
        self.hitrost_y += 0.4
        if self.hitrost_y > 20:
            self.hitrost_y = 20
        self.rect.y += self.hitrost_y
        self.rect.y %= VISINA_EKRANA
        if self.ovire:
            trki = pygame.sprite.spritecollide(self, self.ovire, False)
            for ovira in trki:
                if self.hitrost_y < 0:
                    self.rect.top = ovira.rect.bottom
                if self.hitrost_y > 0:
                    self.st_skokov = self.max_skokov
                    self.rect.bottom = ovira.rect.top
                self.hitrost_y = 0


    def pojdi_levo(self):
        self.hitrost_x = -6
    def pojdi_desno(self):
        self.hitrost_x = 6
    def stop(self):
        self.hitrost_x = 0
    def skoci(self):
        self.rect.y += 2
        trki = pygame.sprite.spritecollide(self, self.ovire, False)
        self.rect.y -= 2
        if len(trki):
            self.hitrost_y = -10
        elif self.st_skokov > 0:
            self.st_skokov -= 1
            self.hitrost_y = -8


class Ploscad(pygame.sprite.Sprite):
    def __init__(self, x, y, s, v):
        super().__init__()
        self.image = pygame.Surface((s, v))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



def main():
    ekran = pygame.display.set_mode(
        [SIRINA_EKRANA, VISINA_EKRANA])

    ploscadi = pygame.sprite.Group()
    ploscadi.add(
        Ploscad(100, 100, 100, 20),
        Ploscad(200, 200, 100, 20),
        Ploscad(300, 300, 100, 20))

    skupina = pygame.sprite.Group()

    luigi = Mario(ploscadi)
    skupina.add(luigi)

    kaca = Kaca()

    konec_zanke = False
    ura = pygame.time.Clock()
    while not konec_zanke:
        ura.tick(60)
        # User input
        for dogodek in pygame.event.get():
            if dogodek.type == pygame.QUIT:
                konec_zanke = True
            elif dogodek.type == pygame.KEYDOWN:
                if dogodek.key == pygame.K_LEFT:
                    luigi.pojdi_levo()
                elif dogodek.key == pygame.K_RIGHT:
                    luigi.pojdi_desno()
                elif dogodek.key == pygame.K_UP:
                    luigi.skoci()
                elif dogodek.key == pygame.K_a:
                    kaca.pojdi_levo()
                elif dogodek.key == pygame.K_d:
                    kaca.pojdi_desno()
                elif dogodek.key == pygame.K_s:
                    kaca.pojdi_dol()
                elif dogodek.key == pygame.K_w:
                    kaca.pojdi_gor()
                elif dogodek.key == pygame.K_q:
                    kaca.povecaj_se()
            if dogodek.type == pygame.KEYUP:
                if dogodek.key == pygame.K_LEFT and luigi.hitrost_x < 0:
                    luigi.stop()
                elif dogodek.key == pygame.K_RIGHT and luigi.hitrost_x > 0:
                    luigi.stop()
        # Zganjaj fiziko
        skupina.update()
        kaca.update()
        # Risanje
        ekran.fill((200, 200, 255))
        ploscadi.draw(ekran)
        skupina.draw(ekran)
        kaca.moji_kosi.draw(ekran)
        pygame.display.flip()

    pygame.quit()


main()
