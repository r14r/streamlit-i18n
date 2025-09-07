import streamlit as st

# -------------------------------------------------------------------------------------------------
from lib.i18n import i18n
from lib.ui import add_i18n_to_sidebar

st.set_page_config(page_title="i18n Suite", page_icon="🌍", layout="wide")

lang = add_i18n_to_sidebar()

# -------------------------------------------------------------------------------------------------
st.title("🌍 " + i18n.APP.TITLE)

col1, col2 = st.columns(2)
with col1:
    st.write("**i18n.APP.TITLE**")
    st.write("**i18n.APP.DESC**")
    st.write("**i18n.t('app.desc')**")
with col2:
    st.write(i18n.APP.TITLE)
    st.write(i18n.APP.DESC)
    st.write(i18n.t("app.desc"))





col1, col2 = st.columns(2)
with col1:
    st.write("**i18n.PAGES.PAGE1.TITLE**")
    st.write("**getattr(i18n.PAGES.PAGE1, 'DESC', '(no desc)')**")

    st.write("**i18n.PAGES.PAGE2.TITLE**")
    st.write("**getattr(i18n.PAGES.PAGE2, 'DESC', '(no desc)')**")

with col2:
    st.write(i18n.PAGES.PAGE1.TITLE)
    st.write(getattr(i18n.PAGES.PAGE1, "DESC", "(no desc)"))

    st.write(i18n.PAGES.PAGE2.TITLE)
    st.write(getattr(i18n.PAGES.PAGE2, "DESC", "(no desc)"))
    


st.subheader("Quick preview")
key = st.text_input("Dotted key", "app.title")
st.write(f"key: {key} --> {i18n.t(key)}")    