class Main:
    def function_name():
        char=['a','a','b','b','c','d']
        seen={}

        for i,c in enumerate(char):
            if c not in seen:
                seen[c]=1
                print(c+str(seen[c]),end="")
            else:
                seen[c]+=1
                print(c+str(seen[c]),end="")
            if i!=len(char)-1:
                print(",",end="")
                
                
Main.function_name()