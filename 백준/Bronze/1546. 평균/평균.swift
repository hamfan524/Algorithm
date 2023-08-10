let subject = Double(readLine()!)!

let score = readLine()!.split(separator: " ").map{ Double(String($0))!}

var sum = 0.0
let maxScore = score.max()!
let otherScore = score.map{$0 / maxScore * 100}

for i in otherScore{
    sum += i
}
print(sum / subject)
