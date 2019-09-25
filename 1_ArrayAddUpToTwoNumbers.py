def sumOfTwoInArray(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                print(f'{arr[i]} and {arr[j]} make {sum}')

sumOfTwoInArray([1,2,3], 3)
sumOfTwoInArray([10,15,3,7], 17)
sumOfTwoInArray([-4,0,2.3,7,4], 0)
