


class Player:
    name = ''
    wins = 0
    loss = 0
    totalgames = 0
    winloss = 0
    winpercent = 0
    points = 0
    # losspoints = 0
    rank = 0

    def __init__(self, name = ""):
        self.name = name

    def show_name(self):
        return self.name

    def add_win(self):
        self.wins += 1
        self.totalgames += 1

    def show_win(self):
        return self.wins

    def add_loss(self):
        self.loss += 1
        self.totalgames += 1

    def show_loss(self):
        return self.loss

    def show_totalgames(self):
        return self.totalgames

    def add_point(self):
        self.points += 1

    def show_point(self):
        return self.points

    def set_rank(self, rank):
        self.rank = rank

    def show_rank(self):
        return self.rank

    def show_winloss(self):
        self.winloss = self.wins / self.loss
        return self.winloss

    def show_winpercent(self):
        self.winpercent = self.wins / self.totalgames
        return self.winpercent



class Main:
    import xlrd
    path = "Foosball Game (Responses).xlsx"
    inputWorkbook = xlrd.open_workbook(path)
    inputWorksheet = inputWorkbook.sheet_by_index(0)

    player_names_list = ('Abdullah', 'Akhtar', 'Arjun', 'Daniel', 'Dmytro', 'Fadi', 'Flavio', 'Frederik', 'Jaiden',
                         'John C', 'John Vu', 'Marc Flores', 'Michael (Apple)', 'Nathan', 'Nav', 'PK', 'Razel', 'Reem',
                         'Reggy Loisy', 'Ricardo', 'Shourya', 'Shray', 'Siraj', 'Tome', 'Tyler', 'Victor (Beats)',
                         'Vini', 'William', '')

    players = []

    def __init__(self):
        for name in self.player_names_list:
            self.players.append(Player(name))

    def search(self, name):
        counter = 0
        for n in self.player_names_list:
            if n == name:
                return counter
            counter += 1

    def game_results(self, player1, player2, points1, points2):
        temp = 0
        points1 = int(points1)
        points2 = int(points2)
        player1_index = self.search(player1)
        player2_index = self.search(player2)

        if points1 > points2:
            self.players[player1_index].add_win()
            self.players[player2_index].add_loss()
        else:
            self.players[player1_index].add_loss()
            self.players[player2_index].add_win()

    def last_three_games(self):
        totallines = self.inputWorksheet.nrows
        for j in self.players:
            for k in self.players:
                count = 0
                game_results = []
                # i = totallines - 1
                i = 1
                while not count == 3:
                    i = i + 1
                    if self.inputWorksheet.cell_value(totallines - i, 1) == j.show_name() and \
                            self.inputWorksheet.cell_value(totallines - i, 2) == k.show_name():
                        count += 1
                        if self.inputWorksheet.cell_value(totallines - i, 3) > self.inputWorksheet.cell_value(totallines - i, 4):
                            game_results.append("W")
                        else:
                            game_results.append("L")
                    elif self.inputWorksheet.cell_value(totallines - i, 2) == j.show_name() and \
                            self.inputWorksheet.cell_value(totallines - i, 1) == k.show_name():
                        count += 1
                        if self.inputWorksheet.cell_value(totallines - i, 4) > self.inputWorksheet.cell_value(totallines - i, 3):
                            game_results.append("W")
                        else:
                            game_results.append("L")

                    if game_results.count("W") >= 2:
                        j.add_point()

                    # elif game_results.count("L") >= 2:
                    #     temp = losspoints[j] + 1
                    #     losspoints.pop(j)
                    #     losspoints.insert(j, temp)

    def rankings(self):
        points = []
        for x in range(len(self.player_names_list)):
            points_and_index = [self.players[x].showpoint(), x]
            points.append(points_and_index)

        for i in range(1, len(points)):
            key = points[i][0]
            j = i - 1
            while j >= 0 and key < points[j][0]:
                points[j + 1][0] = points[j][0]
                j -= 1
            points[j + 1][0] = key

        return points

    def print_rankstable(self):
        print("Ranking Table")
        print(": Name             : Rank   : Record W-L :")
        print("---------------------------------------")
        for i in self.players:
            print(':', self.players.show_name(), " " * (15 - len(self.players.show_name())), ":", self.players.show_rank(),
                  " " * (5 - len(str(self.players.show_rank()))),
                  ":", self.players.show_win(),
                  '-', self.players.show_loss(), " " * (9 - (len(str(self.players.show_win()))) - len(str(self.players.show_loss())) - 3), ":")

    def print_standingstable(self):
        print("Current Stats")
        print(': Name             : Rank   : Wins   : Loss   : Win/Loss Ratio   : Win Percent    : Games Played   : '
              'Points     :')
        print(
            '---------------------------------------------------------------------------------------------------------------')

        for item in self.players:
            print(':', self.players.show_name(), " " * (15 - len(self.players.show_name())), ":", self.players.show_rank(),
                  " " * (5 - len(str(self.players.show_rank()))), ":", self.players.show_win(),
                  " " * (5 - len(str(self.players.show_win()))), ":", self.players.show_loss(),
                  " " * (5 - len(str(self.players.show_loss()))), ":", self.players.show_winloss(),
                  " " * (15 - len(str(self.players.show_winloss()))), ":", str(self.players.show_winpercent()) + '%',
                  " " * (12 - len(str(self.players.show_winpercent()))), ":", self.players.show_totalgames(),
                  " " * (13 - len(str(self.players.show_totalgames()))), ":", self.players.show_point(),
                  ' ' * (9 - (len(str(self.players.show_point()))), ':'))

    def main(self):

        for x in range(1, self.inputWorksheet.nrows):
            l = []
            for y in range(1, 5):
                l.append(self.inputWorksheet.cell_value(x, y))
            self.game_results(l[0], l[1], l[2], l[3])
            # print(l[0], l[1], l[2], l[3])
            choice = 100
            self.last_three_games()
            self.rankings()
            while choice != 0:
                print("")
                print("")
                print("WELCOME TO THE BB FOOSBALL LEAGUE TABLE SYSTEM")
                print("1. PRINT TABLES")
                # print("2. CHECK ALL THE GAMES FROM A SPECIFIC DATE")
                # print("3. LAUNCH BETTING SYSTEM")
                # print("0. TO EXIT THE CODE ENTER 0")

                choice = input("ENTER YOUR CHOICE: ")
                while not choice.isdigit():
                    print("ERROR. CHOICE MUST BE AN INTEGER VALUE")
                    choice = input("ENTER YOUR CHOICE: ")
                choice = int(choice)
                while choice != 1:
                    print("ERROR. CHOICE MUST BE BE 1")
                    choice = int(input("ENTER YOUR CHOICE: "))
                if choice == 1:
                    self.print_rankstable()
                    print('')
                    self.print_standingstable()
                # elif choice == 2:
                #     printGames()
                # elif choice == 3:
                #     betting()


run = Main()
run.main()
