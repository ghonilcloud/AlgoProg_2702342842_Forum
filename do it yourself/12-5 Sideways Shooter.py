#Changes to game_function.py

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

#Changes to ship.py

    # Start each new ship at the left side of the screen.
    self.rect.centerx = self.screen_rect.left

    # Movement flag
    self.moving_down = False
    self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
            
#Changes to bullet.py

    # Create a bullet rect at (0, 0) and then set correct position.
    self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        ai_settings.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.rect.right = ship.rect.right