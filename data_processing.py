alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
data_in = [["harold","dave","albert","danial","auther","ben","dylan"],[],[],[]] # names(str), Hp(int), Bp(int), Bp reasons(2d)(str)
#sort data
i = 0
swaps = True
while swaps == True:
    swaps = False
    for name_ndx in range(len(data_in[0])):
        if name_ndx < len(data_in[0])-1:
            for letter_ndx in range(len(data_in[0][name_ndx])):
                if alphabet.index(data_in[0][name_ndx][letter_ndx]) > alphabet.index(data_in[0][name_ndx+1][letter_ndx]):
                    name_1 = data_in[0][name_ndx]
                    data_in[0][name_ndx] = data_in[0][name_ndx+1]
                    data_in[0][name_ndx+1] = name_1
                    swaps = True
                    break
                elif alphabet.index(data_in[0][name_ndx][letter_ndx]) < alphabet.index(data_in[0][name_ndx+1][letter_ndx]):
                    break
    i += 1
    print(f"pass number {i}: {data_in}")
print(f"sorted: {data_in}")
