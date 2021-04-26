file_name='random_nums.txt'

def counten():
    f=open(file_name,"r")
    texten=f.read()
    f.close()
    return len(texten.split("\n"))
        
def summan():
    summa=0
    with open(file_name,"r") as f:
        for line in f:
           summa=summa+int(line)
    return summa

def averagen():
    return summan()/counten()

def minmaxen():
    isFirst=True
    minnen=None;
    maxen=None;
    with open(file_name,"r") as f:
        for line in f:
            talet=int(line)
            if isFirst:
                minnen=talet
                maxen=talet
                isFirst=False
            if talet<minnen:
                minnen=talet
            if talet>maxen:
                maxen=talet
    return minnen,maxen

if __name__ == '__main__':
    print(counten())
    print(summan())
    print(averagen())
    minnen,maxen=minmaxen()
    print(minnen)
    print(maxen)

