"""
GIven slotA and slotB with time availabilty of 2 students and a duration.Return the earliest time slot taht works for both of them and is of duration dur.Assume that slots are sorted by slot's start time and duration is always positive.
"""

slotA = [[10, 50], [60, 120], [140, 210]]
slotB = [[0, 15], [60, 70]]


def time_overlap(slotA, slotB, duration):
    i = 0
    j = 0

    while i < len(slotA) or j < len(slotB):
        overlap_start = max(slotA[i][0], slotB[j][0])
        overlap_stop = min(slotA[i][1], slotB[j][1])
        if overlap_start+duration <= overlap_stop:
            return [overlap_start, overlap_start+duration]
        else:
            if slotA[i][1] < slotB[j][1]:
                i = i+1
            else:
                j = j+1
    return None


print(time_overlap(slotA, slotB, 8))
