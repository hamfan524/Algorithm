func solution(_ s: String) -> [Int] {
    var binaryTransformCount = 0
    var removedZeroCount = 0
    var currentString = s
    
    while currentString != "1" {
        let zeroCount = currentString.filter { $0 == "0" }.count
        removedZeroCount += zeroCount
        let length = currentString.count - zeroCount
        currentString = String(length, radix: 2)
        binaryTransformCount += 1
    }
    
    return [binaryTransformCount, removedZeroCount]
}