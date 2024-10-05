import st_function_lib as stl
import streamlit as st

stl.appSetupKeys()    
#st.write(st.session_state)

col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
with col1:
    pass
with col2:
    st.selectbox('New card', stl.cardTable, key="new_card", format_func=stl.getCardName, label_visibility="collapsed", placeholder="Select a card")
    st.button('Add card', key="new_card_button", on_click=stl.addCard, use_container_width=True)
with col3:
    pass
        
for ID, card in enumerate(st.session_state.card_set):
    with st.expander(stl.getCardTitle(card), expanded = True):
        for line in card["Short"]:
            st.write(line)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Remove card', key="del_card_ID_"+str(ID)+"_button", on_click=stl.removeCard, args=[ID], use_container_width=True)
        with col3:
            pass