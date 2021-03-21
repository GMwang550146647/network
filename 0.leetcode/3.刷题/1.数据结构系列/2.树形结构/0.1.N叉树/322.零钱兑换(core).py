from fundamentals.tree import TreeNode, Tree
import time


class Solution():
    def __init__(self):
        pass

    '''我的方法'''
    INF = 10000

    def coinChange_force(self, coins, amount):
        """
        这个方法容易太多重复，太慢
        """

        def coinChangeAssist(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            current_coins = self.INF
            for coin_i in coins:
                new_amount = amount - coin_i
                count = coinChangeAssist(new_amount)
                if count >= 0:
                    current_coins = min(current_coins, 1 + count)
            return current_coins if current_coins != self.INF else -1

        return coinChangeAssist(amount)

    def coinChange_digui_dp(self, coins, amount):
        """
        递归 DP
        用dict记录着每部分的最优解，简化不必要运算，但是还是慢
        """

        def get_coinChange_assist(amount):
            if amount < 0:
                return self.INF
            if amount in record_dict:
                return record_dict[amount]
            min_coin = self.INF
            for coin_i in coins:
                min_coin_i = get_coinChange_assist(amount - coin_i) + 1
                min_coin = min(min_coin_i, min_coin)
            record_dict[amount] = min_coin
            return min_coin

        record_dict = {coin_i: 1 for coin_i in coins}
        record_dict[0] = 0
        result = get_coinChange_assist(amount)
        return -1 if result >= self.INF else result

    def coinChange_list_dp(self, coins, amount):
        """
        循环 DP
        用dict记录每一部分的最优解简化不必要运算
        """
        def get_coinChange_assist(amount):
            for i in range(1, amount + 1):
                for coin_i in coins:
                    if i >= coin_i:
                        record_list[i] = min(record_list[i - coin_i] + 1, record_list[i])
            return record_list[amount]

        record_list = [self.INF] * amount
        record_list.insert(0, 0)
        result = get_coinChange_assist(amount)
        return -1 if result >= self.INF else result

    def testTime(self, fun, args, test_times=10):
        # 计时
        start = time.process_time()
        for i in range(test_times):
            result = fun(*args)
        elapsed = (time.process_time() - start)
        print(fun.__name__, ":")
        print("Time used:", elapsed)
        print("Result:", result)

    def main(self):
        coins = [1, 2, 5, 7, 9, 12]
        amount = 30
        # self.testTime(self.coinChange_force, args=(coins, amount))
        self.testTime(self.coinChange_digui_dp, args=(coins, amount))
        self.testTime(self.coinChange_list_dp, args=(coins, amount))


if __name__ == '__main__':
    SL = Solution()
    SL.main()
