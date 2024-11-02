class Solution:

    def find_median_sorted_lists(self, l1: list[int], l2: list[int]) -> float:

        l = l1 + l2
        l.sort()

        if len(l) % 2 == 0:
            return (l[(len(l)-1)//2] + l[len(l)//2]) / 2
        else:
            return l[(len(l))//2]