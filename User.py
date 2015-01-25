import requests

BASE_URL = "http://csh.rit.edu:56124/"

class User(object):

    __slots__ = ('username', 'drink_credits', 'display_name',
            'ibutton_id', 'is_drink_admin')

    """
    Initializes object and instance variables based on ibuttonId

    Makes a request to csh.rit.edu:56124/?ibutton and gets user information
    """
    def __init__(self, ibutton_id):
        r = requests.get(BASE_URL, params={"ibutton": ibutton_id})

        user = r.json()

        self.username = user['uid']
        self.drink_credits = user['credits']
        self.display_name = user['cn']
        self.ibutton_id = ibutton_id
        self.is_drink_admin = user['drinkAdmin']

        print(self)

    def __repr__(self):
        string = self.display_name
        string += "\n  "
        string += "username: " + self.username
        string += "\n  "
        string += "credits: " + str(self.drink_credits)
        string += "\n  "
        string += "admin: " + str(self.is_drink_admin)
        return string
