import streamlit as st
import math

def setup_initial_state():
    if "show_results" not in st.session_state:
        st.session_state.show_results = False

def select_category():
    category = st.selectbox(
        '무선국종선택:',
        ['무선국종을 선택하세요', '41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국'],
        index=0
    )
    return category

def select_subcategory(category):
    options = {
        '41': ['VHF(DSC)', 'MF/HF', 'MF/HF(DSC)', 'D-MF/HF', 'EPIRB', 'AIS', 'TWO-WAY'],
        '42': ['VHF(DSC)', 'MF/HF', 'MF/HF(DSC)', 'D-MF/HF', 'EPIRB', 'AIS', 'TWO-WAY'],
        '44': ['기타', 'TRS'],
        '92': ['기타'],
        '94': ['기타', '마을방송'],
        '': ['먼저 무선국종을 선택하세요']
    }
    selected_category = category.split('.')[0]
    subcategory_options = options.get(selected_category, ['먼저 무선국종을 선택하세요'])
    subcategory = st.selectbox(
        '세부장치:',
        subcategory_options
    )
    return subcategory

def convert_to_hz(value, unit):
    if unit == 'GHz':
        return value * 1e9
    elif unit == 'MHz':
        return value * 1e6
    elif unit == 'kHz':
        return value * 1e3
    elif unit == 'Hz':
        return value
    else:
        return 0
    

def input_output_frequency_waveform():
    output = st.number_input('출력값을 입력하세요:', value=0.0, step=1.0, format="%.1f")

    initial_frequency = st.number_input('센터주파수를 입력하세요:', value=0.0, step=1.0, format="%.1f")

    # 전역 버튼 스타일 설정
    st.markdown("""
    <style>
    .stButton>button {
        min-width: -30px;  # 버튼의 최소 너비를 0으로 설정하여 강제로 한 줄에 유지
        padding: 0.25em 0.5em;  /* 작은 패딩 */
        font-size: 0.75em;      /* 작은 글꼴 크기 */
        width: 100%;            /* 컬럼 너비에 맞춤 */
    }
    </style>
    """, unsafe_allow_html=True)

    # 단위 선택 버튼
    col1, col2, col3, col4 = st.columns(4)
    units = ['GHz', 'MHz', 'kHz', 'Hz']
    for i, unit in zip([col1, col2, col3, col4], units):
        with i:
            if st.button(unit):
                frequency = convert_to_hz(initial_frequency, unit)
                st.session_state.frequency = frequency  # 세션 상태에 저장

    # 세션 상태에 주파수가 저장되었다면, 그 값을 사용
    frequency = st.session_state.get('frequency', initial_frequency)
    frequency_display = format_frequency(frequency)
    st.markdown(f"주파수: <span style='color: red;'>{frequency_display}</span>", unsafe_allow_html=True)

    waveform = st.text_input('전파형식(예:8k5f3e 등)', max_chars=8)

    return output, frequency, waveform






def display_results(category, subcategory, output, frequency, waveform):
    if st.session_state.show_results:
        # Waveform 처리
        extracted_waveform = extract_and_uppercase_waveform(waveform)


def extract_and_uppercase_waveform(waveform):
    waveform_part = waveform[:-3]
    waveform_upper = waveform_part.upper()
    return waveform_upper


            

def show_input_info(category, subcategory, output, frequency, waveform):
    st.markdown("""
    <style>
    .result-header {
        color: red;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    <div class='result-header'>ㅡ입력 정보ㅡ</div>
    """, unsafe_allow_html=True)
    
    st.write(f"무선국종: {category}")
    st.write(f"세부장치: {subcategory}")
    st.write(f"출력: {output} W")
    frequency_display = format_frequency(frequency)
    st.write(f"주파수: {frequency_display}")
    description_html = get_waveform_description(waveform)
    st.markdown(f"전파형식: {description_html}", unsafe_allow_html=True)



def Contrast(category, subcategory, output):
    st.markdown("""
<style>
.centered-success {
    background-color: #28a745;
    color: white;
    padding: 10px;
    border-radius: 5px;
    text-align: center;
}
</style>
<div class="centered-success">✅ 대조 결과 ✅</div>
""", unsafe_allow_html=True)

    # 시설자에 대한 정보
    if category in ['41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 시설자</p>", unsafe_allow_html=True)

    # 설치장소에 대한 정보
    if category in ['41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 설치장소</p>", unsafe_allow_html=True)

    # 기기형식에 대한 정보
    if category in ['41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 기기형식</p>", unsafe_allow_html=True)

    # 전원설비에 대한 정보
    if category in ['41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 전원설비</p>", unsafe_allow_html=True)

    # 안테나에 대한 정보
    if category in ['41.선박국', '42.의무선박국', '44.육상이동국', '92.아마추어국', '94.간이무선국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 안테나</p>", unsafe_allow_html=True)

    # 보호장치에 대한 정보 (10W 초과 시)
    if output > 10:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 보호장치(10W초과)</p>", unsafe_allow_html=True)

    # 예비전원에 대한 정보
    if category in ['41.선박국', '42.의무선박국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 예비전원</p>", unsafe_allow_html=True)

    # 의사안테나 및 비상등에 대한 정보
    if category in ['41.선박국', '42.의무선박국']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 의사안테나및 비상등</p>", unsafe_allow_html=True)

    # 식별부호에 대한 정보
    if subcategory in ['VHF(DSC)', 'EPIRB', 'MF/HF(DSC)']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ 식별부호</p>", unsafe_allow_html=True)

    # DSC위치정보확인에 대한 정보
    if subcategory in ['VHF(DSC)', 'MF/HF(DSC)']:
        st.markdown("<p style='font-size: 20px; font-weight: bold;'>※ DSC위치정보확인</p>", unsafe_allow_html=True)


def Performance(category, subcategory, output, frequency, waveform, extracted_waveform):
    st.markdown("""
<style>
.centered-success {
    background-color: #80C783;
    color: black;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
</style>
<div class="centered-success">✅ 성능 결과 ✅</div>
""", unsafe_allow_html=True)

#############################################출력
    # 아마추어국인 경우 출력 범위 계산 및 표시
    if category == '92.아마추어국':
        calculated_output_range12 = output * 1.2  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: 0W ~ {calculated_output_range12:.1f}W(하한없음 ~ 상한 20%)</p>", unsafe_allow_html=True )
    # 간이,육상
    if category in ['94.간이무선국', '44.육상이동국']:
        calculated_output_range05 = output * 0.5  # 출력 최소 범위 계산
        calculated_output_range12 = output * 1.2  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: {calculated_output_range05:.1f}W ~ {calculated_output_range12:.1f}W(하한 50% ~ 상한 120%)</p>", unsafe_allow_html=True)

    # VHF(DSC), AIS
    if subcategory in ['VHF(DSC)', 'AIS']:
        calculated_output_range05 = output * 0.5  # 출력 최대 범위 계산
        calculated_output_range12 = output * 1.2  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: {calculated_output_range05:.1f}W ~ {calculated_output_range12:.1f}W(하한50% ~ 상한 20%)</p>", unsafe_allow_html=True )

    # Two-Way
    if subcategory == 'TWO-WAY':
        calculated_output_range08 = output * 0.8  # 출력 최대 범위 계산
        calculated_output_range15 = output * 1.5  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: {calculated_output_range08:.1f}W ~ {calculated_output_range15:.1f}W(하한80% ~ 상한 50%)</p>", unsafe_allow_html=True )

    # EPIRB
    if subcategory == 'EPIRB':
        calculated_output_range08 = output * 0.8  # 출력 최대 범위 계산
        calculated_output_range15 = output * 1.5  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: {calculated_output_range08:.1f}W ~ {calculated_output_range15:.1f}W(하한80% ~ 상한 50%) // On-Air측정시 'ㅡ'처리</p>", unsafe_allow_html=True )

    if subcategory in ["MF/HF", "MF/HF(DSC)"] and 1605000 < frequency <= 3900000:
        calculated_output_range08 = output * 0.8  # 출력 최대 범위 계산
        calculated_output_range11 = output * 1.1  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: {calculated_output_range08:.1f}W ~ {calculated_output_range11:.1f}W(하한80% ~ 상한 10%)</p>", unsafe_allow_html=True )

    if subcategory in ["MF/HF", "MF/HF(DSC)"] and 4000000 < frequency <= 28500000:
        calculated_output_range05 = output * 0.5  # 출력 최대 범위 계산
        calculated_output_range12 = output * 1.2  # 출력 최대 범위 계산
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>안테나 공급전력: {calculated_output_range05:.1f}W ~ {calculated_output_range12:.1f}W(하한50% ~ 상한 20%)</p>", unsafe_allow_html=True )


#############################################대역폭
    if st.session_state.show_results:
        # Waveform 값이 비어있지 않은 경우에만 처리
        if waveform.strip():  # .strip()을 사용하여 공백만 있는 입력도 걸러냄
            extracted_waveform = extract_and_uppercase_waveform(waveform)
            # 대역폭 표시
            st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>대역폭 : {extracted_waveform}</p>", unsafe_allow_html=True)
        else:
            # Waveform 값이 비어있으면 메시지 표시
            st.markdown("<p style='font-size: 20px; font-weight: bold; color: red;'>전파형식을 입력해주세요.</p>", unsafe_allow_html=True)

#############################################주파수편차
    # EPIRB
    if subcategory == 'EPIRB':
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>주파수편차: 기준 X 측정값 입력", unsafe_allow_html=True )

    if category == "92.아마추어국" and 100000000 < frequency <= 470000000 and output > 1:
        st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>주파수편차: 1000Hz</p>", unsafe_allow_html=True)
    else:
        st.write(f"현재 주파수: {frequency} Hz, 현재 출력: {output} W (조건 불만족)")



def format_frequency(frequency):
    try:
        frequency_value = int(frequency)
        if frequency_value >= 1_000_000_000:
            return f"{frequency_value / 1_000_000_000} GHz"
        elif frequency_value >= 1_000_000:
            return f"{frequency_value / 1_000_000} MHz"
        elif frequency_value >= 1_000:
            return f"{frequency_value / 1_000} kHz"
        else:
            return f"{frequency_value} Hz"
    except ValueError:
        return "주파수는 숫자로 입력해야 합니다"
def get_waveform_description(waveform):
    waveform = waveform.upper()[-3:]
    descriptions = {
        'first': {
            'N': "무변조파", 'A': "양측파대", 'H': "단측파대의 전반송파",
            'R': "단측파대의 저감 또는 가변레벨 반송파", 'J': "단측파대의 억압반송파",
            'B': "독립측파대", 'C': "잔류측파대", 'F': "주파수변조(각)",
            'G': "위상변조(각)", 'D': "동시 또는 순서에 따라 진폭과 각변조",
            'P': "무변조 연속펄스", 'K': "진폭변조", 'L': "폭(기간)변조",
            'M': "위치(위상)변조", 'Q': "펄스기간 중 각변조",
            'V': "변조 조합 또는 다른 방법", 'W': "규정된 것 외의 조합변조",
            'X': "규정된 것 외의 변조"
        },
        'second': {
            '0': "무변조", '1': "부반송파를 사용하지 않는 디지털 1개 채널",
            '2': "부반송파를 사용하는 디지털 1개 채널", '3': "아날로그 1개 채널",
            '7': "디지털 2개 채널", '8': "아날로그 2개 채널",
            '9': "아날로그+디지털", 'X': "규정된 것 외의 형태"
        },
        'third': {
            'N': "정보송출 없음", 'A': "전신: 가청수신용", 'B': "전신: 자동수신용",
            'C': "팩시밀리", 'D': "데이터, 비가청", 'E': "전화",
            'F': "텔레비전(비디오)", 'W': "2개 이상의 조합", 'X': "규정된 것 외의 형태"
        }
    }
    if len(waveform) != 3:
        return "잘못된 전파형식"
    
    firstDescription = descriptions['first'].get(waveform[0], "알 수 없음")
    secondDescription = descriptions['second'].get(waveform[1], "알 수 없음")
    thirdDescription = descriptions['third'].get(waveform[2], "알 수 없음")
    
    return f'<span style="color: red;">{firstDescription}</span>, <span style="color: green;">{secondDescription}</span>, <span style="color: blue;">{thirdDescription}</span>'

def calculate_button():
    if st.button('결과 열기', key='open'):
        st.session_state.show_results = True
###############결과 화면
def display_results(category, subcategory, output, frequency, waveform):
    if st.session_state.show_results:
        # Waveform 처리
        extracted_waveform = extract_and_uppercase_waveform(waveform)
        
        # 입력 정보와 추가 정보 표시
        show_input_info(category, subcategory, output, frequency, waveform)
        Contrast(category, subcategory, output)
        
        # 성능 결과 표시, 이제 extracted_waveform을 정확히 전달
        Performance(category, subcategory, output, frequency, waveform, extracted_waveform)
 
        # 접기 버튼
        if st.button("접기", key='close'):
            st.session_state.show_results = False


def main():

    
    st.title('일반무선국 기술기준 Helper')
    setup_initial_state()
    category = select_category()
    subcategory = select_subcategory(category)
    output, frequency, waveform = input_output_frequency_waveform()

    calculate_button()
    display_results(category, subcategory, output, frequency, waveform)

    st.title('dBm - W 계산기')
    dbm_value = st.number_input('dBm 값을 입력하세요:', value=0)
    watt_value = dbm_to_watt(dbm_value)
    st.write(f"{dbm_value} dBm = {watt_value} W")

    st.title('W - dBm 계산기')
    watt_value = st.number_input('W (와트) 값을 입력하세요:', value=0.0, format="%f")
    dbm_value = watt_to_dbm(watt_value)
    st.write(f"{watt_value} W = {dbm_value} dBm")

def dbm_to_watt(dbm):
    return 10 ** (dbm / 10) * 0.001

def watt_to_dbm(watt):
    if watt > 0:
        return 10 * math.log10(watt * 1000)
    else:
        return '0'



if __name__ == "__main__":
    main()
