import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star])")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Claire Deniau, Full Time Writter')

st.info('Developer Advocate, Content Creator and ex-Professor with an interest in Data Science and Bioinformatics')

icon_size = 20

st_button('', 'https://904043qbs92b1wclrfqrl2o04f.hop.clickbank.net', 'Start Your Business Here ', icon_size)
st_button('', 'https://c5d9b7qiu4492reblg1v63x7-a.hop.clickbank.net', 'Sign Up Chat Jobs', icon_size)
st_button('', 'https://ab27d-ofq1v34x97opuivnpx2g.hop.clickbank.net', 'Lose Weight Here', icon_size)
st_button('', 'https://afflat3e1.com/trk/lnk/6EE20DC6-6A0D-4E6D-B3A3-88C5A208DE04/?o=16680&c=918277&a=629795&k=3B399C50958C7CDA94FF99C779121934&l=17850', 'Claim FREE Paypal Pay', icon_size)
st_button('', 'https://afflat3e1.com/trk/lnk/6EE20DC6-6A0D-4E6D-B3A3-88C5A208DE04/?o=6365&c=918277&a=629795&k=ABD3BB5FE3B257E042716B56F465D35B&l=5077', 'Earn Reviewing Apps', icon_size)
st_button('', 'https://d1b569pjq6s8bscm64u3ba2g2k.hop.clickbank.net', 'Sign Earn Exra Reviewing Apps', icon_size)
