let X = Int(readLine()!)!
let n = Int(readLine()!)!
var sum = 0
for _ in 0..<n{
    var a = readLine()!.split(separator: " ").map{ Int($0)! }
    sum += a[0] * a[1]
}
if X == sum{
    print("Yes")
}else{
    print("No")
}
