func solution(_ s:String) -> String {
    var answer = ""
    
    for st in s.components(separatedBy: " ") {
        for (i, char) in st.enumerated() {
            if i % 2 == 0 {
                answer.append(char.uppercased())
            } else {
                answer.append(char.lowercased())
            }
        }
        answer.append(" ")
    }
    
    return String(answer.dropLast())
}