from random import randint as r


class Lottery:
    def __init__(self):
        pass


    def exists(self, lista, valor):
        for idx in lista:
            if idx == valor:
                return True
        return False


    def create_arrays(self):
        nums = []
        stars = []

        for i in range(5):
            num = r(1, 51)
            while Lottery.exists(self, nums, num):
                num = r(1, 51)
            nums.append(num)

        for i in range(2):
            star = r(1, 13)
            while Lottery.exists(self, stars, star):
                star = r(1, 13)
            stars.append(star)

        return nums, stars

