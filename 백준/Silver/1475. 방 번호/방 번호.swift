let n = String(readLine()!)
var num: [Int] = Array(repeating: 0, count: 10)

for i in n{
    num[Int(String(i))!] += 1
}
num[6] = (num[6] + num.removeLast() + 1) / 2
print(num.max()!)
