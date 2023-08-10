let n = String(readLine()!)
print(n.sorted(by: >).map({String($0)}).joined())