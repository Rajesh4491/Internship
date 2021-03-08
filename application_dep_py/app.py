import streamlit as st
import pickle
from PIL import Image

st.markdown('<style>body{background-color: lightgreen;}</style>',unsafe_allow_html=True)

pickle_in = open('pickle/rbf_pickle.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
def prediction(col1,col2):
    if col1=='Yes':
        col1 = 1
    else:
        col1 = 0
    if col2=='Yes':
        col2 =1
    else:
        col2 =0

    prediction=classifier.predict([[col1,col2]])
    if prediction==1:
        pred='YES'
    elif prediction==0:
        pred='NO'
    else:
        pred=None
    return pred
def main():
    st.markdown("<h1 style='text-align: center; color: black;'>SVM WITH KERNEL RBF</h1>", unsafe_allow_html=True)

    st.subheader('col1')
    col1=st.number_input('Enter The Number In Col1')

    st.subheader('col2')
    col2=st.number_input('Enter The Number In Col2')

    if st.button('Now Predict'):
        predict=prediction(col1,col2)
        st.success(predict)

if __name__=='__main__':
    main()
