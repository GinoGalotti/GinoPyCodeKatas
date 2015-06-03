__author__ = 'Luis'

class StringMesser:

    @staticmethod
    def char_concat(word):
        response = ""
        if len(word) <= 1:
            return response

        cut_word = word
        for i in range(len(word)//2):
            response = response + cut_word[0] + cut_word[-1] + str(i + 1)
            cut_word = cut_word[1:-1]

        return response

    @staticmethod
    def char_concat_optimized(word):
        string = ''
        for i in range(len(word)//2):
            string += word[i] + word[-i-1] + str(i+1)
        return string
