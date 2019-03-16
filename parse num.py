def parse_number(n):
    if type(n) != int:
        return False
    dict_={'even':0 , 'odd':0}
    odd=0
    even=0
    for i in str(n):
        if int(i) % 2 == 0:
            odd+=1
        else:
            even+=1
    dict_['odd'] = odd
    dict_['even'] = even
    return dict_

print(parse_number(34567))
print(parse_number(100))
print(parse_number("word"))
        
