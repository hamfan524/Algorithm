import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var answer = 0
    var tmp = 0
    var n = n
    while n >= a {
        answer += Int(n / a) * b
        n = (Int(n / a) * b) + (n % a)
    }
    return answer
}
