strikevalue = 15000
nostrikes = 11
underlying_value = []
middle_list = {1:3,2:5, 3:7, 4:9, 5:11} 
middle_val =   next((k for k in middle_list if middle_list[k] == nostrikes), None)
minus_val = 100
plu_val = 100
for i in reversed(range(middle_val)):
    print(i)
    underlying_value.insert(i, strikevalue-minus_val)
    minus_val = minus_val + 100
underlying_value.insert(middle_val, strikevalue)
for j in range((nostrikes-(middle_val+1))):
    #print(j)
    underlying_value.insert((middle_val+j+1), strikevalue+plu_val)
    plu_val = plu_val + 100
print(underlying_value)