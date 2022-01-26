# %%
import requests

# %% 
res = requests.post("http://localhost:8000/create_borrower", data={"name": "Aly"})
print(res.json())

# %% 
res = requests.get("http://localhost:8000/view_borrowers", data={})
print(res.json())

# %% 
res = requests.post("http://localhost:8000/create_investor", data={"name": "Farida", "balance": 5500.0})
print(res.json())

# %% 
res = requests.get("http://localhost:8000/view_investors", data={})
print(res.json())

# %%
res = requests.post("http://localhost:8000/loan_request", data={"amount": 5000.0, "period": 6})
print(res.json())

# %%
res = requests.post("http://localhost:8000/offer_request", data={"interest_rate": 0.15})
print(res.json())

# %%
res = requests.post("http://localhost:8000/accept_offer", data={})
print(res.json())

# %%

## Schedular Simulator
for i in range(6):
    res = requests.post("http://localhost:8000/monthly_payment", data={"amount_settled": 895.84})
    print(res.json())

# %%
