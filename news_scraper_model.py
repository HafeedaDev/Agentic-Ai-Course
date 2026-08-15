from pydantic import BaseModel, Field
from typing import List, Optional
 
from pydantic import BaseModel, Field
from typing import List, Optional

# Create Pydantic Schema
class NewsArticle(BaseModel):
    title: str
    source_url: str
    catogory: str = Field(default="General")
    tags: List[str] = []
    read_time_minutes: int = Field(ge= 1)
    summary: Optional[str] = None



# --- 1. Testing Valid Data ---
try:
    article1 = NewsArticle(
        title = "LangGraph v0.2 Released",
        source_url="https://example.com/news/1",
        tags = ["AI", "LangChain", "Python"],
        read_time_minutes = 5
    )
    print("✅ Valid Article Created:")
    print(article1)
except Exception as e:
    print(f"❌ Error: {e}")


# --- 2. Testing Invalid Data (Read time is less than 1) ---
try:
    article2 = NewsArticle(
        title="Invalid Read Time Test",
        source_url="https://example.com/news/2",
        read_time_minutes=0  # ge=1 it'll get Error
    )
    print(article2)
except Exception as e:
    print("\n✅ Pydantic Caught Invalid Read Time Successfully:")
    print(e)
















     
