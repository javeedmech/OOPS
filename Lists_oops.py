# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) ,
# {"key1" :"sudh" , 234:[23,45,656]}]
# 1 . Try to reverse a list
# 2. try to access 234 out of this list
# 3 . try to access 456
# 4 . Try to extract only a list collection form list l
# 5 . Try to extract "sudh"
# 6 . Try to list all the key in dict element avaible in list
# 7 . Try to extract all the value element form dict available in list

import logging as logg
logg.basicConfig(filename="Lists.txt", level=logg.INFO,format=' %(levelname)s : %(message)s')

class LST:

    def reverse(self, l):
        logg.info(" the revers of List \n %s \n is \n  %s  ", l, l[::-1])

    def access(self,n,l):
        for i in l:
            if i==n:
                logg.info(" the index of %s is %s", n, i)
            elif type(i)==list:
                for j in i:
                    if j==n:
                        logg.info("we can access %s inside the sub-list %s", n, i )
            elif type(i)==tuple:
                for k in i:
                    if k==n:
                        logg.info("we can access %s inside the tuple %s", n, i)

    def accessl(self, l,val):
        logg.info("all the lists inside the passed list %s are \n",l)
        for i in l:
            if type(i)==list:
                logg.info(i)
            elif type(i)==dict:
                for j in i.values():
                    if type(j)==list:
                         logg.info("lists inside  dictionary are \n %s", j)
        for v in l:
            if type(v)==dict:
                for w in v.values():
                    if w==val:
                         logg.info("we can access the value %s inside dictionary %s ", val,v )
        for i in l:
            if type(i) == dict:
                logg.info("all the keys of the dictionary are \n %s", i.keys())
                logg.info("all the values of the dictionary are \n %s", i.values())

obj=LST()
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656],"k2":23}]
obj.reverse(l)
obj.access(234,l)
obj.access(456,l)
obj.accessl(l,"sudh")