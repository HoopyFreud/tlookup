import streamlit as st
import json

def appSetupKeys():
    if "card_set" not in st.session_state:
        st.session_state.card_set = []
    if "new_card" not in st.session_state:
        st.session_state.new_card = None

def getCards():
    with open('jsonDB/cardTable.json', encoding='utf-8') as fh:
        jsonObject = json.load(fh)
    return jsonObject

def addCard():
    st.session_state.card_set.append(st.session_state.new_card)
    st.session_state.new_card = None

def removeCard(ID):
    st.session_state.card_set.pop(ID)

def getCardName(card):
    if card["Suit"] == "Major Arcana":
        nameString = toRoman(card["Number"]) + ": " + card["Name"]
    else:
        match card["Number"]:
            case 1:
                nameString = "Ace"
            case 11:
                nameString = "Page"
            case 12:
                nameString = "Knight"
            case 13:
                nameString = "Queen"
            case 14:
                nameString = "King"
            case _:
                nameString = toRoman(card["Number"])
        nameString = nameString + " of " + card["Suit"]
    return nameString

def getCardTitle(card):
    titleString = "**"
    if card["Suit"] == "Major Arcana":
        titleString = titleString + card["Name"] + " &nbsp;&nbsp;&nbsp;- &nbsp;&nbsp;&nbsp;" + toRoman(card["Number"])
    else:
        match card["Number"]:
            case 1:
                titleString = titleString + "Ace"
            case 11:
                titleString = titleString + "Page"
            case 12:
                titleString = titleString + "Knight"
            case 13:
                titleString = titleString + "Queen"
            case 14:
                titleString = titleString + "King"
            case _:
                titleString = titleString + toRoman(card["Number"])
        titleString = titleString + " of " + card["Suit"]
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
cardTable = getCards()