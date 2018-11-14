import pygame as pg
from classes.bullet import Bullet
from classes.alien import Alien
from time import sleep


def check_keydown_events(screen, ai_settings, event, ship, bullets):
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.key == pg.K_SPACE:
        fire_bullet(screen, ai_settings, ship, bullets)
    elif event.key == pg.K_BACKQUOTE:
        exit()


def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False


def check_events(screen, ai_settings, stats, ship, aliens, bullets, play_button):
    """Reakcja na zdarzenie generowane przez klawiature i mysz"""

    for event in pg.event.get():  # petla zdarzen
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            check_play_button(screen, ai_settings, stats, ship, aliens, bullets, play_button)
        elif event.type == pg.KEYDOWN:
            check_keydown_events(screen, ai_settings, event, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(screen, ai_settings, stats, ship, aliens, bullets, play_button):
    mouse_x, mouse_y = pg.mouse.get_pos()
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pg.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(screen, ai_settings, stats, ship, aliens, bullets, play_button):
    """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # wyswietlenie statku na ekranie
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pg.display.flip()  # wyswietlenie ostatnio zmodyfikowanego obrazu


def update_bullets(screen, ai_settings, ship, aliens, bullets):
    """Uakt. polozenia pociskow i usuniecie tych niewidocznych na ekranie"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship)


def check_bullet_alien_collisions(ai_settings, aliens, bullets, screen, ship):
    pg.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(screen, ai_settings, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets):
    # screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= ship.rect.centery:
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets)


def create_alien_row(screen, ai_settings, aliens, alien_number, rows_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rows_number
    aliens.add(alien)


def check_fleet_edges(aliens, ai_settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break


def change_fleet_direction(aliens, ai_settings):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(screen, ai_settings, stats, ship, aliens, bullets):
    """Spr czy flota znajduje sie przy krawedzi ekranu, a nast. uaktualnienie polozenia obcych we flocie"""
    check_fleet_edges(aliens, ai_settings)
    aliens.update()
    if pg.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, screen, stats, ship, aliens, bullets)


def get_number_free_rows(ai_settings, ship_height, alien_height):
    """Ustalenie ile rzedow obcych zmiesci sie na ekranie"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    rows_number = int(available_space_y / (2 * alien_height))
    return rows_number


def create_fleet(ai_settings, screen, ship, aliens):
    """Utworzenie pelnej floty obcych"""
    alien = Alien(screen, ai_settings)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    rows_number = get_number_free_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Utworzenie pierwszego rzedu obcych
    for row_number in range(rows_number):
        for alien_number in range(number_aliens_x):
            create_alien_row(screen, ai_settings, aliens, alien_number, row_number)


def ship_hit(ai_settings, screen, stats, ship, aliens, bullets):
    """Reakcja na uderzenie obcego w statek"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pg.mouse.set_visible(True)
