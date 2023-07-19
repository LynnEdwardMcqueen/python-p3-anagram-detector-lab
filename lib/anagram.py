# your code goes here!
class Anagram:

    def __init__(self, base_word):
        self.set_base_word(base_word)

    def get_base_word(self):
        return self._base_word

    def set_base_word(self, base_word):
        self._base_word = base_word
        return
    
    def match(self, candidate_array):
        sorted_base_word = sorted([letter for letter in self._base_word])
        anagram_list = []

        for candidate in candidate_array:
            sorted_candidate = sorted([letter for letter in candidate])
            if sorted_candidate == sorted_base_word:
                anagram_list.append(candidate)

        return anagram_list
    
    base_word = property(get_base_word, set_base_word,)

candidate = Anagram("squeeze")
print(candidate.base_word)
candidate.match(["queezes", "pookie", "skunk"])