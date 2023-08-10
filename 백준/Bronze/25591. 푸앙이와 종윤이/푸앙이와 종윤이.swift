let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
var num1 = inputValues[0]
var num2 = inputValues[1]

let a = 100 - num1
let b = 100 - num2
let c = 100 - (a + b)
var d = a * b
var q = 0
var r = 0
if d >= 100 {
    q = d / 100
    r = d % 100
} else{
    q = 0
    r = d
}

print(a, b, c, d, q, r)
print(c + q, r)