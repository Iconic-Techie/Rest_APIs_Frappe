import frappe
from frappe.model.document import Document
import pandas as pd
import csv
import glob #library

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

@frappe.whitelist()
def getTestData(label, text):
		# csv_files = glob.glob(r"csv_files\*.csv")
		training_documents = r"./library.localhost/private/files/training_documents.csv"
		testing_documents = r"./library.localhost/private/files/testing_documents.csv"

		#reads file into pandas dataframe
		training_df = pd.read_csv(training_documents, delimiter=",", quoting=csv.QUOTE_ALL, engine="python", on_bad_lines="skip")

		#removes any row that is has empty text or label
		training_df = training_df.dropna(subset=['text', 'label'])



		print(training_df)
		print("--------------------------------------------------------------------------------------------------------------")
		print(training_df['label'].value_counts())
		print("--------------------------------------------------------------------------------------------------------------")

		# Extract text and labels
		X_train = training_df['text'] 
		Y_train = training_df['label']  

		# converts text into numerical vectors
		vectorizer = TfidfVectorizer(stop_words='english')
		X_train_vec = vectorizer.fit_transform(X_train)

		model = LogisticRegression(max_iter=1000)
		model.fit(X_train_vec, Y_train)

		#reads file into pandas dataframe
		training_df = pd.read_csv(training_documents, delimiter=",", quoting=csv.QUOTE_ALL, engine="python", on_bad_lines="skip")

		#removes any row that is has empty text or label
		training_df = training_df.dropna(subset=['text', 'label'])



		print(training_df)
		print("--------------------------------------------------------------------------------------------------------------")
		print(training_df['label'].value_counts())
		print("--------------------------------------------------------------------------------------------------------------")


		# Extract text and labels
		X_train = training_df['text'] 
		Y_train = training_df['label']  

		# converts text into numerical vectors
		vectorizer = TfidfVectorizer(stop_words='english')
		X_train_vec = vectorizer.fit_transform(X_train)

		model = LogisticRegression(max_iter=1000)
		model.fit(X_train_vec, Y_train)


		testing_df = pd.read_csv(testing_documents, delimiter=",", quoting=csv.QUOTE_ALL, engine="python", on_bad_lines="skip")
		testing_df = testing_df.dropna(subset=['text', 'label'])  # Remove rows with missing text or labels

		# Prepare the new data
		X_test = testing_df['text']  # Extract text
		Y_expected = testing_df['label']  # Extract expected labels
		X_test_vec = vectorizer.transform(X_test)  # Transform new text using the same vectorizer

		# Make predictions
		Y_pred = model.predict(X_test_vec)

		# Compare predictions with expected labels
		testing_df['Predicted_Label'] = Y_pred
		testing_df['Correct'] = testing_df['Predicted_Label'] == Y_expected

		# Print the results
		print("\nClassification Results:")

		#prints the text, label, what the model predicted, and if it was correct or not
		print(testing_df[['text', 'label', 'Predicted_Label', 'Correct']])
		print("--------------------------------------------------------------------------------------------------------------")

		#prints classifaction report
		print(f"\nAccuracy on Data: {accuracy_score(Y_expected, Y_pred):.4f}")
		print("Classification Report for New Data:")
		print(classification_report(Y_expected, Y_pred, zero_division=0))

		return {
			classification_report(Y_expected, Y_pred, zero_division=0)
		}

		# return {
		# 	"API returned Inputs received as parameters: \n\n" + "HI" +
		# 	'label:' + label +
		# 	'\n text:' + text + 'DF:' + classification_report(Y_expected, Y_pred, zero_division=0).to_string()
		# }
		
		# return {
		# "classification_report": classification_report(
		# 	Y_expected, 
		# 	Y_pred, 
		# 	zero_division=0
		# 		)
		# 		}
