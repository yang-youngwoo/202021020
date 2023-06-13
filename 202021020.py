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


# 전달함수 그래프
st.header("unit step입력 응답곡선")

if st.button("코드 보기1"):
    code = '''
    # 시간 t 변수 정의
    t = sp.symbols('t', positive=True)

    # 폐루프 전달함수 H(s) 정의
    s = sp.symbols('s')
    H = 100 / ((s+2)*(s+3) + 100)

    # 라플라스 역변환을 통한 시간 영역의 전달함수 계산
    h = sp.inverse_laplace_transform(H, s, t)

    # 시간 t 범위 설정
    t_vals = np.linspace(0, 10, 100)

    # 응답곡선 계산
    h_vals = [sp.N(h.subs(t, val)) for val in t_vals]

    # Matplotlib 백엔드 설정
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.switch_backend('Agg')

    # 응답곡선 그래프 표시
    fig = plt.figure()
    plt.plot(t_vals, h_vals)
    plt.xlabel('Time')
    plt.ylabel('Response')
    plt.title('Step Response')
    plt.grid(True)

    # 그래프 표시
    st.pyplot(fig)
    '''
    st.code(code, language="python")

fig1, ax1 = plt.subplots()
t, y, _ = signal.lsim(s1, np.ones_like(t), t)
ax1.plot(t, y)
ax1.set_xlabel('Time')
ax1.set_ylabel('Output')
st.pyplot(fig1)

# Bode Plot
st.header("주파수 응답 보드선")

if st.button("코드 보기2"):
    code2 = '''
# 주파수 범위 설정
frequencies = np.logspace(-2, 2, num=1000)

# 폐루프 전달함수 H(s)의 분자와 분모 계수 설정
numerator = [100]
denominator = [1, 5, 106, 100]

# 주파수 응답 계산
_, magnitude, phase = signal.bode((numerator, denominator), frequencies)

# Matplotlib 백엔드 설정
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.switch_backend('Agg')

# 그래프 그리기
fig_magnitude = plt.figure()
plt.semilogx(frequencies, magnitude)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Magnitude [dB]')
plt.title('Bode Plot - Magnitude')
plt.grid(True)

fig_phase = plt.figure()
plt.semilogx(frequencies, phase)
plt.xlabel('Frequency [rad/s]')
plt.ylabel('Phase [degrees]')
plt.title('Bode Plot - Phase')
plt.grid(True)

# 그래프 표시
st.pyplot(fig_magnitude)
st.pyplot(fig_phase)
    '''
    st.code(code2, language="python")

fig2, (ax2_mag, ax2_phase) = plt.subplots(2, 1)
ax2_mag.semilogx(w, mag)
ax2_mag.set_ylabel('Magnitude [dB]')
ax2_mag.set_title('Bode plot of G(s) = 100 / (s^2 + 5s + 106)')
ax2_phase.semilogx(w, phase)
ax2_phase.set_xlabel('Frequency [rad/s]')
ax2_phase.set_ylabel('Phase [degrees]')
st.pyplot(fig2)
