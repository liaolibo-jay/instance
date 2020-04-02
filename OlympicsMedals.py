import os

class medal:
    nation_name = 'china'
    nglodens = 0
    nslivers = 0
    nbronzes = 0
    totScore = 0
    
    def addmedals(self):
        nranks = int(input('请输入%s名次:' %(self.nation_name)))
        if nranks == 1:
            self.nglodens += 1 
        elif nranks == 2:
            self.nslivers += 1
        elif nranks == 3:
            self.nbronzes += 1
        else:
            pass
        self.totScore =self.nbronzes+self.nslivers+self.nglodens

    def outmedals(self):
        print('%s的奖牌数为:金牌%i块，银牌%i块，铜牌%i块。总数为%i.'%(self.nation_name,self.nglodens,self.nslivers,self.nbronzes,self.totScore))

acountry = []
NumCountry =0
while True:
    name = input('请输入一个国家名：')
    if not name:
        break
    else:
        acountry.append(medal())
        acountry[NumCountry].nation_name = name
    NumCountry += 1

while True:
    inMedal = input('是否更新奖牌情况（输入y或者n）:')
    if inMedal == 'n':
        break
    elif inMedal == 'y':
        for i in acountry:
            i.addmedals()
        acountry = sorted(acountry,key=lambda medal:(medal.totScore,medal.nglodens,medal.nslivers,medal.nbronzes) ,reverse=True)
        
        for i in acountry:
            i.outmedals()
    else:
        break
