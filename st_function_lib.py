import streamlit as st
from extra_streamlit_components import CookieManager
import time
import json

def appSetupKeys():
    time.sleep(5)
    if "card_set" not in st.session_state:
        st.session_state.card_set = []
    if "new_card" not in st.session_state:
        st.session_state.new_card = None
    if "numeral_type" not in st.session_state:
        if "numeral_type" in st.context.cookies.keys():
            st.write(cookieVal)
            st.session_state.numeral_type = st.context.cookies["numeral_type"]
        else:
            st.session_state.numeral_type = "Mixed"
    if "show_line_message" not in st.session_state:
        if "show_line_message" in st.context.cookies.keys():
            st.session_state.cookieVal = st.context.cookies["show_line_message"]
            st.write(st.session_state.cookieVal)
            st.session_state.show_line_message = (st.session_state.cookieVal == "True")
        else:
            st.session_state.show_line_message = True
    if "show_line_inverse" not in st.session_state:
        if "show_line_inverse" in st.context.cookies.keys():
            st.session_state.cookieVal = st.context.cookies["show_line_inverse"]
            st.write(st.session_state.cookieVal)
            st.session_state.show_line_inverse = (st.session_state.cookieVal == "True")
        else:
            st.session_state.show_line_inverse = True
    if "show_card_preview" not in st.session_state:
        if "show_card_preview" in st.context.cookies.keys():
            st.session_state.cookieVal = st.context.cookies["show_card_preview"]
            st.write(st.session_state.cookieVal)
            st.session_state.show_card_preview = (st.session_state.cookieVal == "True")
        else:
            st.session_state.show_card_preview = True
    time.sleep(5)

def appUpdateCookies():
    cookie_manager.batch_set({"numeral_type": st.session_state.numeral_type,"show_line_message": str(st.session_state.show_line_message),"show_line_inverse": str(st.session_state.show_line_inverse),"show_card_preview": str(st.session_state.show_card_preview)},max_age = 34560000)

def resetCards():
    st.session_state.card_set = []
    st.session_state.new_card = None

def resetSettings():
    st.session_state.numeral_type = "Mixed"
    st.session_state.show_line_message = True
    st.session_state.show_line_inverse = True
    st.session_state.show_card_preview = True
    
def get_manager():
    return CookieManager()
            
def updateCookie(key):
    cookie_manager.set(key,str(st.session_state[key]),max_age = 34560000)
            
def displayNumeralType(numType):
    if numType == "Mixed":
        numType = "Mixed (Default)"
    return numType

def getCards():
    with open('jsonDB/cardTable.json', encoding='utf-8') as fh:
        jsonObject = json.load(fh)
    return jsonObject

def writeCard(card):
    for line in card["Text"]:
        if isinstance(line,dict):
            (lineType, line), = line.items()
            if (lineType == "Message" and st.session_state.show_line_message == False) or (lineType == "Inverse" and st.session_state.show_line_inverse == False):
                continue
            line = "*" + lineType + "*: " + line
        st.write(line)

def addCard():
    if st.session_state.new_card:
        st.session_state.card_set.append(st.session_state.new_card)
        st.session_state.new_card = None

def removeCard(ID):
    st.session_state.card_set.pop(ID)

def getCardName(card):
    if card["Suit"] == "Major Arcana":
        if st.session_state.numeral_type == "Arabic":
            cardNumberString = str(card["Number"])
        else:
            cardNumberString = toRoman(card["Number"])
        nameString = cardNumberString + ": " + card["Name"]
    else:
        match card["Number"]:
            case 1:
                cardNumberString = "Ace"
            case 11:
                cardNumberString = "Page"
            case 12:
                cardNumberString = "Knight"
            case 13:
                cardNumberString = "Queen"
            case 14:
                cardNumberString = "King"
            case _:
                if st.session_state.numeral_type == "Roman":
                    cardNumberString = toRoman(card["Number"])
                else:
                    cardNumberString = str(card["Number"])
        nameString = cardNumberString + " of " + card["Suit"]
    return nameString

def getCardTitle(card):
    titleString = "**"
    if card["Suit"] == "Major Arcana":
        if st.session_state.numeral_type == "Arabic":
            cardNumberString = str(card["Number"])
        else:
            cardNumberString = toRoman(card["Number"])
        titleString = titleString + cardNumberString + " &nbsp;&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;" + card["Name"]
    else:
        match card["Number"]:
            case 1:
                cardNumberString = "Ace"
            case 11:
                cardNumberString = "Page"
            case 12:
                cardNumberString = "Knight"
            case 13:
                cardNumberString = "Queen"
            case 14:
                cardNumberString = "King"
            case _:
                if st.session_state.numeral_type == "Roman":
                    cardNumberString = toRoman(card["Number"])
                else:
                    cardNumberString = str(card["Number"])
        titleString = titleString + cardNumberString + " of " + card["Suit"]
    return titleString + " &nbsp;&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;" + card["Keyword"]+"**"

def toRoman(n):
    if not isinstance(n, int):
        raise NotIntegerError("decimals cannot be converted")
    if not (-1 < n < 5000):
        raise OutOfRangeError("number out of range (must be 0..4999)")

    # special case
    if n == 0:
        return '0'

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result
    
# Define digit mapping
romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('C', 100),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                   ('I', 1))
numeralTypeList = ["Mixed","Arabic","Roman"]
cookie_manager = get_manager()
cardTable = getCards()