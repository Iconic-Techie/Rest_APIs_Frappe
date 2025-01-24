// Copyright (c) 2025, Shruti Gupta and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Classification of Text", {
// 	refresh(frm) {

// 	},
// });


//On Training Model Form- if we click button train -   refresh form and add new custom button with name Training-training_data field- execute the function
frappe.ui.form.on("Classification of Text", {
    refresh: function(frm) {


        frm.add_custom_button(__('Training'), function() {

            //API CALL on click on Training button inside Train
            frappe.call({
                method:"library_management.training_api.getTestData",
                args: {
                     label: frm.doc.label,
                     text: frm.doc.text,
                 },
                callback: function(response) {
                    if(response.exc) {
                        console.log("Error",response.exc);
                    } else {
                        console.log(response.message);
                    }
                }
            })

        }, __("Train"));
    }

});