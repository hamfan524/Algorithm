import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var students = Array(repeating:1, count: n)
    for l in lost {
        students[l-1] -= 1
    }
    for r in reserve {
        students[r-1] += 1
    } 
    
    for i in 0..<students.count {
        if students[i] == 0 {
            if i > 0 && students[i-1] == 2 {
                students[i-1] -= 1
                students[i] += 1
            } else if i < n-1 && students[i+1] == 2 {
                students[i+1] -= 1
                students[i] += 1
            }
        }
    }
    
    let answer = students.filter{ $0 > 0 }.count
    
    return answer
}