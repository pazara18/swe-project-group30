import pandas as pd

def drop_necessities(csv):


		df = pd.read_csv(csv)
		df = df[df['Age'].notna() & df['Gender'].notna() & df['Race'].notna() &  
				df['Tobacco smoking status NHIS'].notna() & df['Respiratory rate'].notna() 
				& df['Pain severity - 0-10 verbal numeric rating [Score] - Reported'].notna() & df['Heart rate'].notna() & df['Body Height'].notna()
				& df['Body Weight'].notna() & df['Body Mass Index'].notna() & df['Low Density Lipoprotein Cholesterol'].notna()
				& df['High Density Lipoprotein Cholesterol'].notna() & df['Triglycerides'].notna() & df['Total Cholesterol'].notna() 
				& df['Hemoglobin [Mass/volume] in Blood'].notna() & df['Sodium'].notna() & df['Systolic Blood Pressure'].notna() 
				& df['Diastolic Blood Pressure'].notna() & df["Stress is when someone feels tense  nervous  anxious or can't sleep at night because their mind is troubled. How stressed are you?"].notna()]



		#df.to_csv(csv.split(.)[0] + "_dropped.csv", index = False)
		return df


def drop_extras(df):
	df_dropped_any_nul_columns =  df.dropna(axis=1)

	return df_dropped_any_nul_columns.drop(['What language are you most comfortable speaking?',
											'What address do you live at?'], axis=1)


def keep_only_necessities(df):
	necessity_list = ['Age','Gender','Race', 'Tobacco smoking status NHIS', 'Respiratory rate',  'Pain severity - 0-10 verbal numeric rating [Score] - Reported',
					 'Heart rate', 'Body Height', 'Body Weight', 'Body Mass Index', 'Low Density Lipoprotein Cholesterol', 'High Density Lipoprotein Cholesterol','Triglycerides',
					 'Total Cholesterol', 'Hemoglobin [Mass/volume] in Blood', 'Sodium', 'Systolic Blood Pressure', 'Diastolic Blood Pressure', "Stress is when someone feels tense  nervous  anxious or can't sleep at night because their mind is troubled. How stressed are you?",
					 'Hypertension']
	
	df_heavy_filtered =df.filter(necessity_list)
	return df_heavy_filtered 


	

if __name__ == '__main__':


	df_non_hypertension = drop_necessities('non_hypertension_table.csv')
	df_hypertension =  drop_necessities('hypertension_table.csv')
	print(df_hypertension)

	df_appended = df_non_hypertension.append(df_hypertension)
	df_appended.to_csv("merged_final_data.csv", index=False)

	df_appended_clean = drop_extras(df_appended)
	df_appended_clean.to_csv("merged_final_data_clean.csv", index=False)


	df_heavy_filtered = keep_only_necessities(df_appended)
	df_heavy_filtered.to_csv("merged_final_data_heavy_filtered.csv", index=False)




