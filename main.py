def calculate_money(distance, weight):
    distance = round(distance)
    weight = round(weight)
    if distance <= 10:
        if weight <= 10:
            return 50
        else:
            return weight * 5
    elif distance <= 50:
        if weight <= 10:
            return weight * 5
        elif weight <= 50:
            return weight * 10
        else:
            return weight * 15
    else:
        return weight * 20

print(calculate_money(5, 8))    # Output: 50