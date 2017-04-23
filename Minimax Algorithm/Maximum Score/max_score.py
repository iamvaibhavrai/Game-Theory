def minimax(depth,nodeIndex,isMax,l,h):
    if h == depth:
        return l[nodeIndex]
    if isMax:
        return max(minimax(depth+1,nodeIndex*2,False,l,h),minimax(depth+1,(nodeIndex*2)+1,False,l,h))
    else:
        return min(minimax(depth+1,nodeIndex*2,True,l,h),minimax(depth+1,(nodeIndex*2)+1,False,l,h))

def log2(n):
    return 0 if n ==1 else 1+log2(n//2)

def main():
    l = [3,5,2,9,12,5,23,23]
    h = log2(len(l))
    res = minimax(0,0,True,l,h)
    print(res)


if __name__ == '__main__':
    main()
