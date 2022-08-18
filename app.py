import streamlit as st

with st.sidebar:
    st.header("This is my sidebar")
    my_input = st.text_input(label="Enter the language you want", value="")
    st.multiselect(
        label="Python version",
        options=["Python 2.7", "Python 3.6", "Python 3.7", "Python 3.8"]
    )


st.header("Hello world")

st.text(my_input)

button_dispaly = st.button('Display Python')

if button_dispaly:
    st.code("""a = 5
    b = 6
    print(a+b)
    """, language="python")

st.text("Json file")

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })