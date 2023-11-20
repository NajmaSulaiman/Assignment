#Q1
Rockwell_hardness=int(input("enter Rockwell hardness: "))
Carbon_content=int(input("enter Carbon content: "))
Tensile_strength=int(input("enter Tensile strength in kg/cm2: "))

if(Rockwell_hardness > 50 and Carbon_content > 0.7 and Tensile_strength > 5600):
    print ("Grade is 10 ")
elif(Rockwell_hardness > 50 and Carbon_content > 0.7 ):
    print("Grade is 9 ")
elif(Carbon_content > 0.7 and Tensile_strength > 5600):
    print ("Grade is 8 ")
elif(Rockwell_hardness > 50  and Tensile_strength > 5600):
    print("Grade is 7 ")
else:
    print("Grade is 0 ")
    
    


#Q2
tuition = 10000    
years = 10  
i = 0  
current_year = 1
while(current_year <= years):
    tuition = tuition+(tuition * 0.05)  
    print("Tuition in year "+str(current_year)+": "+ "$"+str(tuition))
    
    
    if current_year <= 4:
        i+= tuition
    
    current_year += 1


print("Total cost for four years after the tenth year: $"+str(i))


    
#Q3    
a=8
for i in range(1, a+1):
    
    
    for j in range (a,i,-1):
        
        print(" ",end=" ")
    for j in range (1,i+1):
        x=2**(j-1)
        print(x,end=" ")
        
    for j in range (i-1 ,0 ,-1):
        x=2**(j-1)
        print(x,end=" ")
        
    print()
    
        
    
    
    
    
    
    

    