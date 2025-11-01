import streamlit as st

st.subheader("GC COUNT")
SEQ=st.text_area(f"Enter a DNA or RNA sequence: ")
st.write (f"The entered sequence is: {SEQ}")
length=len(SEQ)
st.write (f"the length of the given sequence is: {length}")
G=SEQ.count("G")
C=SEQ.count("C")
GC=G+C
perGC=(GC/length)*100
st.write (f"The percentage of 'GC' in the sequence is: {perGC}")

