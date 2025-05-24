import streamlit as st

st.title("ATP 생성량 계산기 🔋")

기준 = st.selectbox(
    "기준을 선택하세요",
    ["포도당 1분자", "해당과정 1회", "피루브산 산화 1회", "TCA 회로 1회", "NADH 1개", "FADH₂ 1개"]
)

if 기준 == "포도당 1분자":
    atp = 2 + 2 * 2.5 + 2 * (1 * 2.5 + 1 * 10)  # 해당 + 산화 + TCA×2
elif 기준 == "해당과정 1회":
    atp = 2 + 2 * 2.5
elif 기준 == "피루브산 산화 1회":
    atp = 1 * 2.5
elif 기준 == "TCA 회로 1회":
    atp = 3 * 2.5 + 1 * 1.5 + 1
elif 기준 == "NADH 1개":
    atp = 2.5
elif 기준 == "FADH₂ 1개":
    atp = 1.5

st.write(f"예상 생성 ATP: **{atp:.1f} ATP**")
