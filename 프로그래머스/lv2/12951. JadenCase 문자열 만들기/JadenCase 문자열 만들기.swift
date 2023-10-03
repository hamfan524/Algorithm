func solution(_ s:String) -> String {
    let words = s.components(separatedBy: " ")
    var result = ""

    for (index, word) in words.enumerated() {
        if !word.isEmpty {
            let firstCharacter = word.prefix(1).capitalized
            let restOfWord = word.dropFirst().lowercased()
            result += firstCharacter + restOfWord
        }

        if index < words.count - 1 {
            result += " "
        }
    }

    return result
}