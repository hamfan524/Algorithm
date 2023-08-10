let n = Int(readLine()!)!
var count = 0

func findHanSoo(_ num: Int) -> Bool{
    let a = String(num).map{Int(String($0))! }
    if a.count <= 2  { return true }
    var sum = 0
    for i in a{
        sum += Int(i)
    }
    if (Double(sum) / Double(3)) == Double(a[1]){
        return true
    }
    
    return false
}

(1...n).forEach{
    if findHanSoo($0) == true{
        count += 1
    }
}
print(count)
