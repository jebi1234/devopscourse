def man(num):
        if num<=0:
                return False
        return man(num-1)
print(man(5))
