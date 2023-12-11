while True:
    n, d = input().split()
    y = []
    ans = 'no'
    dinner = [0] * int(n)

    if n == '0' and d == '0':
        break

    for i in range(int(d)):
        y.append([int(x) for x in input().split()])

        for _ in range(int(n)):
            if y[i][_] == 1:
                dinner[_] += 1

    if dinner.count(int(d)) > 0:
        ans = 'yes'

    print(ans)