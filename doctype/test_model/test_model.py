# Copyright (c) 2025, Bhuvanesh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

class TestModel(Document):
	model = LogisticRegression(max_iter=1000)
	vectorizer = TfidfVectorizer(stop_words='english')

	def before_save(self):
		self.predicted_label = self.expected_label

		if self.csv_file:
			file_path = self.csv_file
			full_path = frappe.get_site_path(file_path.lstrip('/'))
			print(full_path)
			
		self.train_model()
		self.predicted_label = self.predict_label()
	
	
	def train_model(self):
		#update file path based on where training documents are
		training_documents = r"./development.localhost/private/files/training_documents.csv"

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
		X_train_vec = self.vectorizer.fit_transform(X_train)

		self.model.fit(X_train_vec, Y_train)

	def predict_label(self):
		X_test = [self.document_text]
		X_test_vec = self.vectorizer.transform(X_test)

		Y_pred = self.model.predict(X_test_vec)
		
		return Y_pred

