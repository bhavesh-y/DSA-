def find_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    
    return False

numbers = [10,22,34,30,64,6,46,53,22,53,64]

result = find_duplicate(numbers)

if result:
    print("Dulplicate Found")

else:
    print("Not found")



    