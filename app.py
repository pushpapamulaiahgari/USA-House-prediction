import streamlit as st
import joblib
#load trined model
model=joblib.load('model_trained.pkl')

#title
st.title("🏡⛪🏰🙄 House Price Prediction")
st.write(" House Price Prediction using Machine Learning")
#input fields
Avg_Area_Income=st.number_input("Avg_Area_Income",min_value=0.0)
Avg_Area_House_Age=st.number_input("Avg_Area_House_Age",min_value=0.0)
Avg_Area_Number_of_Rooms=st.number_input("vg_Area_Number_of_Rooms",min_value=0.0)
Avg_Area_Number_of_Bedrooms=st.number_input("Avg_Area_Number_of_Bedrooms",min_value=0.0)
Area_Population=st.number_input("Area_Population",min_value=0.0)


#prediction button
if st.button("House Prediction"):

    input_list = [[
        Avg_Area_Income,
        Avg_Area_House_Age,
        Avg_Area_Number_of_Rooms,
        Avg_Area_Number_of_Bedrooms,
        Area_Population
    ]]
    #pridict
    final_prediction = model.predict(input_list)
    
    #display output
    predicted_price=round(final_prediction[0],2)

    st.success(f"🏛🏤 Predicted House Price: ${predicted_price:,.2f} ")
    
