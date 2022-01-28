from math import sqrt




def letnum(char):
    return (ord(char)-97)

def letter_count_list(list_of_words):
    complete_list = []
    temp_list = [0] * 26
    for word in list_of_words:
        for i in range(5):
            temp_list[letnum(word[i])] = 1
        complete_list.append(temp_list)
        temp_list = [0] * 26
    return complete_list

def countlets(list_of_freq):
    final_lst = [0] * 26
    for freq in list_of_freq:
        for i in range(26):
            final_lst[i] = final_lst[i] + freq[i]
    return final_lst

def corlets(list_of_words):
    final_lst = [[0 for columns in range(26)] for rows in range(26)]
    for word in list_of_words:
        for i in range(5):
            for j in range(0,i):
                final_lst[letnum(word[i])][letnum(word[j])] = final_lst[letnum(word[i])][letnum(word[j])] + 1
            for j in range(i+1,5):
                final_lst[letnum(word[i])][letnum(word[j])] = final_lst[letnum(word[i])][letnum(word[j])] + 1
    return final_lst

def half_letter(lflst, numwords):
    best_index = 0
    best_pct = abs(.5 - (lflst[0] / numwords))
    for i in range(26):
        cur_pct = abs(.5 - (lflst[i] / numwords))
        if cur_pct < best_pct:
            best_pct = cur_pct
            best_index = i
    return best_index

def no_cor(corlst, index, numwords):
    best_index = 0
    best_pct = abs(.5 - (corlst[index][0] / numwords))
    for i in range(26):
        cur_pct = abs(.5 - (corlst[index][i] / numwords))
        if cur_pct < best_pct:
            best_pct = cur_pct
            best_index = i
    return best_index







def remove_words(list_of_words, letter_count_lst, num_words, index, code, pos):
    remove_word_list = []
    if code == 0 or code == 1:
        for i in range(num_words):
            if letter_count_lst[i][index] != code:
                remove_word_list.append(list_of_words[i])
            if code == 1 and list_of_words[i][pos] == chr(index + 97):
                remove_word_list.append(list_of_words[i])
    else:
        for i in range(num_words):
            if list_of_words[i][pos] != chr(index + 97):
                remove_word_list.append(list_of_words[i])
    for word in remove_word_list:
        list_of_words.remove(word)
    return list_of_words

def find_word(letter_counts, numwords, index1, index2):
    for i in range(numwords):
        if letter_counts[i][index1] == 1 and letter_counts[i][index2] == 1:
            return i
    return 0

def play_wordle():
    words = open("new new new.txt", 'r')
    word_list = words.readlines()
    num_words = len(word_list)
    letter_count_lst = letter_count_list(word_list)
    while num_words > 1:
        letter_freq_lst = countlets(letter_count_lst)
        letter_cor_lst = corlets(word_list)
        first_index = half_letter(letter_freq_lst, num_words)
        second_index = no_cor(letter_cor_lst, first_index, letter_freq_lst[first_index])
        index = find_word(letter_count_lst, num_words, first_index, second_index)
        cur_word = word_list[index]
        print(cur_word)
        val = input("Input your results: ")
        if val == "22222":
            print("congrats")
            break
        for i in range(5):
            word_list = remove_words(word_list, letter_count_lst, num_words, letnum(cur_word[i]), ord(val[i]) - 48, i)
            num_words = len(word_list)
            letter_count_lst = letter_count_list(word_list)
        print(word_list)
    cur_word = word_list[0]
    print(cur_word)


play_wordle()
