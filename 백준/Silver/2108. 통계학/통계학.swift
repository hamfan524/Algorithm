import Foundation

let n = Int(readLine()!)!
var nums = [Int]()
var dic = [Int : Int]()
for _ in 0..<n{
    let num = Int(readLine()!)!
    nums.append(num)
    dic[num, default: 0] += 1
}

nums.sort()
var sum = nums.reduce(0, +)
let ave = (Double(sum) / Double(n))

print(Int(round(ave))) // 산술평균
print(nums[n/2]) // 중앙값

//최빈값
let max = dic.max(by: {$0.value < $1.value})!.value
var mode = dic.filter {$0.value == max}.keys.sorted()
if mode.count > 1{
    print(mode[1])
}else{
    print(mode[0])
}

//범위
print(nums.max()! - nums.min()!)
