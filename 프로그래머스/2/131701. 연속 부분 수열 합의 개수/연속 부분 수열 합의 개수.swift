import Foundation

func solution(_ elements:[Int]) -> Int {
    let n = elements.count
    var setArr = Set<Int>()

    for i in 0..<n {
        var sum = 0
        for j in 0..<n {
            sum += elements[(i + j) % n]
            setArr.insert(sum)
        }
    }
    
    return setArr.count
}