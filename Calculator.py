class Calculator:

    def add(self,a,b):
        return a+b

    def sub(a,b):
        if a<b:
            return -(b-a)
        else:
            return a-b

    def mul(a,b):
        return a*b

    def div(a,b):
        return a/b if b!=0 else print("zero division error")
        
    def sqrt(a):
        import math
        return math.sqrt(a)
        
    def perct(a):
        x=int(input("enter the percentage"))
        output=(a*x)/100
        return output

if __name__== '__main__':
    #empty array    
    arr = []
    
    # enter the first number    
    a=int(input("enter any number: "))
    
    arr.append(a) # appended first number in the array
    
    #enter the operator needed    
    op=input("enter the operator (+,-,*,/,sqt,%,M-,M+): ")
    
    # if these operator ,it can do sum,sub,mul and div    
    if op== '+' or op=='-' or op== '*' or op=='/':
        
            #check how many numerics to do the operation.            
            num = int(input('how many numbers to operate?'))           
            
            #if its more than 2
            if num >2 and (op== '+' or op=='-' or op== '*' or op == '/') :
                
                for nums in range(1,num): 
                    z = input("enter the numbers:")
                    if z.isdigit():                                               
                        arr.append(int(z))
                        print(arr)
                    continue
                    
                if len(arr) == num:
                    y = input("Enter =")                    
                    if y =='=':
                        if  op=='+':
                            #return sum(arr)
                            sum=0
                            for items in arr:
                                sum +=items
                            c= sum                              
                                    
                        elif op=='-':
                            sub = 0
                            for items in arr:
                                sub -=items
                            c=sub                                   
                    
                        elif op =='*':
                            mul = 0
                            for items in arr:
                                mul *=items
                            c= mul 
                        elif op =='/':
                            for items in arr:
                                div /= items if items!=0 else print("zero division error")   
                        else:
                            print("Not Valid Operations")
                    elif y == '+' or y=='-' or z== '*' or y=='/' or y == '%' or y=='M-' or y=='M+':
                        print("Not valid operations")                           
                                            
            elif num==2:
                    b=int(input("enter any number: "))
                
                    c=0
                    #if + comes the numbers has to added
                    #if - comes the numbers has to subtracted
                    #if * comes the numbers has to multiplied
                    #if / comes the numbers has to divided
                    if op =='+':
                        c=Calculator.add(a,b)
                    elif op =='-':
                        c=sub(a,b)
                    elif(op =='*'):
                        mul(a,b)
                    elif(op =='/'):
                        c=div(a,b)          
                    else:print("other operations are not supported")
            elif num <2:
                c=a                
            else:
                print("Not valid")                
    elif(op =='sqt'):
        c=sqrt(a)
    elif(op =='%'):
        c=perct(a)
    
            
print(c)

      