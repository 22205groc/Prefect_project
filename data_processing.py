alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
data_in = [["harold","dave","albert","danial","auther","ben","dylan"],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[["bunking"],["sent out","bunking"],["bunking","bunking","late"],["rep","late","sent out","rep"],["sent out","late","late","rep","sent out"],["late","late","rep","rep","rep","rep"],["rep","rep","rep","late","late","sent out","late"]]] # names(str), Hp(int), Bp(int), Bp reasons(2d)(str)
#sort data using bubble sort
# Thomas' test
i = 0
swaps = True
while swaps == True:
    swaps = False
    for name_ndx in range(len(data_in[0])):
        if name_ndx < len(data_in[0])-1:
            for letter_ndx in range(len(data_in[0][name_ndx])):
                if alphabet.index(data_in[0][name_ndx][letter_ndx]) > alphabet.index(data_in[0][name_ndx+1][letter_ndx]):
                    name_x = data_in[0][name_ndx]
                    hp_x = data_in[1][name_ndx]
                    bp_x = data_in[2][name_ndx]
                    reasons_x = data_in[3][name_ndx]
                    data_in[0][name_ndx] = data_in[0][name_ndx+1]
                    data_in[1][name_ndx] = data_in[1][name_ndx+1]
                    data_in[2][name_ndx] = data_in[2][name_ndx+1]
                    data_in[3][name_ndx] = data_in[3][name_ndx+1]
                    data_in[0][name_ndx+1] = name_x
                    data_in[1][name_ndx+1] = hp_x
                    data_in[2][name_ndx+1] = bp_x
                    data_in[3][name_ndx+1] = reasons_x
                    swaps = True
                    break
                elif alphabet.index(data_in[0][name_ndx][letter_ndx]) < alphabet.index(data_in[0][name_ndx+1][letter_ndx]):
                    break
    i += 1
    #print(f"pass number {i}: {data_in}")
print(f"sorted: {data_in[0]}\n{data_in[1]}\n{data_in[2]}\n{data_in[3]}\n")
