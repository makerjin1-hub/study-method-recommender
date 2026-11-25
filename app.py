
import streamlit as st

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="공부 레벨 UP!",
    page_icon="🎮"
)

# 2. 화면 제목
st.title("🎮 공부 레벨 UP!")
st.subheader("나에게 맞는 공부 방법을 찾아보자!")
st.write("과목을 선택하고 공부 미션에 도전해 보세요!")

# 3. 과목별 공부 방법 리스트
korean = [
    "교과서를 소리 내어 읽기",
    "핵심 내용을 노트에 정리하기",
    "틀린 문제 다시 풀어보기"
]

english = [
    "영어 단어 10개 외우기",
    "영어 문장을 소리 내어 읽기",
    "영어 듣기 연습하기"
]

math = [
    "수학 개념 이해하기",
    "유형별 문제 풀기",
    "오답 노트 작성하기"
]

science = [
    "과학 핵심 개념 정리하기",
    "실험 과정 이해하기",
    "단원별 퀴즈 풀기"
]

# 4. 공부 방법 추천 함수
def recommend_study(subject):

    if subject == "국어":
        return korean

    elif subject == "영어":
        return english

    elif subject == "수학":
        return math

    else:
        return science


# 5. 점수와 완료 미션 저장
if "score" not in st.session_state:
    st.session_state.score = 0

if "completed" not in st.session_state:
    st.session_state.completed = []

# 6. 과목 선택
subject = st.selectbox(
    "📚 공부할 과목을 선택하세요!",
    ["국어", "영어", "수학", "과학"]
)

# 7. 추천 결과 출력
methods = recommend_study(subject)

st.success(subject + " 추천 공부 방법입니다!")

st.metric("추천 공부 방법 개수", len(methods))

# 8. 반복문으로 공부 방법 출력
for i, method in enumerate(methods):

    st.write("📌 " + method)

    mission_id = subject + str(i)

    if mission_id in st.session_state.completed:

        st.success("미션 완료! ⭐")

    else:

        if st.button("미션 완료하기 (+10점)", key=mission_id):

            st.session_state.completed.append(mission_id)
            st.session_state.score += 10

            st.rerun()

# 9. 점수와 레벨 출력
st.divider()

st.metric("⭐ 나의 총 점수", st.session_state.score)

st.metric(
    "완료한 미션",
    len(st.session_state.completed)
)

if st.session_state.score >= 120:

    st.balloons()
    st.success("🏆 축하합니다! 전 과목 공부왕!")

elif st.session_state.score >= 60:

    st.success("🥇 공부 고수 레벨!")

elif st.session_state.score >= 30:

    st.info("🥈 공부 중수 레벨!")

else:

    st.info("🌱 공부 새싹 레벨!")

# 10. 게임 초기화
if st.button("🔄 처음부터 다시 하기"):

    st.session_state.score = 0
    st.session_state.completed = []

    st.rerun()
