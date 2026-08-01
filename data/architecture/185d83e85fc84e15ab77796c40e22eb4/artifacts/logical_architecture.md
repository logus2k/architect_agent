# Logical Architecture

| Definition | Usage | Attributes | Responsibility | Requirement |
|---|---|---|---|---|
| Category | category | id: String, name: String, description: String, order: Integer | Represents a distinct grouping entity within the system. | REQ-0034 |
| Image | image | description: String, itemId: String, languageElement: String, generatedText: String, approvedFlag: Boolean, timestamp: String | Stores the metadata and content associated with an image. | REQ-0037 |
| Reservation | reservation | id: String, userGoogleId: String, tenantId: String, dateTime: String, numberOfPeople: Integer, status: String, timestamp: String, notes: String | Stores the details and state of a booking. | REQ-0038 |
| Tenant | tenant | — | Represents an entity that requires a contact form. | REQ-0045 |
| ContactForm | contactForm | — | Provides the interface and mechanism for users to submit contact information for a tenant. | REQ-0045 |
