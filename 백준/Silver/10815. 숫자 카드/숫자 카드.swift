let n = Int(readLine()!)!
var cards = readLine()!.split(separator: " ").map{ Int($0)! }
let m = Int(readLine()!)!
let myCards = readLine()!.split(separator: " ").map{ Int($0)! }
cards.sort()

var answer = [String]()

for i in myCards{
    if binarySearch(0, n-1, i, cards){
        answer.append("1")
    } else{
        answer.append("0")
    }
    
}

print(answer.joined(separator: " "))

func binarySearch(_ left: Int, _ right: Int,_ num: Int, _ cards: [Int]) -> Bool{
    var result = false
    if left > right{
        return false
    }
    let middle = (left + right) / 2
    
    if cards[middle] > num {
        result = binarySearch(left, middle - 1, num, cards)
    }else if cards[middle] < num {
        result = binarySearch(middle + 1, right, num, cards)
    }else{
        return true
    }
    return result
}
