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
                tmp[key]['未分類']['未分類'] = {}
                tmp[key]['未分類']['未分類']['先手'] = [0, 0, 0]
                tmp[key]['未分類']['未分類']['後手'] = [0, 0, 0]
                for k, v in value.items():
                    tmp[key][k] = {}
                    tmp[key][k]['未分類'] = {}
                    tmp[key][k]['未分類']['先手'] = [0, 0, 0]
                    tmp[key][k]['未分類']['後手'] = [0, 0, 0]

                    for x in v:
                        tmp[key][k][x] = {}
                        tmp[key][k][x]['先手'] = [0, 0, 0]
                        tmp[key][k][x]['後手'] = [0, 0, 0]
        tmp['未分類'] = {}
        tmp['未分類']['未分類'] = {}
        tmp['未分類']['未分類']['未分類'] = {}
        tmp['未分類']['未分類']['未分類']['先手'] = [0, 0, 0]
        tmp['未分類']['未分類']['未分類']['後手'] = [0, 0, 0]

        for x in data:

            x = x[1]
            # print(x)
            l1 = x[0]
            l2 = x[1]
            l3 = x[2]
            teban = x[3]
            kati_make = x[4]
            if kati_make == '勝ち':
                tmp[l1][l2][l3][teban][0] += 1
            elif kati_make == '負け':
                tmp[l1][l2][l3][teban][1] += 1
            else:
                tmp[l1][l2][l3][teban][2] += 1
        for l1, values in tmp.items():
            for l2, value in values.items():
                for l3, v in value.items():

                    if (v["先手"][0]+v["先手"][1]) != 0:
                        v["先手"].insert(0, float(v["先手"][0]) / (v["先手"][0]+v["先手"][1]))
                    else:
                        v["先手"].insert(0, 0.0)
                    if (v["後手"][0]+v["後手"][1]) != 0:
                        v["後手"].insert(0, float(v["後手"][0]) / (v["後手"][0]+v["後手"][1]))
                    else:
                        v["後手"].insert(0, 0.0)

        for l1, values in tmp.items():
            analitics[l1] = {}
            ts = [0, 0, 0, 0]
            tg = [0, 0, 0, 0]
            for l2, value in values.items():

                tts = [0, 0, 0, 0]
                ttg = [0, 0, 0, 0]
                for l3, x in value.items():
                    tts[1] += x["先手"][1]
                    tts[2] += x["先手"][2]
                    tts[3] += x["先手"][3]
                    ttg[1] += x["後手"][1]
                    ttg[2] += x["後手"][2]
                    ttg[3] += x["後手"][3]
                    if tts[1]+tts[2] != 0:
                        tts[0] = float(tts[1]) / (tts[1]+tts[2])

                    else:
                        tts[0] = 0.0
                    if ttg[1]+ttg[2] != 0:
                        ttg[0] = float(ttg[1]) / (ttg[1]+ttg[2])
                    else:
                        ttg[0] = 0.0
                analitics[l1][l2] = [{"先手":tts, "後手":ttg}, tmp[l1][l2]]
            for k, v in analitics[l1].items():
                ts[1] += v[0]["先手"][1]
                ts[2] += v[0]["先手"][2]
                ts[3] += v[0]["先手"][3]
                tg[1] += v[0]["後手"][1]
                tg[2] += v[0]["後手"][2]
                tg[3] += v[0]["後手"][3]
                if ts[1]+ts[2] != 0:
                    ts[0] = float(ts[1]) / (ts[1]+ts[2])

                else:
                    ts[0] = 0.0
                if tg[1]+tg[2] != 0:
                    tg[0] = float(tg[1]) / (tg[1]+tg[2])
                else:
                    tg[0] = 0.0
            analitics[l1] = [{"先手":ts, "後手":tg}, analitics[l1]]

        #analitics[key] = [{"先手":tts, "後手":ttg}, tmp[key]]
        self.analitics = analitics
    def get_analitics(self):
        return self.analitics
