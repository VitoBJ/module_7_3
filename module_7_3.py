import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    contents = file.read()
                    contents = contents.lower()
                    contents = contents.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    words = contents.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}

        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                positions[file_name] = words.index(word) + 1
            else:
                positions[file_name] = None

        return positions

    def count(self, word):
        word = word.lower()
        counts = {}

        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)

        return counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
import os

print("Текущая директория:", os.getcwd())