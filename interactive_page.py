from st_setup import appSetupKeys
import st_state_change_lib as stc
import st_function_lib as stl
import st_render_char_lib as strc
import build_char as bc
import streamlit as st
import copy

appSetupKeys()    
#st.write(st.session_state)

col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
with col1:
    pass
with col2:
    st.button('New Character', key = "new_character", on_click = stc.charReset, use_container_width=True)
with col3:
    pass
        


#ROW 1 - CLASS
if st.session_state.stage >= 1:
    st.header("Class")
    if not st.session_state.select_disable_class:
        dropdownList = stl.fieldTableDB["ClassTable"]
        col1, col2, col3 = st.columns([10,2,2],vertical_alignment="bottom")
        with col1:
            st.radio('Class', dropdownList, horizontal=True, key="t_char_class", label_visibility="collapsed", index=None, disabled=st.session_state.select_disable_class)
        with col2:
            st.button('Random', key = "class_random", on_click = stl.randomSelector, args=["t_char_class",dropdownList], disabled=st.session_state.select_disable_class)
        with col3:
            st.button('Finalize', key = "class_finalize", on_click = stc.finalizeClass, disabled=st.session_state.select_disable_class)
        if st.session_state.err_text_class:
            st.error(stl.errTextDB["err_text_class"])
    else:
        with st.container(border=True):
            st.write(st.session_state.PC.pc_class)
        
#ROW 2 - STATS
if st.session_state.stage >= 2:
    st.header("Stats")
    statList = stl.fieldTableDB["StatTable"]
    if not st.session_state.select_disable_stat:
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1,1],vertical_alignment="bottom")
        with col1:
            st.write(statList[0]+":")
            rollString = stl.statifyString(st.session_state.class_table["AgilityRoll"])
            st.text_input(statList[0]+":", key = "t_char_agi", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=["t_char_agi","err_text_stat"], kwargs={"roll": rollString}, disabled=st.session_state.select_disable_stat)
        with col2:
            st.write(statList[1]+":")
            rollString = stl.statifyString(st.session_state.class_table["KnowledgeRoll"])
            st.text_input(statList[1]+":", key = "t_char_knw", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=["t_char_knw","err_text_stat"], kwargs={"roll": rollString}, disabled=st.session_state.select_disable_stat)
        with col3:
            st.write(statList[2]+":")
            rollString = stl.statifyString(st.session_state.class_table["PresenceRoll"])
            st.text_input(statList[2]+":", key = "t_char_pre", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=["t_char_pre","err_text_stat"], kwargs={"roll": rollString}, disabled=st.session_state.select_disable_stat)
        with col4:
            st.write(statList[3]+":")
            rollString = stl.statifyString(st.session_state.class_table["StrengthRoll"])
            st.text_input(statList[3]+":", key = "t_char_str", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=["t_char_str","err_text_stat"], kwargs={"roll": rollString}, disabled=st.session_state.select_disable_stat)
        with col5:
            st.write(statList[4]+":")
            rollString = stl.statifyString(st.session_state.class_table["ToughnessRoll"])
            st.text_input(statList[4]+":", key = "t_char_tou", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=["t_char_tou","err_text_stat"], kwargs={"roll": rollString}, disabled=st.session_state.select_disable_stat)
        with col6:
            st.button('Random', key = "stat_random", on_click = stl.randomStats, disabled=st.session_state.select_disable_stat)
        with col7:
            st.button('Finalize', key = "stat_finalize", on_click = stc.finalizeStats, disabled=st.session_state.select_disable_stat)
        if st.session_state.err_text_stat:
            st.error(stl.errTextDB["err_text_stat"])
    else:
        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1],vertical_alignment="bottom")
        with col1:
            st.write(statList[0]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_agi)
        with col2:
            st.write(statList[1]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_knw)
        with col3:
            st.write(statList[2]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_pre)
        with col4:
            st.write(statList[3]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_str)
        with col5:
            st.write(statList[4]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_tou)
        
if st.session_state.stage >= 3:
#ROW 3 - SECONDARY STATS
    st.header("Derived Stats")
    secondaryStatList = stl.fieldTableDB["SecondaryStatTable"]
    if not st.session_state.select_disable_secondary_stat:
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,1,1,1,1],vertical_alignment="bottom")
        with col1:
            st.write(secondaryStatList[0]+":")
            rollString = stl.statifyString(st.session_state.class_table["HPRoll"])
            st.text_input(secondaryStatList[0]+":", key = "t_char_hpmax", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=("t_char_hpmax","err_text_secondary_stat"), kwargs={"roll": rollString}, disabled=st.session_state.select_disable_secondary_stat)
        with col2:
            st.write(secondaryStatList[1]+":")
            rollString = stl.statifyString(st.session_state.class_table["GlitchRoll"])
            st.text_input(secondaryStatList[1]+":", key = "t_char_glitch", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=("t_char_glitch","err_text_secondary_stat"), kwargs={"roll": rollString}, disabled=st.session_state.select_disable_secondary_stat)
        with col3:
            st.write(secondaryStatList[2]+":")
            with st.container(border=True):
                st.write(stl.statifyString(st.session_state.class_table["CarryingCapacityRoll"]))
        with col4:
            st.write(secondaryStatList[3]+":")
            rollString = stl.statifyString(st.session_state.class_table["CreditsRoll"])
            st.text_input(secondaryStatList[3]+":", key = "t_char_creds", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=("t_char_creds","err_text_secondary_stat"), kwargs={"roll": rollString}, disabled=st.session_state.select_disable_secondary_stat)
        with col5:
            st.write(secondaryStatList[4]+":")
            rollString = stl.statifyString(st.session_state.class_table["DebtRoll"])
            st.text_input(secondaryStatList[4]+":", key = "t_char_debt", placeholder=rollString, label_visibility="collapsed", on_change=stl.changeNumInput, args=("t_char_debt","err_text_secondary_stat"), kwargs={"roll": rollString}, disabled=st.session_state.select_disable_secondary_stat)
        with col6:
            st.button('Random', key = "sec_stat_random", on_click = stl.randomSecondaryStats, disabled=st.session_state.select_disable_secondary_stat)
        with col7:
            st.button('Finalize', key = "sec_stat_finalize", on_click = stc.finalizeSecondaryStats, disabled=st.session_state.select_disable_secondary_stat)
        if st.session_state.err_text_secondary_stat:
            st.error(stl.errTextDB["err_text_secondary_stat"])
    else:
        col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1],vertical_alignment="bottom")
        with col1:
            st.write(secondaryStatList[0]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_hp_max)
        with col2:
            st.write(secondaryStatList[1]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_glitch_current)
        with col3:
            st.write(secondaryStatList[2]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_carrying_max)
        with col4:
            st.write(secondaryStatList[3]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_creds)
        with col5:
            st.write(secondaryStatList[4]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_debt)
            
#ROW 4 - DESCRIPTION
if st.session_state.stage >= 4:
    st.header("Description")
    descFieldList = stl.fieldTableDB["DescTable"]
    if not st.session_state.select_disable_desc:
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            st.write(descFieldList[0]+":")
            st.text_input(descFieldList[0]+":", key = "t_char_name", label_visibility="collapsed", on_change=stl.resetErrField, args=("err_text_desc"), disabled=st.session_state.select_disable_desc)
        with col2:
            st.write(descFieldList[1]+":")
            st.text_input(descFieldList[1]+":", key = "t_char_feature", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        with col3:
            st.write(descFieldList[2]+":")
            st.text_input(descFieldList[2]+":", key = "t_char_quirk", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            st.write(descFieldList[3]+":")
            st.text_input(descFieldList[3]+":", key = "t_char_style", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        with col2:
            st.write(descFieldList[4]+":")
            st.text_input(descFieldList[4]+":", key = "t_char_obsession", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        with col3:
            st.write(descFieldList[5]+":")
            st.text_input(descFieldList[5]+":", key = "t_char_desire", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        st.write(descFieldList[6]+":")
        st.text_input(descFieldList[6]+":", key = "t_char_lender", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        if "RandomClassLore" in st.session_state.class_table.keys():
            st.write(st.session_state.class_table["RandomClassLorePrompt"]+":")
            st.text_area(st.session_state.class_table["RandomClassLorePrompt"]+":", key = "t_char_class_lore", label_visibility="collapsed", disabled=st.session_state.select_disable_desc)
        col1, col2, col3, col4 = st.columns([1,1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Random', key = "desc_random", on_click = stl.randomDesc, disabled=st.session_state.select_disable_desc)
        with col3:
            st.button('Finalize', key = "desc_finalize", on_click = stc.finalizeDesc, disabled=st.session_state.select_disable_desc)
        with col4:
            pass
        if st.session_state.err_text_desc:
            st.error(stl.errTextDB["err_text_desc"])
    else:
        col1, col2 = st.columns([1,4],vertical_alignment="top")
        with col1:
            st.write(descFieldList[0]+":")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_name)
        with col2:
            st.write("Description:")
            with st.container(border=True):
                st.write(st.session_state.PC.pc_desc)
    
        
#ROW 5 - STUFF
if st.session_state.stage >= 5:
    if not st.session_state.select_disable_stuff:
        if "RandomClassStuff" in st.session_state.class_table.keys():
            st.header(st.session_state.class_table["RandomClassStuffText"])
            stl.insertStuffEntry(bc.StuffField("RandomItem", None, {}), "RandomClassStuff", customStuffTable = st.session_state.class_table["RandomClassStuff"])
            st.header("You also have:")
        else:
            st.header("You have:")
        
        stuffList = st.session_state.class_table["Stuff"]
        if "ClassStuff" in st.session_state.class_table.keys():
            stuffList = st.session_state.class_table["ClassStuff"] + stuffList
        for stuffItem in stuffList:
            stl.insertStuffEntry(stuffItem, stuffItem.p_source)
        col1, col2, col3 = st.columns([1,1,1],vertical_alignment="bottom")
        with col1:
            pass
        with col2:
            st.button('Finalize', key = "stuff_finalize", on_click = stc.finalizeStuff, use_container_width=True, disabled=st.session_state.select_disable_stuff)
        with col3:
            pass
            
#FULL CHARACTER SHEET
if st.session_state.stage < 0:
    st.markdown('<h1 style="width:100%;text-align:center">'+"You are "+st.session_state.PC.pc_name+'</h1>',unsafe_allow_html=True)
    
    st.divider()
    statList = stl.fieldTableDB["StatTable"]
    headerString = ""
    statString = "+"+str(st.session_state.PC.pc_agi) if st.session_state.PC.pc_agi > 0 else str(st.session_state.PC.pc_agi)
    headerString = headerString + '<div>' + statList[0]+": " + statString + '</div>'
    statString = "+"+str(st.session_state.PC.pc_knw) if st.session_state.PC.pc_knw > 0 else str(st.session_state.PC.pc_knw)
    headerString = headerString + '<div>' + statList[1]+": " + statString + '</div>'
    statString = "+"+str(st.session_state.PC.pc_pre) if st.session_state.PC.pc_pre > 0 else str(st.session_state.PC.pc_pre)
    headerString = headerString + '<div>' + statList[2]+": " + statString + '</div>'
    statString = "+"+str(st.session_state.PC.pc_str) if st.session_state.PC.pc_str > 0 else str(st.session_state.PC.pc_str)
    headerString = headerString + '<div>' + statList[3]+": " + statString + '</div>'
    statString = "+"+str(st.session_state.PC.pc_tou) if st.session_state.PC.pc_tou > 0 else str(st.session_state.PC.pc_tou)
    headerString = headerString + '<div>' + statList[4]+": " + statString + '</div>'
    headerString = headerString + '<div>' + "HP: " +str(st.session_state.PC.pc_hp_current)+"/"+str(st.session_state.PC.pc_hp_max) + '</div>'
    headerString = headerString + '<div>' + "Glitches: " +str(st.session_state.PC.pc_glitch_current)+" ("+str(st.session_state.PC.pc_glitch_roll)+')</div>'
    st.markdown('<div style="width:100%;display:flex;justify-content:space-between">'+headerString+'</div>',unsafe_allow_html=True)
    st.divider()
    
    st.write(st.session_state.PC.pc_desc)