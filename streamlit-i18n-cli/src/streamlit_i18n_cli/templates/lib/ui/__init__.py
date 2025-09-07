import streamlit as st
from lib.i18n import i18n

def add_i18n_to_sidebar():
    if "languages" not in st.session_state:
        languages = i18n.languages()
        st.session_state["languages"] = languages
        st.session_state["nrof_languages"] = len(languages)

    # -------------------------------------------------------------------------------------------------
    languages = st.session_state["languages"]
    nrof_languages = st.session_state["nrof_languages"]

    # -------------------------------------------------------------------------------------------------
    with st.sidebar:
        if nrof_languages == 0:
            st.warning(f"No languages found in package '{i18n._package}' with template '{i18n._tmpl}'.")
        elif nrof_languages < 5:
            lang = st.segmented_control("Language", languages, selection_mode="single", key="lang_select")
        else:
            lang = st.selectbox("Current language", options=languages, index=0)
        
    # -------------------------------------------------------------------------------------------------
    if lang:
        i18n.set_lang(lang)

    return lang