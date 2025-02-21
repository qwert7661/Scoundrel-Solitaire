# ================================================================================================================= #
#                                                    start of code                                                  #
# ================================================================================================================= #
import random as rng
import pygame as pg
pg.init()
pg.font.init()

print("Welcome to Scoundrel!")

# Setting up Screen, Clock & Font
screen_width = 1000
screen_height = 800
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Scoundrel!")
clock = pg.time.Clock()
font = pg.font.Font(None,50)

# ================================================================================================================= #
#                                                     CARD CLASS                                                    #
# ================================================================================================================= #
# Defining Card Class
class Card(pg.sprite.Sprite):
    def __init__(self, name: str, rank: int, suit: str, surf):
        super().__init__()
        self.name = name
        self.rank = rank
        self.suit = suit
        self.surf = surf
        self.surf = pg.transform.scale(self.surf,(138,200))
        self.rect = self.surf.get_rect()

# Initializing Cards Objects, Filling and Shuffling Deck
if True:
    cBack = Card(name='back', rank=0, suit='none', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/card_back.png'))

    c2h = Card(name='🂲2♥', rank=2, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/2_of_hearts.png'))
    c3h = Card(name='🂳3♥', rank=3, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/3_of_hearts.png'))
    c4h = Card(name='🂴4♥', rank=4, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/4_of_hearts.png'))
    c5h = Card(name='🂵5♥', rank=5, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/5_of_hearts.png'))
    c6h = Card(name='🂶6♥', rank=6, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/6_of_hearts.png'))
    c7h = Card(name='🂷7♥', rank=7, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/7_of_hearts.png'))
    c8h = Card(name='🂸8♥', rank=8, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/8_of_hearts.png'))
    c9h = Card(name='🂹9♥', rank=9, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/9_of_hearts.png'))
    c10h = Card(name='🂺10♥', rank=10, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/10_of_hearts.png'))
    cJh = Card(name='🂻J♥', rank=11, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/jack_of_hearts2.png'))
    cQh = Card(name='🂽Q♥', rank=12, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/queen_of_hearts2.png'))
    cKh = Card(name='🂾K♥', rank=13, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/king_of_hearts2.png'))
    cAh = Card(name='🂱A♥', rank=14, suit='heart', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/ace_of_hearts.png'))

    c2d = Card(name='🃂2♦', rank=2, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/2_of_diamonds.png'))
    c3d = Card(name='🃃3♦', rank=3, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/3_of_diamonds.png'))
    c4d = Card(name='🃄4♦', rank=4, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/4_of_diamonds.png'))
    c5d = Card(name='🃅5♦', rank=5, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/5_of_diamonds.png'))
    c6d = Card(name='🃆6♦', rank=6, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/6_of_diamonds.png'))
    c7d = Card(name='🃇7♦', rank=7, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/7_of_diamonds.png'))
    c8d = Card(name='🃈8♦', rank=8, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/8_of_diamonds.png'))
    c9d = Card(name='🃉9♦', rank=9, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/9_of_diamonds.png'))
    c10d = Card(name='🃊10♦', rank=10, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/10_of_diamonds.png'))
    cJd = Card(name='🃋J♦', rank=11, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/jack_of_diamonds2.png'))
    cQd = Card(name='🃍Q♦', rank=12, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/queen_of_diamonds2.png'))
    cKd = Card(name='🃎K♦', rank=13, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/king_of_diamonds2.png'))
    cAd = Card(name='🃁A♦', rank=14, suit='diamond', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/ace_of_diamonds.png'))

    c2c = Card(name='🃒2♣', rank=2, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/2_of_clubs.png'))
    c3c = Card(name='🃓3♣', rank=3, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/3_of_clubs.png'))
    c4c = Card(name='🃔4♣', rank=4, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/4_of_clubs.png'))
    c5c = Card(name='🃕5♣', rank=5, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/5_of_clubs.png'))
    c6c = Card(name='🃖6♣', rank=6, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/6_of_clubs.png'))
    c7c = Card(name='🃗7♣', rank=7, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/7_of_clubs.png'))
    c8c = Card(name='🃘8♣', rank=8, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/8_of_clubs.png'))
    c9c = Card(name='🃙9♣', rank=9, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/9_of_clubs.png'))
    c10c = Card(name='🃚10♣', rank=10, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/10_of_clubs.png'))
    cJc = Card(name='🃛J♣', rank=11, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/jack_of_clubs2.png'))
    cQc = Card(name='🃝Q♣', rank=12, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/queen_of_clubs2.png'))
    cKc = Card(name='🃞K♣', rank=13, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/king_of_clubs2.png'))
    cAc = Card(name='🃑A♣', rank=14, suit='club', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/ace_of_clubs.png'))

    c2s = Card(name='🂢2♤', rank=2, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/2_of_spades.png'))
    c3s = Card(name='🂣3♤', rank=3, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/3_of_spades.png'))
    c4s = Card(name='🂤4♤', rank=4, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/4_of_spades.png'))
    c5s = Card(name='🂥5♤', rank=5, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/5_of_spades.png'))
    c6s = Card(name='🂦6♤', rank=6, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/6_of_spades.png'))
    c7s = Card(name='🂧7♤', rank=7, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/7_of_spades.png'))
    c8s = Card(name='🂨8♤', rank=8, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/8_of_spades.png'))
    c9s = Card(name='🂩9♤', rank=9, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/9_of_spades.png'))
    c10s = Card(name='🂪10♤', rank=10, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/10_of_spades.png'))
    cJs = Card(name='🂫J♤', rank=11, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/jack_of_spades2.png'))
    cQs = Card(name='🂭Q♤', rank=12, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/queen_of_spades2.png'))
    cKs = Card(name='🂮K♤', rank=13, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/king_of_spades2.png'))
    cAs = Card(name='🂡A♤', rank=14, suit='spade', surf=pg.image.load('Scoundrel_Assets/graphics/playing_cards/ace_of_spades.png'))
deck = [c2h, c3h, c4h, c5h, c6h, c7h, c8h, c9h, c10h, # Red face cards and
        c2d, c3d, c4d, c5d, c6d, c7d, c8d, c9d, c10d, # red Aces removed
        c2c, c3c, c4c, c5c, c6c, c7c, c8c, c9c, c10c, cJc, cQc, cKc, cAc,
        c2s, c3s, c4s, c5s, c6s, c7s, c8s, c9s, c10s, cJs, cQs, cKs, cAs]
rng.shuffle(deck)

# ================================================================================================================= #
#                                                     GAME CLASS                                                    #
# ================================================================================================================= #
# Defining Game Class
class Scoundrel:
    board = []
    discard = []
    hp = 20
    weapon = None
    killed = []
    last_kill = 20      # Starting at 20 ensures new weapons can attack any card
    has_weapon = False
    use_fists = True
    use_weapon = False
    has_run = False
    has_healed = False

    # Refills the Board
    def refill_board(self):
        game.has_healed = False
        if len(self.board) > 1:
            return
        while len(self.board) < 4 and len(deck) > 0:
            self.board.append(deck.pop(0))

    # Determines Card Type & Calls Correct Method
    def determine_suit(self, card):
        if card.suit == 'heart':
            print("You drink a potion.")
            game.select_heart(card)
        if card.suit == 'diamond':
            print("You equip a new weapon.")
            game.select_diamond(card)
        if card.suit == 'club' or card.suit == 'spade':
            print("You attack the monster.")
            game.select_black(card)

    # Drink a Health Potion
    def select_heart(self, card):
        if not self.has_healed:
            self.hp += card.rank
            if self.hp > 20:
                self.hp = 20
                print("You are fully healed!")
            else: print(f"You heal up to {self.hp}.")
        if self.has_healed:
            print("The potion has no effect!")
        self.board.remove(card)
        self.discard.append(card)
        self.has_healed = True



    # Equip a Weapon
    def select_diamond(self,card):
        if self.weapon:
            self.discard.append(self.weapon)
        if self.killed:
            for e in self.killed:
                self.discard.append(e)
        self.has_weapon = True
        self.weapon = card
        self.killed = []
        self.last_kill = 20     # Starting at 20 ensures new weapons can attack any card
        self.board.remove(card)
        print(f'Weapon power: {self.weapon.rank}')

    # Fight a Monster
    def select_black(self, card):
        if self.use_fists:
            self.hp -= card.rank
            print(self.hp)
            if self.hp <= 0:
                print('You lose!')
            else:
                game.board.remove(card)
                self.discard.append(card)
        elif self.use_weapon:
            if self.last_kill > card.rank:
                if card.rank > self.weapon.rank:
                    self.hp -= (card.rank - self.weapon.rank)
                    if self.hp <= 0:
                        print("You lose!")
                    else:
                        self.last_kill = card.rank
                        self.killed.append(card)
                        self.board.remove(card)
                if card.rank <= self.weapon.rank:
                    self.last_kill = card.rank
                    self.killed.append(card)
                    self.board.remove(card)
            else: print("You must use your fists, or equip a new weapon.")

    # Run From Board
    def run_away(self):
        self.has_run = True
        rng.shuffle(self.board)
        for r in self.board: deck.append(r)
        game.board = []
        print("You flee the room!")
        game.refill_board()

# Reset For Next Game
def restart():
    global deck, game_active, win, lose
    deck = [c2h, c3h, c4h, c5h, c6h, c7h, c8h, c9h, c10h,  # Red face cards and
            c2d, c3d, c4d, c5d, c6d, c7d, c8d, c9d, c10d,  # red Aces removed
            c2c, c3c, c4c, c5c, c6c, c7c, c8c, c9c, c10c, cJc, cQc, cKc, cAc,
            c2s, c3s, c4s, c5s, c6s, c7s, c8s, c9s, c10s, cJs, cQs, cKs, cAs]
    rng.shuffle(deck)
    game_active = True
    win = False
    lose = False
    game.board = []
    game.discard = []
    game.hp = 20
    game.weapon = None
    game.killed = []
    game.last_kill = 20
    game.has_weapon = False
    game.use_fists = True
    game.use_weapon = False
    game.has_run = False
    game.has_healed = False
    print("Starting a new game...")

# Initializing Game Object
game = Scoundrel()

# ================================================================================================================= #
#                                              NON-CARD SURFACES & TEXT                                             #
# ================================================================================================================= #
if True:
    # Stat Text: Health, Remaining Cards, Defeated Cards
    health_text = font.render(f'Health: {game.hp}/20',True,'Red')
    health_text_pos = (440, 420)
    remaining_text = font.render(f'Remaining: {len(deck)+len(game.board)}',True,'White')
    remaining_text_pos = (440, 520)
    defeated_text = font.render(f'Defeated: {len(game.discard)}',True,'White')
    defeated_text_pos = (440, 620)

    # Fist, Weapon and Drop Buttons & Text
    weapon_fists_text = font.render('FISTS       WEAPON       DROP',True,'Black')
    weapon_fists_text_pos = (440, 320)
    fists_button_surf = pg.Surface((120,50)); fists_button_surf.fill('Green')
    fists_button_rect = fists_button_surf.get_rect(topleft = (430,310))
    weapon_button_surf = pg.Surface((180,50)); weapon_button_surf.fill('Grey')
    weapon_button_rect = weapon_button_surf.get_rect(topleft = (593,310))
    drop_button_surf = pg.Surface((120,50)); drop_button_surf.fill('Grey')
    drop_button_rect = drop_button_surf.get_rect(topleft = (815,310))

    # Hide Weapon, Drop and Run Buttons
    hide_weapon_button_surf = pg.Surface((180,50)); hide_weapon_button_surf.fill('Black')
    hide_drop_button_surf = pg.Surface((120,50)); hide_weapon_button_surf.fill('Black')
    hide_run_button_surf = pg.Surface((180,50)); hide_weapon_button_surf.fill('Black')

    # Run Button & Text
    run_text = font.render('RUN',True,'Black')
    run_text_pos = (835, 420)
    run_button_surf = pg.Surface((100,50)); run_button_surf.fill('Red')
    run_button_rect = run_button_surf.get_rect(topleft = (825,410))

    # Rules Button & Text
    rules_text = font.render('RULES',True,'Black')
    rules_text_pos = (810,520)
    rules_button_surf = pg.Surface((150,50)); rules_button_surf.fill('lightblue')
    rules_button_rect = rules_button_surf.get_rect(topleft = (795, 510))

    # Restart Button & Text
    restart_text = font.render('RESTART',True,'Black')
    restart_text_pos = (790,620)
    restart_button_surf = pg.Surface((180,50)); restart_button_surf.fill('brown4')
    restart_button_rect = restart_button_surf.get_rect(topleft = (780,610))

    # Non-Game Screens and Replay Button
    intro_surf = pg.image.load('Scoundrel_Assets/graphics/scoundrel_intro.png')
    lose_surf = pg.image.load('Scoundrel_Assets/graphics/scoundrel_lose.png')
    win_surf = pg.image.load('Scoundrel_Assets/graphics/scoundrel_win.png')
    intro_surf_pos = (0,0); lose_surf_pos = (0,0); win_surf_pos = (0,0)
    replay_button_surf = pg.Surface((300,100))
    replay_button_rect = replay_button_surf.get_rect(topleft = (330,450))

# ================================================================================================================= #
#                                                STARTING VARIABLES                                                 #
# ================================================================================================================= #
if True:
    game_active = False
    win = False
    lose = False
    rules = True

    # Card Coordinates
    board_pos_deck = (50,50)
    board_pos1 = (240,50)
    board_pos2 = (430,50)
    board_pos3 = (620,50)
    board_pos4 = (810,50)
    board_pos_discard = (50,400)
    board_pos_weapon = (240,300)
    board_pos_killed = (240,350)

# Game Loop
while True:
    # ============================================================================================================= #
    #                                                EVENT LOOP                                                     #
    # ============================================================================================================= #
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        else:
            if game_active:
                # Clicking to clear the rules screen in-game
                if rules:
                    if event.type == pg.MOUSEBUTTONDOWN: rules = False
                else:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        # Clicking cards on the board:
                        if board1_rect.collidepoint(mouse_pos):
                            game.determine_suit(game.board[0])
                        if board2_rect.collidepoint(mouse_pos):
                            game.determine_suit(game.board[1])
                        if board3_rect.collidepoint(mouse_pos):
                            game.determine_suit(game.board[2])
                        if board4_rect.collidepoint(mouse_pos):
                            game.determine_suit(game.board[3])
                        # Clicking run, rules or restart buttons:
                        if run_button_rect.collidepoint(mouse_pos) and game.has_run == False:
                            game.run_away()
                        if rules_button_rect.collidepoint(mouse_pos):
                            rules = True
                        if restart_button_rect.collidepoint(mouse_pos):
                            restart()
                    # Clicking fists, weapon and drop buttons:
                    if game.has_weapon:
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            if fists_button_rect.collidepoint(mouse_pos):
                                game.use_fists = True
                                game.use_weapon = False
                            if weapon_button_rect.collidepoint(mouse_pos):
                                game.use_fists = False
                                game.use_weapon = True
                            if drop_button_rect.collidepoint(mouse_pos):
                                if game.weapon:
                                    game.discard.append(game.weapon)
                                if game.killed:
                                    for e in game.killed:
                                        game.discard.append(e)
                                game.has_weapon = False
                                game.weapon = None
                                game.killed = []
                                game.last_kill = 20

            # Clicking to start the game, or to play again
            if not game_active:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if win == False and lose == False:
                        rules = False
                        restart()
                    else:
                        mouse_pos = event.pos
                        if replay_button_rect.collidepoint(mouse_pos):
                            restart()



    #                       ======================= CHECKING GAME STATE =======================
    # Refilling the board
    if len(game.board) <= 1 and len(deck) != 0:
        game.has_run = False
        game.refill_board()

    # Losing
    if game.hp <= 0 or lose == True:
        lose = True
        lose_text = font.render(f'You cleared {len(game.discard) + len(game.killed) + (1 if game.weapon else 0)} cards, '
                                f'with {len(deck) + len(game.board)} remaining.',True,'black')
        game_active = False
    # Winning
    if (len(deck) == 0 and len(game.board) == 0) or win == True:
        win = True
        win_text = font.render(f'You cleared the dungeon with {game.hp} health remaining!',True,'blue')
        # if game.hp == 20:                                                                   # I don't feel like getting
        #     if c2h or c3h or c4h or c5h or c6h or c7h or c8h or c9h or c10h in game.board:  # scores over 20 working
        # pass                                                                                # so...
        game_active = False

    # ============================================================================================================= #
    #                                               BLITTING SURFACES                                               #
    # ============================================================================================================= #

    # Blackground
    screen.fill((0,0,0))
    #                      ======================= GAME ACTIVE SURFACES =======================
    if game_active:
        if rules: screen.blit(intro_surf,intro_surf_pos)
        elif not rules:

            # Update & Blit Cards on Board
            if len(game.board) >= 1:
                board1_rect = game.board[0].surf.get_rect(topleft=board_pos1)
                screen.blit(game.board[0].surf, board1_rect)
            if len(game.board) >= 2:
                board2_rect = game.board[1].surf.get_rect(topleft=board_pos2)
                screen.blit(game.board[1].surf, board2_rect)
            if len(game.board) >= 3:
                board3_rect = game.board[2].surf.get_rect(topleft=board_pos3)
                screen.blit(game.board[2].surf, board3_rect)
            if len(game.board) >= 4:
                board4_rect = game.board[3].surf.get_rect(topleft=board_pos4)
                screen.blit(game.board[3].surf, board4_rect)

            # Dynamically Blit Deck, Discard, Weapon & Kills
            y = 0
            for n in deck:
                screen.blit(cBack.surf,(board_pos_deck[0], board_pos_deck[1] + y))
                y += 3
            y = 0
            for n in range(len(game.discard)):
                screen.blit(cBack.surf, (board_pos_discard[0], board_pos_discard[1] + y))
                y += 3
            if game.has_weapon:
                screen.blit(game.weapon.surf, board_pos_weapon)
                y = 0
                for n in game.killed:
                    screen.blit(n.surf, (board_pos_killed[0], board_pos_killed[1] + y))
                    y += 30

            # Blit Weapon, Fists, Drop Buttons
            if game.has_weapon:
                screen.blit(weapon_button_surf, weapon_button_rect)
                screen.blit(drop_button_surf, drop_button_rect)
            else:
                screen.blit(hide_weapon_button_surf, weapon_button_rect)
                screen.blit(hide_drop_button_surf, drop_button_rect)
                game.use_fists = True
                game.use_weapon = False
            if game.use_fists:
                fists_button_surf.fill('Green')
                weapon_button_surf.fill('Grey')
            elif game.use_weapon:
                fists_button_surf.fill('Grey')
                weapon_button_surf.fill('Green')
            screen.blit(fists_button_surf, fists_button_rect)
            screen.blit(weapon_fists_text, weapon_fists_text_pos)

            # Blit Run, Rules and Restart Buttons
            if not game.has_run:
                screen.blit(run_button_surf, run_button_rect)
                screen.blit(run_text, run_text_pos)
            screen.blit(rules_button_surf,rules_button_rect)
            screen.blit(rules_text,rules_text_pos)
            screen.blit(restart_button_surf,restart_button_rect)
            screen.blit(restart_text,restart_text_pos)

            # Update & Blit Stats: Health, Remaining Cards, Defeated Cards
            health_text = font.render(f'Health: {game.hp}/20',True,'Red')
            remaining_text = font.render(f'Remaining: {len(deck) + len(game.board)}',True,'White')
            defeated_text = font.render(f'Defeated: {len(game.discard) + len(game.killed)}',True,'White')
            screen.blit(health_text,health_text_pos)
            screen.blit(remaining_text,remaining_text_pos)
            screen.blit(defeated_text,defeated_text_pos)

    #                       ======================= GAME INACTIVE BLIT =======================
    else:
        if win:
            screen.blit(win_surf,win_surf_pos)
            screen.blit(win_text,(80,330))
        elif lose:
            screen.blit(lose_surf,lose_surf_pos)
            screen.blit(lose_text,(180,350))
        else: screen.blit(intro_surf,intro_surf_pos)



    # Updating display and limiting FPS
    pg.display.flip()
    clock.tick(60)
# ================================================================================================================= #
#                                                     end of code                                                   #
# ================================================================================================================= #
