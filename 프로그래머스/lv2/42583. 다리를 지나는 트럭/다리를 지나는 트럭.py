def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = []
    on_time = []

    while truck_weights or on_bridge:
        time += 1
        if on_time and on_time[0] + bridge_length == time:
            on_bridge.pop(0)
            on_time.pop(0)
        if truck_weights and sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append(truck_weights.pop(0))
            on_time.append(time)

    return time