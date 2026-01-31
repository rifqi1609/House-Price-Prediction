# Import libraries
import pandas as pd                                       
import numpy as np
import dill                                             
import streamlit as st

# Load model file
with open('deployment/model_final.pkl', 'rb') as f:
    best_model = dill.load(f)

def run():
    st.title('House Price Prediction')
    st.markdown('## Input Single Data')
   
    # Form
    with st.form('form_input'):
        area = st.text_input('Input District Name')
        city = st.text_input('Input City Name')
        lattitude = st.number_input('Input Lattitude', format="%.10f", step=0.0000000001)
        logitude = st.number_input('Input Longitude', format="%.10f", step=0.0000000001)
        bedroom = st.number_input('Input Number of Bedroom', value=0, step=1)
        bathroom = st.number_input('Input Number of Bathroom', value=0, step=1)
        land_area = st.number_input('Input Size of Land Area', value=0, step=1)
        building_area = st.number_input('Input Size of Building Area', value=0, step=1)
        floor = st.number_input('Input Number of Floor', value=0, step=1)
        maid_bedroom = st.number_input('Input Number of Maid Bedroom', value=0, step=1)
        maid_bathroom = st.number_input('Input Number of Maid Bathroom', value=0, step=1)
        cat_cert = ['shm - sertifikat hak milik', 'hgb - hak guna bangunan', 'lainnya (ppjb,girik,adat,dll)']
        certificate = st.radio('Select Condition', cat_cert, index=1)
        voltage = st.number_input('Input Voltage Capacity', value=0, step=1)
        voltage_with_unit = f"{voltage} mah"
        building_age = st.number_input('Input Building Age', value=0, step=1)
        year = st.number_input('Input Constructed Year', value=0, step=1)
        cat_con = ['bagus', 'bagus sekali', 'baru', 'sudah renovasi', 'butuh renovasi']
        condition = st.radio('Select Condition', cat_con, index=1)
        garage = st.number_input('Input Number of Garage', value=0, step=1)
        carport = st.number_input('Input Number of Carport', value=0, step=1)        
        submit_btn = st.form_submit_button('Predict')

    if submit_btn:
        df_inf={"area":area,
                "city":city,
                "lattitude":lattitude,
                "logitude":logitude,
                "property_type":'rumah',
                "bedrooms":bedroom,
                "bathrooms":bathroom,
                "land_area":land_area,
                "building_area":building_area,
                "floors":floor,
                "maid_bedrooms":maid_bedroom,
                "maid_bathrooms":maid_bathroom,
                "certificate":certificate,
                "voltage":voltage_with_unit,
                "building_age":building_age,
                "year":year,
                "condition":condition,
                "garage":garage,
                "carport":carport}
        df_inf = pd.DataFrame([df_inf])
        st.dataframe(df_inf)
        # Predict
        y_pred_inf = best_model.predict(df_inf)

        # Display Data
        df_inf['Prediction (Million)']=y_pred_inf/1000000
        st.success("Prediction Complete!")
        st.dataframe(df_inf)
        st.write(f"The prediction price of this house is '{df_inf['Prediction (Million)']}'")

if __name__ == '__main__':
    run()


def run_file():
    st.markdown('## Input Multiple Data')

    # 2. Upload File CSV
    uploaded_file = st.file_uploader("Upload Data", type=["csv"])

    if uploaded_file is not None:
        # Load New Data
        df_inf = pd.read_csv(uploaded_file)

        # Tombol Prediksi
        if st.button('Predict All'):
            try:
                # Prediksi
                y_pred_inf = best_model.predict(df_inf)

                # Display Data
                df_inf['Prediction (Million)']=y_pred_inf/1000000

                # Menampilkan Hasil
                st.success("Prediction Complete!")
                st.dataframe(df_inf)

                # Tombol Download Hasil
                csv = df_inf.to_csv(index=False).encode('utf-8')
                st.download_button("Download Prediction", csv, "prediction.csv", "text/csv")
            
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == '__main__':
    run_file()

