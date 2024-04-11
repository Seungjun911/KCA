import streamlit as st

st.title('일반무선국 기술기준 Helper')

# 초기 상태 설정
if "show_results" not in st.session_state:
    st.session_state.show_results = False

# 무선국종 선택
st.session_state.category = st.selectbox(
    '무선국종선택:',
    ['무선국종을 선택하세요', '41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국'],
    index=0
)

options = {
    '41': ['VHF(DSC)', 'MF/HF', 'MF/HF(DSC)', 'D-MF/HF', 'EPIRB', 'AIS', 'TWO-WAY'],
    '42': ['VHF(DSC)', 'MF/HF', 'MF/HF(DSC)', 'D-MF/HF', 'EPIRB', 'AIS', 'TWO-WAY'],
    '44': ['TRS', '기타'],
    '92': ['기타'],
    '94': ['마을방송', '기타'],
    '': ['먼저 무선국종을 선택하세요']  # 기본값
}

# 무선국종에 따른 세부장치 옵션 설정
selected_category = st.session_state.category.split('.')[0]
st.session_state.subcategory_options = options.get(selected_category, ['먼저 카테고리를 선택하세요'])
st.session_state.subcategory = st.selectbox(
    '세부장치:',
    st.session_state.subcategory_options
)

st.session_state.output = st.text_input('출력 (W)')
st.session_state.frequency = st.text_input('주파수 (Hz)')
st.session_state.waveform = st.text_input('전파형식')

if st.button('계산하기'):
    st.session_state.show_results = True

# 계산 결과 표시
if st.session_state.show_results:
    st.title('계산 결과')
    st.write(f"무선국종: {st.session_state.category}")
    st.write(f"세부장치: {st.session_state.subcategory}")
    st.write(f"출력: {st.session_state.output} W")
    st.write(f"주파수: {st.session_state.frequency} Hz")
    st.write(f"전파형식: {st.session_state.waveform}")
    
    if st.button("접기"):
        st.session_state.show_results = False
