func solution(_ wallpaper: [String]) -> [Int] {
    var left = wallpaper[0].count
    var right = 0
    var top = 0
    var bottom = wallpaper.count

    for i in 0..<wallpaper.count {
        for j in 0..<wallpaper[0].count {
            let index = wallpaper[i].index(wallpaper[i].startIndex, offsetBy: j)
            if wallpaper[i][index] == "#" {
                left = min(left, j)
                right = max(right, j + 1)
                bottom = min(bottom, i)
                top = max(top, i + 1)
            }
        }
    }

    return [bottom, left, top, right]
}