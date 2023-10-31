import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var K = k
    var dic = [Int: Int]()
    for i in tangerine {
        dic[i, default:0] += 1
    }
    var sortedDic = dic.values.sorted(by: {$0 > $1})
    
    var answer = 0
    for i in 0..<sortedDic.count {
        answer += 1
        K -= sortedDic[i]
        if K <= 0 {
            break
        }
    }
    return answer
}