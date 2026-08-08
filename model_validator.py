from pydantic import BaseModel, Field, model_validator
from typing import Optional

class AgentDeploymentConfig(BaseModel):
    agent_name: str
    environment: str  # e.g., 'production' or 'development'
    api_key: Optional[str] = None
    timeout_seconds: int = Field(default=30)

    # 💡 Cross-Field Validation using mode='after'
    @model_validator(mode='after')
    def validate_environment_and_keys(self) -> 'AgentDeploymentConfig':
    # Rule 1: If the environment is 'production', the api_key is mandatory.
        if self.environment.lower() == 'production' and not self.api_key:
            raise ValueError("Production environment requires an 'api_key' to be explicitly provided!")

        # Rule 2: In production, the timeout should not be less than 10 seconds.
        if self.environment.lower() == 'production' and self.timeout_seconds < 10:
            raise ValueError("Timeout seconds for production must be at least 10 seconds.")

    # Return 'self' if validation succeeds.
        return self


# Test Case 1: Valid Production Config
try:
    prod_agent = AgentDeploymentConfig(
        agent_name="DataExtractionAgent",
        environment="production",
        api_key="SK-PROD-998877",
        timeout_seconds=15
    )
    print("✅ Success:", prod_agent.model_dump())
except Exception as e:
    print("❌ Error:", e)



# Test Case 2: Invalid Production Config (api_key missing -> ValidationError will occur)
try:
    invalid_agent = AgentDeploymentConfig(
        agent_name="DataExtractionAgent",
        environment="production",
        timeout_seconds=5
    )
    print("✅ Success:", invalid_agent.model_dump())
except Exception as e:
    print("\n❌ Expected Validation Error:\n", e)