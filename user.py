import json
import os
class Users(object):
    users = {}
    def __init__(self):
        if not os.path.exists("user_pass.json"):
            pass
        else:
            f = open("user_pass.json")
            self.users = json.load(f)
            f.close()

    def get_users(self):
        return self.users

    def add_user(self, user_name, password):
        self.users[user_name] = password
        self.save()

    def delete_user(self, user_name):
        del self.users[user_name]
        self.save()

    def save(self):
        f = open("user_pass.json", 'w')
        f.write(json.dumps(self.users))
        f.close()
