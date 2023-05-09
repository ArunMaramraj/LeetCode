class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        output = ""
        
        st = []
        
        flag=0
        
        i=0
        while i< len(s):
            
            if(s[i]=='('):
                flag = 1 if flag == 0 else flag
                st.append(s[i])
                
                
            elif(s[i]==')' and flag==1):
                temp= ""
                while(st[-1]!='('):
                    temp+=st.pop()
                st.pop()
                if len(st)==0:
                    flag=0   
                    output+=temp
                else:
                    [st.append(temp[i]) for i in range (len(temp))]
            
            else:
                if(flag==0):
                    output+=s[i]
                else:
                    st.append(s[i])
                
            i+=1
        
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        