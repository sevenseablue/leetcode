class solution:

    def min_diff(self, collects):
        """
        collects: list[list[string]]
        there are same string in list, set a int to every string, make the sum of the max int minus the min string of all list least.
        """
        allset = set([])
        for c in collects:
            allset.update(c)
        num = len(allset)
        eles = list(allset)
        def sum_diff(eles, inds, collects):
            dic1 = dict(zip(eles, inds))
            sum1 = 0
            for c in collects:
                indlist = [dic1[e] for e in c]
                max1 = max(indlist)
                min1 = min(indlist)
                sum1 += max1-min1
            return sum1

        self.result = 2 ** 31
        def dfs(n, i, inds, remainset):
            if len(inds) == n:
                sum1 = sum_diff(eles, inds, collects)
                if self.result > sum1:
                    self.result = sum1
            for r in remainset:
                inds.append(r)
                remainsetcp = remainset.copy()
                remainsetcp.remove(r)
                dfs(n, i, inds, remainsetcp)

                inds.pop()

        pass


l1 = [["a", "b", "c"], ["c", "b", "d"], ["d", "a", "e"]]  # 1,2,3 2,3,0 0,1,-1
l1 = [["a", "b", "c"], ["c", "b", "d"], ["d", "a", "c"]]  # 1,2,3 2,3,0 0,1,-1
l1 = [["a", "b", "c"], ["c", "b", "d"], ["d", "a", "b"]]  # 1,2,3 2,3,0 0,1,-1

# 每个对象出现的次数
# 集合数
# 集合之间的


