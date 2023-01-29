from settings import *
from reel import *
from wins import *
from player import Player
import pygame

class Machine:
    def __init__(self):
         self.display_surface = pygame.display.get_surface()
         self.reel_index = 0
         self.reel_list = {}
         self.can_toggle = True
         self.spinning = False
         self.win_animation_ongoing = False

         # RESULTS
         self.prev_result = {0: None, 1: None, 2: None, 3: None, 4: None}
         self.spin_result = {0: None, 1: None, 2: None, 3: None, 4: None}

         self.spawn_reels()
         self.currPlayer = Player()

    def cooldowns(self):
        #  Only lets player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True
            self.spin_result = self.get_result()
            # print(flip_horizontal(self.get_result())) # Show symbols in a rows

            if self.check_wins(self.spin_result):
                self.win_data = self.check_wins(self.spin_result)
                # Play the win sound
                # self.play.win_sound(self.win_data)
                self.pay_player(self.win_data, self.currPlayer)
                print(self.currPlayer.get_data())
                # self.win_animation_ongoing = True
                # self.ui.win_text_angle = random.randint(-4, 4)
                


    def input(self):
        keys = pygame.key.get_pressed()

        # Checks for space key, ability to toggle spin and balance to cover bet size
        # if keys(pygame.K_SPACE) and  self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE]:    
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            # self.currPlayer.place_bet()
            # self.machine_balance += self.currPlayer.bet_size
            # self.currPlayer.last_payout = None

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 547, 120
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (140 + X_OFFSET), y_topleft

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft)) # Need to create reel class
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                # self.spin_sound.play()

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result

    def check_wins(self, result):
        hits = {}
        horizontal = flip_horizontal(result)
        for row in horizontal:
            for sym in row:
                if row.count(sym) > 2: # Potential win
                    possible_win = [idx for idx, val in enumerate(row) if sym == val]

                    # Check possible_win for a subsequence longer than 2 and to hits
                    if len(longest_sequence(possible_win)) > 2:
                        hits[horizontal.index(row) + 1] = [sym, longest_sequence(possible_win)]
        if hits: 
            return hits

    def pay_player(self, win_data, curr_player):
        pass


    def update(self, delta_time):
        self.cooldowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()
