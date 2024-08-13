############
#
# Cheap Crowdfunding Problem
#
# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#
# You would like to get the reward, while spending the least amount > 0.
#
# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.
#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.
#
############

def find_min_pledge(pledge_list: list[int]) -> int:
    """
        Find the minimum amount greater than 0 that can be pledged
        without matching any existing pledge amounts.

        Args:
            pledge_list (list[int]): A list of integers representing the amounts
                                    already pledged to the project.

        Returns:
            int: The smallest integer greater than 0 that is not in the pledge_list.
    """

    pledge_list = set(pledge_list)
    least_amount = 1

    while least_amount in pledge_list:
        least_amount += 1
    
    return least_amount
 


assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1