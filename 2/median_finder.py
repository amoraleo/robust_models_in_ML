class MedianFinder:
    def __init__(self):
        self.seq = []

    def add_num(self, num):
        self.seq.append(num)

    def find_median(self):
        sort_seq = sorted(self.seq)
        if (l := len(sort_seq)) == 0:
            return 0.0
        if l % 2 == 0:
            return (sort_seq[l//2 - 1] + sort_seq[l//2]) / 2
        else:
            return float(sort_seq[(l-1)//2])

median_finder = MedianFinder()
assert median_finder.find_median() == 0.0

median_finder.add_num(1)
median_finder.add_num(2)
assert median_finder.find_median() == 1.5

median_finder.add_num(3)
assert median_finder.find_median() == 2.0