def find_interest(sum, months):
    interest = 0
    if 1000 <= sum <= 10000:
        if 6 <= months < 12:
            interest = 5
        elif 12 <= months < 24:
            interest = 6
        elif 24 <= months:
            interest = 5
        else:
            interest = 0
    elif 10000 < sum <= 100000:
        if 6 <= months < 12:
            interest = 6
        elif 12 <= months < 24:
            interest = 7
        elif 24 <= months:
            interest = 6.5
        else:
            interest = 0
    elif 100000 < sum <= 1000000:
        if 6 <= months < 12:
            interest = 7
        elif 12 <= months < 24:
            interest = 8
        elif 24 <= months:
            interest = 7.5
        else:
            interest = 0
    else:
        interest = 0
    return interest


def calc_sum(sum, months):
    year = months // 12
    month = months - year * 12
    total_sum = sum

    for y in range(year):
        for m in range(12):
            interest = find_interest(total_sum, months)
            total_sum += total_sum / 100 * interest / 12

    for m in range(month):
        interest = find_interest(total_sum, months)
        total_sum += total_sum / 100 * interest / 12 * month

    return total_sum


print(calc_sum(1000, 30))
