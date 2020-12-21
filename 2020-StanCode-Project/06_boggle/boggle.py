"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

all_word = []
input_all_ch =[]
index_all_ch = []
str_all_ch = []
all_ans = []
count = 0

def main():
    global all_word
    global input_all_ch
    global index_all_ch
    global str_all_ch
    """
    TODO:to find all words which are made from input ch 
    """
    read_dictionary()

    for i in range(1, 5):
        ch = input(str(i) + ' row of letters:')
        ch = ch.split(' ')
        for letter in ch:
            if len(letter) != 1:
                print('Illegal input')
                return
        input_all_ch.append(ch)
    for y in range(len(input_all_ch)):
        for x in range(len(input_all_ch[0])):
            index = (x, y)
            ch = input_all_ch[y][x]
            ch = ch.lower()
            index_all_ch.append(index)
            str_all_ch.append(ch)
    get_sub_ch(index_all_ch,  str_all_ch, '', [], [])
    print('There are ' + str(count) + ' words in total.')


def get_sub_ch(index_ch, str_ch, current_str, checked_index_list, neighbor_list):
    """
    :param index_ch: [list]:all index of input letter
    :param str_ch: [list]:all letter of input
    :param current_str: [str]:to get the current letters
    :param checked_index_list: [list]:to put the checked index
    :param neighbor_list: [list]:to put indexes of neighborhood
    :return:
    """
    global all_ans
    global count
    if not has_prefix(current_str):
        return

    for j in range(len(current_str) + 1):
        sub_list = current_str[:j]
        sub_s = ''
        for k in range(len(sub_list)):
            sub_s += sub_list[k]
        if sub_s in all_word:
            if len(sub_s) >= 4:
                if sub_s not in all_ans:
                    all_ans.append(sub_s)
                    count += 1
                    print('Found " ' + current_str + '"')

    # has prefix
    else:
        # 查找16個座標
        for i in range(len(index_ch)):

            # 已經比較過的
            if i in checked_index_list:
                continue
            # 有座標可以比較才進去
            elif len(neighbor_list) > 0:
                # 最後一個進去neighbor_list：自己，比較16個座標()是否是鄰居，不是鄰居continue現在這個index[i]
                if neighbor_list[- 1][0] + 1 < index_ch[i][0] \
                        or neighbor_list[- 1][0] - 1 > index_ch[i][0] \
                        or neighbor_list[- 1][1] + 1 < index_ch[i][1] \
                        or neighbor_list[- 1][1] - 1 > index_ch[i][1]:
                    continue

            checked_index_list.append(i)
            neighbor_list.append(index_ch[i])

            if has_prefix(current_str):
                get_sub_ch(index_ch, str_ch, current_str + str_all_ch[i], checked_index_list, neighbor_list)

            checked_index_list.pop()
            neighbor_list.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    global all_word
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()  # 去除換行字元與空白
            all_word.append(word)


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in all_word:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
