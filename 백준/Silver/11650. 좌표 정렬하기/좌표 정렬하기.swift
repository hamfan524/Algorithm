let n = Int(readLine()!)!
var result = [(Int, Int)]()

for _ in 0..<n{
    let inputValues = readLine()!.split(separator: " ").map{ Int($0)!}
    result.append((inputValues[0], inputValues[1]))
}
result.sort(by: {$0.0 == $1.0 ? $0.1 < $1.1 : $0.0 < $1.0})

for i in result{
    print(i.0, i.1)
}
