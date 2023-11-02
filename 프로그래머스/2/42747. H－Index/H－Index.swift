import Foundation

func solution(_ citations:[Int]) -> Int {
    let sortedCitations = Array(citations.sorted().reversed())
    for i in 0..<sortedCitations.count {
        if sortedCitations[i] < i + 1 {
            return i
        }
    }
    return sortedCitations.count
}