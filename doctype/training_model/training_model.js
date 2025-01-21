// Copyright (c) 2025, Frappe Technologies and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Training Model", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Training Model", {
    refresh: function(frm) {

        console.log(frm.doc.training_label);

        frm.add_custom_button(__('Training'), function() {


            //API CALL on click on Training button inside Train
            frappe.call({
                //change path for method accordingly
                method:"frappe.api.api.getTestData",
                args: {
                     training_label: frm.doc.training_label,
                     training_data: frm.doc.training_data,
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

// //On Training Model Form- if we click button train -   refresh form and add new custom button with name Training-training_data field- execute the function
// frappe.ui.form.on("Training Model", {
//     refresh: function(frm) {
//         frm.add_custom_button(__('Training'), function() {
//             console.log(frm.doc.training_data);
//             console.log(frm.doc.training_label);
//         }, __("Train"));
//     }
// });


// //On Training Model Form- if something happens in training_data field- execute the function
// frappe.ui.form.on("Training Model",'training_data', function(frm) {
//     // frappe.msgprint("Training Data Added ");
//     console.log(frm.doc.training_data);
//     console.log(frm.doc.training_label);
//    });
