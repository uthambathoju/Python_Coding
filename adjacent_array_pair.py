
def get_closest_elements(ar_1 , ar_2 , target):
    ar_1.sort()
    ar_2.sort()
    inc_counter = 0
    dec_counter = len(ar_2) -1
    init_sub_value = abs(ar_1[0] + ar_2[0] - target)
    result = (ar_1[0] , ar_2[0])
    while(inc_counter < len(ar_1) and dec_counter >= 0):
        ar1_ele = ar_1[inc_counter]
        ar2_ele = ar_2[dec_counter]
        latest_sub_value = ar1_ele + ar2_ele - target
        if(abs(latest_sub_value) < init_sub_value):
            init_sub_value = abs(latest_sub_value)
            result = (ar1_ele , ar2_ele)

        if(abs(latest_sub_value) == 1):
            result = (ar1_ele , ar2_ele)
            return result
        elif(latest_sub_value < 0):
            inc_counter += 1
        else:
            dec_counter -= 1
    return result

    
if __name__ == "__main__":
    ar_1 = list(map(int, input().rstrip().split()))
    ar_2 = list(map(int, input().rstrip().split()))
    target = int(input())
    result = get_closest_elements(ar_1 , ar_2 , target)
    print(result)
    