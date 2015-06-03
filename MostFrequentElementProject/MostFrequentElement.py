__author__ = 'Luis'

class MostFrequentElement:
    @staticmethod
    def find_most_frequent(l):
        unique_values = set(l)
        if len(l) <= 1:
            return unique_values

        max = 0
        most_frequent = []

        for value in unique_values:
            number_of_times = l.count(value)
            if number_of_times > max:
                max = number_of_times
                most_frequent = [value]

            elif number_of_times == max:
                most_frequent.append(value)

        return set(most_frequent)

    @staticmethod
    def optimized_most_frequent_element(l):
        return set(x for x in set(l) if l.count(x) == max([l.count(y) for y in l]))