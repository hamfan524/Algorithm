import Foundation

func check(_ s: String) -> Bool {
    var stack = [Character]()
    let brackets: [Character: Character] = [")": "(", "}": "{", "]": "["]
    
    for char in s {
        if let bracket = brackets[char] {
            if let top = stack.last, top == bracket {
                stack.removeLast()
            } else {
                return false
            }
        } else {
            stack.append(char)
        }
    }
    return stack.isEmpty
}

func solution(_ s:String) -> Int {
    var answer = 0
    var tmp = s
    for _ in 0..<s.count {
        if check(tmp) {
            answer += 1
        }
        tmp.append(tmp.removeFirst())
    }
    return answer
}