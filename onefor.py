a=[[22,'dustin'],[28,'yuppy'],[31,'lubber'],[31,'lubber2'],[44,'guppy'],[58,'rusty']]
b=[[28,103],[28,104],[31,101],[31,102],[42,142],[58,107]]

a=[
[2,'3000'],
[3,'10000'],
[4,'30000'],
[15,'15000'],
[15,'15500'],
[36,'15500'],
[72,'15500']
]

b=[
[1,'timoni'],
[5,'44kathismata'],
[12,'kathismata'],
[13,'rkioszpe'],
[14,'vatomourada'],
[15,'vatomourada2'],
[36,'narkwtikes ousies']]

sorted(a,key=lambda l:l[0], reverse=True)
sorted(b,key=lambda l:l[0], reverse=True)

#print(a)
#print(b)

c=[]
i = 0
j = 0
while (True):
    left_value = a[i][0]
    right_value = b[j][0]
    if left_value == right_value:
        c.append([a[i][0],  a[i][1], b[j][0],  b[j][1]])
        if j != len(b) -1:
            j += 1
        else:
            break
    elif left_value > right_value:
        if  j != len(b)-1:
            j += 1
        else:
            break

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
