# Constraints

| Constraint | Category | Expression | Description | Requirement |
|---|---|---|---|---|
| AssetStorageLocation | resource | storage_location == 'local' | Tenant assets must be stored locally. | REQ-0017 |
| HTTPSEnforcement | safety | isPublicEndpoint == true ? usesHTTPS == true : true | All public endpoints must use HTTPS. | REQ-0023 |
| ReservationAccessControl | safety | isAnonymousUser == false | Anonymous users must be prevented from making reservations. | REQ-0025 |
| UniqueIdentifier | resource | menuItem.identifier == unique | Each menu item must have a unique identifier stored by the system. | REQ-0033 |
| UniqueIdentifierStorage | resource | item.hasUniqueId == true | The system shall store a unique identifier for each item. | REQ-0035 |
| ConcurrentUsers | performance | concurrentUsers >= 5 | The system shall support at least 5 concurrent users. | REQ-0060 |

## Unquantified

Requirements implying a limit with no measurable bound:

- REQ-0017: locally
- REQ-0023: all public endpoints
- REQ-0025: anonymous users
- REQ-0033: menu item
- REQ-0035: item
