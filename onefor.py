a=[[22,'dustin'],[28,'yuppy'],[31,'lubber'],[31,'lubber2'],[44,'guppy'],[58,'rusty']]
b=[[28,103],[28,104],[31,101],[31,102],[42,142],[58,107]]

a=[
['106rallye','3000'],
['audi tt','10000'],
['bmw x5','30000'],
['cupra','15000'],
['cupra','15500']
]

b=[
['cupra','timoni'],
['cupra','kathismata'],
['drill','kathismata'],
['drill','rkioszpe'],
['drill','vatomourada'],
['drill','narkwtikes ousies']]

sorted(a,key=lambda l:l[0], reverse=True)
sorted(b,key=lambda l:l[0], reverse=True)

print(a)
print(b)

c=[]
i = 0
j = 0
while (True):
    left_value = a[i][0]
    right_value = b[j][0]
    if left_value == right_value:
        c.append([a[i][0],  a[i][1], b[j][0],  b[j][1]])
        j += 1
    elif left_value > right_value:
        if i == len(a)-1 and j == len(b)-1:
            break
        j += 1

    elif left_value < right_value:
        i += 1
        if(i<=len(a)-1):
            while (True and j >= 1):
                if a[i][0] <= b[j - 1][0]:
                    j -= 1
                else:
                    break
        else:
            break

print(c)
