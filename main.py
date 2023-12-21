def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    characters = char_count(text)
    sorted_list = sort_list(characters)
    # print(sorted_listed)
    print("--- Begin report of books/frankenstein.txt ---")
    print("\n")
    print(f"{words} words found in the book")
    print("\n")
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")
    print("\n")
    print("--- End Report ---")

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

def sort_on(d):
    return d["char"]

def sort_list(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(reverse=False, key=sort_on)
    return sorted_list

main()