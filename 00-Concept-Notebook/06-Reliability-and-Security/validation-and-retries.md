# Structured output validation and bounded retries

## Two validation layers

| Layer | Responsibility | Project 3 example |
| --- | --- | --- |
| Provider structured output | Encourage/constrain model response shape | JSON Schema sent to the provider |
| Application validation | Protect downstream code and apply business constraints | Pydantic `InvoiceExtraction` model |

Schema-shaped JSON alone is not proof that a value is accurate, supported by source evidence, or complete enough for the business use case.

## Retry rule

Retry only recoverable failures and cap the count. After exhaustion, return a structured error and route the case for review. This prevents runaway cost and infinite loops.

## Exam trap

“Use a stronger prompt” is not a substitute for application validation. Prompts influence behavior; validation deterministically guards the boundary.
