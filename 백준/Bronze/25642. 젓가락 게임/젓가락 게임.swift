let inputValues = readLine()!.split(separator: " ").map{ Int($0)! }
var yt = inputValues[0]
var yj = inputValues[1]

func winner(_ yt: inout Int, _ yj: inout Int) -> String{
    yj += yt
    if yj >= 5{
        return "yt"
    }

    yt += yj
    if yt >= 5{
        return "yj"
    }
    
    return "yt"
}

print(winner(&yt, &yj))
