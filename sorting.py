class Sorting:
    def bubble_sort(self, data):

        for i in range(len(data)-1):
            for j in range(len(data)-1-i):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

    def selection_sort(self, data):

        for i in range(len(data)):
            min_index = i
            for j in range(i+1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
            data[min_index], data[i] = data[i], data[min_index]

        return data

    def insertion_sort(self, data):

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j+1] = data[j]
                j -= 1
            data[j+1] = key
        return data

    def merge_sort(self, data):

        if len(data) <= 1:
            return data
        
        mid = len(data)//2
        left_half = data[:mid]
        right_half = data[mid:]

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)

        merged_list = []
        i, j = 0, 0

        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                merged_list.append(left_sorted[i])
                i += 1
            else:
                merged_list.append(right_sorted[j])
                j += 1
        
        merged_list.extend(left_sorted[i:])
        merged_list.extend(right_sorted[j:])

        return merged_list

    def quick_sort(self, data):

        if len(data) <= 1:
            return data
        
        pivot = data[len(data)//2]

        left = [x for x in data if x < pivot]
        equal = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]

        return self.quick_sort(left) + equal + self.quick_sort(right)

    def heap_sort(self, data):

        n = len(data)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(data, n, i)
        
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.heapify(data, i, 0)

    def heapify(self, data, n, i):

        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if n > left and data[largest] < data[left]:
            largest = left

        if n > right and data[largest] < data[right]:
            largest = right

        if largest != i:
            data[largest], data[i] = data[i], data[largest]
            self.heapify(data, n, largest)
