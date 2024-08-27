class search:

    def linear_search(self, data, element):

        for x in data:
            if x == element:
                return data.index(x)
        
        return "Element not found"

    def binary_search(self, data, element):

        start = 0
        end = len(data) - 1

        data.sort()

        while start <= end:
            mid = (start + end) // 2
            if data[mid] == element:
                return mid
            elif data[mid] < element:
                start = mid + 1
            else:
                end = mid - 1
        
        return "Element not found"

    def jump_search(self, data, element):

        n = len(data)
        jump = int(n ** 0.5)
        previous_jump = 0

        while data[min(jump, n) - 1] < element:
            previous_jump = jump
            jump = int(previous_jump ** 0.5)
            if data[jump] != element:
                return -1

        for i in range(previous_jump, min(previous_jump, n)):
            if data[i] == element:
                return i

        return -1
