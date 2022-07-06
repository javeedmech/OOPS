
import logging
logging.basicConfig(filename="prime.txt", level=logging.INFO,format='%(asctime)s : %(levelname)s : %(message)s')
logging.info("Entred loging ")

class N:
    def askint(self):
        """ This function checks if the entered value is integer or not"""
        while True:
            try:
                a=int(input("Try to enter integer to get the prime numbers"))
                return a
                break
            except:
                print("Enter valid integer")
    def prime (self, a):
        """ This is a prime number function which takes value from askint function """
        l = []
        for i in range(2, a):
            k = 0
            for j in range(2, i):
                if i % j == 0:
                    k = k + 1
                    break
            if k == 0:
                l.append(i)
        logging.info(" the prime numbers with in 1 to  %s is : %s ", a, l)


obj=N()
obj.prime(obj.askint())

