class Solution(object):
    def finalValueAfterOperations(self, operations):
            count=0
            for operation in range(len(operations)):
                if(operations[operation]=="--X"):
                      count-=1
                elif(operations[operation]=="X--"):
                        count-=1
                if(operations[operation]=="++X"):
                      count+=1
                if(operations[operation]=="X++"):
                    count+=1
            return count   
        