let n = Int(readLine()!)!
var arr = [Int]()
for _ in 0..<n {
    let x = Int(readLine()!)!
    if x == 0 {
        if arr.count == 0 { print(0) }
        else{
            var max = 0, maxIndex = 0
            for i in 0..<arr.count{
                if max < arr[i]{
                    max = arr[i]
                    maxIndex = i
                }
            }
            arr[maxIndex] = 0
            print(max)
        }
    } else{
        arr.append(x)
    }
}