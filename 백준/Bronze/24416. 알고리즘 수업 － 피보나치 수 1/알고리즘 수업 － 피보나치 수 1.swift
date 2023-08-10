func fibo(n: Int) -> Int{
    if n == 1 || n == 2{
        return 1
    }else{
        return fibo(n: n-1) + fibo(n: n - 2)
    }
}

func fibonacci(n: Int) -> Int{
    var dp = [Int: Int]()
    
    dp[1] = 1
    dp[2] = 1
    
    for i in 3...n{
        count += 1
        dp[i] = dp[i-1]! + dp[i-2]!
    }

    return count
}

var count = 0

let N = Int(readLine()!)!

print(fibo(n: N), fibonacci(n: N))
