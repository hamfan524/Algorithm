let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
var num1 = inputValues[0]
var num2 = inputValues[1]

let l = num1 * num2
let gcd = findGcd(&num1, &num2)
print(gcd)
print(l / gcd)

func findGcd(_ n1: inout Int, _ n2: inout Int) -> Int{
    var r = 1
    while (n1 % n2 != 0){
        r = n1 % n2
        n1 = n2
        n2 = r
    }
    
    return n2
}
