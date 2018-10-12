def get_indices_of_item_weights(weights, limit):
  return (); 

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 


def get_indices_of_item_weights(arr, limit):
  
  list1 = list(range(len(arr)))
  #print(list1)
  #print(arr)
  dictionary = dict(zip(arr,list1))
  #print(dictionary)
  
  dict_keys = dictionary.keys()
  if len(arr) <= 1 :
    return ()
  else:
    for key in dict_keys:
      weight = limit - key
      if weight in (dict_keys):
        #print(dictionary[weight],dictionary[key])
        return (dictionary[weight],dictionary[key])
   


  

#arr = [4]
#arr = [4, 6, 10, 15, 16]
#limit = 21
# arr = [4,4]
# limit = 8
# get_indices_of_item_weights(arr, limit)

  # dict = {}
  # for(let i=0; i< arr.length; i++):
  #   if(dict[arr[i]] !== undefined):
  #     return tuple([i, dict[arr[i]]])
  #   }else{
  #     dict[limit - arr[i]] = i
  #   }
  # }
  # return ()


# arr = [4,4];
# limit = 8;
# let x = getIndicesOfItemWeights(arr, limit);
# console.log(x)