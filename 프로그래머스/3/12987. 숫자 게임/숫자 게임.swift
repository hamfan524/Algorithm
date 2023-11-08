import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var answer = 0
    var index = 0
    var teamA = a
    var teamB = b
    teamA.sort()
    teamB.sort()
    
    for num in teamB {
        if num > teamA[index] {
            answer += 1
            index += 1
        }
    }
    
    return answer
}