def zeros(n):
    fat = n
    count = 0
    for x in range(2, n+1):
        while fat%10==0:
            fat//=10
            count+=1
        fat*=x
    return count


if __name__ == "__main__":
    print(zeros(1000))