def selection_sort(mylist):
  n = len(mylist)
  for i in range(n-1):
    min = i
    for j in range(i+1,n):
      if (mylist[j] < mylist[min]):
        min = j
    
    temp = mylist[i]
    mylist[i] = mylist[min]
    mylist[min] = temp
    print(mylist)

  return mylist


print('***Enter a letter to end list***\nEnter the elements of the list: \n')

try:
  ll1 = []

  while True:
    ll1.append(int(input()))

except:
  pass


selection_sort(ll1)

print('The sorted list is : \n',ll1)