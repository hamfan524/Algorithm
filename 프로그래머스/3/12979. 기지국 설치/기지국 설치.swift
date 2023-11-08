import Foundation

func solution(_ n:Int, _ stations:[Int], _ w:Int) -> Int{
    var answer = 0
    let std = w * 2 + 1
    var start = 1
    
    for s in stations {
        if s - w - start > 0 {
            answer += (s - w - start) / std
            if (s - w - start) % std > 0 {
                answer += 1
            }
        }
        start = s + w + 1
    }
    
    if n - start + 1 > 0 {
        answer += (n - start + 1) / std
        if (n - start + 1) % std > 0 {
            answer += 1
        }
    }
        
    return answer
}