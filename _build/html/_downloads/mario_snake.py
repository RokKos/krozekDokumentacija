import pygame

SIRINA_EKRANA = 600
VISINA_EKRANA = 400


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
        if self.st_skokov > 0:
            self.st_skokov -= 1
            self.hitrost_y = -10


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
            if dogodek.type == pygame.KEYUP:
                if dogodek.key == pygame.K_LEFT and luigi.hitrost_x < 0:
                    luigi.stop()
                elif dogodek.key == pygame.K_RIGHT and luigi.hitrost_x > 0:
                    luigi.stop()
        # Zganjaj fiziko
        skupina.update()
        # Risanje
        ekran.fill((200, 200, 255))
        ploscadi.draw(ekran)
        skupina.draw(ekran)
        pygame.display.flip()

    pygame.quit()


main()
