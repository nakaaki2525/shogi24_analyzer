from extract_duel_info import RegFileName
import os
import json
import matplotlib.pyplot as plt

class DuelData(object):
    data = {}
    lv_map = {"lv1": 0, "lv2": 1, "lv3": 2}
    def __init__(self):
        if os.path.exists("./data.json"):
            self.load()
        if not os.path.exists("static/kif"):
            os.mkdir("static/kif")
        else:
            files = os.listdir("static/kif")
            for filename in files:
                if ".kif" not in filename:
                    continue
                tmp = RegFileName(filename.replace(".kif", '')).get_result()
                if tmp[-1] not in self.data:
                    self.data[tmp[-1]] = ['未分類', '未分類', '未分類'] + tmp
                    self.data[tmp[-1]][7] = "/static/kif/"+filename
            self.save()

    def load(self):
        f = open("data.json", 'r')
        self.data = json.load(f)
        f.close()

    def save(self):
        f = open("data.json", 'w')
        f.write(json.dumps(self.data))
        f.close()

    def get_data(self, page=None):
        if page!=None:
            return sorted(self.data.items(), reverse=True)[100*(page-1):100*page]
        return sorted(self.data.items(), reverse=True)

    def create_graph(self):
        data = self.get_data()
        rates = []
        for v in data:
            rate = int(v[1][6])
            rates.append(rate)
        plt.plot(list(range(len(rates))), rates)
        plt.savefig( 'static/rate.png' )
        plt.close()

    def create_user_graph(self, user_name):
        data = self.get_data()
        rates = []
        for v in data:
            if v[1][5] == user_name:
                rate = int(v[1][6])
                rates.append(rate)
        plt.plot(list(range(len(rates))), rates)
        plt.savefig( 'static/rate_'+user_name+'.png' )
        plt.close()

    def save_data(self, form):
        for key, value in self.data.items():
            lv1 = form.getlist("lv1_"+key)
            lv2 = form.getlist("lv2_"+key)
            lv3 = form.getlist("lv3_"+key)
            if len(lv1) !=0:
                self.data[key][0] = lv1[0]
            else:
                self.data[key][0] = "未分類"
            if len(lv2) !=0:
                self.data[key][1] = lv2[0]
            else:
                self.data[key][1] = "未分類"
            if len(lv2) !=0:
                self.data[key][2] = lv3[0]
            else:
                self.data[key][2] = "未分類"

        self.save()
