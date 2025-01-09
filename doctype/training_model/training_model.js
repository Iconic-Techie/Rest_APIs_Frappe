// Copyright (c) 2025, Frappe Technologies and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Training Model", {
// 	refresh(frm) {

// 	},
// });


//On Training Model Form- if we click button train -   refresh form and add new custom button with name Training-training_data field- execute the function
frappe.ui.form.on("Training Model", {
    refresh: function(frm) {
        frm.add_custom_button(__('Training'), function() {
            console.log(frm.doc.training_data);
            console.log(frm.doc.training_label);
        }, __("Train"));
    }
});


//On Training Model Form- if something happens in training_data field- execute the function
frappe.ui.form.on("Training Model",'training_data', function(frm) {
    // frappe.msgprint("Training Data Added ");
    console.log(frm.doc.training_data);
    console.log(frm.doc.training_label);
   });