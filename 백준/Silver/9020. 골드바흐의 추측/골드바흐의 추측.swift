import Foundation

let T = Int(readLine()!)!

for _ in 0..<T{
    let num = Int(readLine()!)!
    
    var a = num / 2
    var b = num / 2
    
    while a > 0{
        if isPrime(a) && isPrime(b){
            print(a, b)
            break
        }
        else{
            a -= 1
            b += 1
        }
    }
}

func isPrime(_ n: Int) -> Bool{
    if n == 1 { return false }
    for i in 2..<Int(pow(Double(n), 0.5)) + 1{
        if n % i == 0{
            return false
        }
    }
    return true
}
