let n = Int(readLine()!)!
var A = readLine()!.split(separator: " ").map{ Int($0)! }
var B = readLine()!.split(separator: " ").map{ Int($0)! }

var answer = 0

A.sort()
B.sort{$0 > $1}

for i in 0..<n{
    answer += A[i] * B[i]
}

print(answer)
