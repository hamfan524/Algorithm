import Foundation

var n = Int(readLine()!)!

var num: [Bool] = Array(repeating: true, count: 1003001)
num[1] = false

for i in 2..<(Int(sqrt(1003001.0)) + 1){
    if num[i] == true{
        for j in stride(from: i+i, through: 1003001, by: i){
            num[j] = false
        }
    }
}

while true{
    if isPalindrome(n){
        if isPrime(n){
            print(n)
            break
        }
    }
    n += 1
}


func isPrime(_ n: Int) -> Bool{
    if n == 1{ return false }
    for i in 2..<(Int(sqrt(Double(n))) + 1) {
        if n % i == 0 { return false }
    }
    return true
}

func isPalindrome(_ n: Int) -> Bool{
    let str1 = String(n)
    let str2 = String(str1.reversed())
    if str1 == str2 {
        return true
    }else{
        return false
    }
}
