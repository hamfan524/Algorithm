import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var emptyArr:[Int] = []
    emptyArr += num_list.prefix(n)
    
    return emptyArr
    
}