import Foundation

func solution(_ n:Int) -> Int
{
    func countOnes(_ num: Int) -> Int {
        var count = 0
        var num = num
        while num > 0 {
            if num % 2 == 1 {
                count += 1
            }
            num /= 2
        }
        return count
    }
    
    let targetCount = countOnes(n)
    var nextNumber = n + 1
    
    while countOnes(nextNumber) != targetCount {
        nextNumber += 1
    }
    
    return nextNumber
}