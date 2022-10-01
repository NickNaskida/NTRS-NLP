import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# from transformers import pipeline


def filter_file_text_words(pdf_text) -> list:
    """
    Filter file text words.

    :param pdf_text: pdf extracted text
    :return: filtered word list
    """
    filtered_word_list = []
    stop_words = set(stopwords.words("english"))

    for word in word_tokenize(pdf_text):
        if word.casefold() not in stop_words:
            if word.isalpha() and len(word) > 2:
                filtered_word_list.append(word)

    return filtered_word_list


def extract_keywords_and_collocations(pdf_text) -> tuple:
    """
    Get keywords and collocations from the text.

    :param pdf_text: pdf extracted text
    :return: keywords and collocations
    """
    lemmatizer = WordNetLemmatizer()

    filtered_word_list = filter_file_text_words(pdf_text)

    # Extract keywords
    frequent_words = []
    frequency_distribution = FreqDist(filtered_word_list)

    for item in frequency_distribution.most_common(30):
        frequent_words.append(item[0])

    # Extract collocations
    collocation_words = []
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_word_list]
    nltk_text = nltk.Text(lemmatized_words)

    for item in nltk_text.collocation_list():
        collocation_words.append(str(item[0]) + ' ' + str(item[1]))

    return ",".join(frequent_words), ",".join(collocation_words)


# def summarize_text(pdf_text):
#     summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
#
#     summary = summarizer(pdf_text[:500], min_length=20, max_length=200)
#     print(summary[0]['summary_text'])
