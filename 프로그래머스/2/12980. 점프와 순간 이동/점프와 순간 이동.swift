import Foundation

func solution(_ n:Int) -> Int 
{
    var num = n
    var result = 1
    while num != 1 {
        if num % 2 == 0 {
            num /= 2
        } else {
            num -= 1
            result += 1
        }
    }
    return result
}
