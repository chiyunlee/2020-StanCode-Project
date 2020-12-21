"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

all_word = []
all_ans = []
count = 0


def main():
    start = time.process_time()
    global all_ans
    global count
    read_dictionary()
    while True:
        print('Welcome to stanCode "Anagram Generator" (or' + EXIT + ' to quit)')
        input_word = input('Find anagram for:')
        if input_word == EXIT:
            print('EXIT!')
            break
        else:
            find_anagrams(input_word)
            print(str(len(all_ans)) + ' anagrams:' + str(all_ans))
            count = 0
            all_ans = []
    end = time.process_time()
    print(end-start)


def read_dictionary():
    global all_word
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()  # 去除換行字元與空白
            all_word.append(word)


def find_anagrams(s):
    """
    :param s:input a string for finding its anagrams
    :return:finds all anagrams
    """
    find_anagrams_helper(s, [])


def find_anagrams_helper(s, current):
    global all_ans
    global all_word
    global count

    if len(s) == len(current):
        ans = ''
        for letter in current:
            ans += s[letter]
        if ans in all_word:  #all word存所有的單字
            if ans not in all_ans:
                all_ans.append(ans)
                print('Searching...')
                print('Found: '+ans)

    else:
        for i in range(len(s)):
            if i not in current:
                current.append(i)
                ans = ''
                for letter in current:
                    ans += s[letter]
                    if has_prefix(ans):
                        find_anagrams_helper(s, current)
                current.pop()


def has_prefix(sub_s):
    """
    :param sub_s:input the sub-string until now
    :return:if no words start with sub_s return False,else return True
    """
    for word in all_word:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
