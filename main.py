import streamlit as st
from quiz import quiz

# Page settings
st.set_page_config(
    page_title="Quiz Game",
    page_icon="iconquiz.ico",
    layout="centered"
)

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None


# Function to check answer
def check_answer(choice):
    question = quiz[st.session_state.current_question]

    st.session_state.selected_answer = choice
    st.session_state.answered = True

    if choice == question["answer"]:
        st.session_state.score += 1


# Function to move to next question
def next_question():
    st.session_state.current_question += 1
    st.session_state.answered = False
    st.session_state.selected_answer = None


# Custom CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0A0A0A;
    }

    h1, h2, h3, p, div, label {
        font-family: "Courier New", monospace;
    }

    .question {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: white;
        padding: 20px;
    }

    .score {
        text-align: right;
        font-family: "Courier New", monospace;
        font-size: 20px;
        font-weight: bold;
        color: white;
    }

    .correct {
        background-color: #5EE651;
        color: black;
        padding: 10px;
        text-align: center;
        font-weight: bold;
    }

    .wrong {
        background-color: #C75B52;
        color: black;
        padding: 10px;
        text-align: center;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# Check if quiz is finished
if st.session_state.current_question >= len(quiz):

    st.title("Quiz Completed!")

    st.success(
        f"You have completed the quiz!\n\n"
        f"Your final score is: "
        f"{st.session_state.score}/{len(quiz)}"
    )

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_answer = None
        st.rerun()

else:

    # Get current question
    question = quiz[st.session_state.current_question]

    # Display score
    st.markdown(
        f'<div class="score">'
        f'{st.session_state.score}/{len(quiz)}'
        f'</div>',
        unsafe_allow_html=True
    )

    # Display question
    st.markdown(
        f'<div class="question">'
        f'{question["question"]}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # Display choices
    for choice in question["choices"]:

        # Disable buttons after an answer has been selected
        disabled = st.session_state.answered

        if st.button(
            choice,
            key=f"choice_{st.session_state.current_question}_{choice}",
            disabled=disabled,
            use_container_width=True
        ):
            check_answer(choice)
            st.rerun()

    # Feedback
    if st.session_state.answered:

        if st.session_state.selected_answer == question["answer"]:
            st.markdown(
                '<div class="correct">Correct!</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="wrong">Eh! Wrong!</div>',
                unsafe_allow_html=True
            )

        st.write("")

        # Next button
        if st.button("Next", use_container_width=True):
            next_question()
            st.rerun()

