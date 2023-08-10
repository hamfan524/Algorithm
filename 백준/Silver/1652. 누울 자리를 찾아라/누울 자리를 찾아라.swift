let n = Int(readLine()!)!
var room = [[Character]]()
for _ in 0..<n {
    let line = Array(String(readLine()!))
    room.append(line)
}

var row = 0
var column = 0

for i in 0..<n {
    let splitRow = room[i].split(separator: "X").map{ $0.count }
    let splitCol = room.map({$0[i]}).split(separator: "X").map{ $0.count }
    
    for r in splitRow{
        if r >= 2{
            row += 1
        }
    }
    for c in splitCol{
        if c >= 2{
            column += 1
        }
    }
}

print(row, column)