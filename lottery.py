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

    def sort_nums(self, nums):

        for i in range(len(nums)):
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]

        return nums

    def sort_stars(self, stars):

        if stars[1] < stars[0]:
            stars[0], stars[1] = stars[1], stars[0]
        else:
            pass

        return stars