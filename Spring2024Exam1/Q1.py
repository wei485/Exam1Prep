#PartA
for x in range(0, 7):
    if x == 3 or x == 6:
        continue
    print(x)

#PartB
def vowel_counter(str):
    vowel_count=0
    vowels = "aeiou"
    for char in str:
        if char in vowels:
            vowel_counter+=1
    if vowel_counter == 0:
        print("No Vowels") 
    else:
        print(vowel_counter)

#PartC
def find_warm_days(temp, threshold):
    warm_days = 0
    for i in range(len(temp)-1):
        if temp(i) >= threshold and temp(i + 1) >= threshold:
            warm_days += 1
    print(warm_days)