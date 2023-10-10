import Foundation

func solution(_ n:Int) -> Int
{
    var target = n.nonzeroBitCount
    var nextNumber = n + 1
    
    while target != nextNumber.nonzeroBitCount {
        nextNumber += 1
    }
    
    return nextNumber
}