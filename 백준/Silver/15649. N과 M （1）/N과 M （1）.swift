let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
let n = inputValues[0]
let m = inputValues[1]

var result = [Int]()

func solution(){
    if result.count == m{
        print(result.map{String($0)}.joined(separator: " "))
        return
    }else{
        for i in 1...n{
            if !result.contains(i){
                result.append(i)
                solution()
                result.popLast()!
            }
        }
    }
}

solution()
