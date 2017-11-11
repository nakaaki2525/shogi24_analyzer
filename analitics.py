import codecs
import json
class Analitics(object):
    analitics = {}
    def __init__(self, data):

        f = codecs.open("senkei.json", 'r', "utf-8")
        senkei = json.load(f)
        f.close()
        analitics = {}
        tmp = {}
        for key, value in senkei.items():
            tmp[key] = {}
            tmp[key]['未分類'] = {}
            tmp[key]['未分類']['先手'] = [0, 0, 0]
            tmp[key]['未分類']['後手'] = [0, 0, 0]
            for k in value:
                tmp[key][k] = {}
                tmp[key][k] = {}
                tmp[key][k]['先手'] = [0, 0, 0]
                tmp[key][k]['後手'] = [0, 0, 0]
        tmp['未分類'] = {}
        tmp['未分類']['未分類'] = {}
        tmp['未分類']['未分類']['先手'] = [0, 0, 0]
        tmp['未分類']['未分類']['後手'] = [0, 0, 0]

        for x in data:
            x = x[1]
            key = x[0]
            k = x[1]
            teban = x[2]
            kati_make = x[3]
            if kati_make == '勝ち':
                tmp[key][k][teban][0] += 1
            elif kati_make == '負け':
                tmp[key][k][teban][1] += 1
            else:
                tmp[key][k][teban][2] += 1
        for key, value in tmp.items():
            for k, v in value.items():
                if (v["先手"][0]+v["先手"][1]) != 0:
                    v["先手"].insert(0, '{:.2f}'.format(float(v["先手"][0]) / (v["先手"][0]+v["先手"][1])))
                else:
                    v["先手"].insert(0, '{:.2f}'.format(0.0))
                if (v["後手"][0]+v["後手"][1]) != 0:
                    v["後手"].insert(0, '{:.2f}'.format(float(v["後手"][0]) / (v["後手"][0]+v["後手"][1])))
                else:
                    v["後手"].insert(0, '{:.2f}'.format(0.0))
        for key, value in tmp.items():
            ts = [0, 0, 0, 0]
            tg = [0, 0, 0, 0]
            for x_key, x in value.items():
                ts[1] += x["先手"][1]
                ts[2] += x["先手"][2]
                ts[3] += x["先手"][3]
                tg[1] += x["後手"][1]
                tg[2] += x["後手"][2]
                tg[3] += x["後手"][3]
            if ts[1]+ts[2] != 0:
                ts[0] = '{:.2f}'.format(float(ts[1]) / (ts[1]+ts[2]))

            else:
                ts[0] = 0.0
            if tg[1]+tg[2] != 0:
                tg[0] = '{:.2f}'.format(float(tg[1]) / (tg[1]+tg[2]))
            else:
                tg[0] = 0.0

            analitics[key] = [{"先手":ts, "後手":tg}, tmp[key]]
        self.analitics = analitics
    def get_analitics(self):
        return self.analitics
