# Interfaces

| Interface | Port | Ends | Description | Requirement |
|---|---|---|---|---|
| LanguageSwitchingInterface | LanguageSwitchingInterfacePort | supplier=contactForm, consumer=contactForm | Allows the user to change the interface language between Portuguese and English. | REQ-0003 |
| WorkingHoursSettingInterface | WorkingHoursSettingInterfacePort | supplier=tenant, consumer=tenant | Allows a tenant to define its operational hours. | REQ-0005 |
| MapInterface | MapInterfacePort | supplier=tenant, consumer=tenant | Provides access to an open-source mapping solution for visualization. | REQ-0006 |
| AuthenticationInterface | AuthenticationInterfacePort | supplier=tenant, consumer=reservation | The system requires a user to authenticate via Google login to access reservation functionality. | REQ-0007 |
| UserInterfaceRenderingInterface | UserInterfaceRenderingInterfacePort | supplier=tenant, consumer=tenant | Defines the contract for rendering the user interface across different device layouts. | REQ-0008 |
| UserAuthenticationInterface | UserAuthenticationInterfacePort | supplier=tenant, consumer=contactForm | Allows the system to authenticate users using Google OAuth. | REQ-0009 |
| TenantConfigurationManagementInterface | TenantConfigurationManagementInterfacePort | supplier=tenant, consumer=contactForm | Allows the Tenant administrator to view and modify the tenant's specific configurations. | REQ-0010 |
| ImageUploadInterface | ImageUploadInterfacePort | supplier=contactForm, consumer=image | Allows an authorized user to upload an image file to the system. | REQ-0012 |
| AIDescriptionGenerationInterface | AIDescriptionGenerationInterfacePort | supplier=contactForm | The system needs to provide a specified language to the AI description generation service. | REQ-0013 |
| TenantIdentityResolutionInterface | TenantIdentityResolutionInterfacePort | supplier=tenant, consumer=tenant | The system resolves tenant identity based on the path prefix. | REQ-0015 |
| RequestRoutingInterface | RequestRoutingInterfacePort | supplier=tenant, consumer=reservation | Routes incoming requests to the correct tenant's SQLite instance. | REQ-0016 |
| OAuth2AuthenticationInterface | OAuth2AuthenticationInterfacePort | supplier=tenant, consumer=contactForm | Interface for handling Google OAuth2 authentication flow. | REQ-0018 |
| LanguageSelectionInterface | LanguageSelectionInterfacePort | supplier=contactForm, consumer=contactForm | The system needs to receive a language selection to determine the output language. | REQ-0022 |
| HTTPSEnforcementInterface | HTTPSEnforcementInterfacePort | supplier=tenant, consumer=tenant | Enforces that all public endpoints use HTTPS for secure communication. | REQ-0023 |
| ReservationInitiationInterface | ReservationInitiationInterfacePort | supplier=reservation, consumer=tenant | Allows a user to initiate a reservation process. | REQ-0026 |
| AuthenticationInterface | AuthenticationInterfacePort | supplier=tenant, consumer=contactForm | The system requires a user to authenticate via Google login to access reservation functionality. | REQ-0027 |
| RestaurantNameManagementInterface | RestaurantNameManagementInterfacePort | supplier=tenant, consumer=tenant | Allows the Tenant Administrator to manage the restaurant name. | REQ-0029 |
| LogoManagementInterface | LogoManagementInterfacePort | supplier=tenant, consumer=tenant | Allows the Tenant Administrator to manage the restaurant logo. | REQ-0029 |
| ContactInformationManagementInterface | ContactInformationManagementInterfacePort | supplier=tenant, consumer=contactForm | Allows the Tenant Administrator to manage the restaurant contacts. | REQ-0029 |
| WorkhoursManagementInterface | WorkhoursManagementInterfacePort | supplier=tenant | Allows the Tenant Administrator to manage the restaurant workhours. | REQ-0029 |
| CategoryDataProvisionInterface | CategoryDataProvisionInterfacePort | supplier=category, consumer=category | Provides identification, naming, description, and ordering information for a Category. | REQ-0034 |
| MenuDisplayInterface | MenuDisplayInterfacePort | supplier=tenant, consumer=category | The system needs to retrieve the menu associated with a specific tenant. | REQ-0042 |
| LanguageSwitchingInterface | LanguageSwitchingInterfacePort | supplier=contactForm, consumer=contactForm | Allows the user to change the interface language between Portuguese and English. | REQ-0044 |
| MapDisplayInterface | MapDisplayInterfacePort | — | The system needs to display a map using external OpenStreetMap data. | REQ-0047 |
| ReservationSubmissionInterface | ReservationSubmissionInterfacePort | supplier=reservation, consumer=contactForm | Allows the system to submit a reservation form to Google's authenticated users. | REQ-0048 |
| GoogleOAuthAuthenticationInterface | GoogleOAuthAuthenticationInterfacePort | supplier=tenant, consumer=contactForm | Allows the system to authenticate a user via Google OAuth. | REQ-0049 |
| ConfigurationSettingsDashboardAccessInterface | ConfigurationSettingsDashboardAccessInterfacePort | supplier=tenant, consumer=tenant | Provides access to the configuration settings dashboard for a specific tenant's administrator. | REQ-0050 |
| MenuEntityManagementInterface | MenuEntityManagementInterfacePort | supplier=tenant, consumer=tenant | Allows the tenant administrator to perform CRUD operations on restaurant menu entities. | REQ-0051 |
| ImageUploadInterface | ImageUploadInterfacePort | supplier=tenant, consumer=image | Allows an authorized user to upload an image file to the system. | REQ-0052 |
| ReservationSubmissionInterface | ReservationSubmissionInterfacePort | supplier=reservation, consumer=contactForm | Allows the system to submit a reservation form to Google's authenticated users. | REQ-0054 |
| TenantConfigurationInterface | TenantConfigurationInterfacePort | supplier=tenant, consumer=tenant | Allows a tenant administrator to configure the settings specific to a tenant. | REQ-0055 |
| UserAuthenticationInterface | UserAuthenticationInterfacePort | supplier=tenant, consumer=tenant | Allows the system to authenticate users using Google OAuth. | REQ-0062 |
| ManualMenuImageDescriptionInputInterface | ManualMenuImageDescriptionInputInterfacePort | supplier=contactForm, consumer=tenant | Allows manual text input for menu image descriptions when the LLM service is unavailable. | REQ-0063 |

## Unresolved ends

- REQ-0003: The specific component responsible for managing or receiving the language change request is not explicitly named.
- REQ-0006: The specific component that consumes the map interface is not defined.
- REQ-0007: Google login mechanism
- REQ-0008: The specific component responsible for rendering the user interface is not explicitly named, although 'part tenant' is used as a placeholder for the system context.
- REQ-0009: Google OAuth provider
- REQ-0010: The specific interface for the Tenant administrator to interact with the configuration management system is not fully defined.
- REQ-0012: authorized user
- REQ-0013: The component responsible for generating the AI description is not defined.
- REQ-0013: interface AIDescriptionGenerationInterface names unknown consumer 'new_elements'
- REQ-0016: SQLite instance
- REQ-0018: The specific component responsible for initiating or managing the Google OAuth2 flow is not explicitly named, only the requirement to support it is given.
- REQ-0022: The component responsible for returning the description based on the selected language is not explicitly named.
- REQ-0023: The requirement implies a boundary for enforcing HTTPS on public endpoints, but no specific component or element is named as the entity responsible for enforcing or being subject to this protocol requirement.
- REQ-0026: Google-authenticated user
- REQ-0027: Google credentials provider
- REQ-0029: The interface for managing workhours is implied but no specific element is available to represent it.
- REQ-0029: interface WorkhoursManagementInterface names unknown consumer 'new_elements'
- REQ-0042: The specific component responsible for displaying the menu is not named.
- REQ-0044: The requirement implies a mechanism for language selection that affects the entire system interface, but no specific element in KNOWN ELEMENTS is clearly designated as the central 'User Interface' or 'Language Service' component to act as the consumer or supplier for this global setting.
- REQ-0047: The requirement implies a boundary for displaying a map, but no known elements represent the map display component or the OpenStreetMap data source.
- REQ-0047: interface MapDisplayInterface names unknown supplier 'new_elements'
- REQ-0047: interface MapDisplayInterface names unknown consumer 'new_elements'
- REQ-0048: Google's authenticated users
- REQ-0049: The specific component responsible for initiating or handling the Google OAuth flow is not explicitly named, though 'part contactForm' is used as a potential consumer.
- REQ-0050: The specific component providing the 'configuration settings dashboard' is not named.
- REQ-0051: The specific entity representing the 'restaurant's menu' is not defined in KNOWN ELEMENTS.
- REQ-0052: tenant administrator user
- REQ-0054: Google's authenticated users
- REQ-0055: The specific mechanism or component that performs the configuration action is not named.
- REQ-0062: Google OAuth2 service
- REQ-0063: LLM service availability status
