import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    var answer = 0
    var fruits = [String: Int]()
    
    for (index, char) in want.enumerated() {
        fruits[char] = number[index]
    }
    
    for i in 0..<discount.count-9 {
        let subString = discount[i..<i+10]
        
        var check = [String: Int]()
        for char in subString {
            check[char, default: 0] += 1 
        }
        if fruits == check {
            answer += 1
        }
    }
    
    return answer
}