import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var answer = ""
    
    let numsX = Dictionary(X.map { ($0, 1) }, uniquingKeysWith: +)
    let numsY = Dictionary(Y.map { ($0, 1) }, uniquingKeysWith: +)
    print(numsX)
    print(numsY)
    
    let commonKeys = Set(numsX.keys).intersection(numsY.keys)
    
    if commonKeys.isEmpty {
        return "-1"
    } else if Array(commonKeys) == ["0"] {
        return "0"
    }
    let sortedKeys = commonKeys.sorted(by: >)
    for key in sortedKeys {
        if let countX = numsX[key], let countY = numsY[key] {
            let minCount = min(countX, countY)
            answer += String(repeating: key, count: minCount)
        }
    }
    return answer
}