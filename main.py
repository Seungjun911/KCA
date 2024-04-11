import streamlit as st
import numpy as np

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
st.session_state.waveform = st.text_input('전파형식(대역폭+변조방식)' , max_chars=8)

def get_waveform_description(waveform):
    waveform = waveform.upper()[-3:]
    
    # 설명 사전
    firstCharDescriptions = {
        'N': "무변조파",
        'A': "양측파대",
        'H': "단측파대의 전반송파",
        'R': "단측파대의 저감 또는 가변레벨 반송파",
        'J': "단측파대의 억압반송파",
        'B': "독립측파대",
        'C': "잔류측파대",
        'F': "주파수변조(각)",
        'G': "위상변조(각)",
        'D': "동시 또는 순서에 따라 진폭과 각변조",
        'P': "무변조 연속펄스",
        'K': "진폭변조",
        'L': "폭(기간)변조",
        'M': "위치(위상)변조",
        'Q': "펄스기간 중 각변조",
        'V': "변조 조합 또는 다른 방법",
        'W': "규정된 것 외의 조합변조",
        'X': "규정된 것 외의 변조"
    }
    
    secondCharDescriptions = {
        '0': "무변조",
        '1': "부반송파를 사용하지 않는 디지털 1개 채널",
        '2': "부반송파를 사용하는 디지털 1개 채널",
        '3': "아날로그 1개 채널",
        '7': "디지털 2개 채널",
        '8': "아날로그 2개 채널",
        '9': "아날로그+디지털",
        'X': "규정된 것 외의 형태"
    }
    
    thirdCharDescriptions = {
        'N': "정보송출 없음",
        'A': "전신: 가청수신용",
        'B': "전신: 자동수신용",
        'C': "팩시밀리",
        'D': "데이터, 비가청",
        'E': "전화",
        'F': "텔레비전(비디오)",
        'W': "2개 이상의 조합",
        'X': "규정된 것 외의 형태"
    }
    
    if len(waveform) != 3:
        return "잘못된 전파형식"
    
    firstDescription = firstCharDescriptions.get(waveform[0], "알 수 없음")
    secondDescription = secondCharDescriptions.get(waveform[1], "알 수 없음")
    thirdDescription = thirdCharDescriptions.get(waveform[2], "알 수 없음")
    
    # 수정된 부분: 들여쓰기가 함수 내 다른 줄들과 일치하도록 조정
    return f'<span style="color: red;">{firstDescription}</span>, <span style="color: green;">{secondDescription}</span>, <span style="color: blue;">{thirdDescription}</span>'

if st.button('계산하기'):
    st.session_state.show_results = True




# 결과 표시 로직
if st.session_state.show_results:
    st.subheader('입력 결과')
    st.write(f"무선국종: {st.session_state.category}")
    st.write(f"세부장치: {st.session_state.subcategory}")
    st.write(f"출력: {st.session_state.output} W")

    # 주파수 단위 변환
    try:
        frequency_value = int(st.session_state.frequency)
        if frequency_value >= 1_000_000:
            frequency_display = f"{frequency_value / 1_000_000} MHz"
        elif frequency_value >= 1_000:
            frequency_display = f"{frequency_value / 1_000} kHz"
        else:
            frequency_display = f"{frequency_value} Hz"
        st.write(f"주파수: {frequency_display}")
    except ValueError:
        st.error("주파수는 숫자로 입력해야 합니다.")

    # 전파형식 설명 추가, Markdown으로 처리
    description_html = get_waveform_description(st.session_state.waveform)
    st.markdown(f"전파형식: {description_html}", unsafe_allow_html=True)

if st.session_state.show_results:
    st.subheader('계산 결과')

    
    # "접기" 버튼
if st.button("접기"):
        st.session_state.show_results = False
        
        
        
        
st.title('dBm - W 계산기')
# 사용자 입력 받기
dbm_value = st.number_input('dBm 값을 입력하세요:', value=0.0)

# dBm을 W로 변환하는 함수
def dbm_to_watt(dbm):
    return 10 ** (dbm / 10) * 0.001

# 변환 결과 계산
watt_value = dbm_to_watt(dbm_value)

# 결과 출력
st.write(f"{dbm_value} dBm = {watt_value} W")

st.title('W - dBm 계산기')
# 사용자 입력 받기
watt_value = st.number_input('W (와트) 값을 입력하세요:', value=0.0, format="%f")

# W를 dBm으로 변환하는 함수
def watt_to_dbm(watt):
    return 10 * np.log10(watt * 1000)

# 변환 결과 계산
dbm_value = watt_to_dbm(watt_value)

# 결과 출력
st.write(f"{watt_value} W = {dbm_value} dBm")