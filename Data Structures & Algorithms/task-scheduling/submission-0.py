class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts=defaultdict(int)

        for task in tasks:
            counts[task]+=1
        max_count=max(counts.values())
        num_max=sum(1 for v in counts.values() if v==max_count)

        return max((max_count-1)*(n+1)+num_max,len(tasks))