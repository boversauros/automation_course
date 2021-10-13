# Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''!()-[]{};:'"“”\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
"we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
"their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

file_contents =  "Music has been broadly defined by Fetis as “the art of moving the feelings by combinations of sounds;” taken in this broad sense it may be considered as coeval with the human race music."

# LEARNER CODE START HERE
clean_text = ""
result = {}

for char in file_contents:
    if char not in punctuations:
        clean_text += char

for word in clean_text.lower().split():
    if word not in uninteresting_words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

