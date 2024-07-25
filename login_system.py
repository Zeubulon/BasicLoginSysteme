class LoginSystem:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.credentials = self.load_credentials()

    def load_credentials(self):
        credentials = {}
        try:
            with open(self.credentials_file, 'r') as file:
                for line in file:
                    username, password = line.strip().split(':')
                    credentials[username] = password
        except FileNotFoundError:
            print("Fichier Introuvable")
        return credentials

    def authenticate(self, username, password):
        return self.credentials.get(username) == password