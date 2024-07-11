def print_numbers(n, current=1):
    if current > n:
        return
    print(current)
    print_numbers(n, current+1)


def factorial(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    return n * factorial(n-1)


def reverseString(st, index=0):
    if st is None:
        print("String is empty")
        return
    if index == (len(st)//2):
        st = ''.join(st)
        print(st)
        return
    st = list(st)
    st[index], st[len(st)-index-1] = st[len(st)-index-1], st[index]
    return reverseString(st, index+1)


def binarySearch(arr, target, left, right):
    if left <= right:
        mid = int((left+right)//2)
        if arr[mid] == target:
            print(f"Element found at index {mid}")
            return
        elif arr[mid] < target:
            return binarySearch(arr, target, mid+1, right)
        else:
            return binarySearch(arr, target, left, mid-1)
    else:
        print("Element not found")
        return None


def sumOfNumber(value):
    if value <= 1:
        return value
    return value+sumOfNumber(value-1)


def palindrome(s):
    if len(s) <= 0:
        print(True)
        return
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    print(False)
    return


palindrome("hello")
