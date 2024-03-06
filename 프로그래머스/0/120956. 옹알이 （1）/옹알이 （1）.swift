import Foundation

func solution(_ babbling:[String]) -> Int {
    var babbling = babbling
    var result = 0
    for i in 0..<babbling.count{  
        babbling[i] = babbling[i].replacingOccurrences(of: "aya", with: "1")
        babbling[i] = babbling[i].replacingOccurrences(of: "ye", with: "1")
        babbling[i] = babbling[i].replacingOccurrences(of: "woo", with: "1")
        babbling[i] = babbling[i].replacingOccurrences(of: "ma", with: "1")
        babbling[i] = babbling[i].replacingOccurrences(of: "1", with: "")
        
        if babbling[i].count == 0{
            result += 1
        }
    }
    return result
}