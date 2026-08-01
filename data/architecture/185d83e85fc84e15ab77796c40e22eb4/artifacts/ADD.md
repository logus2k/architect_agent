# Architecture Definition Document — RestaurantMenuManager

## 1. Introduction

This document describes the architecture of RestaurantMenuManager, derived from 60 INCOSE-validated requirements supplied by the Analyst Agent. It is generated from the architecture artifacts and introduces no content of its own.

## 2. Requirements Summary

- Requirements consumed: **60**
- Classified `allocation`: 1
- Classified `constraint`: 6
- Classified `functional`: 51
- Classified `interface`: 30
- Classified `structural`: 4

Source documents:
- `source.md`

## 3. Functional Architecture

| Function | Parent | Description | Requirement |
|---|---|---|---|
| GenerateFoodDescription | — | Creates a textual description based on an input food image. | REQ-0001 |
| DisplayItemImages | — | Shows the images of the items to the user. | REQ-0002 |
| SwitchInterfaceLanguage | — | Allows the user to change the display language between Portuguese and English. | REQ-0003 |
| DiscardContactFormSubmission | — | The system discards the contact form submission after processing. | REQ-0004 |
| SetRestaurantWorkingHours | — | Allows a tenant restaurant to define its operating hours. | REQ-0005 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0007 |
| RenderResponsiveUserInterface | — | The system displays the user interface adapting to different screen sizes. | REQ-0008 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0009 |
| RenderResponsiveUserInterface | — | The system displays the user interface adapting to different screen sizes. | REQ-0010 |
| ManageMenu | — | Allows an authorized user to create, update, or delete a menu. | REQ-0011 |
| AllowUserToUploadImage | — | The system permits an authorized user to upload an image file. | REQ-0012 |
| GenerateFoodDescription | — | Creates a textual description based on an input food image. | REQ-0013 |
| SwitchInterfaceLanguage | — | Allows the user to change the display language between Portuguese and English. | REQ-0013 |
| ConfirmReservation | — | Allows an administrator to manually confirm a reservation. | REQ-0014 |
| ResolveTenantIdentity | — | The system determines the tenant identity based on the provided path prefix. | REQ-0015 |
| ResolveTenantIdentity | — | The system determines the tenant identity based on the provided path prefix. | REQ-0016 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0018 |
| ConfirmReservation | — | Allows an administrator to manually confirm a reservation. | REQ-0019 |
| GenerateFoodDescription | — | Creates a textual description based on an input food image. | REQ-0020 |
| SwitchInterfaceLanguage | — | Allows the user to change the display language between Portuguese and English. | REQ-0022 |
| RenderResponsiveUserInterface | — | The system displays the user interface adapting to different screen sizes. | REQ-0024 |
| DisplayItemImages | RenderResponsiveUserInterface | Shows the images of the items to the user. | REQ-0024 |
| ManageMenu | RenderResponsiveUserInterface | Allows an authorized user to create, update, or delete a menu. | REQ-0024 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0025 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0026 |
| ConfirmReservation | — | Allows an administrator to manually confirm a reservation. | REQ-0026 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0027 |
| ManageMenu | — | Allows an authorized user to create, update, or delete a menu. | REQ-0028 |
| ManageMenu | — | Allows an authorized user to create, update, or delete a menu. | REQ-0029 |
| SetRestaurantWorkingHours | — | Allows a tenant restaurant to define its operating hours. | REQ-0029 |
| ManageMenu | — | Allows an authorized user to create, update, or delete a menu. | REQ-0030 |
| DisplayItemImages | ManageMenu | Shows the images of the items to the user. | REQ-0030 |
| ConfirmReservation | — | Allows an administrator to manually confirm a reservation. | REQ-0031 |
| ManageMenu | — | Allows an authorized user to create, update, or delete a menu. | REQ-0032 |
| AssociateImageIDWithPathMetadata | — | The system links an image ID to its corresponding path metadata. | REQ-0036 |
| ConfirmReservation | — | Allows an administrator to manually confirm a reservation. | REQ-0039 |
| ResolveTenantIdentity | — | The system determines the tenant identity based on the provided path prefix. | REQ-0042 |
| ManageMenu | ResolveTenantIdentity | Allows an authorized user to create, update, or delete a menu. | REQ-0042 |
| DisplayItemImages | ManageMenu | Shows the images of the items to the user. | REQ-0042 |
| DisplayItemImages | — | Shows the images of the items to the user. | REQ-0043 |
| GenerateFoodDescription | — | Creates a textual description based on an input food image. | REQ-0043 |
| SwitchInterfaceLanguage | — | Allows the user to change the display language between Portuguese and English. | REQ-0044 |
| DisplayContactForm | — | The system presents a contact form to the user for a specific tenant. | REQ-0045 |
| SetRestaurantWorkingHours | — | Allows a tenant restaurant to define its operating hours. | REQ-0046 |
| DisplayMapInterface | — | The system displays a map interface using OpenStreetMap data. | REQ-0047 |
| DisplayContactForm | — | The system presents a contact form to the user for a specific tenant. | REQ-0048 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0048 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0049 |
| DisplayConfigurationSettingsDashboard | — | The system presents a dashboard containing configuration settings for the tenant administrator. | REQ-0050 |
| ManageMenu | — | Allows an authorized user to create, update, or delete a menu. | REQ-0051 |
| AllowUserToUploadImage | — | The system permits an authorized user to upload an image file. | REQ-0052 |
| GenerateFoodDescription | — | Creates a textual description based on an input food image. | REQ-0053 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0054 |
| DisplayContactForm | — | The system presents a contact form to the user for a specific tenant. | REQ-0054 |
| DisplayConfigurationSettingsDashboard | — | The system presents a dashboard containing configuration settings for the tenant administrator. | REQ-0055 |
| ResolveTenantIdentity | — | The system determines the tenant identity based on the provided path prefix. | REQ-0056 |
| ResolveTenantIdentity | — | The system determines the tenant identity based on the provided path prefix. | REQ-0057 |
| GenerateFoodDescription | — | Creates a textual description based on an input food image. | REQ-0058 |
| ResolveTenantIdentity | — | The system determines the tenant identity based on the provided path prefix. | REQ-0059 |
| ConfirmReservation | — | Allows an administrator to manually confirm a reservation. | REQ-0059 |
| RequireGoogleAuthentication | — | The system must enforce Google login before granting access to reservation features. | REQ-0062 |
| AllowUserToUploadImage | ManageMenu | The system permits an authorized user to upload an image file. | REQ-0063 |
| GenerateFoodDescription | ManageMenu | Creates a textual description based on an input food image. | REQ-0063 |
| SwitchInterfaceLanguage | — | Allows the user to change the display language between Portuguese and English. | REQ-0065 |

## 4. Logical Architecture

| Definition | Usage | Attributes | Responsibility | Requirement |
|---|---|---|---|---|
| Category | category | id: String, name: String, description: String, order: Integer | Represents a distinct grouping entity within the system. | REQ-0034 |
| Image | image | description: String, itemId: String, languageElement: String, generatedText: String, approvedFlag: Boolean, timestamp: String | Stores the metadata and content associated with an image. | REQ-0037 |
| Reservation | reservation | id: String, userGoogleId: String, tenantId: String, dateTime: String, numberOfPeople: Integer, status: String, timestamp: String, notes: String | Stores the details and state of a booking. | REQ-0038 |
| Tenant | tenant | — | Represents an entity that requires a contact form. | REQ-0045 |
| ContactForm | contactForm | — | Provides the interface and mechanism for users to submit contact information for a tenant. | REQ-0045 |

## 5. Interfaces

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

## 6. Behavior

_None produced._

## 7. Constraints

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

## 8. Allocation

| Function | Component | Rationale | Requirement |
|---|---|---|---|
| ResolveTenantIdentity | tenant | Resolving tenant identity is necessary to route requests to the correct tenant's SQLite records. | REQ-0057 |

## Unallocated

- REQ-0057: ManageMenu

## 9. Verification Approach

| Requirement | Method | Success criterion | Elements |
|---|---|---|---|
| REQ-0001 | demonstration | The system successfully returns a non-empty string in the 'generatedText' attribute after processing a valid food image. | action def GenerateFoodDescription, part def Image, attribute generatedText |
| REQ-0002 | demonstration | When a user navigates to a page displaying item details, all associated item images are visible on the screen. | action def DisplayItemImages |
| REQ-0003 | demonstration | The user interface successfully switches between Portuguese and English when the language switching mechanism is invoked. | action def SwitchInterfaceLanguage, interface def LanguageSwitchingInterface |
| REQ-0004 | demonstration | After a user submits the contact form, the system confirms the submission was processed and the associated data is no longer retrievable or actionable by subsequent requests. | action def DiscardContactFormSubmission, part def ContactForm |
| REQ-0005 | demonstration | The system successfully updates and displays the specified working hours for a tenant restaurant upon administrator input. | action def SetRestaurantWorkingHours, port def WorkingHoursSettingInterface |
| REQ-0006 | demonstration | The map interface successfully displays a map using OpenStreetMap data when accessed by a user. | action def DisplayMapInterface, interface def MapDisplayInterface, interface def MapInterface |
| REQ-0007 | test | Attempting to access any reservation-related endpoint without a valid Google authentication token results in a 401 Unauthorized response. | action def RequireGoogleAuthentication, interface def AuthenticationInterface, interface def GoogleOAuthAuthenticationInterface, interface def UserAuthenticationInterface |
| REQ-0008 | demonstration | The user interface renders correctly and is fully usable when viewed on both a standard desktop screen size (e.g., 1920x1080) and a standard mobile screen size (e.g., 375x667). | action def RenderResponsiveUserInterface |
| REQ-0009 | demonstration | A user can successfully log in using Google credentials and gain access to reservation features. | action def RequireGoogleAuthentication, interface def GoogleOAuthAuthenticationInterface, interface def UserAuthenticationInterface |
| REQ-0010 | demonstration | The system successfully displays the configuration settings dashboard for a specified tenant administrator, and the administrator can modify at least one configuration setting. | action def DisplayConfigurationSettingsDashboard, interface def ConfigurationSettingsDashboardAccessInterface |
| REQ-0011 | demonstration | An authorized user successfully performs at least one create, one update, and one delete operation on a menu entity without system errors. | action def ManageMenu |
| REQ-0012 | demonstration | An authorized user successfully uploads an image file via the ImageUploadInterface, and the system confirms successful storage. | action def AllowUserToUploadImage, interface def ImageUploadInterface |
| REQ-0013 | demonstration | The system successfully generates an AI description using the specified language parameter for at least one test case. | action def GenerateFoodDescription, interface def AIDescriptionGenerationInterface |
| REQ-0014 | demonstration | An administrator successfully calls the ConfirmReservation action, and the status attribute of the associated reservation changes from 'Pending' to 'Confirmed'. | action def ConfirmReservation, part def Reservation, attribute status |
| REQ-0015 | test | The system successfully resolves the tenant identity to the correct tenantId when provided with a valid path prefix. | action def ResolveTenantIdentity, interface def TenantIdentityResolutionInterface, port def TenantIdentityResolutionInterfacePort, part tenant |
| REQ-0016 | test | When a request is made to a specific tenant path prefix, the system successfully routes the request to the corresponding tenant's SQLite instance without error. | action def ResolveTenantIdentity, interface def RequestRoutingInterface, port def RequestRoutingInterfacePort |
| REQ-0017 | inspection | The system configuration and code structure explicitly mandate that all asset storage operations utilize local storage mechanisms, as verified by examining the relevant code modules. | constraint def AssetStorageLocation |
| REQ-0018 | demonstration | A user can successfully log in and gain access to reservation features using Google OAuth2. | action def RequireGoogleAuthentication, interface def GoogleOAuthAuthenticationInterface, interface def OAuth2AuthenticationInterface, port def GoogleOAuthAuthenticationInterfacePort, port def OAuth2AuthenticationInterfacePort |
| REQ-0019 | demonstration | An administrator successfully calls the ConfirmReservation action, and the status attribute of the target reservation changes from 'Pending' to 'Confirmed'. | action def ConfirmReservation, part def Reservation, attribute status |
| REQ-0020 | demonstration | The system successfully generates a textual description for a provided image, and the generated text is present in the 'generatedText' attribute. | action def GenerateFoodDescription, part def Image, attribute generatedText |
| REQ-0022 | test | When the language selection is set to 'PT', the generated text must be in Portuguese; when the language selection is set to 'EN', the generated text must be in English. | action def GenerateFoodDescription, interface def AIDescriptionGenerationInterface, interface def LanguageSelectionInterface, attribute generatedText |
| REQ-0023 | inspection | All public endpoints are configured to require HTTPS. | constraint def HTTPSEnforcement, interface def HTTPSEnforcementInterface |
| REQ-0024 | demonstration | A user without authentication credentials can successfully view the menu content for any tenant. | action def DisplayMenuInterface |
| REQ-0025 | test | When an unauthenticated user attempts to call the ReservationInitiationInterface, the system must return an HTTP 401 Unauthorized status code. | action def ReservationInitiationInterface |
| REQ-0026 | demonstration | A user successfully completes the reservation process, resulting in a reservation record with status 'Confirmed' or 'Pending' in the system. | action def RequireGoogleAuthentication, action def ReservationInitiationInterface, action def ReservationSubmissionInterface, part def Reservation, interface def GoogleOAuthAuthenticationInterface, interface def ReservationInitiationInterface |
| REQ-0027 | demonstration | A Tenant administrator successfully logs in using valid Google credentials and is redirected to a protected area of the application. | action def AllowUserToUploadImage, action def DisplayConfigurationSettingsDashboard, interface def GoogleOAuthAuthenticationInterface, interface def UserAuthenticationInterface, port def GoogleOAuthAuthenticationInterfacePort, port def UserAuthenticationInterfacePort |
| REQ-0028 | demonstration | The Tenant Administrator successfully updates an existing menu item, and the change is reflected in the menu display. | action def ManageMenu, interface def MenuEntityManagementInterface |
| REQ-0029 | demonstration | The Tenant Administrator successfully updates the restaurant name, logo, contact information, and working hours via the respective management interfaces. | action def RestaurantNameManagementInterface, action def LogoManagementInterface, action def ContactInformationManagementInterface, action def WorkhoursManagementInterface |
| REQ-0030 | demonstration | The Tenant Administrator can successfully upload, view, update, and delete images associated with a menu item via the system interface. | action def ManageMenu, action def AllowUserToUploadImage, action def DisplayItemImages, interface def MenuEntityManagementInterface, interface def ImageUploadInterface |
| REQ-0031 | demonstration | The system successfully allows an administrator to change the status of a reservation from pending to confirmed or rejected via the administrative interface. | action def ConfirmReservation |
| REQ-0032 | demonstration | The Tenant Administrator successfully navigates to the configuration settings dashboard and modifies at least one configurable setting for the tenant. | action def DisplayConfigurationSettingsDashboard, action def TenantConfigurationManagementInterface |
| REQ-0033 | inspection | The data model for menu items includes a field designated as a unique identifier, and the persistence layer logic confirms that this field is populated and unique for every new menu item record. | attribute id, constraint def UniqueIdentifierStorage |
| REQ-0034 | inspection | The data model for 'part def Category' includes fields corresponding to id, name, description, and order. | part def Category |
| REQ-0035 | inspection | The data model for menu items includes a field designated as a unique identifier, and the persistence layer logic ensures this field is populated and unique for every new item record. | attribute id, constraint def UniqueIdentifierStorage |
| REQ-0036 | inspection | The system's internal data structure or code logic explicitly shows a successful call to action def AssociateImageIDWithPathMetadata, linking an image ID to its path metadata. | action def AssociateImageIDWithPathMetadata |
| REQ-0037 | inspection | The data model for 'part def Image' must contain fields corresponding to description, itemId, languageElement, generatedText, approvedFlag, and timestamp. | part def Image |
| REQ-0038 | inspection | The data model for 'part def Reservation' includes fields corresponding to id, user_google_id, tenant_id, dateTime, numberOfPeople, status, timestamp, and notes. | part def Reservation, attribute id, attribute userGoogleId, attribute tenantId, attribute dateTime, attribute numberOfPeople, attribute status, attribute timestamp, attribute notes |
| REQ-0039 | demonstration | The system successfully updates the status of a reservation to 'Confirmed' when the ConfirmReservation action is executed by an administrator. | action def ConfirmReservation |
| REQ-0042 | demonstration | When a user requests the menu for a specific tenant ID, the system successfully displays the menu data retrieved from the MenuDisplayInterface. | action def DisplayItemImages, action def MenuDisplayInterface, interface def MenuDisplayInterface, part def Tenant |
| REQ-0043 | demonstration | When a user selects a restaurant, the system successfully displays all associated menu images and their corresponding descriptions on the user interface. | action def DisplayItemImages, action def DisplayMenuInterface |
| REQ-0044 | demonstration | The user interface successfully switches between Portuguese and English when the language switching mechanism is invoked. | action def SwitchInterfaceLanguage, interface def LanguageSwitchingInterface |
| REQ-0045 | demonstration | For every tenant, the system successfully displays the contact form interface to the user. | action def DisplayContactForm |
| REQ-0046 | demonstration | The system successfully updates and displays the restaurant's operating hours after an administrator uses the WorkhoursManagementInterface. | action def SetRestaurantWorkingHours, action def DisplayConfigurationSettingsDashboard, interface def WorkhoursManagementInterface |
| REQ-0047 | demonstration | The map interface displays a recognizable map rendered using OpenStreetMap data when accessed. | action def DisplayMapInterface, interface def MapDisplayInterface, interface def MapInterface |
| REQ-0048 | demonstration | A user successfully accesses the reservation form and submits it while authenticated via Google. | action def DisplayContactForm, action def ReservationInitiationInterface, action def ReservationSubmissionInterface, interface def ReservationInitiationInterface, interface def ReservationSubmissionInterface, interface def UserAuthenticationInterface |
| REQ-0049 | demonstration | A user successfully authenticates via Google OAuth and gains access to reservation features. | action def RequireGoogleAuthentication, interface def GoogleOAuthAuthenticationInterface, interface def OAuth2AuthenticationInterface, port def GoogleOAuthAuthenticationInterfacePort, port def OAuth2AuthenticationInterfacePort |
| REQ-0050 | demonstration | The system successfully displays the configuration settings dashboard for a given tenant administrator upon request. | action def DisplayConfigurationSettingsDashboard, interface def ConfigurationSettingsDashboardAccessInterface |
| REQ-0051 | demonstration | The system successfully allows an authorized tenant administrator to perform at least one create, one update, and one delete operation on a menu entity, and the changes are persisted and visible upon subsequent retrieval. | action def ManageMenu, interface def MenuEntityManagementInterface |
| REQ-0052 | demonstration | The system successfully processes an image file upload request from an authorized tenant administrator, resulting in the creation of an Image entity with a non-null ID and associated metadata. | action def AllowUserToUploadImage, interface def ImageUploadInterface, part def Image |
| REQ-0053 | demonstration | The system successfully generates a textual description for a provided image using the LLM service, and the generated text is present in the 'generatedText' attribute. | action def GenerateFoodDescription, interface def AIDescriptionGenerationInterface, attribute generatedText |
| REQ-0054 | demonstration | A user successfully submits a reservation using the system after authenticating via Google. | action def ReservationSubmissionInterface, action def RequireGoogleAuthentication, interface def GoogleOAuthAuthenticationInterface, interface def ReservationSubmissionInterface |
| REQ-0055 | demonstration | The system successfully displays and allows modification of all configurable tenant settings via the Tenant Configuration Management Interface. | action def DisplayConfigurationSettingsDashboard, action def TenantConfigurationManagementInterface, interface def TenantConfigurationManagementInterface |
| REQ-0056 | analysis | The system successfully resolves the tenant's name by querying the tenant's address data structure, resulting in a non-null tenant name. | part tenant |
| REQ-0057 | inspection | The RequestRoutingInterface implementation correctly routes all incoming requests to the tenant-specific SQLite instance based on the provided path prefix. | action def ResolveTenantIdentity, interface def RequestRoutingInterface, interface def TenantIdentityResolutionInterface |
| REQ-0058 | demonstration | The system successfully generates a textual description for a provided food image using the LLM service, and the generated text is present in the 'generatedText' attribute. | action def GenerateFoodDescription, interface def AIDescriptionGenerationInterface, attribute generatedText, part def Image |
| REQ-0059 | inspection | The data model for 'part def Reservation' includes a field that reliably stores a stable address associated with the reservation. | part def Reservation |
| REQ-0060 | test | The system successfully handles 5 or more concurrent user sessions without performance degradation or failure. | constraint def ConcurrentUsers |
| REQ-0062 | demonstration | A user successfully logs into the system using Google OAuth2 and gains access to reservation features. | action def RequireGoogleAuthentication, interface def GoogleOAuthAuthenticationInterface, interface def OAuth2AuthenticationInterface, interface def UserAuthenticationInterface |
| REQ-0063 | demonstration | When the LLM service is simulated as unavailable, the system successfully allows a user to input a text description for a menu image via the ManualMenuImageDescriptionInputInterface, and this description is saved with the image metadata. | action def ManualMenuImageDescriptionInputInterface |
| REQ-0065 | demonstration | The system successfully displays all user-facing text elements in both Portuguese (PT) and English (EN) when the language is switched via the LanguageSwitchingInterface. | action def SwitchInterfaceLanguage, interface def LanguageSwitchingInterface |

## 10. Traceability

| Requirement | Status | Text | Elements | Architecture elements |
|---|---|---|---|---|
| REQ-0001 | edited | **refined** — source document wording differs | 1 | action def GenerateFoodDescription |
| REQ-0002 | edited | **refined** — source document wording differs | 1 | action def DisplayItemImages |
| REQ-0003 | edited | **refined** — source document wording differs | 3 | action def SwitchInterfaceLanguage, interface def LanguageSwitchingInterface, port def LanguageSwitchingInterfacePort |
| REQ-0004 | edited | **refined** — source document wording differs | 1 | action def DiscardContactFormSubmission |
| REQ-0005 | edited | **refined** — source document wording differs | 3 | action def SetRestaurantWorkingHours, interface def WorkingHoursSettingInterface, port def WorkingHoursSettingInterfacePort |
| REQ-0006 | edited | **refined** — source document wording differs | 2 | interface def MapInterface, port def MapInterfacePort |
| REQ-0007 | edited | **refined** — source document wording differs | 3 | action def RequireGoogleAuthentication, interface def AuthenticationInterface, port def AuthenticationInterfacePort |
| REQ-0008 | edited | **refined** — source document wording differs | 3 | action def RenderResponsiveUserInterface, interface def UserInterfaceRenderingInterface, port def UserInterfaceRenderingInterfacePort |
| REQ-0009 | edited | **refined** — source document wording differs | 3 | action def RequireGoogleAuthentication, interface def UserAuthenticationInterface, port def UserAuthenticationInterfacePort |
| REQ-0010 | edited | **refined** — source document wording differs | 3 | action def RenderResponsiveUserInterface, interface def TenantConfigurationManagementInterface, port def TenantConfigurationManagementInterfacePort |
| REQ-0011 | edited | **refined** — source document wording differs | 1 | action def ManageMenu |
| REQ-0012 | edited | **refined** — source document wording differs | 3 | action def AllowUserToUploadImage, interface def ImageUploadInterface, port def ImageUploadInterfacePort |
| REQ-0013 | edited | **refined** — source document wording differs | 4 | action def GenerateFoodDescription, action def SwitchInterfaceLanguage, interface def AIDescriptionGenerationInterface, port def AIDescriptionGenerationInterfacePort |
| REQ-0014 | edited | **refined** — source document wording differs | 1 | action def ConfirmReservation |
| REQ-0015 | edited | **refined** — source document wording differs | 3 | action def ResolveTenantIdentity, interface def TenantIdentityResolutionInterface, port def TenantIdentityResolutionInterfacePort |
| REQ-0016 | edited | **refined** — source document wording differs | 3 | action def ResolveTenantIdentity, interface def RequestRoutingInterface, port def RequestRoutingInterfacePort |
| REQ-0017 | edited | **refined** — source document wording differs | 1 | constraint def AssetStorageLocation |
| REQ-0018 | edited | **refined** — source document wording differs | 3 | action def RequireGoogleAuthentication, interface def OAuth2AuthenticationInterface, port def OAuth2AuthenticationInterfacePort |
| REQ-0019 | edited | **refined** — source document wording differs | 1 | action def ConfirmReservation |
| REQ-0020 | edited | **refined** — source document wording differs | 1 | action def GenerateFoodDescription |
| REQ-0022 | edited | **refined** — source document wording differs | 3 | action def SwitchInterfaceLanguage, interface def LanguageSelectionInterface, port def LanguageSelectionInterfacePort |
| REQ-0023 | edited | **refined** — source document wording differs | 3 | constraint def HTTPSEnforcement, interface def HTTPSEnforcementInterface, port def HTTPSEnforcementInterfacePort |
| REQ-0024 | edited | **refined** — source document wording differs | 3 | action def DisplayItemImages, action def ManageMenu, action def RenderResponsiveUserInterface |
| REQ-0025 | edited | **refined** — source document wording differs | 2 | action def RequireGoogleAuthentication, constraint def ReservationAccessControl |
| REQ-0026 | edited | **refined** — source document wording differs | 4 | action def ConfirmReservation, action def RequireGoogleAuthentication, interface def ReservationInitiationInterface, port def ReservationInitiationInterfacePort |
| REQ-0027 | edited | **refined** — source document wording differs | 3 | action def RequireGoogleAuthentication, interface def AuthenticationInterface, port def AuthenticationInterfacePort |
| REQ-0028 | edited | **refined** — source document wording differs | 1 | action def ManageMenu |
| REQ-0029 | edited | **refined** — source document wording differs | 10 | action def ManageMenu, action def SetRestaurantWorkingHours, interface def ContactInformationManagementInterface, interface def LogoManagementInterface, interface def RestaurantNameManagementInterface, interface def WorkhoursManagementInterface, port def ContactInformationManagementInterfacePort, port def LogoManagementInterfacePort, port def RestaurantNameManagementInterfacePort, port def WorkhoursManagementInterfacePort |
| REQ-0030 | edited | **refined** — source document wording differs | 2 | action def DisplayItemImages, action def ManageMenu |
| REQ-0031 | edited | **refined** — source document wording differs | 1 | action def ConfirmReservation |
| REQ-0032 | edited | **refined** — source document wording differs | 1 | action def ManageMenu |
| REQ-0033 | edited | **refined** — source document wording differs | 1 | constraint def UniqueIdentifier |
| REQ-0034 | edited | **refined** — source document wording differs | 8 | attribute description, attribute id, attribute name, attribute order, interface def CategoryDataProvisionInterface, part category, part def Category, port def CategoryDataProvisionInterfacePort |
| REQ-0035 | edited | **refined** — source document wording differs | 1 | constraint def UniqueIdentifierStorage |
| REQ-0036 | edited | **refined** — source document wording differs | 1 | action def AssociateImageIDWithPathMetadata |
| REQ-0037 | edited | **refined** — source document wording differs | 8 | attribute approvedFlag, attribute description, attribute generatedText, attribute itemId, attribute languageElement, attribute timestamp, part def Image, part image |
| REQ-0038 | edited | **refined** — source document wording differs | 10 | attribute dateTime, attribute id, attribute notes, attribute numberOfPeople, attribute status, attribute tenantId, attribute timestamp, attribute userGoogleId, part def Reservation, part reservation |
| REQ-0039 | edited | **refined** — source document wording differs | 1 | action def ConfirmReservation |
| REQ-0042 | edited | **refined** — source document wording differs | 5 | action def DisplayItemImages, action def ManageMenu, action def ResolveTenantIdentity, interface def MenuDisplayInterface, port def MenuDisplayInterfacePort |
| REQ-0043 | edited | **refined** — source document wording differs | 2 | action def DisplayItemImages, action def GenerateFoodDescription |
| REQ-0044 | edited | **refined** — source document wording differs | 3 | action def SwitchInterfaceLanguage, interface def LanguageSwitchingInterface, port def LanguageSwitchingInterfacePort |
| REQ-0045 | edited | **refined** — source document wording differs | 5 | action def DisplayContactForm, part contactForm, part def ContactForm, part def Tenant, part tenant |
| REQ-0046 | edited | **refined** — source document wording differs | 1 | action def SetRestaurantWorkingHours |
| REQ-0047 | edited | **refined** — source document wording differs | 3 | action def DisplayMapInterface, interface def MapDisplayInterface, port def MapDisplayInterfacePort |
| REQ-0048 | edited | **refined** — source document wording differs | 4 | action def DisplayContactForm, action def RequireGoogleAuthentication, interface def ReservationSubmissionInterface, port def ReservationSubmissionInterfacePort |
| REQ-0049 | edited | **refined** — source document wording differs | 3 | action def RequireGoogleAuthentication, interface def GoogleOAuthAuthenticationInterface, port def GoogleOAuthAuthenticationInterfacePort |
| REQ-0050 | edited | **refined** — source document wording differs | 3 | action def DisplayConfigurationSettingsDashboard, interface def ConfigurationSettingsDashboardAccessInterface, port def ConfigurationSettingsDashboardAccessInterfacePort |
| REQ-0051 | edited | **refined** — source document wording differs | 3 | action def ManageMenu, interface def MenuEntityManagementInterface, port def MenuEntityManagementInterfacePort |
| REQ-0052 | edited | **refined** — source document wording differs | 3 | action def AllowUserToUploadImage, interface def ImageUploadInterface, port def ImageUploadInterfacePort |
| REQ-0053 | edited | **refined** — source document wording differs | 1 | action def GenerateFoodDescription |
| REQ-0054 | edited | **refined** — source document wording differs | 4 | action def DisplayContactForm, action def RequireGoogleAuthentication, interface def ReservationSubmissionInterface, port def ReservationSubmissionInterfacePort |
| REQ-0055 | edited | **refined** — source document wording differs | 3 | action def DisplayConfigurationSettingsDashboard, interface def TenantConfigurationInterface, port def TenantConfigurationInterfacePort |
| REQ-0056 | edited | **refined** — source document wording differs | 1 | action def ResolveTenantIdentity |
| REQ-0057 | edited | **refined** — source document wording differs | 1 | action def ResolveTenantIdentity |
| REQ-0058 | edited | **refined** — source document wording differs | 1 | action def GenerateFoodDescription |
| REQ-0059 | edited | **refined** — source document wording differs | 2 | action def ConfirmReservation, action def ResolveTenantIdentity |
| REQ-0060 | edited | **refined** — source document wording differs | 1 | constraint def ConcurrentUsers |
| REQ-0062 | edited | **refined** — source document wording differs | 3 | action def RequireGoogleAuthentication, interface def UserAuthenticationInterface, port def UserAuthenticationInterfacePort |
| REQ-0063 | edited | **refined** — source document wording differs | 4 | action def AllowUserToUploadImage, action def GenerateFoodDescription, interface def ManualMenuImageDescriptionInputInterface, port def ManualMenuImageDescriptionInputInterfacePort |
| REQ-0065 | edited | **refined** — source document wording differs | 1 | action def SwitchInterfaceLanguage |

## 11. Assumptions and Open Issues

- 60 requirement(s) were refined upstream; the architecture derives from the rewritten text, not the source document wording: REQ-0001, REQ-0002, REQ-0003, REQ-0004, REQ-0005, REQ-0006, REQ-0007, REQ-0008 ...
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
- REQ-0017: locally
- REQ-0023: all public endpoints
- REQ-0025: anonymous users
- REQ-0033: menu item
- REQ-0035: item
- REQ-0057: ManageMenu
- [DEFECT] constraint UniqueIdentifierStorage (REQ-0035): The requirement asks that a unique identifier *is stored* for each item, but the generated constraint only asserts that the item *has* a unique ID, which doesn't guarantee storage or uniqueness. Suggested: constraint UniqueIdentifierStorage: item.id is unique and not null
- [DEFECT] allocation ResolveTenantIdentity->tenant (REQ-0057): The requirement states that *every request* must be routed to manage the tenant's SQLite records, but the generated element only specifies that a function to resolve tenant identity is performed by the tenant component, which is insufficient. Suggested: The element should specify the routing mechanism or the component responsible for managing the SQLite records for every request.

### Known limitations of this generator

- Semantic review is performed by a judge agent; anything it marks wrong or cannot decide is listed above for human sign-off. An empty list means the judge approved, not that a human did.
- Diagram review, where present, is advisory: it does not gate the build.
- Element names are assigned by the symbol registry, not by the model, so they are stable across regeneration.
