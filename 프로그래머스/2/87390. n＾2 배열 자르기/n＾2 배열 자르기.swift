import Foundation

func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
    var answer: [Int] = []
    let l = Int(left)
    let r = Int(right)
    for i in l...r {
        answer.append(max(i/n, i%n) + 1)
    }
    return answer
}