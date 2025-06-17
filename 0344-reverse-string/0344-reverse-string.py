class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s) - 1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1
        return s

        # Time Complexity:  O(n) - passing over the input array once with our pointers, scales linearly with the size of input arr we are sorting
        # Space Complexity: O(1) - reversing str in place, not using any additional data structures except ptrs and temp var