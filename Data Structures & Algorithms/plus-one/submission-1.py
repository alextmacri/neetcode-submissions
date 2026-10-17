class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        We can abuse Python's built in features by converting the list to
        strings, concatenating, converting to integers, then adding 1, and
        converting back, but that would mean creating new data structures
        for each part, which would mean O(n) space. This would also take
        O(n) time, since we have to iterate through all digits to process it.
        We can do this slightly more efficiently and "manually" by iterating
        backwards through the digits list (since most significant comes first
        in the list of digits), and adding 1 while keeping overflow in mind,
        and if we have overflow at the end, we add 1 to the beginning of the
        list as well. This method also cleanly extends to adding more than
        just 1, or even subtracting. Doesn't specify if we can or can't mutate
        the list passed in, so I will because it's less extra memory, O(1)
        """
        # Add the number
        digits[-1] += 1

        # Process overflow
        overflow = 0

        for i in range(1, len(digits) + 1):
            digits[-i] += overflow
            overflow, digits[-i] = divmod(digits[-i], 10)
        
        # Add extra overflow to end (we are currently only processing cases
        #   that will result in 1-digit overflow, if we are extending this for
        #   any amount to be added, this will need to be worked into the loop
        #   instead)
        if overflow > 0:
            return [overflow] + digits

        return digits