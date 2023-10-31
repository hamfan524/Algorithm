import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    var numA = a
    var numB = b
    var answer = 0
    while numA != numB {
        numA = numA % 2 == 1 ? numA / 2 + 1 : numA / 2
        numB = numB % 2 == 1 ? numB / 2 + 1 : numB / 2
        answer += 1
    }
    return answer
}