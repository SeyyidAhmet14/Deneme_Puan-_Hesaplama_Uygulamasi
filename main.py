import streamlit as st

#Doğru Yanlış Boş Yaptığın Sorular
#Baslik atilacak ve baslik su "Deneme Puani Hesaplama Uygulaması"
def net_hesaplama(d,y):
    return d-y/3 #3 yanlis go to van dogru

katsayi_dusuk=2 #Diger dersler
katsayi_yuksek=3 #Matematik,Fen,Turkce

st.title("Deneme Puanı Hesaplama Uygulaması 📝")
st.header("Matematik")
mat_d=st.number_input("Matematik Doğru Yaptığın Sorular",min_value=0,step=1)
mat_y=st.number_input("Matematik Yanlış Yaptığın Sorular",min_value=0,step=1)
mat_b=st.number_input("Matematik Boş Yaptığın Sorular",min_value=0,step=1)

st.header("Türkçe")
turk_d=st.number_input("Türkçe Doğru Yaptığın Sorular",min_value=0,step=1)
turk_y=st.number_input("Türkçe Yanlış Yaptığın Sorular",min_value=0,step=1)
turk_b=st.number_input("Türkçe Boş Yaptığın Sorular",min_value=0,step=1)

st.header("Fen Bilimleri")
fen_d=st.number_input("Fen Bilimleri Doğru Yaptığın Sorular",min_value=0,step=1)
fen_y=st.number_input("Fen Bilimleri Yanlış Yaptığın Sorular",min_value=0,step=1)
fen_b=st.number_input("Fen Bilimleri Boş Yaptığın Sorular",min_value=0,step=1)

st.header("Sosyal Bilgiler")
sos_d=st.number_input("Sosyal Bilgiler Doğru Yaptığın Sorular",min_value=0,step=1)
sos_y=st.number_input("Sosyal Bilgiler Yanlış Yaptığın Sorular",min_value=0,step=1)
sos_b=st.number_input("Sosyal Bilgiler Boş Yaptığın Sorular",min_value=0,step=1)

st.header("İngilizce")
ing_d=st.number_input("İngilizce Doğru Yaptığın Sorular",min_value=0,step=1)
ing_y=st.number_input("İngilizce Yanlış Yaptığın Sorular",min_value=0,step=1)
ing_b=st.number_input("İngilizce Boş Yaptığın Sorular",min_value=0,step=1)

st.header("Din ve Ahlak Bilgileri")
dkabd_d=st.number_input("Din ve Ahlak Bilgileri Doğru Yaptığın Sorular",min_value=0,step=1)
dkabd_y=st.number_input("Din ve Ahlak Bilgileri Yanlış Yaptığın Sorular",min_value=0,step=1)
dkabd_b=st.number_input("Din ve Ahlak Bilgileri Boş Yaptığın Sorular",min_value=0,step=1)

if st.button("Hesapla"):
    mat_net = net_hesaplama(mat_d, mat_y)
    turk_net = net_hesaplama(turk_d, turk_y)
    fen_net = net_hesaplama(fen_d, fen_y)
    sos_net = net_hesaplama(sos_d, sos_y)
    ing_net = net_hesaplama(ing_d, ing_y)
    dkabd_net = net_hesaplama(dkabd_d, dkabd_y)
    toplam_puan=(katsayi_yuksek*(mat_net+turk_net+fen_net)+katsayi_dusuk*(sos_net+ing_net+dkabd_net))
    st.subheader("Sonuçlar🎯")
    st.write(f"Matematik Net:{mat_net:.3f}")
    st.write(f"Türkçe Net:{turk_net:.2f}")
    st.write(f"Fen Net:{fen_net:.2f}")
    st.write(f"Sosyal Net:{sos_net:.2f}")
    st.write(f"İngilizce Net:{ing_net:.2f}")
    st.write(f"Din Kültürü Net:{dkabd_net:.2f}")
    st.success(f"Toplam Puan: {toplam_puan:.2f}")
#sa
