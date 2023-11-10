func solution(_ n: Int, _ computers: [[Int]]) -> Int {
    var answer = 0
    var visited = [Bool](repeating: false, count: n)
    
    func bfs(_ j: Int) {
        var queue = [j]

        while !queue.isEmpty {
            let tmp = queue.removeFirst()
            visited[tmp] = true
            
            for i in 0..<n {
                if computers[tmp][i] == 1 && !visited[i] {
                    queue.append(i)
                }
            }
        }
    }
    
    for i in 0..<n {
        if visited[i] == false {
            bfs(i)
            answer += 1
        }
    }
    
    return answer
}