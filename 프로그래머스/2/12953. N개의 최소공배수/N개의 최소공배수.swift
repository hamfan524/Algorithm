func GCD(_ a: Int, _ b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return GCD(b, a % b)
    }
}

func LCM(_ a: Int, _ b: Int) -> Int {
    let gcd = GCD(a, b)
    return (a * b) / gcd
}

func solution(_ arr:[Int]) -> Int {
    var result = arr[0]
    
    for i in 1..<arr.count {
        result = LCM(result, arr[i])
    }
    
    return result
}