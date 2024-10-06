import st_function_lib as stl
import streamlit as st

st.markdown(
"""
<style>
    summary * {justify-content:center;font-size:16px !important}
    .st-key-card_preview_title * {display:flex;justify-content:center}
</style>
""",
unsafe_allow_html=True,
)

stl.appSetupKeys()   
stl.appUpdateCookies()

with st.sidebar:
    st.radio('Numeral type', stl.numeralTypeList, key="numeral_type", on_change=stl.updateCookie, args=["numeral_type"], format_func=stl.displayNumeralType)
    st.checkbox('Show message text', key="show_line_message", on_change=stl.updateCookie, args=["show_line_message"])
    st.checkbox('Show inverse text', key="show_line_inverse", on_change=stl.updateCookie, args=["show_line_inverse"])
    st.checkbox('Show card preview', key="show_card_preview", on_change=stl.updateCookie, args=["show_card_preview"])
    st.button('Reset Cards', key="reset_cards", on_click=stl.resetCards, use_container_width=True)
    st.button('Default Settings', key="reset_settings", on_click=stl.resetSettings, use_container_width=True)

if st.session_state.new_card and st.session_state.show_card_preview:
    with st.container(border=True):
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.selectbox('New card', stl.cardTable, key="new_card", index=None, format_func=stl.getCardName, label_visibility="collapsed", placeholder="Select a card")
        with col3:
            pass 
        with st.container(key="card_preview_title"):
            st.write(stl.getCardTitle(st.session_state.new_card),unsafe_allow_html=True)
        stl.writeCard(st.session_state.new_card)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Add card', key="new_card_button", on_click=stl.addCard, use_container_width=True)
        with col3:
            pass
else:
    col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
    with col1:
        pass
    with col2:
        st.selectbox('New card', stl.cardTable, key="new_card", index=None, format_func=stl.getCardName, label_visibility="collapsed", placeholder="Select a card")
        st.button('Add card', key="new_card_button", on_click=stl.addCard, use_container_width=True)
    with col3:
        pass
        
for ID, card in enumerate(st.session_state.card_set):
    with st.expander(stl.getCardTitle(card), expanded = True):
        stl.writeCard(card)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Remove card', key="del_card_ID_"+str(ID)+"_button", on_click=stl.removeCard, args=[ID], use_container_width=True)
        with col3:
            pass