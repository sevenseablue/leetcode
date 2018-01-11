# coding: utf8


# 从array中找小于等于t的， 没有则取-1
def binarysearch_le_hard(array, t):
    if array is None or len(array) == 0:
        raise "array None or empty"
    l = 0
    h = len(array) - 1
    low = 0
    height = len(array) - 1

    while l < h:
        m = int((l + h) / 2)
        if array[m] < t:
            l = m + 1

        elif array[m] > t:
            h = m - 1

        else:
            return m

    if h < low:
        h = low
    if l > height:
        l = height

    if array[l] <= t:
        return l
    elif array[h] <= t < array[l]:
        return h
    elif array[h] > t and h > 0:
        return h - 1
    else:
        return -1  # h == low == 0


def findMedianSortedArrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    ind = int((n1 + n2) / 2)
    if (n1 + n2) % 2 == 1:
        return findKSortedArrays(nums1, nums2, ind)*1.0
    else:
        num1 = findKSortedArrays(nums1, nums2, ind)
        num2 = findKSortedArrays(nums1, nums2, ind-1)
        return (num1+num2)/2.0


# ascend sorted, the k indexed num  # the k-1 indexed num, the kth small num in the 2 sorted arrays
def findKSortedArrays(nums1, nums2, k):
    if len(nums1) > len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp
    n1 = len(nums1)
    n2 = len(nums2)
    if k >= n1 + n2:
        raise "k>=n1+n2"
    if k < 0:
        raise "k<0"

    # print('#'*10,nums1, nums2, n1, n2, k)
    if k == 0:
        if n1 == 0:
            return nums2[0]
        else:
            return nums1[0] if nums1[0]<=nums2[0] else nums2[0]
    elif k == n1+n2-1:
        if n1 == 0:
            return nums2[k]
        else:
            return nums1[n1-1] if nums1[n1-1]>=nums2[n2-1] else nums2[n2-1]
    elif n1 == 0:
        return nums2[k]
    # n1>0, n2>0, k>0, k<n1+n2-1
    # add arr1 max is less or equal than arr2 min
    elif nums1[n1-1] <= nums2[0]:
        if k<=n1-1:
            return nums1[k]
        else:
            return nums2[k-n1]
    elif nums2[n2-1] <= nums1[0]:
        if k<=n2-1:
            return nums2[k]
        else:
            return nums1[k-n2]
    # TODO check which is better to find one element from a long array or a short array
    else:
        # 0:kn2, kn2:n2
        kn2 = int((k+1) * n2 * 1.0 / (n1 + n2))  # kn2 < n2, kn2 > 0 (k*n2>n1, k>0, n2>n1)
        # 0:kn1, kn1:n1
        kn1 = binarysearch_le_hard(nums1, nums2[kn2]) + 1
        if k < kn1 + kn2:
            return findKSortedArrays(nums1[:kn1], nums2[:kn2], k)  # kn2 < n2
        else:
            return findKSortedArrays(nums1[kn1:], nums2[kn2:], k - kn1 - kn2)  # kn2 > 0
        pass



def findKSortedArrays_t():
    lists1 = [[2],
              [],
              [1],
              [1, 3, 5]]

    for l1 in lists1:
        for l2 in lists1:
            # print(l1, l2)
            n1 = len(l1)
            n2 = len(l2)
            for k in range(0, n1 + n2):
                print("#" * 50)
                print(l1, l2, n1, n2, k)
                print(findKSortedArrays(l1, l2, k))

        print(findKSortedArrays(list(range(0, 50)), list(range(50, 1000)), 50))
    pass


def main():
    # binarysearch_t()

    findKSortedArrays_t()


if __name__ == "__main__":
    main()
    print(findMedianSortedArrays([1, 3], [2]))