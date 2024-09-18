import streamlit as st
import pickle
import pandas as pd

# Load the data and models
medicines_dict = pickle.load(open('model/medicine_dictionary.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

def recommend(medicine):
    try:
        # Find the index of the selected medicine
        medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
        distances = similarity[medicine_index]
        # Get top  most similar medicines, excluding the selected one
        medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
        recommended_medicines = [medicines.iloc[i[0]].Drug_Name for i in medicines_list]
        return recommended_medicines
    except IndexError:
        # Handle the case where the medicine is not found
        return []

# Streamlit app
st.title('Medicine Recommender System')

# Dropdown for selecting medicine
selected_medicine_name = st.selectbox(
    'Type your medicine name whose alternative is to be recommended',
    options=medicines['Drug_Name'].values
)

# Button to get recommendations
if st.button('Recommend Medicine'):
    recommendations = recommend(selected_medicine_name)
    if recommendations:
        st.write(f'Recommended Medicines for {selected_medicine_name}:')
        for idx, rec in enumerate(recommendations, 1):
            st.write(f"{idx}. {rec} [Click to Buy](https://pharmeasy.in/search/all?name={rec})")
    else:
        st.write('Medicine not found or no recommendations available.')
