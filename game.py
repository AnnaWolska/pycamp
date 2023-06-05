from deck import Deck
from player import Player
from exception import GameOverException, GameOverCroupierException, GameOverUserException


class Game:
    # mogę dopisać atrybuty
    some_var = "Wolcome in Black Jack Game!"
    def __init__(self):  # metoda wywołana w momencie tworzenia obiektu Game
        self.deck = Deck()  # tworzę instancję klasy Deck
        self.deck.shuffle() # moment, w którym tasuję deck, wywołuję metodę shuffle na obiekcie
        # self.player_points = 0
        print(self.some_var)
        self.some_var = "Chcesz mieć 21 punktów albo coś blisko."

    @staticmethod
    def _print_menu():
        print("Co chcesz zrobić?")
        print("0 - dobieram kartę")
        print("1 - pasuję")

    def croupier_plays(self, user_points):
        croupier = Player()
        croupier_points = 0
        while croupier.calculate_points() < user_points:
            # card = self.deck.hit()
            # croupier.take_card()
            croupier.take_card(self.deck.hit())
            print("krupier ma punktów: ", croupier.calculate_points(), croupier.cards)
        return croupier.calculate_points()

    def _user_plays(self):
        self.user = Player()
        # dla dwóch kart losuję kartę z deck'u i user ją bierze
        for _ in range(2):
            card = self.deck.hit()
            self.user.take_card(card)

        while True:
            print("Twoje karty to:", self.user.cards)
            print("MASZ PUNKTÓW: ", self.user.calculate_points())
            print(self.some_var)
            self._print_menu()
            choice = input("Wybierz 0 lub 1: ")
            if choice == "0":
                self.user.take_card(self.deck.hit())
            elif choice == '1':
                return self.user.calculate_points()
                # print("Skończyłeś grę z ",self.user.calculate_points(), " punktami." )
                # break
            else:
                print("Coś jest źle wpisane:( nie rozumiem")

    def have_fun(self):
        print("user",self.user)

    def play(self):
        try:
            # self._user_plays()
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error
        try:
            croupier_points = self.croupier_plays(user_points)
            # 'from error' pokazuje lepiej gdzie był błąd wyżej w playerze
        except GameOverException as error:
            raise  GameOverCroupierException from error

        print("Kociec gry, wygrania krupiera!")


