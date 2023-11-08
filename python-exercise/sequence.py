"""def arr_list(nums):
    num=""
    for i in nums:
        num = num + str(i)
   
        if "123" in num:
            return True
        else:
            return False
print(arr_list([1,1,2,3,1,4]))"""


def array_check(element):
    value=[1,2,3]
    for i in range (0,len(element)):
      sublist = element[i:i+3]
      if value==sublist:
        return True
      else:
          continue
    return False

print(array_check([1,3,1,4,1,2,3]))
print(array_check([1,3,1,4,1,2]))





    
   

  

   




    


  