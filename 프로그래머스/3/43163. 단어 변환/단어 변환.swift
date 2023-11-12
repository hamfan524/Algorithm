func canTransform(_ word1: String, _ word2: String) -> Bool {
    var diffCount = 0
    for (char1, char2) in zip(word1, word2) {
        if char1 != char2 {
            diffCount += 1
            if diffCount > 1 {
                return false
            }
        }
    }
    return diffCount == 1
}

func solution(_ begin: String, _ target: String, _ words: [String]) -> Int {
    guard words.contains(target) else { return 0 }
    
    var visited = Set<String>()
    var queue = [(begin, 0)]
    
    while !queue.isEmpty {
        let (currentWord, steps) = queue.removeFirst()
        
        if currentWord == target {
            return steps 
        }
        
        visited.insert(currentWord)
        
        for word in words {
            if canTransform(word, currentWord) && !visited.contains(word) {
                queue.append((word, steps + 1))
            }
        }
    }
    return 0
    
}
