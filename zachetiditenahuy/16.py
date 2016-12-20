def kolichestvo(n):
    K=[0,1]+[0]*(n-1)
    for i in range(2, n+1):
        K[i]=K[i-1]+K[i-2]
    return K[n]

Price=[1, 4, 5, 2, 5]

def stoimost(n, Price):
    C=[float('+inf'), Price[1]]+[None]*(n-1)
    for i in range(2, n+1):
        C[i]=Price[i-1] + min(C[i-1], C[i-2])
    return C


def shortest_path(n, Costs):
    path=[n]
    while path[-1] != 1:
        current = path[-1]
        k=current
        if Costs[k-1] < Costs[k-2]:
            path.append(k-1)
        else:
            path.append(k-2)
    path[:]=path[::-1]
    return path

Costs=stoimost(5,Price)

print(shortest_path(5, Costs))
