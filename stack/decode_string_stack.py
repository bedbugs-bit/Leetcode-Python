class Solution:
    def decode_string(self, s: str) -> str:
        stack = []
        size = len(s)

        for i in range(size):
            if s[i] != "]":
                # Push all characters except the closing bracket "]"
                stack.append(s[i])
            else:
                # Found a closing bracket, process the substring
                sub_str = ""
                while stack and stack[-1] != "[":
                    sub_str = stack.pop() + sub_str

                # Pop the "["
                stack.pop()

                # Extract the multiplier
                multiply_val = ""
                while stack and stack[-1].isdigit():
                    multiply_val = stack.pop() + multiply_val

                # Expand the substring and push back to the stack
                expanded_sub_str = int(multiply_val) * sub_str
                stack.append(expanded_sub_str)

        # Join the stack to form the final decoded string
        return ''.join(stack)
