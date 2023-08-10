var dwarfs = [Int]()
var result = [Int]()
for _ in 0..<9 { dwarfs.append(Int(readLine()!)!) }

let combinations = combination(array: dwarfs, length: 7)

for combination in combinations {
    if combination.reduce(0, +) == 100{
        combination.sorted().forEach { height in
            print(height)
        }
        break
    }
}

func combination(array: [Int], length: Int) -> [[Int]]{
    var result = [[Int]]()
    
    func combi(nowIndex index: Int, now: [Int]){
        if now.count == length{
            result.append(now)
            return
        }
        
        for i in index..<array.count{
            combi(nowIndex: i + 1, now: now + [array[i]])
        }
    }
    combi(nowIndex: 0, now: [])
    return result
}


