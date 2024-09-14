from pprint import pprint
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for symbol in symbols:
                    text = text.replace(symbol, ' ')
                words = text.split()
                all_words[i] = words
            return all_words

    def find(self, word):
        number_word = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                number_word[key] = value.index(word.lower()) + 1
        return number_word

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего