def penalty(start,end):
    diffYear = end[2] - start[2]
    diffDate = end[0]- start[0]
    diffMonth = end[1]- start[1]
    
    if diffYear > 0:
        return diffYear * 12000
    if diffMonth > 0:
        return diffMonth * 500
    if diffDate > 0:
        return diffDate * 15

    return 0

print("Enter the Start Date(d1 m1 y1): ")
start = list(map(int, input().split()))
print("Enter the End Date(d2 m2 y2): ")
end = list(map(int,input().split()))
pay = penalty(start,end)

print("Penalty: ", pay)
