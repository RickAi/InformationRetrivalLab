import math


def read_query_dict():
    file = open("cranfield_queries.txt")
    query_dict = dict()
    content = ""
    query_info = file.readline()
    query_index = 1
    while query_info != "":
        file.readline()
        sub_content = file.readline()
        while not sub_content.startswith(".I") and sub_content != "":
            content += sub_content
            sub_content = file.readline()
        query_info = sub_content
        query_dict[query_index] = content
        content = ""
        query_index += 1
    file.close()
    return query_dict

def read_evalution_dict():
    file = open('cranfield_relevance.txt', 'r')
    line_info = file.readline()
    evaluate_dict = dict()
    temp_document_score_list = list()
    query_index = 1
    while line_info != "":
        infos = line_info.split()
        document_index = infos[1]
        relative_score = infos[2]
        temp_document_score_list.append({document_index: abs(int(relative_score))})

        if int(relative_score) < 0:
            evaluate_dict[query_index] = temp_document_score_list
            temp_document_score_list = list()
            query_index += 1

        line_info = file.readline()
    file.close()
    return evaluate_dict

if __name__ == '__main__':
    # calculate NDCG of sample queries

    # read all evaluation data into memory
    evaluate_dict = read_evalution_dict()

    query_dict = read_query_dict()

    G = 0
    CG = 0
    DCG = 0

    g_list = []
    cg_list = []
    dcg_list = []

    for query_index, doc_score in evaluate_dict.items():
        for item_score in doc_score:
            values = list(item_score.values())
            item_score = int(values[0])
            G = item_score
            CG += G
            try:
                DCG += G / math.log(query_index, 2)
            except:
                DCG += 0

        g_list.append(G)
        cg_list.append(CG)
        dcg_list.append(DCG)
        G = 0
        CG = 0
        DCG = 0

    query_index = 0
    while query_index < len(g_list):
        print("Query index: " + str(query_index + 1) + "\tCG: "
              + str(cg_list[query_index]) + "\tDCG: "+ str(dcg_list[query_index]))
        query_index += 1


