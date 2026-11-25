
import logging
from multiprocessing import Value
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError, field_validator, model_validator

#basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="webhook.log",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)


class Order(BaseModel):
    order_id: str
    customer_email: str
    quantity: int
    price: float
    total: float

    @field_validator("customer_email", mode="before")
    @classmethod
    def clean_email(cls, value):
        if isinstance(value, str):
            value = value.strip().lower()
        return value

    @field_validator("quantity", mode="after")
    @classmethod
    def check_quantity(cls, value):
        if value < 1:
            raise ValueError("atleast quantity should be 1")
        return value

    @model_validator(mode="after")
    def check_total(self):
        if self.total != self.quantity * self.price:
            raise ValueError("It will be total = quantity x price ")
        return self

app = FastAPI()


@app.post("/webhook/order")
def recieve_order(data: dict):
    try:
        order = Order(**data)
    except ValidationError as e:
        errors = [err["msg"] for err in e.errors()]
        logger.error(f"Order rejected: {data.get('order_id')} ->{errors}")
        raise HTTPException(status_code=422,detail=errors)

    logger.info(f"Order received: {order.order_id}, {order.customer_email}, total={order.total}")
    return {"status": "received", "order_id": order.order_id}