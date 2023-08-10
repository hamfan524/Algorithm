while true{
    let n = Int(readLine()!)!
    if n == -1 { break }
    let divisors: [Int] = findSosu(n)
    if isPerfect(n, divisors){
        var result = "\(n) = 1"
        for i in 1..<divisors.count{
            result += " + \(divisors[i])"
        }
        print(result)
    }else{
        print("\(n) is NOT perfect.")
    }
}

func findSosu(_ num: Int) -> [Int]{
    var divisor: [Int] = [1]
    
    for i in 2..<num{
        if num % i == 0{
            divisor.append(i)
        }
    }
    
    return divisor
}

func isPerfect(_ num: Int, _ array: [Int]) -> Bool{
    if num == array.reduce(0, +) {
        return true
    }
    else{
        return false
    }
}