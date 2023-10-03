func solution(_ s:String) -> String {
    let nums = s.components(separatedBy: " ").map({(value: String) -> Int in return Int(value)!})
    if let maxNum = nums.max(),
        let minNum = nums.min(){
        return "\(minNum) \(maxNum)"
    } else {
         return  ""
    }
}