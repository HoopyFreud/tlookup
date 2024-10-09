import lib as tll
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

tll.appSetupKeys()   
tll.appUpdateCookies()

with st.sidebar:
    st.button('Reset Cards', key="reset_cards", on_click=tll.resetCards, use_container_width=True)
    st.radio('Numeral type', tll.numeralTypeList, key="numeral_type", on_change=tll.updateCookie, args=["numeral_type"], format_func=tll.displayNumeralType)
    st.checkbox('Show message text', key="show_line_message", on_change=tll.updateCookie, args=["show_line_message"])
    st.checkbox('Show inverse text', key="show_line_inverse", on_change=tll.updateCookie, args=["show_line_inverse"])
    st.checkbox('Show card preview', key="show_card_preview", on_change=tll.updateCookie, args=["show_card_preview"])
    st.button('Default Settings', key="reset_settings", on_click=tll.resetSettings, use_container_width=True)

if st.session_state.new_card and st.session_state.show_card_preview:
    with st.container(border=True):
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.selectbox('New card', tll.cardTable, key="new_card", index=None, format_func=tll.getCardName, label_visibility="collapsed", placeholder="Select a card")
        with col3:
            pass 
        with st.container(key="card_preview_title"):
            st.write(tll.getCardTitle(st.session_state.new_card),unsafe_allow_html=True)
        tll.writeCard(st.session_state.new_card)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Add card', key="new_card_button", on_click=tll.addCard, use_container_width=True)
        with col3:
            pass
else:
    col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
    with col1:
        pass
    with col2:
        st.selectbox('New card', tll.cardTable, key="new_card", index=None, format_func=tll.getCardName, label_visibility="collapsed", placeholder="Select a card")
        st.button('Add card', key="new_card_button", on_click=tll.addCard, use_container_width=True)
    with col3:
        pass
        
for ID, card in enumerate(st.session_state.card_set):
    with st.expander(tll.getCardTitle(card), expanded = True):
        tll.writeCard(card)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Remove card', key="del_card_ID_"+str(ID)+"_button", on_click=tll.removeCard, args=[ID], use_container_width=True)
        with col3:
            pass