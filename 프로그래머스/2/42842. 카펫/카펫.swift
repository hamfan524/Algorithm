import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    let num = brown + yellow
    for i in (2...num).reversed() {
        let a = num / i
        if yellow == (i - 2) * (a - 2) {
            return [i, a]
        }
    }
    return [0]
}