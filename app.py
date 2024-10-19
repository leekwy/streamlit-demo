import streamlit as st
import pandas as pd
import numpy as np
import base64

def render_svg(svg_file):
    with open(svg_file, "r") as f:
        svg = f.read()
    
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" width=250/>'
    st.write(html, unsafe_allow_html=True)

# SVG 파일 경로
svg_file = "azit.svg"

st.write("## SVG 이미지 표시")
render_svg(svg_file)

# URL을 통해 이미지 표시
st.image("http://azitcafe.ddns.net:8282/media/1", caption="온라인 이미지")

# 랜덤 이미지 생성 함수
def generate_random_image(size=(100, 100)):
    return np.random.randint(0, 255, (*size, 3), dtype=np.uint8)

# Streamlit 앱 제목
st.title("가로로 배열된 랜덤 이미지")

# 이미지 개수와 열 개수 설정
num_images = 5
num_columns = 5

# 열 생성
cols = st.columns(num_columns)

# 이미지 생성 및 표시
for i in range(num_images):
    with cols[i % num_columns]:
        img = generate_random_image()
        st.image(img, caption=f"이미지 #{i+1}", use_column_width=True)

# 새로운 이미지 생성 버튼
if st.button("새로운 이미지 생성"):
    st.experimental_rerun()
    
# 기본값 설정
default_value = 5

# 쿼리 파라미터에서 값을 가져오거나 기본값 사용
value = int(st.query_params.get("value", default_value))

# 슬라이더 위젯 표시
new_value = st.slider("값을 선택하세요", min_value=0, max_value=10, value=value)

# 쿼리 파라미터 업데이트
st.query_params["value"] = new_value

# 현재 URL 표시
st.write(f"현재 URL: {st.query_params}")

view = [100, 150, 30]
st.write('# Youtube view')
st.write('## 원 데이터')
view
st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview