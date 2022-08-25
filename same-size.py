"""
Yusuf bought a few pieces of mats that rectangle in shape. All the mats have the same size. He wants to arrange the mats in a rectangle space, with conditions that the mats are not to be cut, folded, or overlapped.

Initially, Yusuf will fill in the available space by arranging the mat horizontally. If there is remainder space, he will arrange the mat vertically.

Given the measurement of the mat’s size and the space size to be used.
You are to determine the maximum number of mats that can be arranged by Yusuf.
"""

matl, matw = 3, 2
rooml, roomw = 11, 7

matl, matw = int(matl), int(matw)
rooml, roomw = int(rooml), int(roomw)

used_mats = 0

# find out how many we can arrange vertically, with the mat horizontally
arv1 = roomw // matw
# how many we can arrange horizontally
arh1 = rooml // matl
# times the two so we know how many carpets we used
used_mats += arh1 * arv1

# leftover length minus the top operation
leftover_length = rooml - (matl * arh1)

arv2 = roomw // matl
arh2 = leftover_length // matw
used_mats += arv2 * arh2

print(used_mats)
