from random import randint as r


class Lottery:
    def __init__(self):
        pass


    def exists(self, lista, valor):
        for idx in lista:
            if idx == valor:
                return True
        return False

    # Not being used currently
    def define_nums(self):
        list1 = []

        while len(list1) < 5:
            try:
                x = int(input("Enter a number between 1 and 50: "))
                if 0 < x < 51:
                    if x not in list1:
                        list1.append(x)
                    else:
                        print("Repeated numbers")

                else:
                    print("Invalid number")

            except ValueError:
                print("Please enter a integer")

        return list1

    # Not being used currently
    def define_stars(self):
        list2 = []

        while len(list2) < 2:
            try:
                y = int(input("Enter a number between 1 and 12: "))
                if 0 < y < 13:
                    if y not in list2:
                        list2.append(y)
                    else:
                        print("Repeated star")

                else:
                    print("Invalid star")

            except ValueError:
                print("Please enter a integer")

        return list2


    def create_arrays(self):
        nums = []
        stars = []

        for i in range(5):
            num = r(1, 50)
            while Lottery.exists(self, nums, num):
                num = r(1, 50)
            nums.append(num)

        for i in range(2):
            star = r(1, 12)
            while Lottery.exists(self, stars, star):
                star = r(1, 12)
            stars.append(star)

        return nums, stars

    # Not being used currently
    def compare_nums(self, guessed_nums, result_nums):
        matches = set(guessed_nums).intersection(result_nums)
        percentage = (len(matches) / len(result_nums)) * 100
        print(f"You matched {len(matches)} numbers out of {len(result_nums)}. ({percentage:.2f}% correct)")

    # Not being used currently
    def compare_stars(self, guessed_stars, result_stars):
        matches = set(guessed_stars).intersection(result_stars)
        percentage = (len(matches) / len(result_stars)) * 100
        print(f"You matched {len(matches)} stars out of {len(result_stars)}. ({percentage:.2f}% correct)")