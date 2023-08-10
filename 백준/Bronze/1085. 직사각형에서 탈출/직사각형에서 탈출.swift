var arr = readLine()!.split(separator: " ").map{ Int($0)! }
arr[2] = arr[2] - arr[0]
arr[3] = arr[3] - arr[1]

var temp = arr[0]
for i in 1..<arr.count{
    if temp > arr[i]{
        temp = arr[i]
    }
}

print(temp)
