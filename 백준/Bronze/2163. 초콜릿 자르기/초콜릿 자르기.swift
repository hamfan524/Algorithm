var inputValues = readLine()!.split(separator: " ").map{ Int($0)! }

let n = inputValues[0]
let m = inputValues[1]

print((n-1) + (m-1)*n)
