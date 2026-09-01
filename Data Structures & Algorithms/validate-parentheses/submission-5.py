class Solution:
    def isValid(self, s: str) -> bool:
        # Define dictionary to get corresponding bracket pairs quick and easy
        bracketPair = {'(': ')', '[': ']', '{': '}'}

        # Need to keep track of most recent bracket to close, while also keeping
        #   memory of the old ones that need to be closed in order, and need to
        #   be able to track a 'new most recent' bracket at any time,
        #   'interrupting' the current/previous bracket. This seems like a
        #   RECURSION problem. BUT... we only need 'recursive memory' of past
        #   brackets to keep track of and can otherwise just process it
        #   linearly, so we will use a STACK, i.e. a RECURSIVE DATA STRUCTURE
        stack = []

        for c in s:
            # If a character is an opening bracket, add to the 'top' of the
            #   stack (doesn't mean a violation necessarily, we need to check
            #   to see if it closes legally)
            if c in bracketPair.keys():
                stack.append(c)
            else:
                # EDGE CASE: stack must be populated with an opening brakcet if
                #   we're now looking at a closing bracket, or else that's an
                #   instant VIOLATION
                if len(stack) < 1:
                    return False

                # If it's a closing bracket, it's either closing the most
                #   recently opened one (legal), or it's a VIOLATION
                if c == bracketPair[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        # If it gets through without the condition violating, we need to also
        #   make sure that it does't leave any opened brackets unclosed, or else
        #   that's a VIOLATION
        return len(stack) == 0