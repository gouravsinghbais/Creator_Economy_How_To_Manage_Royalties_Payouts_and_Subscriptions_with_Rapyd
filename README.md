# Creator Payment System with Rapyd API (FastAPI + Python)

This project demonstrates how to manage royalty payments, affiliate payouts, and subscriptions in the creator economy using the [Rapyd API](https://docs.rapyd.net/). It’s built with **FastAPI** in Python and supports secure, scalable global transactions.

---

## 🚀 Features

- **Royalty Payments**: Distribute revenue to collaborators based on predefined splits.
- **Affiliate Payouts**: Track and process commission-based payouts.
- **Subscription Management**: Handle recurring payments and flexible tiers.

---

## 🧰 Prerequisites

Before running the app, make sure you have the following:

- Python 3.8+
- [Rapyd Sandbox Account](https://dashboard-sandbox.rapyd.net/)
- Rapyd API Credentials (`RAPYD_ACCESS_KEY` and `RAPYD_SECRET_KEY`)
- [ngrok](https://ngrok.com/) (optional, for testing webhooks)

---

## Add Rapyd API Credentials

RAPYD_ACCESS_KEY=your_rapyd_access_key
RAPYD_SECRET_KEY=your_rapyd_secret_key

## How to Run the App
`uvicorn main:app --reload`

Visit the Swagger API docs at:

http://localhost:8000/docs