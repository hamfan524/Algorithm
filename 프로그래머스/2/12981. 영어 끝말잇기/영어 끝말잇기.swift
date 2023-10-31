import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var usedWords: [String] = []
    var lastAlphabet = words[0].first
    for i in 0..<words.count {
        if usedWords.contains(words[i]) || lastAlphabet != words[i].first {
            return [i%n+1, i/n+1]
        }
        usedWords.append(words[i])
        lastAlphabet = words[i].last
    }
    return [0, 0]
}