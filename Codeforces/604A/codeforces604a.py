def problem_score(maxPoints, time, wrong):
    points1 = 0.3 * maxPoints
    points2 = (1 - (time / 250.0)) * maxPoints - (50 * wrong)
    if points1 > points2:
       return points1
    else:
        return points2

def compute_hacks(success, wrong):
    return 100 * success - 50 * wrong

def compute_final_score(times, wrongs, hacks):
    maximum = [500, 1000, 1500, 2000, 2500]
    score = 0
    for i in range(0, 5):
        score = score + problem_score(maximum[i], times[i], wrongs[i])
    score = score + compute_hacks(hacks[0], hacks[1])
    return score

def read_input():
    rowOne = map(int, raw_input().split())
    rowTwo = map(int, raw_input().split())
    rowThree = map(int, raw_input().split())
    print int(compute_final_score(rowOne, rowTwo, rowThree))

read_input()
