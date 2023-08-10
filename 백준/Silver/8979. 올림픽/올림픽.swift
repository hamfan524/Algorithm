let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
let n = inputValues[0]
let k = inputValues[1]

typealias medals = (gold: Int, silver: Int, bronze: Int)
var data = [Int: medals]()

for _ in 0..<n{
    let inputData = readLine()!.split(separator: " ").map{ Int($0)! }
    data[inputData[0]] = (inputData[1], inputData[2], inputData[3])
}

let sortedData = data.sorted(by: {$0.value > $1.value})
var rank = [[Int]]()
for i in sortedData{
    rank.append([i.key, i.value.gold * 1000001 * 1000001 + i.value.silver * 1000001 + i.value.bronze])
}

var index = 0
for i in 0..<n{
    if rank[i][0] == k{
        index = i
    }
}
for i in 0..<n{
    if rank[index][1] == rank[i][1]{
        print(i + 1)
        break
    }
}