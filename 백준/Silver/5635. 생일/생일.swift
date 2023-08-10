typealias birth = (year: Int, month: Int, day: Int)
var data = [String: birth]()
for _ in 0..<Int(readLine()!)! {
    let inputValues = readLine()!.split(separator: " ").map{ String($0) }
    data[inputValues[0]] = (Int(inputValues[3])!, Int(inputValues[2])!, Int(inputValues[1])!)
}

print(data.sorted(by: {$0.value > $1.value})[0].key)
print(data.sorted(by: {$0.value < $1.value})[0].key)