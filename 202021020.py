import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 애플리케이션 제목
st.title('제어공학 202021020 양영우')
st.header('폐루프 전달함수 L(S)')
st.write('L(s) = 100/(s^2 + 5s + 106)')

# 전달함수 정의
s1 = signal.lti([100], [1, 5, 106])

# 주파수 범위 설정
frequencies = np.logspace(-2, 2, 500)

# 전달함수 그래프 계산
t, y = signal.step(s1)

# 주파수 응답 계산
w, mag, phase = s1.bode(frequencies)


# unit step입력 응답곡선 그래프
st.header("unit step입력 응답곡선")

if st.button("코드 보기1"):
    code = '''
    # 전달함수 정의
s1 = signal.lti([100], [1, 5, 106])

# 주파수 범위 설정
frequencies = np.logspace(-2, 2, 500)

# 전달함수 그래프 계산
t, y = signal.step(s1)

# 주파수 응답 계산
w, mag, phase = s1.bode(frequencies)

#그래프 
fig1, ax1 = plt.subplots()
t, y, _ = signal.lsim(s1, np.ones_like(t), t)
ax1.plot(t, y)
ax1.set_xlabel('Time')
ax1.set_ylabel('Output')
st.pyplot(fig1)
    '''
    st.code(code, language="python")

#그래프 
fig1, ax1 = plt.subplots()
t, y, _ = signal.lsim(s1, np.ones_like(t), t)
ax1.plot(t, y)
ax1.set_xlabel('Time')
ax1.set_ylabel('Output')
st.pyplot(fig1)

# 주파수 응답 보드선도 그래프
st.header("주파수 응답 보드선도")

if st.button("코드 보기2"):
    code2 = '''
# 전달함수 정의
s1 = signal.lti([100], [1, 5, 106])

# 주파수 범위 설정
frequencies = np.logspace(-2, 2, 500)

# 전달함수 그래프 계산
t, y = signal.step(s1)

# 주파수 응답 계산
w, mag, phase = s1.bode(frequencies)

#그래프 그리기
fig2, (ax2_mag, ax2_phase) = plt.subplots(2, 1)
ax2_mag.semilogx(w, mag)
ax2_mag.set_xlabel('Frequency [rad/s]')
ax2_mag.set_ylabel('Magnitude [dB]')
ax2_phase.semilogx(w, phase)
ax2_phase.set_xlabel('Frequency [rad/s]')
ax2_phase.set_ylabel('Phase [degrees]')
plt.subplots_adjust(hspace=0.3)
st.pyplot(fig2)
    '''
    st.code(code2, language="python")

#그래프 그리기
fig2, (ax2_mag, ax2_phase) = plt.subplots(2, 1)
ax2_mag.semilogx(w, mag)
ax2_mag.set_xlabel('Frequency [rad/s]')
ax2_mag.set_ylabel('Magnitude [dB]')
ax2_phase.semilogx(w, phase)
ax2_phase.set_xlabel('Frequency [rad/s]')
ax2_phase.set_ylabel('Phase [degrees]')

plt.subplots_adjust(hspace=0.3)

st.pyplot(fig2)
