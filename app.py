import streamlit as st
import random

# 공부 시간 생성
def random_study_time():
    # 0시간(0분) ~ 10시간(600분)까지 30분 단위 -> 총 21개(option)
    time_options = [30 * i for i in range(0, 21)]
    minutes = random.choice(time_options)
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}시간 {mins}분"

# 과목 리스트 생성
def random_subject_list():
    subjects = ["국어", "영어", "수학", "사회", "과학"]
    result = []

    # 각 과목은 최대 2번만 포함 가능
    counts = {subj: 0 for subj in subjects}

    # 총 5개 선택
    for _ in range(5):
        available = [s for s in subjects if counts[s] < 2]
        choice = random.choice(available)
        result.append(choice)
        counts[choice] += 1

    return result

# Streamlit UI
st.title("📘 랜덤 공부 생성기")
st.write("공부 시간과 과목 리스트를 랜덤으로 만들어주는 간단한 앱입니다!")

if st.button("생성하기"):
    time_result = random_study_time()
    subjects_result = random_subject_list()

    st.subheader("⏰ 랜덤 공부 시간")
    st.success(time_result)

    st.subheader("📚 랜덤 과목 리스트 (5개)")
    st.info(", ".join(subjects_result))
