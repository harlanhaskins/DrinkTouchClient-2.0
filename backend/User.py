import requests

class user:
    username = None
    drinkCredits = None
    displayName = None
    ibuttonId = None
    drinkAdmin = False


    """
    initializes object and instance variables based on ibuttonId

    Makes a request to csh.rit.edu:56124/?ibutton and gets user information
    """
    def __init__(self, ibuttonId):
        print("New User Object:" + ibuttonId)

        self.username = "testuser"
        self.drinkCredits = 1
        selfdisplayName = "Test User"
        self.ibuttonId = ibuttonId
        self.drinkAdmin = False


