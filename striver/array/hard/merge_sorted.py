# Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. 
# Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 
# so that it contains the last M elements.

def mergeSortedArray(nums1,m, nums2,n):
    idx1, idx2, extra = m-1, n-1, m + n - 1
    # print(nums1[extra])
    while idx2 >= 0:
        if idx1 >=0 and nums1[idx1] > nums2[idx2]:
            nums1[extra] = nums1[idx1]
            idx1-=1
        else:
            nums1[extra] = nums2[idx2]
            idx2-=1
        extra-=1

if __name__=='__main__':
    nums1=[1,4,8,10]
    nums2 = [2,3,9]
    mergeSortedArray(nums1,4,nums2,3)
    print(nums1 + nums2)