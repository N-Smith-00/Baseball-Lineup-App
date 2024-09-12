class App:
    def __init__(self, data_file) -> None:
        self.logged_in = False
        self.account = None
        # load data

class Account:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.teams = []