class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This problem reminds me of Two Sum, which uses a HashMap to keep
        #   track of what is needed for a specific position. This will let us
        #   do it in 2 full scans of the entire board, meaning it will be
        #   O(n), where n is the amount of total squares (not just the side
        #   length)
        boxes = [set() for _ in range(9)]
        horizontal_lines = [set() for _ in range(9)]
        vertical_lines = [set() for _ in range(9)]

        curr_box = 0

        for row_i in range(len(board)):
            for col_i in range(len(board[row_i])):
                curr_value = board[row_i][col_i]

                if curr_value == '.':
                    continue

                curr_box = (row_i // 3) * 3 + col_i // 3

                # Check to see if it's in any of the 3 sets for validation
                if curr_value in boxes[curr_box] or curr_value in horizontal_lines[row_i] or curr_value in vertical_lines[col_i]:
                    return False
                
                # Add it to the sets for future validation
                boxes[curr_box].add(curr_value)
                horizontal_lines[row_i].add(curr_value)
                vertical_lines[col_i].add(curr_value)
        
        return True