import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    let sortedA = A.sorted() 
    let sortedB = B.sorted(by: >)
    
    var result = 0
    for i in 0..<sortedA.count {
        result += sortedA[i] * sortedB[i]
    }
    
    return result
}