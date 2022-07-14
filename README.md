# Building a REST API with Django Framework

A borrower submitted a loan request for $5,000 to pay them back in 6 months. They received an offer from one of the investors on the platform with a 15% Annual Interest Rate. A $3.00 additional fee will be added to the total loan amount to be paid by the investor.

Requirements:
* You are required to develop a Django REST project to be able to build the following flow-through its APIs;
* The borrower submits a loan request for $5,000 `loan amount` and 6 months `loan period`
* The investor will submit an offer to the borrower with 15% `Annual Interest Rate`
* The borrower will accept the offer
* Check if the investor has sufficient balance in their account to fund the `Total Loan Amount` (Loan Amount + Additional Fee)
* The loan will be funded successfully and the loan status will be `Funded`
* Six monthly payments will be scheduled from the day the loan was funded successfully (Note: Developing an external scheduler is not required)
* Once all the payments are successfully paid back to the investor, the loan status will be changed to `Completed`
