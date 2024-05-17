def lower_triangular(n):
    for i in range(1,n+1):
        print('*' * i)


n = int(input("Enter the number of rows for lower triangular pattern: "))
lower_triangular(n)