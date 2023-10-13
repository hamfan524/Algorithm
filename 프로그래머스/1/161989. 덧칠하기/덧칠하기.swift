import Foundation

func solution(_ n: Int, _ m: Int, _ section: [Int]) -> Int {
    var answer = 1
    var tmp = section[0] + m
    for i in 1..<section.count {
        if section[i] < tmp {
            continue
        }
        tmp = section[i] + m
        answer += 1
    }
    return answer
}