let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
let score = readLine()!.split(separator: " ").map{ Int($0)! }.sorted()
let reversedScore = Array(score.reversed())
print(reversedScore[inputValues[1]-1])
