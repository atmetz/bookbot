def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    num_words = word_count(file_contents)
    char_dict = character_count(file_contents)
    char_sorted = chars_dict_to_sorted_list(char_dict)

    report(book_path, num_words, char_sorted)

def word_count(book):
    count = 0
    words = book.split()
    for word in words:
        count += 1
    return count

def character_count(book):
    lowercase = book.lower()
    char_count = {}

    for character in lowercase:
        
        if character in char_count:
            char_count[character] += 1
        else:
            char_count.update({character: 1})

    return(char_count)

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(book_path, num_words, char_dict):
    #char_dict.sort(reverse=True, key=sort_on)

    print(f"--- Begin reprot of {book_path} ---")
    print(f"{num_words} words found in the docutment")
    print()
    for item in char_dict:
        if item['char'].isalpha():
            print(f"The '{item['char']}' was found {item['num']} times")
    print("--- End report")

main()
