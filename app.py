import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍽️")

st.title("🍽️ 오늘의 점심 메뉴 추천기")
st.write("결정하기 어려운 점심 메뉴, 버튼 한 번으로 정해보세요!")

# 추천할 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", "떡볶이",
    "마라탕", "햄버거", "초밥", "파스타", "쌀국수",
    "비빔밥", "칼국수", "순대국밥", "샌드위치", "짜장면",
    "짬뽕", "치킨마요덮밥", "부대찌개"
]

# 버튼을 눌렀을 때 실행되는 동작
if st.button("🎲 메뉴 추천받기", use_container_width=True):
    chosen_menu = random.choice(lunch_menus)
    st.balloons()  # 화면에 축하 풍선 효과 표시
    st.success(f"오늘의 추천 점심 메뉴는 **{chosen_menu}**입니다! 맛있게 드세요! 😋")
