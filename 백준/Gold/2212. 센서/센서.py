def solve(n, k, sensors):
    sensors.sort()
    distances = []

    for i in range(1, n):
       distances.append(sensors[i] - sensors[i - 1])
    distances.sort()

    for i in range(1, k):
        distances[-i] = 0

    return sum(distances)

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

if n <= k:
    print(0)
    exit()
print(solve(n, k, sensors))