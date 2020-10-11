# fizz="FIZZ"
# buzz="BUZZ"
# for i in range(100):
#     if i%3==0:
#         if i%5==0:
#             print(f"{i} -> {fizz}{buzz}")
#         else:
#             print(f"{i} -> {fizz}")
#     elif i%5==0:
#         print(f"{i} -> {buzz}")
#     else:
#         print(f'{i} ->')

fizz="FIZZ"
buzz="BUZZ"
for i in range(100):
    if i%3==0 or i%5==0:
        if i%3==0 and i%5!=0:     
            print(f"{i} -> {fizz}")
        elif i%5==0 and i%3!=0:
            print(f"{i} -> {buzz}")
        else:
           print(f"{i} -> {fizz}{buzz}")
    else:
        print(f'{i} ->')             


print("---------------------")
for i in range(100):
    out = ''
    if i % 3 == 0:
        out += 'fizz'
    if i % 5 == 0:
        out += 'buzz'
    
    if out == '':
        print(i)
    else:
        print(out)