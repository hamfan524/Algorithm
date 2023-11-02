import Foundation

func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    let row1 = arr1.count
    let column1 = arr1[0].count
    let column2 = arr2[0].count
    var answer = Array(repeating: Array(repeating: 0, count: column2), count: row1)
    
    for i in 0..<row1 {
        for j in 0..<column2 {
            for k in 0..<column1 {
                answer[i][j] += arr1[i][k] * arr2[k][j]
            }
        }
    }
    
    return answer
}