def get_num_words(book_text):
    word_list = book_text.split()
    l = len(word_list)
    return l


def get_num_char(book_text):
    char_text = {}
    for j in book_text:
        i = j.lower()
        if i.lower() in char_text:
            char_text[i] += 1
        else:
            char_text[i] = 1
    return char_text

def sort_on(dict):
    return dict["num"]


def sort_dict(unsorted_dict):
    unsorted_list = []

    for i in unsorted_dict:
        unsorted_list.append({"name": i, "num": unsorted_dict[i]})

    unsorted_list.sort(reverse=True, key=sort_on)
    return unsorted_list