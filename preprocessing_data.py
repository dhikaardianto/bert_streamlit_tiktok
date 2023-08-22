import re
# Mengubah kalimat ke kata dasar menggunakan sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas as pd

# stopword dari file stopword.txt
txt_stopword = pd.read_csv(f"data/stopword_tiktok.txt", names = ["stopwords"], header= None)
stopword_full = list(txt_stopword.stopwords.values)
normalized_word = pd.read_csv(f'data/kamus_alay.csv')

normalized_word_dict={}

for index, row in normalized_word.iterrows():
  if row[0] not in normalized_word_dict:
    normalized_word_dict[row[0]] = row[1]

factory = StemmerFactory()
stemmer = factory.create_stemmer()



def clean_text(review_text):
  # Mengganti titik di akhir text dengan spasi
  review_text = re.sub(r'(\w)[.](\w)', r'\1 \2', review_text.lower())
  # Mengganti baris baru \n dan lebih dari satu titik dengan spasi
  review_text = re.sub(r'\n', ' ', review_text)
  # Mengganti lebih dari 1 titik menjadi spasi
  review_text = re.sub(r'[.]+', ' ', review_text)
  # Mengganti lebih dari 1 koma menjadi spasi
  review_text = re.sub(r'[,]+', ' ', review_text)
	# hanya ambil alfabet dan spasi
  review_text = "".join(c.lower() for c in review_text if c.isalpha() or c in [" "])
	# buang spasi berlebih dan gabung lagi
  review_text = " ".join(kata for kata in review_text.split())
  return review_text


# Membuat fungsi menghapus stopword
def remove_stopword(sentence):
  result = sentence.split(' ')
  result = [ word for word in result if word not in stopword_full]
  result = " ".join(result)
  return result

# Normalize words
def normalized_term(sentence):
  words = sentence.split()  # Memisahkan teks menjadi kata-kata
  normalized_words = [normalized_word_dict.get(word, word) for word in words]  # Normalisasi kata-kata
  normalized_document = ' '.join(normalized_words)  # Menggabungkan kembali kata-kata menjadi teks
  return normalized_document

# preprocessing review tiktok
def preprocessing_tiktok(text):
  result = clean_text(text)    # Membersihakn review
  result = normalized_term(result) # Normalisasi Review
  result = remove_stopword(result) # Menghapus stopword
  result = stemmer.stem(result)    # Stemming

  return result
