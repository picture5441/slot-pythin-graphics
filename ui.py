from player import Player
from settings import *
import pygame, random

class UI:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.font, self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE), pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.win_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        

    def display_info(self):
        player_data = self.player.get_data()

        # Balance and bet size
        balance_surf = self.font.render("Balance: $" + player_data['balance'], True, TEXT_COLOR, None)
        x, y = 200, self.display_surface.get_size()[1] - 210
        balance_rect = balance_surf.get_rect(bottomleft = (x, y))

        bet_surf = self.bet_font.render("Wager: $" + player_data['bet_size'], True, TEXT_COLOR, None)
        x = self.display_surface.get_size()[0] - 210
        bet_rect = bet_surf.get_rect(bottomright = (x, y))

        # Draw player data
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surf, balance_rect)
        self.display_surface.blit(bet_surf, bet_rect)

        # Print last win if applicable
        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surf = self.win_font.render("WIN! $" + last_payout, True, TEXT_COLOR, None)
            x1 = 960
            y1 = self.display_surface.get_size()[1] - 240
            win_rect = win_surf.get_rect(center = (x1, y1))
            self.display_surface.blit(win_surf, win_rect)

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(100, 760, 1920, 300))
        self.display_info()

