from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer

corpus = [
    '我 是 一名 中国人 。',
    '你 也 是 一名 中国人 。',
    '他 是 一个 日本人 。',
    '那个 东西 是 不是 一个 人',
]
vectorizer = CountVectorizer()
count = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names())   #打印所有词
# print(vectorizer.vocabulary_)            #打印词向量中每个词的顺序
# print(count.toarray())                  #打印每句话词频向量

transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count)
# print(tfidf_matrix.toarray())


# 求列表array中最大的k个数的下标，返回一个k元素的列表，当k大于array的个数时，无效的结果返回None
def part_sort(array, k):
    # result中存的是下标
    result = []
    # 来个初始化，当k>arr.len时，无效的结果返回None
    for i in range(k):
        result.append(None)
    for i in range(array.__len__()):
        for j in range(result.__len__()):
            if result[j] is None:
                result[j] = i
                break
            if array[i] > array[result[j]]:
                # 将下标 i 插入 result[j] 位置,并弹出最后一个无用的下标
                result.insert(j, i)
                result.pop()
                break
    return result

for i in range(4):
    for j in part_sort(tfidf_matrix.toarray()[i], 2):
        print(vectorizer.get_feature_names()[j])