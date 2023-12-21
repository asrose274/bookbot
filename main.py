def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = char_count(text)
    print(characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    count = len(words)
    return count

def char_count(text):
    num_of_chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if(char in num_of_chars):
            count = num_of_chars[char]
            num_of_chars[char] = count + 1
        else:
            num_of_chars[char] = 1
    return num_of_chars

main()