import game_functions as gf
from player import Player
import title as t
import scene as s

def run_game():
    t.title_screen()
    pi = Player()
    pi.player_race = gf.player_race()
    pi.player_class = gf.player_class()
    pi.player_name = gf.player_name()
    gf.greetings(pi)
    s.start_path(pi)


run_game()
