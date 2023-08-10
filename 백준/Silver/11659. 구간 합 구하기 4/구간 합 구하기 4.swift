let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
let n = inputValues[0]
let m = inputValues[1]
let nums = readLine()!.split(separator: " ").map{ Int($0)! }
var sums = Array(repeating: 0, count: n+1)

for i in 1...n{
    sums[i] = sums[i-1] + nums[i-1]
}

for _ in 0..<m{
    let s = readLine()!.split(separator: " ").map{ Int($0)! }
    print(sums[s[1]]-sums[s[0]-1])
}