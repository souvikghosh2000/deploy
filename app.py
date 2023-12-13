import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def pred(input_data):
    input_data = np.array([0,2035,1,1,6,1042.0,1,1,0,7,141.0,59,1,0,3,1368654.0,0])   #taking user input
    input_data_as_numpy_array = np.asarray(input_data) # Convert to numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) # it's reshaping the data into a 2D array with one row and as many columns as there are elements in
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return 'The person wont buy Term Deposit'
    else:
       return 'The person will buy Term Deposit'

def main():
    # providing a title
    st.title('Term Deposit Prediction')
    job_options = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    binary = [0,1]
    contact_option = [0,1,2,3,4]
    marital_option = [0,1,2,3]
    education_option = [0,1,2,3,4,5,6]


    # getting input from user
    insurance = st.selectbox("Insurance: No-0 Yes-1",binary)
    balance = st.text_input("Enter the balance")
    housing = st.select_slider("Housing Loan:  No-0 Yes-1", [0,1])
    loan = st.selectbox("Loan:  No-0 Yes-1",binary)
    contact = st.selectbox("Contact Type: unknown-4', 'cellular-0', 'telephone-3', 'Mobile-1', 'Tel-2",contact_option)
    duration = st.text_input("Duration")
    campaign = st.text_input("Number of contacts performed")
    previous = st.text_input("Number of contacts performed before this campaign and for this client ")
    poutcome = st.text_input("Outcome of the previous marketing campaign ")
    count_txn = st.text_input("Number of Transactions Done by the customer ")
    age = st.text_input("Age of the customer ")
    job = st.selectbox("Select the job of the customer",job_options )
    marital = st.selectbox("Job of the customer",marital_option)
    education = st.selectbox("Education",education_option)
    annual_income = st.text_input("Annual Income ")
    gender = st.select_slider("Housing Loan:  Male-1 Female-0", [0.1])



    # prdiction value
    output = ' '
    if st.button("Predict"):
        input_data = np.array([insurance, balance, housing,loan , contact, duration, campaign, previous,poutcome,count_txn, age, job, marital, education,annual_income,gender])
        output = pred(input_data)
    st.success(output)


if __name__ == '__main__':
    main()

