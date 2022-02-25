import csv
import pandas as pd
import numpy as np
from tqdm import tqdm
#0 date
#1 patient
#2 encounter
#3 category
#4 code
#5 description
#6 value
#7 units
#8 type


#df = pd.read_csv("observations_sorted.csv")
df = pd.read_csv("observations.csv")
df = df.sort_values(by=["PATIENT", "DATE"], ascending=True)

#df_encounters = pd.read_csv("encounters_sorted.csv")
df_encounters =pd.read_csv('encounters.csv')
df_encounters = df_encounters.sort_values(by=["PATIENT", "START"], ascending=True)

patients_info = pd.read_csv("patients.csv")




hypertension_patients_table =df_encounters[(df_encounters['REASONDESCRIPTION'] == 'Hypertension')]
hypertension_patients = hypertension_patients_table['PATIENT'].values

new_df =df[df['PATIENT'].isin(hypertension_patients)]
new_df.to_csv("hypertension_observations.csv", index = False)
new_df = pd.read_csv("hypertension_observations.csv")


a = ((df_encounters['REASONDESCRIPTION'] == 'Hypertension')).values

hypertension_indices = np.where(a==True)[0]
temp  =  hypertension_indices - 1
indices_to_be_deleted_in_temp = []

for i in range(len(temp)):    
    if temp[i] in hypertension_indices:
        indices_to_be_deleted_in_temp.append(i)
    
indices_just_before_hypertension = np.delete(temp, indices_to_be_deleted_in_temp)
new_hypertension_indices =np.sort(np.concatenate((hypertension_indices, indices_just_before_hypertension)))

#print(new_hypertension_indices)

filtered_df_encounters =df_encounters.iloc[new_hypertension_indices]
#print(filtered_df_encounters)
filtered_df_encounters['START'] = filtered_df_encounters['START'].str.split('T').str[0]

print("distinct hypertension patients:",len(set(hypertension_patients)))



#data = [None, None, None, None, None, None, None, None, None]
columns = []
wr = open('hypertension_table.csv', 'w', encoding='UTF8', newline='')
writer =csv.writer(wr)

unique_columns = list(pd.read_csv("header_template.csv", header=None).values[0])

writer.writerow(unique_columns)



HISTORY_LENGTH_YEARS = 120

patient_history = np.empty([HISTORY_LENGTH_YEARS,len(unique_columns)],  dtype="<U100")
patient_history[:,:] = ""
patient_current_row = [""] * len(unique_columns)
patient_row_counter = 0


at_least_one_flag = False


	
	

append_row = [""] * len(unique_columns)
prev_patient_id = 0
prev_time = 0
prev_hypertension_dates = []

ROW_LIMIT = new_df.shape[0]
chunk_df = new_df[0:ROW_LIMIT]
low=0
high= ROW_LIMIT
while(high<=new_df.shape[0]):

	for i, line in tqdm(chunk_df.iterrows(),total=chunk_df.shape[0]): #tqdm(df.iterrows(),total=df.shape[0]):    #5-6 hour with python csv to read and iterate.




	
		if(i==0):
			continue

	 	


		time = line[0]
		time = time.split("T")[0]
		
		patient_id = line[1]

		
		if(prev_patient_id != patient_id):
			hypertension_dates =filtered_df_encounters[filtered_df_encounters['PATIENT'] == patient_id]['START'].values #get hypertension dates for this patient. [if it does not have any hypertension history, then we simply skip that patient by conecutive continue statements]

		if(all(hypertension_date < time for hypertension_date in hypertension_dates)): # if every hypertension date is smaller than the current date, then simply skip that date.
		
			continue
		

		if(patient_id not in hypertension_patients):
			
			continue

		if(prev_time != time):
			patient_history[patient_row_counter,:]=patient_current_row
			patient_row_counter += 1
			patient_current_row = [""] * len(unique_columns)

		if(((patient_id != prev_patient_id and i>1) or (patient_row_counter >= HISTORY_LENGTH_YEARS)) and (at_least_one_flag)): # new patient, so write old patient's row



			
			
			temp =patients_info[(patients_info['Id'] == prev_patient_id)]

			time_age = int(prev_time.split('-')[0])
			birth_year = int((temp['BIRTHDATE'].str.split('-').str[0]).values)

			age =  str(time_age - birth_year)
			gender =temp['GENDER'].values[0]
			race =temp['RACE'].values[0]

			patient_history[:,2] = age
			patient_history[:,3] = gender
			patient_history[:,4] = race



		
			patient_history[:,-1] = '1' # insert hypertension  = 1 to the last column.

			append_row = patient_history[patient_row_counter-1, :]

			missing_feature_indices = np.where(append_row == '')[0]

			#df = pd.DataFrame(patient_history, columns = unique_columns)
			#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
			#    print(df)
			#df.to_csv("first_hypertension_patient.csv")


			temp = patient_row_counter-2 # go to previous row.

			for j in range(len(missing_feature_indices)):

				temp = patient_row_counter -2
				while(temp>=0): # if you cannot find a substitute, then missing column will be PERMAMENT.

					current_missing_column = missing_feature_indices[j]
					if (patient_history[temp,current_missing_column] != ''):
						append_row[current_missing_column] = patient_history[temp,current_missing_column]
						break #break the while

					else:
						temp -= 1 

				
			writer.writerow(append_row)
			append_row = [""] * len(unique_columns)

			patient_history = np.empty([HISTORY_LENGTH_YEARS,len(unique_columns)],  dtype="<U100")
			patient_history[:,:] = ""
			patient_current_row = [""] * len(unique_columns)
			patient_row_counter = 0
			at_least_one_flag = False



		patient_current_row[0] = time
		patient_current_row[1] = patient_id

		description = line[5]
		index_of_current_description =unique_columns.index(description)

		value = line[6]
		patient_current_row[index_of_current_description] = value

		prev_patient_id = patient_id
		prev_time = time
		prev_hypertension_dates = hypertension_dates
		at_least_one_flag = True

	if(high<=new_df.shape[0]):
		chunk_df = new_df[low+ROW_LIMIT:high+ROW_LIMIT]
		low = low+ROW_LIMIT
		high = high+ROW_LIMIT



		

wr.close()






