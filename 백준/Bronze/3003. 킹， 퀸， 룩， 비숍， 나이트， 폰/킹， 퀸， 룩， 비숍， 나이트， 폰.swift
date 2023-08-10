var rule = [1, 1, 2, 2, 2, 8]
let piece = readLine()!.split(separator: " ").map{ Int($0)! }
for i in 0..<rule.count{
    print(rule[i] - piece[i], terminator: " ")
}

