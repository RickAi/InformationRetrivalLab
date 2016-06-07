import numbers
import operator
import time
import os
import re
import porter
from utils import Utils
from article import Article

# steps to generate cache files, I have explain it in README.txt

# step1: extract all the data to files
# step1_extract_raw_files()

# step1_5: break sentences into words
# step1_5_break_into_words()

# step2: remove words in stop words list
# step2_remove_stop_words()

# step3: stemming pre-processing step
# step3_stemming_processing()

# setp4_tf_rtf_basis()

# step5_tf_rtfs_cos()

# ask user to input first, then parse words to list

def query_loop(query, appear_count_word_set):
    word_list = query.split()
    words = []
    count = 0
    for word in sorted(word_list):
        word_with_re = re.sub(r'[^\w]', '', word)
        if word_with_re != "" and not word_with_re.isdigit():
            words.insert(count, word_with_re)
            count += 1

    after_stopped_words = []
    count = 0
    for word in words:
        if not Utils.is_in_stop_words_list(word):
            after_stopped_words.insert(count, word)
            count += 1

    # stem each word
    p = porter.PorterStemmer()
    stemmed_words = []
    count = 0
    for word in after_stopped_words:
        stemmed_word = p.stem(word)
        stemmed_words.insert(count, stemmed_word)
        count += 1

    if len(stemmed_words) == 0:
        print("\nNo result!\n")
        return

    # calculate tf rtf for each word, return a dict
    tf_rtf_dict = Utils.calculate_tf_rtf_in_document(stemmed_words, appear_count_word_set)
    # print("\n" + "Query tf-idf:\n")
    # print(tf_rtf_dict)
    # print("\n")

    # calculate cos result for each document
    result_dict = Utils.return_query_result_dict(tf_rtf_dict, index_length_dict, index_tf_idf_dict)

    if len(result_dict) == 0:
        print("\nNo result!\n")
        return

    # sort the dict
    sorted_dict = sorted(result_dict.items(), key=operator.itemgetter(1))
    reverse_sorted_dict = sorted_dict[::-1]

    # get top 100 of cos result
    count = 0
    top_10_list = []
    for item in reverse_sorted_dict:
        if count < 100:
            top_10_list.insert(count, item)
            count += 1

    # print it out to user
    rank = 1
    for item in top_10_list:
        index = item[0]
        cos_value = item[1]
        if float(cos_value) != 0.0:
            print("top \t" + str(rank) + ":\tindex: " + str(index) + "\tvalue: " + str(cos_value))
        rank += 1


def step1_extract_raw_files():
    file = open('cranfield_collection.txt', 'r')
    line_index = 1

    # jump to first title
    file.readline()
    next_line = file.readline()

    # extract data
    while next_line != "":
        article = Article()
        # index
        article.index = line_index
        line_index += 1

        article.title = Utils.get_next_content(file, ".A")
        article.author = Utils.get_next_content(file, ".B")
        article.bubble = Utils.get_next_content(file, ".W")
        article.content = Utils.get_next_content(file, ".I")

        Utils.step1_write(article)

        next_line = file.readline()

    print("completed!")


def step1_5_break_into_words():
    files = os.listdir("step1")
    for file_name in files:
        if not file_name.endswith(".txt"):
            continue

        file_path = "step1/" + file_name
        file = open(file_path, "r")
        word_list = file.read().split()
        Utils.step1_5_write(word_list, file_name)


def step2_remove_stop_words():
    files = os.listdir("step1_5")
    for file_name in files:
        if not file_name.endswith(".txt"):
            continue
        file_path = "step1_5/" + file_name
        word_list = Utils.get_word_list_from_file(file_path)
        new_word_list = list()
        for word in word_list:
            if not Utils.is_in_stop_words_list(word):
                new_word_list.insert(0, word)
        Utils.step2_write(new_word_list, file_name)


def step3_stemming_processing():
    files = os.listdir("step2")
    for file_name in files:
        if not file_name.endswith(".txt"):
            continue
        file_path = "step2/" + file_name
        word_list = Utils.get_word_list_from_file(file_path)
        new_word_list = list()
        for word in word_list:
            p = porter.PorterStemmer()
            new_word_list.insert(0, p.stem(word))
        Utils.step3_write(new_word_list, file_name)


def setp4_tf_rtf_basis():
    Utils.generate_word_appear_time_files()
    # do not need that file
    Utils.generate_word_largest_appear_time_files()
    Utils.generate_documents_contain_this_word_count()
    pass


def step5_tf_rtfs_cos():
    Utils.generate_tf_rtfs()


if __name__ == '__main__':
    start_time = time.time()

    # init start
    tf_idf_infos_file = open("tf_idf_infos.txt", "r")
    index_length_dict = dict()
    index_tf_idf_dict = dict()
    appear_count_word_set = Utils.get_word_count_set_from_file("words_count_appear_in_document.txt")

    # cache dicts into memory
    tf_idf_one_file_info = tf_idf_infos_file.readline()

    # parse tf-idf info from file generated before
    while tf_idf_one_file_info != "":
        infos = tf_idf_one_file_info.split(" ")
        index_info = infos[0]
        length_info = infos[1]
        index_splits = index_info.split("-")
        length_splits = length_info.split("-")
        index_length_dict[int(index_splits[1])] = float(length_splits[1])
        index_tf_idf_dict[int(index_splits[1])] = Utils.get_tf_idf_dic(infos)
        tf_idf_one_file_info = tf_idf_infos_file.readline()
    tf_idf_infos_file.close()

    end_time = time.time()
    # init finished, print init cost time
    print("init success! Cost time: %.2f seconds" % (end_time - start_time))

    # ready to query from input
    query = input("Ready to query (enter nothing to exit):")
    while query != "":
        query_start_time = time.time()
        query_loop(query, appear_count_word_set)
        query_end_time = time.time()
        # print result
        print("query success! Cost time: %.2f seconds" % (query_end_time - query_start_time) + "\n")

        # ask user a document number to get content of article
        see_document = input("Enter document number to see content (enter nothing to exit):")
        while see_document != "":
            try:
                # the number should be a valid range
                if int(see_document) > 1400 or int(see_document) < 1:
                    print("cannot find that document, enter again!")
                    see_document = input("Enter document number to see content (enter nothing to exit):")
                    continue
                file = open("step1/" + see_document + ".txt")
                content = file.read()
                print("\n============================================")
                print(content)
                print("============================================\n")
                file.close()
                see_document = input("Enter document number to see content (enter nothing to exit):")
            except ValueError:
                # if user enter wrong number, like string, it should not be allowed
                print("please enter valid integer number for document!");
                see_document = input("Enter document number to see content (enter nothing to exit):")
        query = input("Ready to query(enter nothing to stop):")
