import Foundation

// func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
//     var answer: [Int] = []
//     let l = Int(left)
//     let r = Int(right)
//     for i in l...r {
//         answer.append(max(i/n, i%n) + 1)
//     }
//     return answer
// }

func solution(_ n:Int, _ left:Int64, _ right:Int64) -> [Int] {
    return (left...right).map { max(Int($0) / n, Int($0) % n) + 1 }
}