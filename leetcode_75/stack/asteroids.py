class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [asteroids[0]]
        for asteroid in asteroids[1:]:
            if len(stack) == 0:
                stack.append(asteroid)
                continue
            if stack[-1] / abs(stack[-1]) == asteroid / abs(asteroid):
                stack.append(asteroid)
            else:
                append = True
                while (stack[-1] / abs(stack[-1]) != asteroid / abs(asteroid)) and stack[-1] > 0 > asteroid:
                    if len(stack) == 0:
                        append = True
                        break
                    if abs(stack[-1]) == abs(asteroid):
                        stack.pop()
                        append = False
                        break
                    elif abs(stack[-1]) > abs(asteroid):
                        append = False
                        break
                    else:
                        stack.pop()
                        append = True
                    if len(stack) == 0:
                        append = True
                        break
                if append:
                    stack.append(asteroid)
        return stack



