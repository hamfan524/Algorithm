let S = Int(readLine()!)!
var sum = 0
var n = 1
while true{
    sum += n
    if sum > S { break }
    n += 1
}
print(n-1)