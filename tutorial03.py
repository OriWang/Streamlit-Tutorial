import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title("Hi, I am a streamlit app.")
st.subheader("Tutorial")
st.header("Header")
st.text("Simple text")
st.markdown("`print('good')` is a code")
st.caption("Caption")
st.latex(r"\frac{4}{6}")
j = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
st.json(j)
code = """
print("Hello, world!")
if a == "3":
    print(a)
else:
    print(a+1)
"""
st.code(code, language="python")
df = pd.DataFrame(j)
st.write(df)
st.metric(label="wind speed", value="12 ms⁻¹", delta="1.1 ms⁻¹")
st.table(df)
st.dataframe(df.style.highlight_max(axis=0, color="skyblue"))

st.markdown("---")
flower_image = Image(r".\flower.jpg")
st.image(flower_image, width=500, caption="花廊")

st.markdown("---")
state = st.checkbox("learn streamlit", value=False, key=1)
if state:
    st.write("ticked")
else:
    st.write("unticked")

st.write("String", 32.2, {10: 1, 20: 2, 30: 3})

# map_data = {
#     "longitude": [116.7461293, 116.8846094, 119.75],
#     "latitude": [36.5598627, 36.6715457, 36.38],
#     "name": ["长清", "槐荫", "高密"],
# }
# st.map(map_data)

count = 0
def show_count(count: int):
    count += 1
    base = f"点了**{count}**次了"
    if count >= 5:
        string = base + ", 还点!"
    else:
        string = base
    st.markdown(string)
    
if st.button("click", key="btn1"):
    st.header("clicked")

country = st.radio("In which country do you live? ", options=("US", "UK", "China"))
car = st.selectbox("What's your favorite car?", options=("Benz", "BMW", "Tesla"))
sports = st.multiselect("What sports do you like?", options=("Football", "Basketball", "tennis", "table tennis"))
st.write(sports)

st.markdown("---")
st.markdown("## Upload File")
imgs = st.file_uploader("Upload an image file.", 
                       type=["jpg", "png", "jpeg"],
                       accept_multiple_files=True)
if imgs:
    st.image(imgs)
    
st.markdown("---")
st.markdown("## Other interactive wigits")
st.slider("你的年龄: ", min_value=1, max_value=120)
st.select_slider("Grade", options=(1, 60, 80, 90, 100))
st.text_area("Input some text")


