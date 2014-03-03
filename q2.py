class A(list):
    def __init__(self):
        list.__init__([])
    def new(self):
        n=0
        while(n < 2):
            try:
                peoplelist.append({"name":(raw_input("name: ")), "year":input("year: ")})
            except:
                print("error")
            n+=1
 
peoplelist=A()
peoplelist.new()
print("n1")
n1=0
for v in sorted(peoplelist):
    if n1<1:
        print(v['name']+' '+str(v['year']))
        n1+=1
print("n2")
n2=0
for v in sorted(peoplelist,reverse=True):
    if n2<1:
        print(v['name']+' '+str(v['year']))
        n2+=1

    
