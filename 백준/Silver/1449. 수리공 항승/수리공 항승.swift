let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }

let l = inputValues[1]
var places = readLine()!.split(separator: " ").map{ Int($0)! }
places.sort()

var start = places[0]
var end = places[0] + l
var count = 1

for i in 0..<places.count{
    if start <= places[i] && places[i] < end{
        continue
    }else{
        start = places[i]
        end = places[i] + l
        count += 1
    }
}
print(count)
