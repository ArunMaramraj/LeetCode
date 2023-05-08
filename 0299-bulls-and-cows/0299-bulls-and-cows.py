class Solution:
    def getHint(self, secret: str, guess: str) -> str:


        dic = {}
        cows = 0
        bulls = 0

        output = ""

        #knowing the number of bulls initially

        for i in secret:
            if(dic.get(i)):
                dic[i]+=1
            else:
                dic[i] = 1
        
        for i in range (len(secret)):
            if(secret[i] == guess[i]):
                bulls+=1

        for i in range (len(guess)): 
            if(secret[i] == guess[i] and dic[guess[i]]>0):
                if(dic[guess[i]]>0):
                    dic[guess[i]]-=1

        for i in range (len(guess)):
            if(secret[i]!=guess[i] and dic.get(guess[i]) and dic[guess[i]] >0):
                dic[guess[i]]-=1
                cows+=1           

        output = str(bulls) + "A" + str(cows) + "B"
        return output


        




















            
