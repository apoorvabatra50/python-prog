def bsearch(idx0,idxn,list,val):



    if (idx0>idxn):
        return None
    else:
        midval=(idx0+idxn)//2
        if(list[midval]==val):
            return midval+1;

        else:
            if(list[midval]>val):
               idxn =midval-1;
               return bsearch(idx0,idxn,list,val);
            elif(list[midval]<val):
                idx0= midval+1;
                return bsearch(idx0,idxn,list,val);



list=[]
print ("enter no. in range 5")
for i in range(0,5):
    p=int(input("enter no  "))
    list.append(int(p))




idx0=0
idxn=len(list)-1
print(bsearch(idx0,idxn,list,int(input("enter a no. to search its position"))))