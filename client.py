"""Written by Caleb Mathurin
   May 7, 2024 - July 28, 2024,
   Written through PyCharm Community Edition 2024.1.1 with Python 3.12
   This program is a QTE-focused game made with the Pygame library."""

#CM 5/7/24-6/28/24 - imports
import pygame
from random import randint
import time
import socket

#CM 5/7/24-5/26/24 - initializes pygame
pygame.init()
clock = pygame.time.Clock()

#CM 5/7/24 - initializes window size and gives it a caption
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("QTE Heaven")

#6/28/24 - networking variables
host = socket.gethostbyname(socket.gethostname())
port = 5050
client_socket = socket.socket()

#CM 5/8/24-7/23/24 - sprites
key = [pygame.image.load("Keys/Player 1/Q.png"), pygame.image.load("Keys/Player 1/W.png"),
       pygame.image.load("Keys/Player 1/E.png"), pygame.image.load("Keys/Player 1/A.png"),
       pygame.image.load("Keys/Player 1/S.png"), pygame.image.load("Keys/Player 1/D.png")]
key_pressed = [pygame.image.load("Keys/Player 1/Q_pressed.png"), pygame.image.load("Keys/Player 1/W_pressed.png"),
               pygame.image.load("Keys/Player 1/E_pressed.png"), pygame.image.load("Keys/Player 1/A_pressed.png"),
               pygame.image.load("Keys/Player 1/S_pressed.png"), pygame.image.load("Keys/Player 1/D_pressed.png")]
key2 = [pygame.image.load("Keys/Player 2/U.png"), pygame.image.load("Keys/Player 2/I.png"),
        pygame.image.load("Keys/Player 2/O.png"), pygame.image.load("Keys/Player 2/J.png"),
        pygame.image.load("Keys/Player 2/K.png"), pygame.image.load("Keys/Player 2/L.png")]
key_pressed2 = [pygame.image.load("Keys/Player 2/U_pressed.png"), pygame.image.load("Keys/Player 2/I_pressed.png"),
                pygame.image.load("Keys/Player 2/O_pressed.png"), pygame.image.load("Keys/Player 2/J_pressed.png"),
                pygame.image.load("Keys/Player 2/K_pressed.png"), pygame.image.load("Keys/Player 2/L_pressed.png")]
stage = pygame.image.load("Backgrounds/Designerresize.jpg")
online_play = pygame.image.load("Backgrounds/online_play_screen.png")
connecting_to_server = pygame.image.load("Backgrounds/connecting_to_server.png")
searching_for_players = pygame.image.load("Backgrounds/searching_for_players.png")
could_not_connect = pygame.image.load("Backgrounds/could_not_connect.png")
title = pygame.image.load("Backgrounds/title_screen.png")
checkerboard_bg = pygame.image.load("Backgrounds/checkerboard_bg.png")
checkerboard_bg_green = pygame.image.load("Backgrounds/checkerboard_bg_green.png")
checkerboard_bg_red = pygame.image.load("Backgrounds/checkerboard_bg_red.png")
checkerboard_bg_tan = pygame.image.load("Backgrounds/checkerboard_bg_tan.png")
checkerboard_bg_dark_blue = pygame.image.load("Backgrounds/checkerboard_bg_dark_blue.png")
skin_select_stage = pygame.image.load("Sprites/skin_select_stage.png")
skin_select_spotlight = pygame.image.load("Sprites/skin_select_spotlight.png")
player_sprite = pygame.image.load("Sprites/ice_cream_kid.png")
cpu_sprite = pygame.image.load("Sprites/CPU.png")
buttons = [pygame.image.load("Buttons/online_play_button.png"), pygame.image.load("Buttons/offline_play_button.png"),
           pygame.image.load("Buttons/item_shop_button.png"), pygame.image.load("Buttons/extras_button.png"),
           pygame.image.load("Buttons/back_button.png"), pygame.image.load("Buttons/1P_vs_COM_button.png"),
           pygame.image.load("Buttons/1P_vs_2P_button.png"), pygame.image.load("Buttons/match_rules_button.png"),
           pygame.image.load("Buttons/match_rules_2_button.png"), pygame.image.load("Buttons/match_rules_3_button.png"),
           pygame.image.load("Buttons/match_rules_4_button.png"), pygame.image.load("Buttons/match_rules_5_button.png"),
           pygame.image.load("Buttons/match_rules_6_button.png"), pygame.image.load("Buttons/match_rules_8_button.png"),
           pygame.image.load("Buttons/match_rules_12_button.png"),
           pygame.image.load("Buttons/match_rules_16_button.png"),
           pygame.image.load("Buttons/match_rules_20_button.png"), pygame.image.load("Buttons/p1_skin_button.png"),
           pygame.image.load("Buttons/p2_skin_button.png"), pygame.image.load("Buttons/cpu_skin_button.png"),
           pygame.image.load("Buttons/stage_button.png"), pygame.image.load("Buttons/skin_select_button.png"),
           pygame.image.load("Buttons/animal_select_left_button.png"),
           pygame.image.load("Buttons/animal_select_right_button.png"),
           pygame.image.load("Buttons/item_shop_skins_button.png"),
           pygame.image.load("Buttons/item_shop_stages_button.png"),
           pygame.image.load("Buttons/item_shop_music_button.png"),
           pygame.image.load("Buttons/be_server_host_button.png"),
           pygame.image.load("Buttons/be_server_guest_button.png")]
buttons_hover = [pygame.image.load("Buttons/online_play_button_hover.png"),
                 pygame.image.load("Buttons/offline_play_button_hover.png"),
                 pygame.image.load("Buttons/item_shop_button_hover.png"),
                 pygame.image.load("Buttons/extras_button_hover.png"),
                 pygame.image.load("Buttons/back_button_hover.png"),
                 pygame.image.load("Buttons/1P_vs_COM_button_hover.png"),
                 pygame.image.load("Buttons/1P_vs_2P_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_2_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_3_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_4_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_5_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_6_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_8_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_12_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_16_button_hover.png"),
                 pygame.image.load("Buttons/match_rules_20_button_hover.png"),
                 pygame.image.load("Buttons/p1_skin_button_hover.png"),
                 pygame.image.load("Buttons/p2_skin_button_hover.png"),
                 pygame.image.load("Buttons/cpu_skin_button_hover.png"),
                 pygame.image.load("Buttons/stage_button_hover.png"),
                 pygame.image.load("Buttons/skin_select_button_hover.png"),
                 pygame.image.load("Buttons/animal_select_left_button_hover.png"),
                 pygame.image.load("Buttons/animal_select_right_button_hover.png"),
                 pygame.image.load("Buttons/item_shop_skins_button_hover.png"),
                 pygame.image.load("Buttons/item_shop_stages_button_hover.png"),
                 pygame.image.load("Buttons/item_shop_music_button_hover.png"),
                 pygame.image.load("Buttons/be_server_host_button_hover.png"),
                 pygame.image.load("Buttons/be_server_guest_button_hover.png")]
button_select = [pygame.image.load("Button Select/match_rules_button_select.png"),
                 pygame.image.load("Button Select/skin_select_button_select.png")]
ui_elements = [pygame.image.load("UI Elements/rounds_of_qtes_ui.png"),
               pygame.image.load("UI Elements/letters_per_qte_ui.png"),
               pygame.image.load("UI Elements/seconds_per_qte_ui.png")]
trophy = pygame.image.load("Sprites/trophy.png")
player_win = pygame.image.load("Backgrounds/player_win.png")
cpu_win = pygame.image.load("Backgrounds/cpu_win.png")
game_countdown_sprites = [pygame.image.load("Game Countdown Sprites/3.png"),
                          pygame.image.load("Game Countdown Sprites/2.png"),
                          pygame.image.load("Game Countdown Sprites/1.png"),
                          pygame.image.load("Game Countdown Sprites/GO.png")]
cat_idle_1 = [pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_1.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_2.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_3.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_4.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_5.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_6.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_7.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_8.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_9.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_10.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_11.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_12.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_13.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_14.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_15.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_16.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_17.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_18.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_19.png"),
              pygame.image.load("Sprites/Cat/Idle 1/cat_idle_1_20.png")]
cat_idle_2 = [pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_1.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_2.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_3.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_4.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_5.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_6.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_7.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_8.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_9.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_10.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_11.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_12.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_13.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_14.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_15.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_16.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_17.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_18.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_19.png"),
              pygame.image.load("Sprites/Cat/Idle 2/cat_idle_2_20.png")]
cat_nice = [pygame.image.load("Sprites/Cat/Nice/cat_nice_1.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_2.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_3.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_4.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_5.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_6.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_7.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_8.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_9.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_10.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_11.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_12.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_13.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_14.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_15.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_16.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_17.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_18.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_19.png"),
            pygame.image.load("Sprites/Cat/Nice/cat_nice_20.png")]
cat_miss = [pygame.image.load("Sprites/Cat/Miss/cat_miss_1.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_2.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_3.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_4.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_5.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_6.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_7.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_8.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_9.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_10.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_11.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_12.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_13.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_14.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_15.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_16.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_17.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_18.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_19.png"),
            pygame.image.load("Sprites/Cat/Miss/cat_miss_20.png")]
cat_timeout = [pygame.image.load("Sprites/Cat/Timeout/cat_timeout_1.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_2.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_3.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_4.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_5.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_6.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_7.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_8.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_9.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_10.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_11.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_12.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_13.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_14.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_15.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_16.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_17.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_18.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_19.png"),
               pygame.image.load("Sprites/Cat/Timeout/cat_timeout_20.png")]
dog_idle_1 = [pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_1.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_2.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_3.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_4.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_5.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_6.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_7.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_8.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_9.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_10.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_11.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_12.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_13.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_14.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_15.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_16.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_17.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_18.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_19.png"),
              pygame.image.load("Sprites/Dog/Idle 1/dog_idle_1_20.png")]
dog_idle_2 = [pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_1.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_2.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_3.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_4.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_5.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_6.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_7.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_8.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_9.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_10.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_11.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_12.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_13.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_14.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_15.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_16.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_17.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_18.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_19.png"),
              pygame.image.load("Sprites/Dog/Idle 2/dog_idle_2_20.png")]
dog_nice = [pygame.image.load("Sprites/Dog/Nice/dog_nice_1.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_2.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_3.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_4.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_5.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_6.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_7.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_8.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_9.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_10.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_11.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_12.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_13.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_14.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_15.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_16.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_17.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_18.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_19.png"),
            pygame.image.load("Sprites/Dog/Nice/dog_nice_20.png")]
dog_miss = [pygame.image.load("Sprites/Dog/Miss/dog_miss_1.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_2.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_3.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_4.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_5.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_6.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_7.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_8.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_9.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_10.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_11.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_12.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_13.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_14.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_15.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_16.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_17.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_18.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_19.png"),
            pygame.image.load("Sprites/Dog/Miss/dog_miss_20.png")]
dog_timeout = [pygame.image.load("Sprites/Dog/Timeout/dog_timeout_1.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_2.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_3.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_4.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_5.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_6.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_7.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_8.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_9.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_10.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_11.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_12.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_13.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_14.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_15.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_16.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_17.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_18.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_19.png"),
               pygame.image.load("Sprites/Dog/Timeout/dog_timeout_20.png")]
bear_idle_1 = [pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_1.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_2.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_3.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_4.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_5.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_6.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_7.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_8.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_9.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_10.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_11.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_12.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_13.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_14.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_15.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_16.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_17.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_18.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_19.png"),
               pygame.image.load("Sprites/Bear/Idle 1/bear_idle_1_20.png")]
bear_idle_2 = [pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_1.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_2.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_3.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_4.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_5.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_6.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_7.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_8.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_9.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_10.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_11.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_12.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_13.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_14.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_15.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_16.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_17.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_18.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_19.png"),
               pygame.image.load("Sprites/Bear/Idle 2/bear_idle_2_20.png")]
bear_idle_3 = [pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_1.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_2.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_3.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_4.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_5.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_6.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_7.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_8.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_9.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_10.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_11.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_12.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_13.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_14.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_15.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_16.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_17.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_18.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_19.png"),
               pygame.image.load("Sprites/Bear/Idle 3/bear_idle_3_20.png")]
bear_nice = [pygame.image.load("Sprites/Bear/Nice/bear_nice_1.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_2.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_3.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_4.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_5.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_6.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_7.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_8.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_9.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_10.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_11.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_12.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_13.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_14.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_15.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_16.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_17.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_18.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_19.png"),
             pygame.image.load("Sprites/Bear/Nice/bear_nice_20.png")]
bear_miss = [pygame.image.load("Sprites/Bear/Miss/bear_miss_1.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_2.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_3.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_4.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_5.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_6.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_7.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_8.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_9.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_10.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_11.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_12.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_13.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_14.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_15.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_16.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_17.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_18.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_19.png"),
             pygame.image.load("Sprites/Bear/Miss/bear_miss_20.png")]
bear_timeout = [pygame.image.load("Sprites/Bear/Timeout/bear_timeout_1.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_2.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_3.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_4.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_5.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_6.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_7.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_8.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_9.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_10.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_11.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_12.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_13.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_14.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_15.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_16.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_17.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_18.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_19.png"),
                pygame.image.load("Sprites/Bear/Timeout/bear_timeout_20.png")]
duck_idle_1 = [pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_1.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_2.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_3.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_4.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_5.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_6.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_7.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_8.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_9.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_10.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_11.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_12.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_13.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_14.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_15.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_16.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_17.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_18.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_19.png"),
               pygame.image.load("Sprites/Duck/Idle 1/duck_idle_1_20.png")]
duck_idle_2 = [pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_1.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_2.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_3.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_4.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_5.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_6.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_7.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_8.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_9.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_10.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_11.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_12.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_13.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_14.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_15.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_16.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_17.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_18.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_19.png"),
               pygame.image.load("Sprites/Duck/Idle 2/duck_idle_2_20.png")]
duck_nice = [pygame.image.load("Sprites/Duck/Nice/duck_nice_1.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_2.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_3.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_4.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_5.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_6.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_7.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_8.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_9.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_10.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_11.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_12.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_13.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_14.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_15.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_16.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_17.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_18.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_19.png"),
             pygame.image.load("Sprites/Duck/Nice/duck_nice_20.png")]
duck_miss = [pygame.image.load("Sprites/Duck/Miss/duck_miss_1.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_2.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_3.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_4.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_5.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_6.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_7.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_8.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_9.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_10.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_11.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_12.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_13.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_14.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_15.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_16.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_17.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_18.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_19.png"),
             pygame.image.load("Sprites/Duck/Miss/duck_miss_20.png")]
duck_timeout = [pygame.image.load("Sprites/Duck/Timeout/duck_timeout_1.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_2.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_3.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_4.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_5.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_6.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_7.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_8.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_9.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_10.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_11.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_12.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_13.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_14.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_15.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_16.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_17.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_18.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_19.png"),
                pygame.image.load("Sprites/Duck/Timeout/duck_timeout_20.png")]

#CM 5/8/24-5/16/24 - Menu class
class Menu(object):
    def __init__(self):
        self.screen = " "


#CM 5/14/24-7/23/24 - Button class for menu buttons
class Button(object):
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
        self.sprite_rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        self.highlight = False

    #CM 7/4/24 - draw method
    def draw(self):
        window.blit(self.sprite, (self.x, self.y))
        if self.sprite_rect.collidepoint(pygame.mouse.get_pos()):
            window.blit(buttons_hover[buttons.index(self.sprite)], (self.x, self.y))

    #CM 7/4/24 - click method
    def click(self, destination):
        if self.sprite_rect.collidepoint(pygame.mouse.get_pos()):
            menu.screen = destination
            return True

    #CM 7/20/24-7/23/24 - select_draw method for selection buttons
    def select_draw(self, sprite_list, range_lower, range_upper, button_select_index):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if self.sprite_rect.collidepoint(pygame.mouse.get_pos()):
                    for bound_index in range(range_lower, range_upper):
                        sprite_list[bound_index].highlight = False
                    self.highlight = True

        if self.highlight == True:
            window.blit(button_select[button_select_index], (self.x, self.y))

    #CM 7/22/24 - select_click method for selection button clicking
    def select_click(self, variable, value, target_object):
        if self.highlight == True:
            if target_object == "all":
                setattr(player, variable, value)
                setattr(player2, variable, value)
                setattr(cpu, variable, value)
            else:
                setattr(target_object, variable, value)


#CM 6/7/24 - GameCountdown class for countdown before a match
class GameCountdown(object):
    def __init__(self):
        self.three = time.time() + 1
        self.two = time.time() + 2
        self.one = time.time() + 3
        self.go = time.time() + 4
        self.stop = time.time() + 5
        self.ready = False

    def draw(self):
        if time.time() < self.three:
            window.blit(game_countdown_sprites[0], (window_width // 2 - game_countdown_sprites[0].get_width() // 2,
                                                    window_height // 2 - game_countdown_sprites[0].get_height() // 2))
        if self.three < time.time() < self.two < self.one:
            window.blit(game_countdown_sprites[1], (window_width // 2 - game_countdown_sprites[1].get_width() // 2,
                                                    window_height // 2 - game_countdown_sprites[1].get_height() // 2))
        if self.two < time.time() < self.one < self.go:
            window.blit(game_countdown_sprites[2], (window_width // 2 - game_countdown_sprites[2].get_width() // 2,
                                                    window_height // 2 - game_countdown_sprites[2].get_height() // 2))
        if self.one < time.time() < self.go < self.stop:
            window.blit(game_countdown_sprites[3], (window_width // 2 - game_countdown_sprites[3].get_width() // 2,
                                                    window_height // 2 - game_countdown_sprites[3].get_height() // 2))
        if time.time() > self.go:
            self.ready = True


#CM 5/7/24-7/23/24 - Player class
class Player(object):
    def __init__(self, player_num, online):
        self.player_num = player_num
        self.online = online
        self.spin_order = 0
        self.score = 0
        self.spin = 0
        self.i = 0
        self.rounds_of_qtes = 8
        self.letters_per_qte = 3
        self.seconds_per_qte = 5
        self.order_timer = time.time() + self.seconds_per_qte
        self.miss_timer = time.time() + 0.8
        self.timeout_timer = time.time() + 0.8
        self.nice_timer = time.time() + 0.5
        self.wait = False
        self.miss = False
        self.nice = False
        self.timeout = False
        self.drawing_words = False
        self.animal = "cat"
        self.skin_number = 0
        self.pressed = [False, False, False, False, False, False]
        self.qte_order = [" ", " ", " ", " ", " ", " "]
        if self.player_num == 1:
            self.qte_range = ["q", "w", "e", "a", "s", "d"]
        if self.player_num == 2:
            self.qte_range = ["u", "i", "o", "j", "k", "l"]
        if self.animal == "cat":
            self.idle_1_sprite = cat_idle_1[self.skin_number]
            self.idle_2_sprite = cat_idle_2[self.skin_number]
            self.nice_sprite = cat_nice[self.skin_number]
            self.miss_sprite = cat_miss[self.skin_number]
            self.timeout_sprite = cat_timeout[self.skin_number]
        elif self.animal == "dog":
            self.idle_1_sprite = dog_idle_1[self.skin_number]
            self.idle_2_sprite = dog_idle_2[self.skin_number]
            self.nice_sprite = dog_nice[self.skin_number]
            self.miss_sprite = dog_miss[self.skin_number]
            self.timeout_sprite = dog_timeout[self.skin_number]
        elif self.animal == "bear":
            self.idle_1_sprite = bear_idle_1[self.skin_number]
            self.idle_2_sprite = bear_idle_2[self.skin_number]
            self.idle_3_sprite = bear_idle_3[self.skin_number]
            self.nice_sprite = bear_nice[self.skin_number]
            self.miss_sprite = bear_miss[self.skin_number]
            self.timeout_sprite = bear_timeout[self.skin_number]
        elif self.animal == "duck":
            self.idle_1_sprite = duck_idle_1[self.skin_number]
            self.idle_2_sprite = duck_idle_2[self.skin_number]
            self.nice_sprite = duck_nice[self.skin_number]
            self.miss_sprite = duck_miss[self.skin_number]
            self.timeout_sprite = duck_timeout[self.skin_number]

    #CM 7/23/24 - this method sets sprites for skin selection
    def set_sprites(self):
        if self.animal == "cat":
            self.idle_1_sprite = cat_idle_1[self.skin_number]
            self.idle_2_sprite = cat_idle_2[self.skin_number]
            self.nice_sprite = cat_nice[self.skin_number]
            self.miss_sprite = cat_miss[self.skin_number]
            self.timeout_sprite = cat_timeout[self.skin_number]
        elif self.animal == "dog":
            self.idle_1_sprite = dog_idle_1[self.skin_number]
            self.idle_2_sprite = dog_idle_2[self.skin_number]
            self.nice_sprite = dog_nice[self.skin_number]
            self.miss_sprite = dog_miss[self.skin_number]
            self.timeout_sprite = dog_timeout[self.skin_number]
        elif self.animal == "bear":
            self.idle_1_sprite = bear_idle_1[self.skin_number]
            self.idle_2_sprite = bear_idle_2[self.skin_number]
            self.idle_3_sprite = bear_idle_3[self.skin_number]
            self.nice_sprite = bear_nice[self.skin_number]
            self.miss_sprite = bear_miss[self.skin_number]
            self.timeout_sprite = bear_timeout[self.skin_number]
        elif self.animal == "duck":
            self.idle_1_sprite = duck_idle_1[self.skin_number]
            self.idle_2_sprite = duck_idle_2[self.skin_number]
            self.nice_sprite = duck_nice[self.skin_number]
            self.miss_sprite = duck_miss[self.skin_number]
            self.timeout_sprite = duck_timeout[self.skin_number]

    #CM 5/8/24-7/22/24 - this method is used to execute the qte_sequence that is the main source of gameplay
    def qte_sequence(self):
        #CM 5/7/24-7/22/24 - randomize QTE sequence; variable wait acts as a checkpoint throughout the program
        #                    to ensure there is no overflow in QTE generation
        if self.wait == False:
            self.order_timer = time.time() + self.seconds_per_qte
            self.wait = True
            for self.spin in range(0, self.letters_per_qte):
                self.i = randint(0, 5)
                self.qte_order[self.spin] = self.qte_range[self.i]
            for i in range(0, 6):
                self.pressed[i] = False

        #CM 5/7/24 - take in QTE inputs
        keys = pygame.key.get_pressed()
        #CM 5/27/24-7/7/24 - if no text drawings are on screen
        if self.drawing_words == False:
            #CM 5/7/24-7/11/24 - if time hasn't run out and no qte status is true and program is waiting for next
            #                    qte sequence
            if (time.time() <= self.order_timer and self.miss == False and self.nice == False and self.timeout == False
                    and self.wait == True):
                #CM 5/19/24-7/7/24 - if key is entered that is equivalent to the expected qte_order input
                for e in events:
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.key.key_code(self.qte_order[self.spin_order]):
                            self.wait = True
                            self.pressed[self.spin_order] = True
                            self.spin_order += 1
                        #CM 5/19/24-7/22/24 - if key is entered inappropriately, reset QTE
                        elif (((keys[pygame.key.key_code("q")] and self.qte_order[self.spin_order] != "q" or
                                keys[pygame.key.key_code("w")] and self.qte_order[self.spin_order] != "w" or
                                keys[pygame.key.key_code("e")] and self.qte_order[self.spin_order] != "e" or
                                keys[pygame.key.key_code("a")] and self.qte_order[self.spin_order] != "a" or
                                keys[pygame.key.key_code("s")] and self.qte_order[self.spin_order] != "s" or
                                keys[pygame.key.key_code("d")] and self.qte_order[self.spin_order] != "d") and
                               self.player_num == 1) or
                              (keys[pygame.key.key_code("u")] and self.qte_order[self.spin_order] != "u" or
                               keys[pygame.key.key_code("i")] and self.qte_order[self.spin_order] != "i" or
                               keys[pygame.key.key_code("o")] and self.qte_order[self.spin_order] != "o" or
                               keys[pygame.key.key_code("j")] and self.qte_order[self.spin_order] != "j" or
                               keys[pygame.key.key_code("k")] and self.qte_order[self.spin_order] != "k" or
                               keys[pygame.key.key_code("l")] and self.qte_order[self.spin_order] != "l") and
                              self.player_num == 2):
                            self.spin_order = 0
                            self.order_timer = time.time() + self.seconds_per_qte
                            self.miss_timer = time.time() + 0.8
                            self.miss = True
                            for i in range(0, 6):
                                self.pressed[i] = False
                            if self.score > 0:
                                self.score -= 1
            #CM 5/8/24-7/22/24 - if timeout, reset QTE
            else:
                self.spin_order = 0
                self.order_timer = time.time() + self.seconds_per_qte
                self.timeout_timer = time.time() + 0.8
                self.timeout = True
                for i in range(0, 6):
                    self.pressed[i] = False
                if self.score > 0:
                    self.score -= 1

            #CM 5/8/24-7/22/24 - if all letters entered, reset simulation
            if self.spin_order == self.letters_per_qte:
                self.spin_order = 0
                self.score += 1
                self.order_timer = time.time() + self.seconds_per_qte
                self.nice_timer = time.time() + 0.5
                self.nice = True

            #CM 5/16/24-7/22/24 - if player wins, go to win screen
            if self.score == self.rounds_of_qtes:
                menu.screen = "player_win"
                self.score = 0
                self.wait = False
                self.miss = False
                self.nice = False
                self.timeout = False
                self.drawing_words = False
                for i in range(0, 6):
                    self.pressed[i] = False

        #CM 6/29/24-7/2/24 - if in online match, send score to server to be sent to other player(s)
        if self.online == True:
            client_socket.send((str(self.score)).encode("utf-8"))

    #CM 5/9/24-6/6/24 - draw score and player movement
    def draw(self):
        #CM 5/9/24-6/6/24 - draw score
        font = pygame.font.Font("SODA.TTF", 30)
        text = font.render("Score: " + str(self.score), 1, (255, 0, 0))
        if self.player_num == 1:
            window.blit(text, (50, 10))
        if self.player_num == 2:
            window.blit(text, (1000, 10))

        #CM 5/9/24-7/25/24 - player movement
        if self.player_num == 1:
            if self.nice == True:
                window.blit(self.nice_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
            elif self.miss == True:
                if self.animal == "duck":  # if duck, custom miss animation
                    if frame_counter <= 15:
                        window.blit(self.miss_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
                    elif frame_counter <= 30:
                        window.blit(pygame.transform.flip(self.miss_sprite, True, False),
                                    (self.score * (410 // self.rounds_of_qtes), 400))
                    elif frame_counter <= 45:
                        window.blit(self.miss_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
                    else:
                        window.blit(pygame.transform.flip(self.miss_sprite, True, False),
                                    (self.score * (410 // self.rounds_of_qtes), 400))
                else:
                    window.blit(self.miss_sprite, (self.score * (410 // self.rounds_of_qtes), 400))  # regular miss
            elif self.timeout == True:
                window.blit(self.timeout_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
            else:
                if self.animal == "bear":  # if bear, custom idle animation
                    if frame_counter <= 15:
                        window.blit(self.idle_1_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
                    elif frame_counter <= 30:
                        window.blit(self.idle_2_sprite, (3 + self.score * (410 // self.rounds_of_qtes), 400))
                    elif frame_counter <= 45:
                        window.blit(self.idle_1_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
                    else:
                        window.blit(self.idle_3_sprite, (-3 + self.score * (410 // self.rounds_of_qtes), 400))
                else:  # regular idle
                    if frame_counter <= 30:
                        window.blit(self.idle_1_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
                    else:
                        window.blit(self.idle_2_sprite, (self.score * (410 // self.rounds_of_qtes), 400))
        if self.player_num == 2:
            if self.nice == True:
                window.blit(pygame.transform.flip(self.nice_sprite, True, False),
                            ((window_width - self.idle_1_sprite.get_width()) -
                             (self.score * (410 // self.rounds_of_qtes)), 400))
            elif self.miss == True:
                if self.animal == "duck":  # if duck, custom miss animation
                    if frame_counter <= 15:
                        window.blit(pygame.transform.flip(self.miss_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    elif frame_counter <= 30:
                        window.blit(self.miss_sprite,
                                    ((window_width - self.idle_1_sprite.get_width()) - 3 -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    elif frame_counter <= 45:
                        window.blit(pygame.transform.flip(self.miss_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    else:
                        window.blit(self.miss_sprite, ((window_width - self.idle_1_sprite.get_width()) - 3 -
                                                       (self.score * (410 // self.rounds_of_qtes)), 400))
                else:
                    window.blit(pygame.transform.flip(self.miss_sprite, True, False),  # regular miss
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
            elif self.timeout == True:
                window.blit(pygame.transform.flip(self.timeout_sprite, True, False),
                            ((window_width - self.idle_1_sprite.get_width()) -
                             (self.score * (410 // self.rounds_of_qtes)), 400))
            else:
                if self.animal == "bear":  # if bear, custom idle animation
                    if frame_counter <= 15:
                        window.blit(pygame.transform.flip(self.idle_1_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    elif frame_counter <= 30:
                        window.blit(pygame.transform.flip(self.idle_2_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) - 3 -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    elif frame_counter <= 45:
                        window.blit(pygame.transform.flip(self.idle_1_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    else:
                        window.blit(pygame.transform.flip(self.idle_3_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) + 3 -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                else:  # regular idle
                    if frame_counter <= 30:
                        window.blit(pygame.transform.flip(self.idle_1_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))
                    else:
                        window.blit(pygame.transform.flip(self.idle_2_sprite, True, False),
                                    ((window_width - self.idle_1_sprite.get_width()) -
                                     (self.score * (410 // self.rounds_of_qtes)), 400))

    #CM 5/9/24-7/22/24 - draw qte keys
    def qte_draw(self):
        #CM 5/19/24-7/22/24 - display key sprite to screen when key order is formed from the method qte_sequence()
        #CM 5/19/24-7/22/24 - if simulation is ready, spin and display keys based on if the right key has been pressed
        if self.qte_order[self.spin] != " ":
            for self.spin in range(0, self.letters_per_qte):
                #CM 5/19/24 - pairs the letter in qte_order with its qte_range letter
                i = self.qte_range.index(self.qte_order[self.spin])
                #CM 5/19/24-7/22/24 - if key is not pressed
                if self.pressed[self.spin] == False:
                    if self.player_num == 1:
                        window.blit(key[i], ((window_width // 4 - key[i].get_width() // 2) + (self.spin * 104) -
                                             (key[i].get_width() * self.letters_per_qte // 2) +
                                             (key[i].get_width() // 2) - 20, 100))
                    if self.player_num == 2:
                        window.blit(key2[i], ((window_width * 0.75 - key2[i].get_width() // 2) + (self.spin * 104) -
                                              (key2[i].get_width() * self.letters_per_qte // 2) +
                                              (key2[i].get_width() // 2) - 4, 100))
                #CM 5/19/24-7/22/24 - if key is pressed
                else:
                    if self.player_num == 1:
                        window.blit(key_pressed[i], ((window_width // 4 - key_pressed[i].get_width() // 2) +
                                                     (self.spin * 104) - (key_pressed[i].get_width() *
                                                     self.letters_per_qte // 2) + (key[i].get_width() // 2) - 20, 100))
                    if self.player_num == 2:
                        window.blit(key_pressed2[i], ((window_width * 0.75 - key_pressed2[i].get_width() // 2) +
                                                      (self.spin * 104) - (key_pressed2[i].get_width() *
                                                      self.letters_per_qte // 2) + (key2[i].get_width() // 2) - 4, 100))

            #CM 5/20/24-6/6/24 - if key is missed
            if self.miss == True:
                if time.time() <= self.miss_timer:
                    font = pygame.font.Font("SODA.TTF", 50)
                    text = font.render("MISS!", 1, (255, 0, 0))  # TODO: or "SLOPPY!", "SAD", "NOT QUITE!"
                    if self.player_num == 1:
                        window.blit(text, (300, 300))
                    if self.player_num == 2:
                        window.blit(text, (window_width - 300, 300))
                    self.drawing_words = True
                else:
                    self.wait = False
                    self.miss = False
                    self.drawing_words = False

            #CM 5/20/24-6/6/24 - if a single qte sequence is cleared
            if self.nice == True:
                if time.time() <= self.nice_timer:
                    font = pygame.font.Font("SODA.TTF", 50)
                    text = font.render("NICE!", 1, (0, 0, 255))  # TODO: or "COOL!", "GREAT"
                    if self.player_num == 1:
                        window.blit(text, (300, 300))
                    if self.player_num == 2:
                        window.blit(text, (window_width - 300, 300))
                    self.drawing_words = True
                else:
                    self.wait = False
                    self.nice = False
                    self.drawing_words = False

            #CM 5/20/24-7/11/24 - if time runs out
            if self.timeout == True:
                if time.time() <= self.timeout_timer:
                    font = pygame.font.Font("SODA.TTF", 50)
                    text = font.render("TOO LATE!", 1, (0, 255, 0))  # TODO: or "SLOW!", "FAIL!"
                    if self.player_num == 1:
                        window.blit(text, (300, 300))
                    if self.player_num == 2:
                        window.blit(text, (window_width - 300, 300))
                    self.drawing_words = True
                else:
                    self.wait = False
                    self.timeout = False
                    self.drawing_words = False

    #CM 7/22/24 - reset player mathematics (not cosmetics) after a match
    def reset(self):
        self.spin_order = 0
        self.score = 0
        self.spin = 0
        self.i = 0
        self.order_timer = time.time() + self.seconds_per_qte
        self.miss_timer = time.time() + 0.8
        self.timeout_timer = time.time() + 0.8
        self.nice_timer = time.time() + 0.5
        self.wait = False
        self.miss = False
        self.nice = False
        self.timeout = False
        self.drawing_words = False
        self.pressed = [False, False, False, False, False, False]
        self.qte_order = [" ", " ", " ", " ", " ", " "]
        if self.player_num == 1:
            self.qte_range = ["q", "w", "e", "a", "s", "d"]
        if self.player_num == 2:
            self.qte_range = ["u", "i", "o", "j", "k", "l"]


#CM 5/24/24-7/25/24 - CPU class (all elements modified from Player class)
class CPU(object):
    def __init__(self):
        self.spin_order = 0
        self.score = 0
        self.spin = 0
        self.i = 0
        self.cpu_chance = 90
        self.rounds_of_qtes = 8
        self.letters_per_qte = 3
        self.seconds_per_qte = 5
        self.order_timer = time.time() + self.seconds_per_qte
        self.miss_timer = time.time() + 0.8
        self.timeout_timer = time.time() + 0.8
        self.nice_timer = time.time() + 0.5
        self.input_timer = (time.time() + self.seconds_per_qte / self.letters_per_qte - (self.seconds_per_qte * 0.02) +
                            (randint(-5, 5) * 0.01))
        self.wait = False
        self.miss = False
        self.nice = False
        self.timeout = False
        self.drawing_words = False
        self.animal = "cat"
        self.skin_number = 0
        self.pressed = [False, False, False, False, False, False]
        self.cpu_qte_range = ["q", "w", "e", "a", "s", "d"]
        self.cpu_qte_order = [" ", " ", " ", " ", " ", " "]
        if self.animal == "cat":
            self.idle_1_sprite = cat_idle_1[self.skin_number]
            self.idle_2_sprite = cat_idle_2[self.skin_number]
            self.nice_sprite = cat_nice[self.skin_number]
            self.miss_sprite = cat_miss[self.skin_number]
            self.timeout_sprite = cat_timeout[self.skin_number]
        elif self.animal == "dog":
            self.idle_1_sprite = dog_idle_1[self.skin_number]
            self.idle_2_sprite = dog_idle_2[self.skin_number]
            self.nice_sprite = dog_nice[self.skin_number]
            self.miss_sprite = dog_miss[self.skin_number]
            self.timeout_sprite = dog_timeout[self.skin_number]
        elif self.animal == "bear":
            self.idle_1_sprite = bear_idle_1[self.skin_number]
            self.idle_2_sprite = bear_idle_2[self.skin_number]
            self.idle_3_sprite = bear_idle_3[self.skin_number]
            self.nice_sprite = bear_nice[self.skin_number]
            self.miss_sprite = bear_miss[self.skin_number]
            self.timeout_sprite = bear_timeout[self.skin_number]
        elif self.animal == "duck":
            self.idle_1_sprite = duck_idle_1[self.skin_number]
            self.idle_2_sprite = duck_idle_2[self.skin_number]
            self.nice_sprite = duck_nice[self.skin_number]
            self.miss_sprite = duck_miss[self.skin_number]
            self.timeout_sprite = duck_timeout[self.skin_number]

    #CM 7/25/24 - this method sets sprites for skin selection
    def set_sprites(self):
        if self.animal == "cat":
            self.idle_1_sprite = cat_idle_1[self.skin_number]
            self.idle_2_sprite = cat_idle_2[self.skin_number]
            self.nice_sprite = cat_nice[self.skin_number]
            self.miss_sprite = cat_miss[self.skin_number]
            self.timeout_sprite = cat_timeout[self.skin_number]
        elif self.animal == "dog":
            self.idle_1_sprite = dog_idle_1[self.skin_number]
            self.idle_2_sprite = dog_idle_2[self.skin_number]
            self.nice_sprite = dog_nice[self.skin_number]
            self.miss_sprite = dog_miss[self.skin_number]
            self.timeout_sprite = dog_timeout[self.skin_number]
        elif self.animal == "bear":
            self.idle_1_sprite = bear_idle_1[self.skin_number]
            self.idle_2_sprite = bear_idle_2[self.skin_number]
            self.idle_3_sprite = bear_idle_3[self.skin_number]
            self.nice_sprite = bear_nice[self.skin_number]
            self.miss_sprite = bear_miss[self.skin_number]
            self.timeout_sprite = bear_timeout[self.skin_number]
        elif self.animal == "duck":
            self.idle_1_sprite = duck_idle_1[self.skin_number]
            self.idle_2_sprite = duck_idle_2[self.skin_number]
            self.nice_sprite = duck_nice[self.skin_number]
            self.miss_sprite = duck_miss[self.skin_number]
            self.timeout_sprite = duck_timeout[self.skin_number]

    def play(self):
        #CM 5/7/24-7/22/24 - randomize QTE sequence; variable wait acts as a checkpoint throughout the program
        #                    to ensure there is no overflow in QTE generation
        if self.wait == False:
            self.order_timer = time.time() + self.seconds_per_qte
            self.wait = True
            for self.spin in range(0, self.letters_per_qte):
                self.i = randint(0, 5)
                self.cpu_qte_order[self.spin] = self.cpu_qte_range[self.i]
            for i in range(0, 6):
                self.pressed[i] = False

        #CM 5/27/24-5/28/24 - if no text drawings are on screen and enough time has passed after last qte "input"
        if self.drawing_words == False and time.time() >= self.input_timer:
            #CM 5/7/24-7/11/24 - if time hasn't run out and no qte status is true and program is waiting for next
            #                    qte sequence
            if (time.time() <= self.order_timer and self.miss == False and self.nice == False and self.timeout == False
                    and self.wait == True):
                #CM 5/19/24-5/29/24 - if CPU hits a random chance depending on its level, it gets a correct letter
                if randint(1, 100) <= self.cpu_chance:
                    self.input_timer = (time.time() + self.seconds_per_qte / self.letters_per_qte -
                                        (self.seconds_per_qte * 0.02) + (randint(-5, 5) * 0.01))
                    self.wait = True
                    self.pressed[self.spin_order] = True
                    self.spin_order += 1
                #CM 5/19/24-5/28/24 - if CPU misses the chance, reset QTE
                else:
                    self.spin_order = 0
                    self.order_timer = time.time() + self.seconds_per_qte
                    self.miss_timer = time.time() + 0.8
                    self.miss = True
                    for i in range(0, 6):
                        self.pressed[i] = False
                    if self.score > 0:
                        self.score -= 1
            #CM 5/8/24-7/11/24 - if timeout, reset QTE
            else:
                self.spin_order = 0
                self.order_timer = time.time() + self.seconds_per_qte
                self.timeout_timer = time.time() + 0.8
                self.timeout = True
                for i in range(0, 6):
                    self.pressed[i] = False
                if self.score > 0:
                    self.score -= 1

            #CM 5/8/24-7/22/24 - if all chances hit, reset simulation
            if self.spin_order == self.letters_per_qte:
                self.spin_order = 0
                self.score += 1
                self.order_timer = time.time() + self.seconds_per_qte
                self.nice_timer = time.time() + 0.5
                self.nice = True

            #CM 5/16/24-7/22/24 - if CPU wins, go to win screen
            if self.score == self.rounds_of_qtes:
                menu.screen = "cpu_win"
                self.score = 0
                self.wait = False
                self.miss = False
                self.nice = False
                self.timeout = False
                self.drawing_words = False
                for i in range(0, 6):
                    self.pressed[i] = False

    #CM 5/24/24-7/25/24 - this method draws CPU movement
    def draw(self):
        if self.nice == True:
            window.blit(pygame.transform.flip(self.nice_sprite, True, False),
                        ((window_width - self.idle_1_sprite.get_width()) -
                         (self.score * (410 // self.rounds_of_qtes)), 400))
        elif self.miss == True:
            if self.animal == "duck":  # if duck, custom miss animation
                if frame_counter <= 15:
                    window.blit(pygame.transform.flip(self.miss_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                elif frame_counter <= 30:
                    window.blit(self.miss_sprite,
                                ((window_width - self.idle_1_sprite.get_width()) - 3 -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                elif frame_counter <= 45:
                    window.blit(pygame.transform.flip(self.miss_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                else:
                    window.blit(self.miss_sprite, ((window_width - self.idle_1_sprite.get_width()) - 3 -
                                                   (self.score * (410 // self.rounds_of_qtes)), 400))
            else:
                window.blit(pygame.transform.flip(self.miss_sprite, True, False),  # regular miss
                            ((window_width - self.idle_1_sprite.get_width()) -
                             (self.score * (410 // self.rounds_of_qtes)), 400))
        elif self.timeout == True:
            window.blit(pygame.transform.flip(self.timeout_sprite, True, False),
                        ((window_width - self.idle_1_sprite.get_width()) -
                         (self.score * (410 // self.rounds_of_qtes)), 400))
        else:
            if self.animal == "bear":  # if bear, custom idle animation
                if frame_counter <= 15:
                    window.blit(pygame.transform.flip(self.idle_1_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                elif frame_counter <= 30:
                    window.blit(pygame.transform.flip(self.idle_2_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) - 3 -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                elif frame_counter <= 45:
                    window.blit(pygame.transform.flip(self.idle_1_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                else:
                    window.blit(pygame.transform.flip(self.idle_3_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) + 3 -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
            else:  # regular idle
                if frame_counter <= 30:
                    window.blit(pygame.transform.flip(self.idle_1_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))
                else:
                    window.blit(pygame.transform.flip(self.idle_2_sprite, True, False),
                                ((window_width - self.idle_1_sprite.get_width()) -
                                 (self.score * (410 // self.rounds_of_qtes)), 400))

    #CM 5/24/24-6/7/24 - this method draws CPU QTE keys
    def qte_draw(self):
        #CM 5/19/24-7/22/24 - if simulation is ready, spin and display keys based on if the right key has been pressed
        if self.cpu_qte_order[self.spin] != " ":
            for self.spin in range(0, self.letters_per_qte):
                #CM 5/19/24 - pairs the letter in cpu_qte_order with its qte_range letter
                i = self.cpu_qte_range.index(self.cpu_qte_order[self.spin])
                # CM 5/19/24-7/22/24 - if key is not pressed
                if self.pressed[self.spin] == False:
                    window.blit(key[i], ((window_width * 0.75 - key[i].get_width() // 2) + (self.spin * 104) -
                                         (key[i].get_width() * self.letters_per_qte // 2) + (key[i].get_width() // 2) -
                                         4, 100))
                # CM 5/19/24-7/22/24 - if key is pressed
                else:
                    window.blit(key_pressed[i], ((window_width * 0.75 - key_pressed[i].get_width() // 2) +
                                                 (self.spin * 104) - (key_pressed[i].get_width() *
                                                 self.letters_per_qte // 2) + (key[i].get_width() // 2) - 4, 100))

            #CM 5/20/24-7/11/24 - if key is missed
            if self.miss == True:
                if time.time() <= self.miss_timer:
                    font = pygame.font.Font("SODA.TTF", 50)
                    text = font.render("MISS!", 1, (255, 0, 0))  # TODO: or "SLOPPY!", "SAD", "NOT QUITE!"
                    window.blit(text, (window_width - 300, 300))
                    self.drawing_words = True
                else:
                    self.wait = False
                    self.miss = False
                    self.drawing_words = False

            #CM 5/20/24-5/28/24 - if a single qte sequence is cleared
            if self.nice == True:
                if time.time() <= self.nice_timer:
                    font = pygame.font.Font("SODA.TTF", 50)
                    text = font.render("NICE!", 1, (0, 0, 255))  # TODO: or "COOL!", "GREAT"
                    window.blit(text, (window_width - 300, 300))
                    self.drawing_words = True
                else:
                    self.wait = False
                    self.nice = False
                    self.drawing_words = False

            #CM 5/20/24-7/11/24 - if time runs out
            if self.timeout == True:
                if time.time() <= self.timeout_timer:
                    font = pygame.font.Font("SODA.TTF", 50)
                    text = font.render("TOO LATE!", 1, (0, 255, 0))  # TODO: or "SLOW!", "FAIL!"
                    window.blit(text, (window_width - 300, 300))
                    self.drawing_words = True
                else:
                    self.wait = False
                    self.timeout = False
                    self.drawing_words = False

    #CM 7/22/24 - reset CPU mathematics (not cosmetics) after a match
    def reset(self):
        self.spin_order = 0
        self.score = 0
        self.spin = 0
        self.i = 0
        self.cpu_level = 5  # Designed to be between 1 and 10 (inclusive)
        self.cpu_chance = 85 + (self.cpu_level * 1)
        self.order_timer = time.time() + self.seconds_per_qte
        self.miss_timer = time.time() + 0.8
        self.timeout_timer = time.time() + 0.8
        self.nice_timer = time.time() + 0.5
        self.input_timer = time.time() + ((((self.cpu_level * -1) + 10) * 0.12) + (randint(-5, 5) * 0.01))
        self.wait = False
        self.miss = False
        self.nice = False
        self.timeout = False
        self.drawing_words = False
        self.pressed = [False, False, False, False, False, False]
        self.cpu_qte_range = ["q", "w", "e", "a", "s", "d"]
        self.cpu_qte_order = [" ", " ", " ", " ", " ", " "]


#CM 6/29/24-7/2/24 - OnlinePlayer class
class OnlinePlayer(object):
    def __init__(self):
        self.online_player_score = 0

    #CM 6/29/24 - receive score from server
    def receive_score(self):
        self.online_player_score = int(client_socket.recv(8).decode("utf-8"))

    #CM 6/29/24-7/2/24 - draw online player
    def draw(self):
        window.blit(player_sprite, ((window_width - 10 - player_sprite.get_width())
                                    - (self.online_player_score * 20), 300))


#CM 7/17/24 - define bg_scroll and its variable to scroll a screen-sized image across the screen to the left
bg_scroll_speed = 0
def bg_scroll(background):
    global bg_scroll_speed
    window.blit(background, (0 - bg_scroll_speed, 0))
    window.blit(background, (1280 - bg_scroll_speed, 0))
    bg_scroll_speed += 0.5
    if bg_scroll_speed >= 1280:
        bg_scroll_speed = 0

    '''global scroll
    global tiles
    i = 0
    if i < tiles:
        window.blit(background, (background.get_width() * i + scroll, 0))
        i += 0
    # FRAME FOR SCROLLING
    scroll -= 6

    # RESET THE SCROLL FRAME
    if abs(scroll) > background.get_width():
        scroll = 0'''


#CM 5/7/24-7/30/24 - define redraw_game_window to redraw (update) game window
def redraw_game_window():
    #CM 5/16/24 - keys for menu navigation
    keys = pygame.key.get_pressed()

    #CM 5/9/24-5/14/24 - title screen events
    if menu.screen == "title":
        bg_scroll(checkerboard_bg)

        #CM 5/14/24-7/4/24 - draw title screen buttons
        online_play_button.draw()
        offline_play_button.draw()

    #CM 6/13/24-7/18/24 - online_play menu events (code modified from offline_play menu events below)
    if menu.screen == "online_play":
        #CM 7/18/2024 - scroll checkerboard_bg_green
        bg_scroll(checkerboard_bg_green)

        #CM 7/30/24 - draw buttons
        P1_vs_P2_button.draw()
        p1_skin_button.draw()
        window.blit(pygame.transform.scale_by(online_player.idle_1_sprite, 0.3), (p1_skin_button.x + 45,
                                                                           p1_skin_button.y + 65))

        #CM 7/18/2024 - back_button draw
        back_button.draw()

    #CM 7/30/24 - server_mode_select events
    if menu.screen == "server_mode_select":
        bg_scroll(checkerboard_bg_green)

        #CM 7/30/24 - button draw
        be_server_host_button.draw()
        be_server_guest_button.draw()

        #CM 7/30/24 - back_button draw
        back_button.draw()

    #CM 7/30/24 - online_p1_skin_select menu events (code modified from p1_skin_select events below)
    if menu.screen == "online_p1_skin_select":
        bg_scroll(checkerboard_bg_dark_blue)
        online_player.set_sprites()

        # CM 7/23/24 - draw stage + online_player character with idle animation + spotlight
        window.blit(skin_select_stage, (0, 0))
        if online_player.animal == "bear":
            if frame_counter <= 15:
                window.blit(pygame.transform.scale_by(online_player.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            elif frame_counter <= 30:
                window.blit(pygame.transform.scale_by(online_player.idle_2_sprite, 2), (window_width // 2 - 315 + 6, 10))
            elif frame_counter <= 45:
                window.blit(pygame.transform.scale_by(online_player.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(online_player.idle_3_sprite, 2), (window_width // 2 - 315 - 6, 10))
        else:
            if frame_counter <= 30:
                window.blit(pygame.transform.scale_by(online_player.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(online_player.idle_2_sprite, 2), (window_width // 2 - 315, 10))
        window.blit(skin_select_spotlight, (0, 0))

        # CM 7/24/24 - set skin selection sprites
        skin_display_list = []
        if online_player.animal == "cat":
            skin_display_list = cat_nice
        elif online_player.animal == "dog":
            skin_display_list = dog_nice
        elif online_player.animal == "bear":
            skin_display_list = bear_nice
        elif online_player.animal == "duck":
            skin_display_list = duck_nice

        # CM 7/22/24-7/24/24 - draw skin buttons, skins, and skin selection
        for i in range(0, 20):
            p1_skin_select_button[i].draw()
        for i in range(0, 5):
            window.blit(pygame.transform.scale_by(skin_display_list[i * 4], 0.3), (80 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 1], 0.3), (190 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 2], 0.3),
                        (window_width - 170 - 110 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 3], 0.3),
                        (window_width - 60 - 110 - 2, 50 + (i * 110)))
        for i in range(0, 20):
            p1_skin_select_button[i].select_draw(p1_skin_select_button, 0, 20, 1)

        # CM 7/23/24 - animal select buttons
        animal_select_left_button.draw()
        animal_select_right_button.draw()

        # CM 7/22/24 - back_button draw
        back_button.draw()

    #CM 6/28/24 - connecting_to_server screen events
    if menu.screen == "connecting_to_server_1v1" or menu.screen == "connecting_to_server_2v2":
        window.blit(connecting_to_server, (0, 0))

    #CM 6/28/24 - searching_for_players screen events
    if menu.screen == "searching_for_players_1v1" or menu.screen == "searching_for_players_2v2":
        window.blit(searching_for_players, (0, 0))

    #CM 6/28/24 - could_not_connect screen events
    if menu.screen == "could_not_connect":
        window.blit(could_not_connect, (0, 0))
        if keys[pygame.K_SPACE]:
            menu.screen = "online_play"

    #CM 6/29/24-7/2/24 - 1p_vs_1p_online game events
    if menu.screen == "1p_vs_1p_online":
        window.blit(stage, (0, 0))
        window.blit(trophy, (window_width // 2 - trophy.get_width() // 2, window_height // 2 - 50))
        online_player.draw()
        online_opponent.draw()
        if game_countdown.ready == False:
            game_countdown.draw()
        else:
            online_player.qte_draw()
            online_opponent.receive_score()

    #CM 5/15/24-7/23/24 - offline_play menu events
    if menu.screen == "offline_play":
        #CM 7/18/24 - scroll checkerboard_bg_red
        bg_scroll(checkerboard_bg_red)

        #CM 7/19/24-7/22/24 - draw game option buttons
        P1_vs_COM_button.draw()
        P1_vs_P2_button.draw()
        match_rules_button.draw()
        p1_skin_button.draw()
        window.blit(pygame.transform.scale_by(player.idle_1_sprite, 0.3), (p1_skin_button.x + 45,
                    p1_skin_button.y + 65))
        p2_skin_button.draw()
        window.blit(pygame.transform.scale_by(player2.idle_1_sprite, 0.3), (p2_skin_button.x + 45,
                    p2_skin_button.y + 65))
        cpu_skin_button.draw()
        window.blit(pygame.transform.scale_by(cpu.idle_1_sprite, 0.3), (cpu_skin_button.x + 45,
                    cpu_skin_button.y + 65))

        #CM 7/18/24 - back_button draw
        back_button.draw()

    #CM 7/19/24-7/23/24 - match_rules menu events
    if menu.screen == "match_rules":
        bg_scroll(checkerboard_bg_tan)

        #CM 7/20/24-7/23/24 - draw UI elements and buttons
        window.blit(ui_elements[0], (80, 65))
        window.blit(ui_elements[1], (80, 245))
        window.blit(ui_elements[2], (80, 425))
        for button in match_rules_button_list:
            button.draw()
        for rounds_of_qtes_option in range(0, 4):
            match_rules_button_list[rounds_of_qtes_option].select_draw(match_rules_button_list,0, 4, 0)
        for letters_per_qte_option in range(4, 8):
            match_rules_button_list[letters_per_qte_option].select_draw(match_rules_button_list, 4, 8, 0)
        for seconds_per_qte_option in range(8, 12):
            match_rules_button_list[seconds_per_qte_option].select_draw(match_rules_button_list, 8, 12, 0)

        #CM 7/19/24 - back_button draw
        back_button.draw()

    #CM 7/23/24-7/28/24 - p1_skin_select menu events
    if menu.screen == "p1_skin_select":
        bg_scroll(checkerboard_bg_dark_blue)
        player.set_sprites()

        #CM 7/23/24 - draw stage + player character with idle animation + spotlight
        window.blit(skin_select_stage, (0, 0))
        if player.animal == "bear":
            if frame_counter <= 15:
                window.blit(pygame.transform.scale_by(player.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            elif frame_counter <= 30:
                window.blit(pygame.transform.scale_by(player.idle_2_sprite, 2), (window_width // 2 - 315 + 6, 10))
            elif frame_counter <= 45:
                window.blit(pygame.transform.scale_by(player.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(player.idle_3_sprite, 2), (window_width // 2 - 315 - 6, 10))
        else:
            if frame_counter <= 30:
                window.blit(pygame.transform.scale_by(player.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(player.idle_2_sprite, 2), (window_width // 2 - 315, 10))
        window.blit(skin_select_spotlight, (0, 0))

        #CM 7/24/24 - set skin selection sprites
        skin_display_list = []
        if player.animal == "cat":
            skin_display_list = cat_nice
        elif player.animal == "dog":
            skin_display_list = dog_nice
        elif player.animal == "bear":
            skin_display_list = bear_nice
        elif player.animal == "duck":
            skin_display_list = duck_nice

        #CM 7/22/24-7/24/24 - draw skin buttons, skins, and skin selection
        for i in range(0, 20):
            p1_skin_select_button[i].draw()
        for i in range(0, 5):
            window.blit(pygame.transform.scale_by(skin_display_list[i * 4], 0.3), (80 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 1], 0.3), (190 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 2], 0.3),
                        (window_width - 170 - 110 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 3], 0.3),
                        (window_width - 60 - 110 - 2, 50 + (i * 110)))
        for i in range(0, 20):
            p1_skin_select_button[i].select_draw(p1_skin_select_button, 0, 20, 1)

        #CM 7/23/24 - animal select buttons
        animal_select_left_button.draw()
        animal_select_right_button.draw()

        #CM 7/22/24 - back_button draw
        back_button.draw()

    #CM 7/24/24-7/28/24 - p2_skin_select menu events (code modified from p1_skin_select menu events above)
    if menu.screen == "p2_skin_select":
        bg_scroll(checkerboard_bg_dark_blue)
        player2.set_sprites()

        #CM 7/23/24 - draw stage + player character with idle animation + spotlight
        window.blit(skin_select_stage, (0, 0))
        if player2.animal == "bear":
            if frame_counter <= 15:
                window.blit(pygame.transform.scale_by(player2.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            elif frame_counter <= 30:
                window.blit(pygame.transform.scale_by(player2.idle_2_sprite, 2), (window_width // 2 - 315 + 6, 10))
            elif frame_counter <= 45:
                window.blit(pygame.transform.scale_by(player2.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(player2.idle_3_sprite, 2), (window_width // 2 - 315 - 6, 10))
        else:
            if frame_counter <= 30:
                window.blit(pygame.transform.scale_by(player2.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(player2.idle_2_sprite, 2), (window_width // 2 - 315, 10))
        window.blit(skin_select_spotlight, (0, 0))

        #CM 7/24/24 - set skin selection sprites
        skin_display_list = []
        if player2.animal == "cat":
            skin_display_list = cat_nice
        elif player2.animal == "dog":
            skin_display_list = dog_nice
        elif player2.animal == "bear":
            skin_display_list = bear_nice
        elif player2.animal == "duck":
            skin_display_list = duck_nice

        #CM 7/22/24-7/24/24 - draw skin buttons, skins, and skin selection
        for i in range(0, 20):
            p2_skin_select_button[i].draw()
        for i in range(0, 5):
            window.blit(pygame.transform.scale_by(skin_display_list[i * 4], 0.3), (80 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 1], 0.3), (190 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 2], 0.3),
                        (window_width - 170 - 110 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 3], 0.3),
                        (window_width - 60 - 110 - 2, 50 + (i * 110)))
        for i in range(0, 20):
            p2_skin_select_button[i].select_draw(p2_skin_select_button, 0, 20, 1)

        #CM 7/23/24 - animal select buttons
        animal_select_left_button.draw()
        animal_select_right_button.draw()

        #CM 7/22/24 - back_button draw
        back_button.draw()

    #CM 7/25/24-7/28/24 - cpu_skin_select menu events (code modified from p2_skin_select menu events above)
    if menu.screen == "cpu_skin_select":
        bg_scroll(checkerboard_bg_dark_blue)
        cpu.set_sprites()

        #CM 7/23/24 - draw stage + cpu character with idle animation + spotlight
        window.blit(skin_select_stage, (0, 0))
        if cpu.animal == "bear":
            if frame_counter <= 15:
                window.blit(pygame.transform.scale_by(cpu.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            elif frame_counter <= 30:
                window.blit(pygame.transform.scale_by(cpu.idle_2_sprite, 2), (window_width // 2 - 315 + 6, 10))
            elif frame_counter <= 45:
                window.blit(pygame.transform.scale_by(cpu.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(cpu.idle_3_sprite, 2), (window_width // 2 - 315 - 6, 10))
        else:
            if frame_counter <= 30:
                window.blit(pygame.transform.scale_by(cpu.idle_1_sprite, 2), (window_width // 2 - 315, 10))
            else:
                window.blit(pygame.transform.scale_by(cpu.idle_2_sprite, 2), (window_width // 2 - 315, 10))
        window.blit(skin_select_spotlight, (0, 0))

        #CM 7/24/24 - set skin selection sprites
        skin_display_list = []
        if cpu.animal == "cat":
            skin_display_list = cat_nice
        elif cpu.animal == "dog":
            skin_display_list = dog_nice
        elif cpu.animal == "bear":
            skin_display_list = bear_nice
        elif cpu.animal == "duck":
            skin_display_list = duck_nice

        #CM 7/22/24-7/24/24 - draw skin buttons, skins, and skin selection
        for i in range(0, 20):
            cpu_skin_select_button[i].draw()
        for i in range(0, 5):
            window.blit(pygame.transform.scale_by(skin_display_list[i * 4], 0.3), (80 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 1], 0.3), (190 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 2], 0.3),
                        (window_width - 170 - 110 - 2, 50 + (i * 110)))
            window.blit(pygame.transform.scale_by(skin_display_list[(i * 4) + 3], 0.3),
                        (window_width - 60 - 110 - 2, 50 + (i * 110)))
        for i in range(0, 20):
            cpu_skin_select_button[i].select_draw(cpu_skin_select_button, 0, 20, 1)

        #CM 7/23/24 - animal select buttons
        animal_select_left_button.draw()
        animal_select_right_button.draw()

        #CM 7/22/24 - back_button draw
        back_button.draw()

    #CM 5/9/24-6/7/24 - 1P vs COM game events
    if menu.screen == "1p_vs_com":
        window.blit(stage, (0, 0))
        window.blit(trophy, (window_width // 2 - trophy.get_width() // 2, window_height // 2 - 50))
        player.draw()
        cpu.draw()
        if game_countdown.ready == False:
            game_countdown.draw()
        else:
            player.qte_draw()
            cpu.qte_draw()
    #CM 6/2/24-6/7/24 - 1P vs 2P game events
    if menu.screen == "1p_vs_2p":
        window.blit(stage, (0, 0))
        window.blit(trophy, (window_width // 2 - trophy.get_width() // 2, window_height // 2 - 50))
        player.draw()
        player2.draw()
        if game_countdown.ready == False:
            game_countdown.draw()
        else:
            player.qte_draw()
            player2.qte_draw()

    #CM 5/16/24 - player win screen events
    if menu.screen == "player_win":
        window.blit(player_win, (0, 0))
        if keys[pygame.K_SPACE]:
            menu.screen = "title"

    #CM 5/28/24 - player win screen events
    if menu.screen == "cpu_win":
        window.blit(cpu_win, (0, 0))
        if keys[pygame.K_SPACE]:
            menu.screen = "title"

    #CM 5/7/24 - update screen
    pygame.display.update()


#CM 5/7/24-7/30/24 - class object definitions + other variables (in if statement so I can compress in PyCharm)
if True:
    player = Player(1, False)
    player2 = Player(2, False)
    online_player = Player(1, True)
    online_opponent = OnlinePlayer()
    cpu = CPU()
    menu = Menu()
    menu.screen = "title"
    game_countdown = GameCountdown()
    online_play_button = Button(buttons[0], (window_width // 2) - buttons[0].get_width() // 2, 360)
    offline_play_button = Button(buttons[1], (window_width // 2) - buttons[1].get_width() // 2, 440)
    item_shop_button = Button(buttons[2], (window_width // 2) - buttons[2].get_width() // 2, 520)
    extras_button = Button(buttons[3], (window_width // 2) - buttons[3].get_width() // 2, 600)
    back_button = Button(buttons[4], 10, 650)
    P1_vs_COM_button = Button(buttons[5], 40, 290)
    P1_vs_P2_button = Button(buttons[6], 680, 30)
    match_rules_button = Button(buttons[7], 90, 120)
    rounds_of_qtes_8_button = Button(buttons[13], 650, 65)
    rounds_of_qtes_12_button = Button(buttons[14], 790, 65)
    rounds_of_qtes_16_button = Button(buttons[15], 930, 65)
    rounds_of_qtes_20_button = Button(buttons[16], 1070, 65)
    letters_per_qte_3_button = Button(buttons[9], 650, 245)
    letters_per_qte_4_button = Button(buttons[10], 790, 245)
    letters_per_qte_5_button = Button(buttons[11], 930, 245)
    letters_per_qte_6_button = Button(buttons[12], 1070, 245)
    seconds_per_qte_5_button = Button(buttons[11], 650, 425)
    seconds_per_qte_4_button = Button(buttons[10], 790, 425)
    seconds_per_qte_3_button = Button(buttons[9], 930, 425)
    seconds_per_qte_2_button = Button(buttons[8], 1070, 425)
    rounds_of_qtes_8_button.highlight = True
    letters_per_qte_3_button.highlight = True
    seconds_per_qte_5_button.highlight = True
    match_rules_button_list = [rounds_of_qtes_8_button, rounds_of_qtes_12_button, rounds_of_qtes_16_button,
                               rounds_of_qtes_20_button, letters_per_qte_3_button, letters_per_qte_4_button,
                               letters_per_qte_5_button, letters_per_qte_6_button, seconds_per_qte_5_button,
                               seconds_per_qte_4_button, seconds_per_qte_3_button, seconds_per_qte_2_button]
    p1_skin_button = Button(buttons[17], 690, 370)
    p2_skin_button = Button(buttons[18], 930, 370)
    cpu_skin_button = Button(buttons[19], 1050, 530)
    stage_button = Button(buttons[20], 810, 530)
    p1_skin_select_button = []
    p2_skin_select_button = []
    cpu_skin_select_button = []
    for i in range(0, 5):
        p1_skin_select_button.append(Button(buttons[21], 70, 40 + (i * 110)))
        p1_skin_select_button.append(Button(buttons[21], 180, 40 + (i * 110)))
        p1_skin_select_button.append(Button(buttons[21], window_width - 180 - 110, 40 + (i * 110)))
        p1_skin_select_button.append(Button(buttons[21], window_width - 70 - 110, 40 + (i * 110)))
        p2_skin_select_button.append(Button(buttons[21], 70, 40 + (i * 110)))
        p2_skin_select_button.append(Button(buttons[21], 180, 40 + (i * 110)))
        p2_skin_select_button.append(Button(buttons[21], window_width - 180 - 110, 40 + (i * 110)))
        p2_skin_select_button.append(Button(buttons[21], window_width - 70 - 110, 40 + (i * 110)))
        cpu_skin_select_button.append(Button(buttons[21], 70, 40 + (i * 110)))
        cpu_skin_select_button.append(Button(buttons[21], 180, 40 + (i * 110)))
        cpu_skin_select_button.append(Button(buttons[21], window_width - 180 - 110, 40 + (i * 110)))
        cpu_skin_select_button.append(Button(buttons[21], window_width - 70 - 110, 40 + (i * 110)))
    p1_skin_select_button[0].highlight = True
    p2_skin_select_button[0].highlight = True
    cpu_skin_select_button[0].highlight = True
    animal_select_left_button = Button(buttons[22], 350, 400)
    animal_select_right_button = Button(buttons[23], window_width - 350 - buttons[23].get_width(), 400)
    item_shop_skins_button = Button(buttons[24], window_width // 2 - (150 + 330), 85)
    item_shop_stages_button = Button(buttons[25], window_width // 2 - 150, 85)
    item_shop_music_button = Button(buttons[26], window_width // 2 + (150 + 30), 85)
    be_server_host_button = Button(buttons[27], 40, 290)
    be_server_guest_button = Button(buttons[28], 680, 30)


#CM 5/7/24-7/17/24 - main while loop
run = True
frame_counter = 1
while run:
    #CM 5/25/24-7/11/24 - framerate + frame_counter
    clock.tick(60)
    if frame_counter == 61:
        frame_counter = 1

    #CM 5/7/24-7/6/24 - event handler
    events = pygame.event.get()
    for event in events:
        #CM 5/7/24 - if window closed, end Pygame safely
        if event.type == pygame.QUIT:
            run = False

        #CM 5/22/24-7/4/24 - mouse click handler
        if event.type == pygame.MOUSEBUTTONUP:
            #CM 5/14/24-6/13/24 - if menu is title
            if menu.screen == "title":
                #CM 5/14/24-7/4/24 - click method for title screen buttons
                online_play_button.click("online_play")
                offline_play_button.click("offline_play")
                break

            #CM 6/24/24 - if menu is online_play
            if menu.screen == "online_play":

                #CM 7/30/24 - button clicks
                P1_vs_P2_button.click("connecting_to_server_1v1")
                p1_skin_button.click("online_p1_skin_select")

                #CM 7/18/2024 - back_button click
                back_button.click("title")
                break

            #CM 7/30/24 - if menu is online_p1_skin_select (code modified from p1_skin_select below)
            if menu.screen == "online_p1_skin_select":
                # CM 7/23/24 - skin selection select_click
                for i in range(0, 20):
                    p1_skin_select_button[i].select_click("skin_number", i, online_player)

                # CM 7/24/24 - animal select clicks
                if online_player.animal == "cat":
                    if animal_select_left_button.click("online_p1_skin_select"):
                        online_player.animal = "duck"
                    if animal_select_right_button.click("online_p1_skin_select"):
                        online_player.animal = "dog"
                elif online_player.animal == "dog":
                    if animal_select_left_button.click("online_p1_skin_select"):
                        online_player.animal = "cat"
                    if animal_select_right_button.click("online_p1_skin_select"):
                        online_player.animal = "bear"
                elif online_player.animal == "bear":
                    if animal_select_left_button.click("online_p1_skin_select"):
                        online_player.animal = "dog"
                    if animal_select_right_button.click("online_p1_skin_select"):
                        online_player.animal = "duck"
                elif online_player.animal == "duck":
                    if animal_select_left_button.click("online_p1_skin_select"):
                        online_player.animal = "bear"
                    if animal_select_right_button.click("online_p1_skin_select"):
                        online_player.animal = "cat"

                # CM 7/22/24 - back_button click
                back_button.click("online_play")

            #CM 5/16/24-6/13/24 - if menu is offline_play
            if menu.screen == "offline_play":
                #CM 5/16/24-7/19/24 - button clicks
                if P1_vs_COM_button.click("1p_vs_com"):
                    #CM 7/22/24 - initialize game objects
                    game_countdown.__init__()
                    player.reset()
                    cpu.reset()
                if P1_vs_P2_button.click("1p_vs_2p"):
                    #CM 7/19/24-7/22/24 - initialize game objects
                    game_countdown.__init__()
                    player.reset()
                    player2.reset()
                match_rules_button.click("match_rules")
                p1_skin_button.click("p1_skin_select")
                p2_skin_button.click("p2_skin_select")
                cpu_skin_button.click("cpu_skin_select")
                stage_button.click("stage_select")

                #CM 7/18/24 - back_button click
                back_button.click("title")

            #CM 7/19/24 - if menu is match_rules
            if menu.screen == "match_rules":
                #CM 7/22/24 - button select_click methods (could probably be better written)
                rounds_of_qtes_8_button.select_click("rounds_of_qtes", 8, "all")
                rounds_of_qtes_12_button.select_click("rounds_of_qtes", 12, "all")
                rounds_of_qtes_16_button.select_click("rounds_of_qtes", 16, "all")
                rounds_of_qtes_20_button.select_click("rounds_of_qtes", 20, "all")
                letters_per_qte_3_button.select_click("letters_per_qte", 3, "all")
                letters_per_qte_4_button.select_click("letters_per_qte", 4, "all")
                letters_per_qte_5_button.select_click("letters_per_qte", 5, "all")
                letters_per_qte_6_button.select_click("letters_per_qte", 6, "all")
                seconds_per_qte_5_button.select_click("seconds_per_qte", 5, "all")
                seconds_per_qte_4_button.select_click("seconds_per_qte", 4, "all")
                seconds_per_qte_3_button.select_click("seconds_per_qte", 3, "all")
                seconds_per_qte_2_button.select_click("seconds_per_qte", 2, "all")

                #CM 7/19/24 - back_button click
                back_button.click("offline_play")

            #CM 7/22/24-7/28/24 - if menu is p1_skin_select
            if menu.screen == "p1_skin_select":
                #CM 7/23/24 - skin selection select_click
                for i in range(0, 20):
                    p1_skin_select_button[i].select_click("skin_number", i, player)

                #CM 7/24/24 - animal select clicks
                if player.animal == "cat":
                    if animal_select_left_button.click("p1_skin_select"):
                        player.animal = "duck"
                    if animal_select_right_button.click("p1_skin_select"):
                        player.animal = "dog"
                elif player.animal == "dog":
                    if animal_select_left_button.click("p1_skin_select"):
                        player.animal = "cat"
                    if animal_select_right_button.click("p1_skin_select"):
                        player.animal = "bear"
                elif player.animal == "bear":
                    if animal_select_left_button.click("p1_skin_select"):
                        player.animal = "dog"
                    if animal_select_right_button.click("p1_skin_select"):
                        player.animal = "duck"
                elif player.animal == "duck":
                    if animal_select_left_button.click("p1_skin_select"):
                        player.animal = "bear"
                    if animal_select_right_button.click("p1_skin_select"):
                        player.animal = "cat"

                #CM 7/22/24 - back_button click
                back_button.click("offline_play")

            #CM 7/24/24-7/28/24 - if menu is p2_skin_select (code modified from p1_skin_select above)
            if menu.screen == "p2_skin_select":
                #CM 7/23/24 - skin selection select_click
                for i in range(0, 20):
                    p2_skin_select_button[i].select_click("skin_number", i, player2)

                #CM 7/24/24 - animal select clicks
                if player2.animal == "cat":
                    if animal_select_left_button.click("p2_skin_select"):
                        player2.animal = "duck"
                    if animal_select_right_button.click("p2_skin_select"):
                        player2.animal = "dog"
                elif player2.animal == "dog":
                    if animal_select_left_button.click("p2_skin_select"):
                        player2.animal = "cat"
                    if animal_select_right_button.click("p2_skin_select"):
                        player2.animal = "bear"
                elif player2.animal == "bear":
                    if animal_select_left_button.click("p2_skin_select"):
                        player2.animal = "dog"
                    if animal_select_right_button.click("p2_skin_select"):
                        player2.animal = "duck"
                elif player2.animal == "duck":
                    if animal_select_left_button.click("p2_skin_select"):
                        player2.animal = "bear"
                    if animal_select_right_button.click("p2_skin_select"):
                        player2.animal = "cat"

                #CM 7/22/24 - back_button click
                back_button.click("offline_play")

            #CM 7/25/24-7/28/24 - if menu is cpu_skin_select (code modified from p2_skin_select above)
            if menu.screen == "cpu_skin_select":
                #CM 7/23/24 - skin selection select_click
                for i in range(0, 20):
                    cpu_skin_select_button[i].select_click("skin_number", i, cpu)

                #CM 7/24/24 - animal select clicks
                if cpu.animal == "cat":
                    if animal_select_left_button.click("cpu_skin_select"):
                        cpu.animal = "duck"
                    if animal_select_right_button.click("cpu_skin_select"):
                        cpu.animal = "dog"
                elif cpu.animal == "dog":
                    if animal_select_left_button.click("cpu_skin_select"):
                        cpu.animal = "cat"
                    if animal_select_right_button.click("cpu_skin_select"):
                        cpu.animal = "bear"
                elif cpu.animal == "bear":
                    if animal_select_left_button.click("cpu_skin_select"):
                        cpu.animal = "dog"
                    if animal_select_right_button.click("cpu_skin_select"):
                        cpu.animal = "duck"
                elif cpu.animal == "duck":
                    if animal_select_left_button.click("cpu_skin_select"):
                        cpu.animal = "bear"
                    if animal_select_right_button.click("cpu_skin_select"):
                        cpu.animal = "cat"

                #CM 7/22/24 - back_button click
                back_button.click("offline_play")

    #CM 5/8/24 - call qte_sequence method from Player class to play game
    if menu.screen == "1p_vs_com":
        if game_countdown.ready == True:
            player.qte_sequence()
            cpu.play()
    if menu.screen == "1p_vs_2p":
        if game_countdown.ready == True:
            player.qte_sequence()
            player2.qte_sequence()

    #CM 7/2/24 - call qte_sequence method from Player class to play game online
    if menu.screen == "1p_vs_1p_online":
        if game_countdown.ready == True:
            online_player.qte_sequence()

    #CM 6/28/24-7/6/24 - connecting to foreign player (code is in front of the one below to avoid a recv error)
    if menu.screen == "searching_for_players_1v1":
        msg = client_socket.recv(1024).decode("utf-8")
        if msg == "Ready!":
            menu.screen = "1p_vs_1p_online"
            game_countdown.__init__()
            online_player.reset()
            online_opponent.__init__()

    #CM 6/28/24-7/2/24 - connect to server
    if menu.screen == "connecting_to_server_1v1":
        #CM 6/28/24 - try to connect to server
        try:
            client_socket.connect((host, port))
            menu.screen = "searching_for_players_1v1"
        #CM 6/28/24 - show error screen if connection fails
        except:
            menu.screen = "could_not_connect"

    #CM 5/7/24 - calls redraw_game_window() to update game window
    redraw_game_window()

    #CM 7/11/24 - increase frame_counter
    frame_counter += 1

#CM 5/7/24 - quit Pygame if loop is exited
pygame.quit()
