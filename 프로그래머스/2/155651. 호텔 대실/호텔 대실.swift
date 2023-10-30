import Foundation

func timeToMinute(_ time: String) -> Int {
    let components = time.components(separatedBy: ":")
    let hour = Int(components[0]) ?? 0
    let minute = Int(components[1]) ?? 0
    return hour * 60 + minute
}

func solution(_ book_time: [[String]]) -> Int {
    var events: [(Int, Int)] = []
    
    for reservation in book_time {
        let start = timeToMinute(reservation[0])    
        let end = timeToMinute(reservation[1]) + 9
        events.append((start, 1))
        events.append((end, -1))
    }
    
    events.sort{ $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 > $1.1 }
    
    var currentRooms = 0
    var maxRooms = 0
    
    for event in events {
        currentRooms += event.1
        maxRooms = max(currentRooms, maxRooms)
    }
    
    return maxRooms
}