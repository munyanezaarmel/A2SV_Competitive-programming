class Solution(object):
    def fizzBuzz(self, n):
        fizz=[]
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                i="FizzBuzz"
                fizz.append(i)
            elif(i%3==0):
                i="Fizz"
                fizz.append(i)
            elif(i%5==0):
                i="Buzz"
                fizz.append(i)
            else:
                i==i
                fizz.append(str(i))
        return fizz