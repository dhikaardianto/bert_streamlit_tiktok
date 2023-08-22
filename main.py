from preprocessing_data import preprocessing_tiktok
from classifier_model import klasifikasi_tiktok
import streamlit as st


st.title('Klasifikasi Sentimen dari Ulasan Aplikasi Tiktok')
st.write('Tentukan sentimen dari ulasan yang diperoleh ')


contoh_teks = st.selectbox(
    'Contoh teks review / ulasan aplikasi Tiktok: ',
    ('Tik tok ko sekarang sering keluar sendiri si aneh abis itu ga bisa masuk lagi ke apk nya', 'Aplikasi yang sangat mantap dan terbaik.', 'Cukup menghibur walau menghabiskan waktu.'))

if contoh_teks != None:
    processed_example = preprocessing_tiktok(contoh_teks)
    hasil_sentimen, persentase = klasifikasi_tiktok(processed_example)
    st.write(f"Sentimen dari '{contoh_teks}' adalah: :blue[{hasil_sentimen}] dengan tingkat persentase = :blue[{persentase}]",
             )
else:
    print('Maaf, ada masalah')

st.subheader('Masukkan :blue[ulasan] yang anda peroleh ke bawah:')

ulasan = st.text_area('Teks Ulasan:', )

if st.button('Prediksi Sentimen'):
    processed_sentence = preprocessing_tiktok(ulasan)
    # Jika hasil preprocessing berupa kalimat kosong
    if len(processed_sentence) == 0:
        st.write(f"Tidak bisa melakukan klasifikasi. Kalimat yang anda masukkan terlalu singkat atau hanya berisi angka, emoticon atau kata-kata stopword.")
        st.write(f"Ulasan anda: {ulasan}")
    else:
        hasil_sentimen_tiktok, persentase_tiktok = klasifikasi_tiktok(
            processed_sentence)
        st.write(f"Teks yang dimasukkan:",
                 )
        st.write(f"'{ulasan}'")
        st.write(
            f"Sentimen: :blue[{hasil_sentimen_tiktok}] dengan tingkat persentase = :blue[{persentase_tiktok}]")

else:
    st.write('Belum ada ulasan yang masuk')
