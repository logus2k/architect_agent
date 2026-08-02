# Architecture — by Aspect

## Tenant Administration

_Manages tenant-specific configurations, menus, items, images, and reservations via a dedicated admin dashboard._

**Components:** Tenant, TenantConfiguration, TenantAsset

**Interfaces:** TenantAdminInterface, ReservationManagementInterface

**Consumes:** authentication, data-management, media, multi-tenancy, FoodImage, Item, Menu, Reservation

## Menu & Item Catalog

_Handles the structure and display of food items, categories, and menus, including image and description presentation._

**Components:** Menu, Category, Item, FoodImage

**Interfaces:** MenuDisplayInterface, MenuManagementInterface, AssetUploadInterface

**Consumes:** multi-tenancy, authentication, data-model

## Reservations

_Manages the process of booking tables, from user submission through to manual administrative confirmation._

**Components:** Reservation

**Interfaces:** ReservationSubmissionInterface, ReservationManagementInterface

**Consumes:** authentication, user-input, data-model, multi-tenancy

## User & Access Control

_Implements user authentication via Google OAuth and manages access levels for anonymous and authenticated users._

**Components:** User, UserGoogleId

**Interfaces:** AuthenticationInterface, AccessControlInterface

**Consumes:** authentication, security, anonymous

## AI Content Generation

_Integrates LLM vision capabilities to generate and manage localized descriptions for food items from images._

**Components:** AiDescription

**Interfaces:** DescriptionGenerationInterface, DescriptionPersistenceInterface

**Consumes:** LLM, Language, Timestamp, data-management, vision, FoodImage, Item

## System Infrastructure

_Manages cross-cutting concerns like multi-tenancy routing, storage, localization, and responsive design._

**Components:** SQLiteInstance

**Interfaces:** TenantRoutingInterface, LocalizationInterface, AssetStorageInterface, MapDisplayInterface

**Consumes:** multi-tenancy, localization, storage, responsiveness, security, data-management, api, TenantAsset, TenantConfiguration
