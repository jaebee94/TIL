def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    cur_weight = 0
    while True:
        answer += 1
        outlet = bridge.pop(0)
        cur_weight -= outlet
        if truck_weights and cur_weight + truck_weights[0] <= weight:
            inlet = truck_weights.pop(0)
            cur_weight += inlet
            bridge.append(inlet)
        else:
            bridge.append(0)
        if cur_weight == 0:
            return answer