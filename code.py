def boardCutting(cost_y, cost_x):
    row=1
    col=1
    count=0
    l=sorted(cost_y,reverse=True)
    k=sorted(cost_x,reverse=True)
    for _ in range(len(cost_y)+len(cost_x)):
        if (l!=[] and k!=[] and l[0]>=k[0]) or (k==[] and l!=[]):
            count+=row*l[0]
            col+=1
            l.remove(l[0])
        elif (k!=[]) or (l==[] and k!=[]):
            count+=col*k[0]
            row+=1
            k.remove(k[0])
    return (count)%(pow(10,9)+7)

