st = "ThIsisCoNfUsInG"
sub_st = "is"
new = ""
new2 = ""

if sub_st.islower() == True:
    try:
        new = st.replace(sub_st.upper(), "")
    except:
        new2 = st.replace(sub_st.capitalize(), "")

if sub_st.isupper() == True:
    try:
        new = st.replace(sub_st.lower(),"")
    except:
        new2 = st.replace(sub_st.capitalize(), "")

print(new)

print(new2)
