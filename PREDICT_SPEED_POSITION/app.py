import streamlit as st
import pickle

# Load the model from the pickle file
with open('predict_collision.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the Streamlit app
def main():
    st.title('Collision Prediction App')
    st.write('This app predicts collisions based on input features.')

    # Collect input features
    feature1 = st.number_input('x_sim', help='Simulated x-coordinate of the satellite')
    feature2 = st.number_input('y_sim', help='Simulated y-coordinate of the satellite')
    feature3 = st.number_input('z_sim', help='Simulated z-coordinate of the satellite')
    feature4 = st.number_input('Vx_sim', help='Simulated velocity in the x-direction of the satellite')
    feature5 = st.number_input('Vy_sim', help='Simulated velocity in the y-direction of the satellite')
    feature6 = st.number_input('Vz_sim', help='Simulated velocity in the z-direction of the satellite')
    feature7 = st.number_input('euclidean_distance', help='Euclidean distance of the satellite from the reference point')

    # Make prediction
    if st.button('Predict'):
        features = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7]]  # Prepare input features as a list of lists
        prediction = model.predict(features)
        prediction_label = 'Yes' if prediction[0] else 'No'  # Map numerical prediction to "Yes" or "No"
        st.write('Potential Collision:', prediction_label)

if __name__ == '__main__':
    main()
