#prefiksi = {6:"miljons",5:""}
skaitli = {0:"",
          1:" viens",
          2:" divi",
          3:" trīs",
          4:" četri",
          5:" pieci",
          6:" seši",
          7:" septiņi",
          8:" astoņi",
          9:" deviņi",
          10:" desmit"
          }

def skaitlavards():
    saraksts = []
    rezultats = ""

    inputs = input("Skaitlis: \n")
    for x in inputs.zfill(7):
        saraksts.append(int(x))

    for i in range(len(saraksts)):
        rezultats += skaitli[saraksts[i]]

    print(saraksts,'\n'+10*'-')
    
    #darbojamies, prefixi!

    if saraksts[0] != 0:
        saraksts[0] += " miljons"
    if saraksts[1] != 0:
        saraksts[1] += ""


skaitlavards()


"""def pipucik():
    ipt = input("Skaitlis: ")
    garums = len(ipt)
    rezultats = []

    if garums >= 7:
        rezultats.append(skaitli[ipt[0]] + " miljons ")
    if garums >= 6:
        rezultats.append(skaitli[ipt[0]]) + "simt tūkstoši"
    elif garums >= 5:"""


"""def func(cip):
    
    rezultats = ""

    if cip >= 1000000:
        rezultats += skaitli[cip // 1000000] + " miljons "
        cip %= 1000000

    if cip >= 100000:
        rezultats += skaitli[cip / 100000].lstrip("viens").lstrip(len(cip)) + "simti tūkstoši"
       #cip %= 100000
    
    if cip >= 10000:
        rezultats += skaitli[cip / 10000] + "desmit tūkstoši"

    print(rezultats)


func(int(input("Skaitlis: ")))"""
