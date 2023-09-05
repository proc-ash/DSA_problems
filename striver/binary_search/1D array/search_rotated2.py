# Problem Statement: Given an integer array arr of size N, sorted in ascending order 
# (may contain duplicate values) and a target value k. Now the array is rotated 
# at some pivot point unknown to you. Return True if k is present and otherwise, return False. 

def search(nums, target) -> bool:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            if nums[low]<= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high= mid -1
                else:
                    low = mid +1
            else:
                if target >= nums[mid] and nums[high] >= target:
                    low = mid +1
                else:
                    high = mid -1
        return False
if __name__ == '__main__':
    array = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    print(search(array, k))