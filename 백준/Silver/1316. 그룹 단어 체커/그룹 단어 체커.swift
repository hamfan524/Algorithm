let n = Int(readLine()!)!

var array = [String]()
var answer = 0
for _ in 0..<n { array.append(String(readLine()!)) }

func findGroup(_ str: String) -> Bool{
    var dp = [Character]()
    for c in str{
        if !dp.contains(c){
            dp.append(c)
        } else if dp.last! != c{
            return false
        }
    }
    
    return true
}

for i in array{
    if findGroup(i) == true { answer += 1}
}

print(answer)