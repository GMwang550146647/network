from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''
    max_route = -1000

    def openLock_single_direction(self, deadends, target):

        def get_all_possible_points(current_point, deadends):
            all_points = []
            for i in range(len(current_point)):
                for j in [1, -1]:
                    num = int(current_point[i]) + j
                    num = '0' if num > 9 else ('9' if num < 0 else str(num))
                    new_point = current_point[:i] + num + current_point[i + 1:]
                    if new_point not in deadends:
                        all_points.append(new_point)
            return all_points

        def search_target(start_point, deadends, target):
            point2search = [start_point]
            steps = 0
            while len(point2search) > 0:
                for i in range(len(point2search)):
                    current_point = point2search.pop(0)
                    if current_point in deadends:
                        continue
                    if current_point == target:
                        return steps
                    deadends.add(current_point)
                    next_steps = get_all_possible_points(current_point, deadends)
                    for item in next_steps:
                        point2search.append(item)
                steps += 1
            return -1

        if '0000' in deadends:
            return -1
        start_point = '0000'
        deadends = set(deadends)
        result = search_target(start_point, deadends, target)
        return result

    '''答案方法1'''

    def openLock_double_direction(self, deadends, target):
        """
        双向的方法比较快！大家同时搜索
        """

        def get_all_possible_points(current_point, deadends):
            all_points = []
            for i in range(len(current_point)):
                for j in [1, -1]:
                    num = int(current_point[i]) + j
                    num = '0' if num > 9 else ('9' if num < 0 else str(num))
                    new_point = current_point[:i] + num + current_point[i + 1:]
                    if new_point not in deadends:
                        all_points.append(new_point)
            return all_points

        def search_target(start_point, deadends, target):
            q1 = [start_point]
            q2 = [target]
            steps = 0
            while q1 and q2:
                for i in range(len(q1)):
                    current_point = q1.pop(0)
                    if current_point in deadends:
                        continue
                    if current_point in q2:
                        return steps
                    deadends.add(current_point)
                    next_steps = get_all_possible_points(current_point, deadends)
                    for item in next_steps:
                        q1.append(item)
                q1, q2 = q2, q1
                steps += 1
            return -1

        if '0000' in deadends:
            return -1
        start_point = '0000'
        deadends = set(deadends)
        result = search_target(start_point, deadends, target)
        return result

    def testTime(self, fun, args, test_times=1):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":", result)
        print("Time used:", elapsed)

    def main(self):
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        target = "0202"
        self.testTime(self.openLock_single_direction, args=(deadends, target))
        self.testTime(self.openLock_double_direction, args=(deadends, target))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
