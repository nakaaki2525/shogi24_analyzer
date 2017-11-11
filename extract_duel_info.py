import re
import os

class RegFileName(object):
    user_name_pattern = "\[[a-zA-Z0-9.\-_\+\s]*\]"
    extract_info = []

    def __init__(self, filename):
        if not os.path.exists("user_pass.txt"):
            pass
        else:
            f = open("user_pass.txt")
            user_account_name = f.readline().strip()
            f.close()
            [user1, user2] = re.findall(self.user_name_pattern, filename)
            user1 = user1[1:-1]
            user2 = user2[1:-1]
            tmp = re.sub(self.user_name_pattern, '', filename).split('_')
            if len(tmp) == 5:
                [kif_id, date, rate1, result, rate2] = tmp
                if user1 == user_account_name and result == "ox":
                        result = "勝ち"
                elif user1 == user_account_name and result == "xo":
                        result = "負け"
                elif user2 == user_account_name and result == "ox":
                        result = "負け"
                elif user2 == user_account_name and result == "xo":
                        result = "勝ち"
            else:
                result = "引き分け"
                [kif_id, date, rate1, rate2] = tmp
            if user1 == user_account_name:
                rate = rate1
                sengo = "先手"
            else:
                rate = rate2
                sengo = "後手"
            self.extract_info = [sengo, result, user_account_name, rate, filename, kif_id]

    def get_result(self):
        return self.extract_info
