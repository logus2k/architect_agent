# Logical Architecture

| Definition | Usage | Attributes | Responsibility | Requirement |
|---|---|---|---|---|
| EmployerRegistration | employerRegistration | registrationStatus: String | Manages the process of new employer sign-up and initial data capture. | REQ-0005 |
| CompanyProfile | companyProfile | companyName: String, contactDetails: String | Stores and manages the detailed information and profile of a registered employer. | REQ-0005 |
| AdministratorAccount | administratorAccount | username: String, passwordHash: String, isActive: Boolean | Manages the credentials and permissions for administrative users. | REQ-0008 |
| SiteManagementAccount | siteManagementAccount | username: String, passwordHash: String, isActive: Boolean | Manages the credentials and permissions for site management users. | REQ-0008 |
| SystemConfiguration | systemConfiguration | configurationData: String | Manages the overall settings and customization options for the system. | REQ-0024 |
| DataManagementService | dataManagementService | dataStore: String | Handles the storage, retrieval, and integrity of all system data. | REQ-0025 |
| BackupManager | backupManager | retentionPolicy: String | Orchestrates the process of creating and maintaining system backups. | REQ-0025 |
| WebApplicationInterface | webApplicationInterface | accessibility: Boolean | Provides the user interface accessible via standard web browsers. | REQ-0030 |
