while true{
    let n = Int(readLine()!)!
    
    if n == 0 { break }
    else if n == 1 {
        print(1)
        continue
    }
    print(findSosu(n))
}

func findSosu(_ num: Int) -> Int {
    var answer = 0
    
    var array: [Int] = Array(repeating: 1, count: (2 * num) + 1)
    
    for i in 2...(num * 2){
        array[i] = i
    }
    
    for j in 2...(num * 2){
        for k in stride(from: j * 2, to: num * 2, by: j){
            array[k] = 0
        }
    }

    for v in (num + 1)...((num * 2) - 1){
        if array[v] != 0{
            answer += 1
        }
    }
    return answer
}
