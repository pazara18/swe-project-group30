import pandas
import tensorflow as tf
import joblib
import pandas as pd
import numpy as np
#from classes import *

class Model():

    def __init__(self, input_size=26, verbose = False):
        self.model = tf.keras.models.Sequential([
          tf.keras.Input(shape=(input_size,)), #Xtrain[0].shape[0] = 108 -> input size
          tf.keras.layers.Dense(128, activation='relu'), #represents 1st hidden layer 
          tf.keras.layers.Dropout(0.2), # dropout regularization with dropout probability 20 percent
          tf.keras.layers.Dense(128, activation='relu'), #represents the 2nd hidden layer 
          tf.keras.layers.Dropout(0.2), # dropout regularization with dropout probability 20 percent
          tf.keras.layers.Dense(128, activation='relu'), #represents the 3rd hidden layer 
          tf.keras.layers.Dropout(0.2), # dropout regularization with dropout probability 20 percent
          tf.keras.layers.Dense(1, activation='sigmoid') # sigmoid activation at output since it is binary classification
        ])

        self.onehotEncoder = None

        self.verbose = verbose

        if(self.verbose):
            print(self.model.summary())
   


    def load_weights(self, model_weights_path = '../utils/weights/model_heavy_filtered_6drop93accuracy/' , onehotEncoder_weights_path = '../utils/weights/encoder.joblib'):

     
        self.model.load_weights(model_weights_path)
        self.onehotEncoder = joblib.load(onehotEncoder_weights_path)

            




    def predict(self, patient, patient_data, columns_to_encode = ["Tobacco smoking status NHIS", "Stress is when someone feels tense  nervous  anxious or can't sleep at night because their mind is troubled. How stressed are you?", "Gender", "Race"]):

        #health_data_frame : [age, gender, race, smoking, pain_severity, 
        #                     heart_rate, height, weight, bmi,
        #                     hemoglobin , systolic_bp, diastolic_bp, stress ]

        #gender -> string : 'M' or 'F'
        #race   -> string : 'white' or 'asian' or 'black' or 'hawaiian' or 'native' or 'other'
        #smoking -> string: 'Former smoker' or 'Never smoker' or 'Current every day smoker'
        #stress ->  string:  'Not at all' or 'Somewhat' or 'Very much' or 'A little bit' or 'Quite a bit' or 'I choose not to answer this question'
        # Other attributes of health_data_frame are float data type.

        columns = ['Age','Gender','Race', 'Tobacco smoking status NHIS',   'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
                     'Heart rate', 'Body Height', 'Body Weight', 'Body Mass Index','Hemoglobin [Mass/volume] in Blood', 'Systolic Blood Pressure', 'Diastolic Blood Pressure', "Stress is when someone feels tense  nervous  anxious or can't sleep at night because their mind is troubled. How stressed are you?",
                     ]


        health_data = zip([patient.age], [patient.gender[0]], [patient.race.lower()], [patient_data.smoking], [patient_data.pain_severity], 
                        [patient_data.heart_rate], [patient.height], [patient.weight], [patient.bmi], [patient_data.hemoglobin], [int(patient_data.systolic_bp)], [int(patient_data.diastolic_bp)], [patient_data.stress])

        health_data_frame = pd.DataFrame(data=health_data, columns=columns)

        encoded_columns = self.onehotEncoder.transform(health_data_frame[columns_to_encode])
      
        only_scalar = health_data_frame.drop(columns_to_encode, axis=1).values

        processed_data = np.concatenate([encoded_columns,only_scalar], axis=1)
        # print(processed_data.shape)


        prediction = self.model.predict(processed_data)
        
        if prediction[0][0] > 0.5:
            return True
        else:
            return False

        # print(prediction)
        # prediction[prediction <= 0.5] = 1.
        # prediction[prediction > 0.5] = 0.
        # print(prediction)

        # if prediction[0] == 1.:
        #     return True
        # else:
        #     return False


if __name__ == '__main__':

    model = Model(verbose=True)
    model.load_weights()

    health_data = zip([19], ['F'], ['white'], ['Current every day smoker'], [2], 
                        [86], [164.1], [51], [18.9], [15.6], [117], [79], ['Not at all'])

    print(health_data)

    columns = ['Age','Gender','Race', 'Tobacco smoking status NHIS',   'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
                     'Heart rate', 'Body Height', 'Body Weight', 'Body Mass Index','Hemoglobin [Mass/volume] in Blood', 'Systolic Blood Pressure', 'Diastolic Blood Pressure', "Stress is when someone feels tense  nervous  anxious or can't sleep at night because their mind is troubled. How stressed are you?",
                     ]

    health_data_frame = pd.DataFrame(data=health_data, columns=columns)


    prediction = model.predict(health_data_frame)  # True label was : Hypertension
    print(prediction)



    df = pd.read_csv('../utils/merged_final_data_heavy_filtered.csv')
    df_input =df.drop(['Hypertension'], axis=1)

    prediction = model.predict(df_input)
    np.savetxt("batch_prediction.csv", prediction, delimiter=",")
  


