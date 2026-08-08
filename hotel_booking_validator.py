
from pydantic import BaseModel,Field, model_validator

class HotelBooking(BaseModel):
    guest_name: str
    check_in_day: int = Field(ge=1 ,  le=31)
    check_out_day:int = Field(ge=1 ,  le=31)
    number_of_guests:int =Field(default=1)
    room_type:str

    @model_validator(mode='after')
    def validate_hote_booking(self)->'HotelBooking':
         if self.check_out_day <= self.check_in_day:
              raise ValueError("check_out_day must be  after check_in_day")
         if self.room_type == "single" and self.number_of_guests >1:
              raise ValueError("Single room can only accomadate 1 guest!")
         return self
# Test Case 1: Valid Booking
try:
    booking1 = HotelBooking(
        guest_name="Faris",
        check_in_day=10,
        check_out_day=12,
        number_of_guests=1,
        room_type="single"
    )
    print("✅ Success:", booking1.model_dump())
except Exception as e:
    print("❌ Error:", e)

# Test Case 2: Invalid Dates (Check-out before Check-in)
try:
    booking2 = HotelBooking(
        guest_name="Rahul",
        check_in_day=15,
        check_out_day=12,
        number_of_guests=2,
        room_type="double"
    )
    print("✅ Success:", booking2.model_dump())
except Exception as e:
    print("❌ Expected Error (Dates):", e)

# Test Case 3: Single room with 2 guests
try:
    booking3 = HotelBooking(
        guest_name="Ajith",
        check_in_day=20,
        check_out_day=22,
        number_of_guests=2,
        room_type="single"
    )
    print("✅ Success:", booking3.model_dump())
except Exception as e:
    print("❌ Expected Error (Capacity):", e)        


