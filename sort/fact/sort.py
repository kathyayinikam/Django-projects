def sort():
   list1=[2,6,7,8,3,1]
   
   leng=len(list1)
   for i in range(1, leng):
        j = i
        while j > 0 and list1[j] < list1[j - 1]:
            temp = list1[j]
            list1[j] = list1[j - 1]
            list1[j - 1] = temp
            j -= 1
    
   return list1

  