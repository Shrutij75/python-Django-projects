import os
import nltk
import textstat
import pandas as pd
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Ensure the necessary NLTK data files are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define a function to calculate syllables in a word
def syllable_count(word):
    return textstat.syllable_count(word)

# Define a function to check if a word is complex (having 3 or more syllables)
def is_complex_word(word):
    return syllable_count(word) >= 3

# Function to count personal pronouns
def count_personal_pronouns(text):
    personal_pronouns = set(['I', 'we', 'my', 'ours', 'us'])
    words = word_tokenize(text)
    return sum(1 for word in words if word.lower() in personal_pronouns)

# Function to perform text analysis
def text_analysis(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    word_count = len(words)
    sentence_count = len(sentences)
    complex_word_count = sum(1 for word in words if is_complex_word(word))
    personal_pronoun_count = count_personal_pronouns(text)
    syllables_per_word = sum(syllable_count(word) for word in words) / word_count
    average_word_length = sum(len(word) for word in words) / word_count
    average_sentence_length = word_count / sentence_count
    percentage_complex_words = (complex_word_count / word_count) * 100
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    
    # Assuming positive and negative scores are predefined as 0 for simplicity
    positive_score = 0
    negative_score = 0
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001)
    
    return {
        'Word Count': word_count,
        'Sentence Count': sentence_count,
        'Average Word Length': average_word_length,
        'Average Sentence Length': average_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Complex Word Count': complex_word_count,
        'Syllables per Word': syllables_per_word,
        'Personal Pronouns': personal_pronoun_count,
        'Flesch Reading Ease': flesch_reading_ease,
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score
    }

# Directory containing the articles
articles_dir = 'articles'

# Data structure for the output
output_data = []

# Process each article and perform text analysis
for file_name in os.listdir(articles_dir):
    file_path = os.path.join(articles_dir, file_name)
    try:
        analysis_results = text_analysis(file_path)
        analysis_results['File Name'] = file_name
        output_data.append(analysis_results)
        print(f'Analysis for {file_name} completed successfully.')
    except Exception as e:
        print(f'Error processing {file_name}: {e}')

print('Text analysis completed.')

# Save the analysis results to an Excel file
output_df = pd.DataFrame(output_data)
output_file = "C:\\Users\\DELL\\Downloads\\Output Data Structure.xlsx"
output_df.to_excel(output_file, index=False)

print(f'Analysis results saved to {output_file}.')
