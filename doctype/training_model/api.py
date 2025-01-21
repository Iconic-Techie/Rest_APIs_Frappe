import frappe
from frappe.model.document import Document

@frappe.whitelist()
def getTestData(training_label, training_data):
		

		return {
			"API returned Inputs received as parameters: \n\n" + "HI" +
			'Training_Label:' + training_label +
			'\n Training_Data:' + training_data
		}
