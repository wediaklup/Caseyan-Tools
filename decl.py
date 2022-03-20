import logging
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


dictionary = {}

def dekl(mode, inflekativ, arg1="0", arg2="0", arg3="0"):
    if mode == "subst":
        # arg1 = Kasus
        # arg2 = Numerus
        if arg1 == "0" and arg2 == "0":
            result = Kasus.sg.dekl(inflekativ)
            tmp = Kasus.pl.dekl(inflekativ)
            for i in range(len(tmp)):
                result.append(tmp[i])
            return result
        elif arg1 == "0" or arg2 == "0":
            logging.warning("Deklinieren: Unzureichende Parameter")
        else:
            pass


def fullformat(mode, liste):
    if mode == "subst":
        resultsg = f"Singular\nNominativ: {liste[0]}\nAkkusativ: {liste[1]}\nLokativ: {liste[2]}\nOrginativ: {liste[3]}\nDirektativ: {liste[4]}\nInstrumentativ: {liste[5]}\nPossessiv: {liste[6]}\nTotalitiv: {liste[7]}\n\n"
        resultpl = f"Plural\nNominativ: {liste[8]}\nAkkusativ: {liste[9]}\nLokativ: {liste[10]}\nOrginativ: {liste[11]}\nDirektativ: {liste[12]}\nInstrumentativ: {liste[13]}\nPossessiv: {liste[14]}\nTotalitiv: {liste[15]}"
        return (resultsg + resultpl)

class Kasus:
    class sg:
        nom = "энзу"
        akk = "энио"
        lok = "эногōрт"
        org = "эногōиаλ"
        dir = "эногōиоλ"
        ins = "эногōба"
        pos = "эногōрy"
        tot = "эногōга"

        def dekl(wort):
            res = []
            res.append(wort + Kasus.sg.nom)
            res.append(wort + Kasus.sg.akk)
            res.append(wort + Kasus.sg.lok)
            res.append(wort + Kasus.sg.org)
            res.append(wort + Kasus.sg.dir)
            res.append(wort + Kasus.sg.ins)
            res.append(wort + Kasus.sg.pos)
            res.append(wort + Kasus.sg.tot)
            return res

    class pl:
        nom = "казу"
        akk = "каио"
        lok = "каогōрт"
        org = "каогōиаλ"
        dir = "каогōиоλ"
        ins = "каогōба"
        pos = "каогōрy"
        tot = "каогōга"

        def dekl(wort):
            res = []
            res.append(wort + Kasus.pl.nom)
            res.append(wort + Kasus.pl.akk)
            res.append(wort + Kasus.pl.lok)
            res.append(wort + Kasus.pl.org)
            res.append(wort + Kasus.pl.dir)
            res.append(wort + Kasus.pl.ins)
            res.append(wort + Kasus.pl.pos)
            res.append(wort + Kasus.pl.tot)
            return res

    def __init__():
        pass

class Wort:
    def __init__(self, wort, wortart):
        pass

class Substantiv:
    def __init__(self, inflekativ, wortart, ipa, definition, dekl):
        pass


while True:
    wrt = input("Zu deklinieren> ")
    print(fullformat("subst", dekl("subst", wrt)) + "\n")


def load():
    with open("liste.kaz", "r") as f:
        for lines in f:
            pass