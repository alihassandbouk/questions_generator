import streamlit as st
from helper_function import Palm_request,Solve_problem

st.title("dataAlgos 🤖🤖")
st.markdown(
    '''
    ### This app generates data stractures and algorithims question

    * **Libraries used:** streamlit, google.generativeai, llamaindix
    * **Inspired by:** Dr Wassim

    ***
'''
)

response = ""
answer = ""
subjects = [
        "linked lists",
        "hashmaps",
        "dynamic programing",
        "stack",
        "heap",
        "two pointers",
        "sliding window",
        ]
subject = st.selectbox("subject",subjects)
levels =["easy","meduim","hard"]
langs = ["python","c++", "java","javascript"]
language = st.selectbox("language",langs,)
difficality = st.select_slider("difficality",levels )


st.markdown("***")


col1, col2 = st.columns(2)

with col1:
    generate = st.button("generate question")
    st.subheader("The question:")
    if generate and difficality and levels:
        response = Palm_request(difficality,subject)
        st.write(response)
with col2:

    solve = st.button("solve")
    if solve and language:
        answer = Solve_problem(response,language)
    st.subheader("Answer:")
    st.write(answer)    





