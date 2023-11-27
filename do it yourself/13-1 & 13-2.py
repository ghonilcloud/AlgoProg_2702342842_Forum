# In alient.py

    # Load the alien image and set its rect attribute.
    self.image = pygame.image.load('images/star.png') # Simply follow textbook instructions but alter the file chosen when loading in aliens.
    self.rect = self.image.get_rect()

# In Game_functions.py

    #Gets 2 random numbers each time the game starts
    from random import randint
    random_number1 = randint(1,10)
    random_number2 = randint(1,10)

    # Def uses the 2 random numbers to determine x and y positions of aliens/stars, each time is different when reloading the same.
    def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + random_number1 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + random_number2 * alien.rect.height * row_number
        aliens.add(alien)