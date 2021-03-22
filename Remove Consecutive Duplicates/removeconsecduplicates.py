def removeConsecutiveDuplicates(str_):
    arr=[]
    for i in str_:
        arr.append(i)
        
    if len(arr)>1:
        i = 0
        j = 1
        new_arr = []
        while i < len(arr) and j< len(arr):
            
            if arr[i] !=arr[j]:
                new_arr.append(arr[i])
                i = j
                j+=1
                #print(j)
                if j == len(arr):
                    #print("asdf")
                    new_arr.append(arr[i])
                    break
                    

            
            elif arr[i] == arr[j]:
                j+=1
                
                if j == len(arr):
                    new_arr.append(arr[i])
                    break
    
        
        return new_arr
    
    else:
        return str_
    
inputString = input()
result = removeConsecutiveDuplicates(inputString)
for data in result:
    print("".join(data),end = "")