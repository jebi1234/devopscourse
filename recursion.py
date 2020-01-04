def human(num):
        if(num==1):
                return 1*50
        else:
                return num*(50)+human(num-1)
        
        
        
        
print("total weight of humans: ",human(10))
