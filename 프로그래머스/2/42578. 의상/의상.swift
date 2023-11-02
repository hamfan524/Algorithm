import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dic = [String: Int]()
    for cloth in clothes {
        if let type = cloth.last {
            dic[type, default: 0] += 1
        }
    }
    var answer = 1
    for value in dic.values {
        answer *= (value + 1)
    }
    return answer - 1
}