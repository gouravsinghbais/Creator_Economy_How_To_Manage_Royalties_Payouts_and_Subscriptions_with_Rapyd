from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from rapyd_utils import make_rapyd_request

app = FastAPI()

# ---------- MODELS ----------
class Collaborator(BaseModel):
    name: str
    wallet_id: str
    share: float

class RoyaltyRequest(BaseModel):
    creator_wallet_id: str
    total_revenue: float
    collaborators: List[Collaborator]

class AffiliateRequest(BaseModel):
    affiliate_wallet_id: str
    commission_amount: float
    sender_wallet_id: str

class SubscriptionRequest(BaseModel):
    customer_email: str
    amount: float
    interval: str = "monthly"

# ---------- ENDPOINTS ----------

@app.post("/royalty-payments")
def distribute_royalties(data: RoyaltyRequest):
    results = []
    for collab in data.collaborators:
        payout_amount = round(data.total_revenue * collab.share, 2)
        body = {
            "beneficiary": {"ewallet": collab.wallet_id},
            "amount": payout_amount,
            "currency": "USD",
            "sender": {"ewallet": data.creator_wallet_id},
            "metadata": {"type": "royalty"}
        }
        res = make_rapyd_request("POST", "/v1/account/transfer", body)
        results.append({
            "name": collab.name,
            "amount": payout_amount,
            "status": res.get("status", "FAILED")
        })
    return {"payouts": results}

@app.post("/affiliate-payout")
def process_affiliate_payout(data: AffiliateRequest):
    body = {
        "beneficiary": {"ewallet": data.affiliate_wallet_id},
        "amount": data.commission_amount,
        "currency": "USD",
        "sender": {"ewallet": data.sender_wallet_id},
        "metadata": {"type": "affiliate_commission"}
    }
    res = make_rapyd_request("POST", "/v1/account/transfer", body)
    return res

@app.post("/create-subscription")
def create_subscription(data: SubscriptionRequest):
    body = {
        "amount": data.amount,
        "currency": "USD",
        "customer": {
            "email": data.customer_email
        },
        "interval": data.interval,
        "metadata": {
            "subscription_tier": "premium"
        }
    }
    res = make_rapyd_request("POST", "/v1/payment_links", body)
    return {
        "redirect_url": res.get("data", {}).get("redirect_url", None)
    }
