func bfs(_ n: Int, _ computers: [[Int]], _ j: Int, _ visited: inout [Bool]) {
    var queue = [j]
    
    while !queue.isEmpty {
        let tmp = queue.removeFirst()
        visited[tmp] = true
        
        for i in 0..<n {
            if i != tmp && computers[tmp][i] == 1 && !visited[i] {
                queue.append(i)
            }
        }
    }

}

func solution(_ n: Int, _ computers: [[Int]]) -> Int {
    var answer = 0
    var visited = [Bool](repeating: false, count: n)
    
    for i in 0..<n {
        if visited[i] == false {
            bfs(n, computers, i, &visited)
            answer += 1
        }
    }
    
    return answer
}