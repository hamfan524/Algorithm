import Foundation

func solution(_ s:String) -> Int{
    var str = Array(s)
    var stack: [Character] = []
    for i in 0..<str.count {
        if let lastChar = stack.last, lastChar == str[i] {
            stack.removeLast()
        } else {
            stack.append(str[i])
        }
    }
    return stack.isEmpty ? 1 : 0
}