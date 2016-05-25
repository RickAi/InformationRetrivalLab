import os
import re

# utils which are handy for file, extract operation etc..
import math


class Utils:
    @staticmethod
    def step3_write(word_list, file_name):
        if not os.path.exists("step3"):
            os.makedirs("step3")

        out_file_path = "step3/" + file_name
        out_file = open(out_file_path, "w")
        for word in sorted(word_list):
            # use regular expressions to remove anything that's not alphanumeric or underscore
            out_file.write(word + "\n")
            out_file.flush()
        out_file.close()
        print("written: " + out_file_path)

    @staticmethod
    def step2_write(word_list, file_name):
        if not os.path.exists("step2"):
            os.makedirs("step2")

        out_file_path = "step2/" + file_name
        out_file = open(out_file_path, "w")
        for word in sorted(word_list):
            # use regular expressions to remove anything that's not alphanumeric or underscore
            out_file.write(word + "\n")
            out_file.flush()
        out_file.close()
        print("written: " + out_file_path)

    @staticmethod
    def get_word_list_from_file(file_path):
        file = open(file_path, "r")
        word_list = list()
        word = file.readline()
        while word != "":
            word_list.insert(0, word.strip("\n"))
            word = file.readline()
        file.close()
        return word_list

    @staticmethod
    def is_in_stop_words_list(check_word):
        file = open("stopword_list.txt", "r")
        word = file.readline()
        while word != "":
            if check_word == word.strip("\n"):
                return True
            word = file.readline()
        file.close()
        return False

    @staticmethod
    def step1_5_write(word_list, file_name):
        if not os.path.exists("step1_5"):
            os.makedirs("step1_5")

        out_file_path = "step1_5/" + file_name
        out_file = open(out_file_path, "w")
        for word in sorted(word_list):
            # use regular expressions to remove anything that's not alphanumeric or underscore
            word_with_re = re.sub(r'[^\w]', '', word)
            if word_with_re != "" and not word_with_re.isdigit():
                out_file.write(word_with_re + "\n")
                out_file.flush()
        out_file.close()
        print("written: " + out_file_path)

    @staticmethod
    def step1_write(article):
        if not os.path.exists("step1"):
            os.makedirs("step1")
        file_name = "step1/" + article.generate_file_name()
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        file = open(file_name, "w")
        with file as write_file:
            write_file.write(article.generate_file_content())
        file.close()
        print("written: " + file_name)

    @staticmethod
    def get_next_content(file, next_index):
        next_content = ""
        next_line = file.readline()
        while not (next_line.startswith(next_index) or next_line == ""):
            next_content += next_line
            next_line = file.readline()
        return next_content.rstrip(" .")

    @staticmethod
    def get_documents_count():
        if not os.path.exists("step3"):
            os.makedirs("step3")
        files = os.listdir("step3")
        count = 0
        for file_name in files:
            if file_name.endswith(".txt"):
                count += 1
        return count

    @staticmethod
    def generate_documents_contain_this_word_count():
        file_path = "words_count_appear_in_document.txt"
        file = open(file_path, "w")
        total_words_set = Utils.get_word_count_set_from_file("words_largest_time_in_document.txt")
        for word_item in total_words_set:
            count = Utils.get_appear_count_in_documents(word_item)
            line = word_item + ", " + str(count) + "\n"
            # print("write:" + line)
            file.write(line)
            file.flush()
        file.close()
        print("write words_count_appear_in_document completed!")

    @staticmethod
    def get_appear_count_in_documents(searched_word):
        count = 0
        step4_files = os.listdir("step4_words")
        for file_name in step4_files:
            if not file_name.endswith(".txt"):
                continue
            file_path = "step4_words/" + file_name
            word_set = Utils.get_word_count_set_from_file(file_path)
            if searched_word in word_set:
                count += 1
        return count

    @staticmethod
    def generate_word_appear_time_files():
        if not os.path.exists("step4_words"):
            os.makedirs("step4_words")
        files = os.listdir("step3")
        for file_name in files:
            if not file_name.endswith(".txt"):
                continue
            file_path = "step3/" + file_name
            word_list = Utils.get_word_list_from_file(file_path)
            counts = {}
            for w in word_list:
                if w in counts:
                    counts[w] += 1
                else:
                    counts[w] = 1
            new_file_path = "step4_words/" + file_name
            new_file = open(new_file_path, "w")
            for w in sorted(counts, key=counts.get, reverse=True):
                line = '{}, {}'.format(w, counts[w]) + "\n"
                new_file.write(line)
                new_file.flush()
            new_file.close()
        print("generate_word_appear_time_files completed!")

    @staticmethod
    def generate_word_largest_appear_time_files():
        words = {}
        files = os.listdir("step4_words")
        for file_name in files:
            if not file_name.endswith(".txt"):
                continue
            file_path = "step4_words/" + file_name
            word_count_set = Utils.get_word_count_set_from_file(file_path)
            for word, count in word_count_set.items():
                if word in words:
                    if count > words[word]:
                        words[word] = count
                else:
                    words[word] = count
        file = open("words_largest_time_in_document.txt", "w")
        for word in sorted(words, key=words.get, reverse=True):
            line = '{}, {}'.format(word, words[word]) + "\n"
            file.write(line)
            file.flush()
        file.close()
        print("generate_word_largest_appear_time_files completed!")

    @staticmethod
    def get_word_count_set_from_file(file_path):
        file = open(file_path, "r")
        word_count_set = {}
        line = file.readline()
        while line != "":
            word_info = line.split(", ")
            word_count_set[word_info[0]] = word_info[1].strip("\n")
            line = file.readline()
        file.close()
        return word_count_set

    @staticmethod
    def get_largest_frequency_in_document(file_path):
        file = open(file_path, "r")
        line = file.readline()
        infos = line.split(", ")
        file.close()
        return int(infos[1].strip("\n"))

    @staticmethod
    def get_words_set_from_file(file_path):
        file = open(file_path, "r")
        word_set = set()
        line = file.readline()
        while line != "":
            infos = line.split(", ")
            word = infos[0]
            word_set.add(word)
            line = file.readline()
        file.close()
        return word_set

    @staticmethod
    def get_word_dic_from_file_with_float(file_path):
        file = open(file_path, "r")
        word_dic = dict()
        line = file.readline()
        while line != "":
            infos = line.split(", ")
            key = infos[0]
            value = infos[1].strip("\n")
            word_dic[key] = float(value)
            line = file.readline()
        file.close()
        return word_dic

    @staticmethod
    def get_word_dic_from_file(file_path):
        file = open(file_path, "r")
        word_dic = dict()
        line = file.readline()
        while line != "":
            infos = line.split(", ")
            key = infos[0]
            value = infos[1].strip("\n")
            word_dic[key] = int(value)
            line = file.readline()
        file.close()
        return word_dic

    @staticmethod
    def get_all_documents_count():
        total_count = 0
        files = os.listdir("step4_words")
        for file_name in files:
            if not file_name.endswith(".txt"):
                continue
            file_path = "step4_words/" + file_name
            file = open(file_path, "r")
            first_line = file.readline()
            if first_line != "":
                total_count += 1
            file.close()
        return total_count

    @staticmethod
    def get_word_count_appear_in_document(word):
        file_path = "words_count_appear_in_document.txt"
        file = open(file_path, "r")
        line = file.readline()
        while line != "":
            infos = line.split(", ")
            key = infos[0]
            if key == word:
                value = infos[1].strip("\n")
                return int(value)
            line = file.readline()
        return 0

    @staticmethod
    def generate_tf_rtfs():
        tf_idf_out_file = open("tf_idf_infos.txt", "w")
        files = os.listdir("step4_words")
        appear_count_word_set = Utils.get_word_count_set_from_file("words_count_appear_in_document.txt")
        for file_name in files:
            if not file_name.endswith(".txt"):
                continue
            file_path = "step4_words/" + file_name
            word_dic_in_each_file = Utils.get_word_dic_from_file(file_path)

            tf_idf_for_one_file = "index-" + file_name.split(".txt")[0] + " "

            tf_idf_values = ""
            word_tf_idf_dict = dict()
            documents_count = 1398
            for word, fre in word_dic_in_each_file.items():
                largest_fre = Utils.get_largest_frequency_in_document(file_path)
                # massive time saved with this way
                appear_in_documents_count = int(appear_count_word_set[word])
                tf = fre / largest_fre
                rtf = math.log((documents_count / appear_in_documents_count), 2)
                result = tf * rtf
                word_tf_idf_dict[word] = result
                item_info = word + "-" + str(result) + " "
                tf_idf_values += item_info

            tf_idf_for_one_file += "length-" + str(Utils.calculate_length_of_document(word_tf_idf_dict)) + " "
            tf_idf_for_one_file += tf_idf_values + "\n"
            tf_idf_out_file.write(tf_idf_for_one_file)
            tf_idf_out_file.flush()

        tf_idf_out_file.close()

    @staticmethod
    def calculate_tf_rtf_in_document(words):
        # convert to word-frequency key-value map
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        # print("input words fres: " + str(words_dict) + "\n")

        fre_values = sorted(words_dict.values())
        max_frequency = fre_values[len(fre_values) - 1]
        document_count = 1398
        appear_count_word_set = Utils.get_word_count_set_from_file("words_count_appear_in_document.txt")

        tf_rtf_dict = {}
        for word in words_dict.keys():
            frequency_in_words = words_dict[word]

            if word not in appear_count_word_set:
                continue

            appear_in_documents_count = int(appear_count_word_set[word])
            tf = frequency_in_words / max_frequency
            rtf = math.log((document_count / appear_in_documents_count), 2)

            result = tf * rtf
            tf_rtf_dict[word] = result

        return tf_rtf_dict

    @staticmethod
    def calculate_length_of_document(words_dict):
        total_square = 0
        for key, value in words_dict.items():
            total_square += value * value
        return math.sqrt(total_square)

    @staticmethod
    def get_float_value_in_dict(word, dict):
        for w, f in dict.items():
            if w == word:
                return f
        return 0

    @staticmethod
    def get_tf_idf_dic(infos):
        word_tf_idf_dict = dict()
        index = -1
        for info in infos:
            index += 1
            if index == 0 or index == 1:
                continue
            tf_idf_info = info.split("-")
            if tf_idf_info[0] == "\n":
                continue
            word_tf_idf_dict[tf_idf_info[0]] = float(tf_idf_info[1])
        return word_tf_idf_dict

    @staticmethod
    def return_query_result_dict(query_words_tf_rtf_dict, index_length_dict, index_tf_idf_dict):
        # init length of query
        result_dict = {}
        query_length = Utils.calculate_length_of_document(query_words_tf_rtf_dict)

        index = 0
        while index < 1398:
            index += 1
            if index == 471 or index == 995:
                continue
            document_length = index_length_dict[index]
            tf_idfs = index_tf_idf_dict[index]
            total_up = 0
            for word, fre in query_words_tf_rtf_dict.items():
                value_in_document = Utils.get_float_value_in_dict(word, tf_idfs)
                # if the document do contain this word
                if value_in_document != 0:
                    total_up += value_in_document * query_words_tf_rtf_dict[word]
            cos_result = total_up / (query_length * document_length)
            result_dict[index] = cos_result

        return result_dict
