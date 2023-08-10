let n = Int(readLine()!)!
var result = [String]()

for _ in 0..<n { result.append((readLine()!)) }

Set(result).sorted{l, r -> Bool in
    return l.count < r.count || (l.count == r.count && l < r)
}.forEach{ word in
    print(word)
}
