# Interfaces

| Interface | Port | Ends | Description | Requirement |
|---|---|---|---|---|
| ExternalJobDataSynchronizationInterface | ExternalJobDataSynchronizationInterfacePort | supplier=contentDeliveryService, consumer=jobPosting | Allows synchronization of job data with external job sites. | REQ-0017 |
| GovernmentalDatabaseDataExchangeInterface | GovernmentalDatabaseDataExchangeInterfacePort | supplier=webApplicationInterface | Provides an API for exchanging data with external governmental databases. | REQ-0018 |
| WebApplicationAccessInterface | WebApplicationAccessInterfacePort | supplier=webApplicationInterface, consumer=networkInfrastructure | Provides the entry point for users to access the web-based application. | REQ-0030 |
| WebInterfacePresentation | WebInterfacePresentationPort | supplier=webApplicationInterface, consumer=userProfile | Provides the responsive interface for users to access the system. | REQ-0031 |
| IntegrationWithMoLSystem | IntegrationWithMoLSystemPort | supplier=webApplicationInterface | Interface to connect with the existing MoL system. | REQ-0036 |
| IntegrationWithPEFSystem | IntegrationWithPEFSystemPort | supplier=webApplicationInterface | Interface to connect with the existing PEF system. | REQ-0036 |
| WebAccessibilityInterface | WebAccessibilityInterfacePort | supplier=webApplicationInterface, consumer=webApplicationInterface | Provides the interface through which users can access the system using standard web browsers. | REQ-0038 |
| ContextSensitiveHelpProvisionInterface | ContextSensitiveHelpProvisionInterfacePort | supplier=webApplicationInterface, consumer=dashboard | Provides help documentation relevant to the current system function being used. | REQ-0050 |
| LoginTrackingInterface | LoginTrackingInterfacePort | supplier=loginTracker, consumer=dashboard | Provides current login counts and session information for the dashboard. | REQ-0063 |
| UserProfileRetrievalInterface | UserProfileRetrievalInterfacePort | supplier=userProfile, consumer=dashboard | Allows the dashboard to retrieve user profiles based on session information. | REQ-0063 |
| UserProfileManagementInterface | UserProfileManagementInterfacePort | supplier=userProfile, consumer=webApplicationInterface | Allows users to register and manage their personal profiles. | REQ-0065 |
| EmployerRegistrationInterface | EmployerRegistrationInterfacePort | supplier=employerRegistration, consumer=webApplicationInterface | Allows employers to register and manage their organizational profiles. | REQ-0065 |
| NotificationInterface | NotificationInterfacePort | supplier=notificationCenter, consumer=webApplicationInterface | Provides mechanisms for sending notifications to users or systems. | REQ-0068 |
| MessagingInterface | MessagingInterfacePort | supplier=notificationCenter, consumer=smsDeliveryTracker | Handles the delivery and tracking of messages. | REQ-0068 |
| CompanyProfileManagementInterface | CompanyProfileManagementInterfacePort | supplier=companyProfile, consumer=webApplicationInterface | Interface for managing the company profile data. | REQ-0069 |
| JobListingBrowsingInterface | JobListingBrowsingInterfacePort | supplier=jobPosting, consumer=webApplicationInterface | Allows guest users to view job listings with basic filtering capabilities. | REQ-0070 |
| JobApplicationInitiationInterface | JobApplicationInitiationInterfacePort | supplier=webApplicationInterface, consumer=jobPosting | Triggers a prompt for guest users to register or log in when applying for a job. | REQ-0071 |
| ListingSavingInterface | ListingSavingInterfacePort | supplier=webApplicationInterface, consumer=favoritesManager | Triggers a prompt for guest users to register or log in when attempting to save job listings. | REQ-0071 |
| NotificationSubscriptionInterface | NotificationSubscriptionInterfacePort | supplier=webApplicationInterface, consumer=notificationCenter | Triggers a prompt for guest users to register or log in when subscribing to notifications. | REQ-0071 |
| JobPostingDisplayInterface | JobPostingDisplayInterfacePort | supplier=jobPosting, consumer=webApplicationInterface | Provides the latest job postings to the user interface. | REQ-0073 |
| FeaturedOpportunitiesDisplayInterface | FeaturedOpportunitiesDisplayInterfacePort | supplier=jobPosting, consumer=webApplicationInterface | Provides featured opportunities data to the user interface. | REQ-0073 |
| CareerAdviceNewsDisplayInterface | CareerAdviceNewsDisplayInterfacePort | supplier=technicalDocumentationRepository, consumer=webApplicationInterface | Provides relevant sector-based news or career advice to the user interface. | REQ-0073 |
| MultilingualContentProvisionInterface | MultilingualContentProvisionInterfacePort | supplier=contentDeliveryService, consumer=webApplicationInterface | Provides localized content for different languages like Arabic and English. | REQ-0075 |
| AIProcessingInterfaceForLanguageSpecificFunctions | AIProcessingInterfaceForLanguageSpecificFunctionsPort | supplier=nlpEngine, consumer=aiProcessingInfrastructure | Allows AI functions and techniques to be utilized based on the input language. | REQ-0075 |
| DisplayJobPostingsOnHomepage | DisplayJobPostingsOnHomepagePort | supplier=jobPosting, consumer=webApplicationInterface | Provides the latest job postings data for display on the homepage. | REQ-0078 |
| DisplayFeaturedOpportunitiesOnHomepage | DisplayFeaturedOpportunitiesOnHomepagePort | supplier=jobPosting, consumer=webApplicationInterface | Provides data for featured opportunities to be displayed on the homepage. | REQ-0078 |
| DisplaySectorBasedNewsAdviceOnHomepage | DisplaySectorBasedNewsAdviceOnHomepagePort | supplier=technicalDocumentationRepository, consumer=webApplicationInterface | Provides relevant sector-based news or career advice content for the homepage. | REQ-0078 |
| ExternalJobSiteIntegrationInterface | ExternalJobSiteIntegrationInterfacePort | supplier=contentDeliveryService, consumer=webApplicationInterface | Interface to communicate with external job sites for job posting and searching. | REQ-0084 |
| InterfaceDocumentationSpecificationInterface | InterfaceDocumentationSpecificationInterfacePort | supplier=webApplicationInterface, consumer=systemConfiguration | Defines the required structure and detail level for documenting all software interfaces. | REQ-0087 |
| WebAccessInterface | WebAccessInterfacePort | supplier=webApplicationInterface, consumer=networkInfrastructure | Provides HTTP/HTTPS access to the web application. | REQ-0089 |
| RealTimeNotificationInterface | RealTimeNotificationInterfacePort | supplier=notificationCenter, consumer=webApplicationInterface | Provides a mechanism for real-time data push, likely via WebSockets. | REQ-0090 |
| EmailSendingInterface | EmailSendingInterfacePort | supplier=emailTemplateManager, consumer=webApplicationInterface | Allows components to send emails using SMTP. | REQ-0091 |
| SMSNotificationInterface | SMSNotificationInterfacePort | supplier=smsDeliveryTracker, consumer=notificationCenter | Handles the sending of SMS notifications to users. | REQ-0092 |
| DataExchangeInterface | DataExchangeInterfacePort | supplier=webApplicationInterface, consumer=dataManagementService | Defines the format for data exchange between components. | REQ-0094 |
| LegacySystemIntegrationInterface | LegacySystemIntegrationInterfacePort | supplier=webApplicationInterface | Interface to handle XML data exchange with a legacy system. | REQ-0097 |
| SecureCommunicationInterface | SecureCommunicationInterfacePort | supplier=webApplicationInterface, consumer=networkInfrastructure | Ensures all communications between components are secured using encryption and authentication. | REQ-0099 |
| DataMigrationInterfaceFromLegacySystems | DataMigrationInterfaceFromLegacySystemsPort | supplier=dataManagementService, consumer=dataManagementService | This interface facilitates the transfer of existing data from MoL and PEF systems into the new platform. | REQ-0101 |
| UITextProvisionInterface | UITextProvisionInterfacePort | supplier=contentDeliveryService, consumer=webApplicationInterface | Provides localized text strings to the user interface components. | REQ-0109 |
| LanguageVariationSupportInterface | LanguageVariationSupportInterfacePort | supplier=webApplicationInterface, consumer=userProfile | Allows components to request or provide language-specific content or settings. | REQ-0114 |
| ContentDeliveryInterface | ContentDeliveryInterfacePort | supplier=contentDeliveryService, consumer=webApplicationInterface | Allows retrieval of region-specific content. | REQ-0115 |
| AccountActivationViaMobileNumber | AccountActivationViaMobileNumberPort | supplier=userProfile, consumer=webApplicationInterface | Allows a user to activate their account using their mobile number. | FR-02 |
| JobSeekerOnboardingDataCollectionInterface | JobSeekerOnboardingDataCollectionInterfacePort | supplier=webApplicationInterface, consumer=jobSeekerProfile | Interface for collecting initial personal and contact information from job seekers. | FR-03 |
| JobSeekerDetailedProfileUpdateInterface | JobSeekerDetailedProfileUpdateInterfacePort | supplier=webApplicationInterface, consumer=jobSeekerProfile | Interface for collecting detailed professional and personal information from job seekers. | FR-03 |
| JobSeekerOptionalProfileEnrichmentInterface | JobSeekerOptionalProfileEnrichmentInterfacePort | supplier=webApplicationInterface, consumer=jobSeekerProfile | Interface for collecting optional social media links and personal statements from job seekers. | FR-03 |
| ResumeCVUploadInterface | ResumeCVUploadInterfacePort | supplier=webApplicationInterface, consumer=dataManagementService | Allows users to upload resume or CV files for processing. | FR-04 |
| CVInformationExtractionInterface | CVInformationExtractionInterfacePort | supplier=userProfile, consumer=nlpEngine | Allows the system to send uploaded CVs to the AI engine for information extraction. | FR-05 |
| ExtractedCVDataInterface | ExtractedCVDataInterfacePort | supplier=nlpEngine, consumer=userProfile | Allows the AI engine to return the extracted information back to the system to update the profile. | FR-05 |
| JobSeekerProfileBuildingInterface | JobSeekerProfileBuildingInterfacePort | supplier=webApplicationInterface, consumer=jobSeekerProfile | Allows job seekers to interactively build their profile through a staged form. | FR-06 |
| ProfileURLQRCodeGenerationInterface | ProfileURLQRCodeGenerationInterfacePort | supplier=jobSeekerProfile, consumer=webApplicationInterface | Provides the mechanism to generate a shareable public profile URL or QR Code for a job seeker. | FR-11 |
| DocumentUploadInterface | DocumentUploadInterfacePort | supplier=jobSeekerProfile, consumer=webApplicationInterface | Allows a job seeker to upload supplementary documents to their profile. | FR-12 |
| JobSubmissionConfirmationInterface | JobSubmissionConfirmationInterfacePort | supplier=webApplicationInterface, consumer=jobPosting | The system returns a unique job ID upon successful job submission via the API. | FR-29 |
| JobPostingTaggingAndLinkingInterface | JobPostingTaggingAndLinkingInterfacePort | supplier=jobPosting, consumer=matcherService | This interface handles the automatic tagging of a job post with its source platform and includes a backlink to the original advertisement. | FR-30 |
| JobUpdateSynchronizationInterface | JobUpdateSynchronizationInterfacePort | supplier=webApplicationInterface, consumer=jobPosting | Allows external job sites to modify job details using the assigned job ID. | FR-31 |
| JobStatusReviewInterface | JobStatusReviewInterfacePort | supplier=syncDashboard, consumer=webApplicationInterface | Allows partners to review the status of jobs posted via the API. | FR-32 |
| IntegrationUsageStatisticsReportingInterface | IntegrationUsageStatisticsReportingInterfacePort | supplier=dataManagementService, consumer=dashboard | Provides access to statistics regarding job submissions, matches, and views for transparency and performance tracking. | FR-33 |
| APISchemaAndValidationRuleProvision | APISchemaAndValidationRuleProvisionPort | supplier=webApplicationInterface, consumer=jobPosting | Provides access to the up-to-date API schema and detailed field validation rules for job postings. | FR-34 |
| SourcePlatformAttributionVisibilityConfigurationInterface | SourcePlatformAttributionVisibilityConfigurationInterfacePort | supplier=systemConfiguration, consumer=jobPosting | Allows configuration of whether a source platform's attribution is public or restricted to admin/logs. | FR-35 |
| JobPostingAuditTrailInterface | JobPostingAuditTrailInterfacePort | supplier=jobPosting, consumer=auditLog | Records external job site creation or modification events for a job posting. | FR-36 |
| JobPostingTraceabilityDisplayInterface | JobPostingTraceabilityDisplayInterfacePort | supplier=auditLog, consumer=dashboard | Provides job posting audit trail information to the MoL admin dashboard. | FR-36 |
| JobPostingStatisticsReportingInterface | JobPostingStatisticsReportingInterfacePort | supplier=dataManagementService, consumer=administratorAccount | Allows administrators to download reports on job postings filtered by sector, region, or industry. | FR-46 |
| UserRegistrationStatisticsReportingInterface | UserRegistrationStatisticsReportingInterfacePort | supplier=dataManagementService, consumer=administratorAccount | Provides statistics on user registrations for administrative review. | FR-46 |
| TopSearchesReportingInterface | TopSearchesReportingInterfacePort | supplier=metricsTracker, consumer=administratorAccount | Provides statistics on the most frequent searches performed by job seekers and employers. | FR-46 |
| UserInteractionReportingInterface | UserInteractionReportingInterfacePort | supplier=dataManagementService, consumer=administratorAccount | Provides statistics on how users interact with job offers. | FR-46 |
| OverallSystemMetricsReportingInterface | OverallSystemMetricsReportingInterfacePort | supplier=metricsTracker, consumer=administratorAccount | Provides comprehensive overall system metrics for administrative review. | FR-46 |
| AuthenticationInterface | AuthenticationInterfacePort | supplier=webApplicationInterface, consumer=loginTracker | Provides mechanisms for user authentication including username/password, email verification, and MFA. | FR-49 |
| JobPostingSubmissionInterface | JobPostingSubmissionInterfacePort | supplier=employerRegistration, consumer=jobPosting | Allows employers to submit a structured job posting. | FR-55 |
| JobPostingDataInputInterface | JobPostingDataInputInterfacePort | supplier=webApplicationInterface, consumer=jobPosting | Provides structured job posting data conforming to Schema.org JobPosting standard. | FR-56 |
| JobPostingManagementInterface | JobPostingManagementInterfacePort | supplier=jobPosting, consumer=webApplicationInterface | Allows employers to edit job details, extend deadlines, and set visibility for job postings. | FR-57 |
| JobSearchInterface | JobSearchInterfacePort | supplier=webApplicationInterface, consumer=jobSeekerProfile | Provides a comprehensive interface for job seekers to search for relevant job opportunities. | FR-59 |
| JobSearchResultsRetrieval | JobSearchResultsRetrievalPort | supplier=matcherService, consumer=webApplicationInterface | Allows the system to retrieve relevant job postings based on search criteria. | FR-59 |
| JobPostingDataAccess | JobPostingDataAccessPort | supplier=jobPosting, consumer=matcherService | Provides access to job posting data for searching and display. | FR-59 |
| SearchInterfaceForBasicAndAdvancedSearchModes | SearchInterfaceForBasicAndAdvancedSearchModesPort | supplier=webApplicationInterface, consumer=matcherService | The web application interface provides the search functionality to users. | FR-60 |
| JobSearchInterface | JobSearchInterfacePort | supplier=webApplicationInterface, consumer=matcherService | Provides a comprehensive interface for job seekers to search for relevant job opportunities. | FR-62 |
| DisplaySearchResultsWithRankingAndSorting | DisplaySearchResultsWithRankingAndSortingPort | supplier=matcherService, consumer=webApplicationInterface | The web application interface consumes search results, including relevance/skills-matching ranking and sorting options. | FR-63 |
| DisplayRecommendedJobsUponLogin | DisplayRecommendedJobsUponLoginPort | supplier=matcherService, consumer=webApplicationInterface | The web application interface displays recommended jobs generated by the AI matching engine after user login. | FR-63 |
| MatchThresholdConfigurationInterface | MatchThresholdConfigurationInterfacePort | supplier=administratorAccount, consumer=matcherService | Allows administrators to set the minimum match threshold for job matches. | FR-75 |
| JobSeekerToMatcherServiceInterface | JobSeekerToMatcherServiceInterfacePort | supplier=jobSeekerProfile, consumer=matcherService | Allows job seeker profiles to be submitted to the matcher service for ranking. | FR-77 |
| MatcherServiceToJobSeekerInterfaceInterface | MatcherServiceToJobSeekerInterfaceInterfacePort | supplier=matcherService, consumer=jobSeekerProfile | Provides ranked job opportunities to the job seeker. | FR-77 |
| EmployerToMatcherServiceInterface | EmployerToMatcherServiceInterfacePort | supplier=jobPosting, consumer=matcherService | Allows job postings to be submitted to the matcher service for reverse ranking. | FR-77 |
| MatcherServiceToEmployerInterfaceInterface | MatcherServiceToEmployerInterfaceInterfacePort | supplier=matcherService, consumer=jobPosting | Provides ranked job seekers to the employer based on their posting. | FR-77 |
| MatchingParameterConfigurationInterface | MatchingParameterConfigurationInterfacePort | supplier=systemConfiguration, consumer=matcherService | Allows configuration of parameters that adjust the importance of different factors in the matching process. | FR-78 |
| LanguageAwareResumeParsingInterface | LanguageAwareResumeParsingInterfacePort | supplier=dataManagementService, consumer=nlpEngine | Allows the system to process resumes in specified languages like Arabic and English. | FR-81 |
| ConfidenceScoreProvisionInterface | ConfidenceScoreProvisionInterfacePort | supplier=nlpEngine, consumer=dashboard | Provides confidence scores for extracted information to the user interface. | FR-83 |
| ManualVerificationHighlightingInterface | ManualVerificationHighlightingInterfacePort | supplier=nlpEngine, consumer=dashboard | Informs the user interface about areas requiring manual verification. | FR-83 |
| RecommendationInputInterface | RecommendationInputInterfacePort | supplier=jobSeekerProfile, consumer=matcherService | Provides location, salary expectations, and work arrangement preferences for generating recommendations. | FR-89 |
| CandidateSearchInterface | CandidateSearchInterfacePort | supplier=webApplicationInterface, consumer=dataManagementService | Allows employers to search the candidate database using advanced filtering options. | FR-93 |
| ExternalJobSiteIntegrationInterface | ExternalJobSiteIntegrationInterfacePort | supplier=matcherService, consumer=contentDeliveryService | Interface to communicate with external job sites for job posting and searching. | FR-97 |
| ExternalJobDataSynchronizationAPI | ExternalJobDataSynchronizationAPIPort | supplier=webApplicationInterface | Provides APIs for real-time job data synchronization with external job sites. | FR-98 |
| JobPostingDataStandardizationInterface | JobPostingDataStandardizationInterfacePort | supplier=jobPosting, consumer=dataManagementService | This interface handles the mapping and transformation of job postings from various sources into a standardized format. | FR-99 |
| JobImportExportInterface | JobImportExportInterfacePort | supplier=jobPosting, consumer=contentDeliveryService | Interface to handle the bidirectional integration of job postings with external sites. | FR-100 |
| IntegrationStatusAndDataFlowMonitoringInterface | IntegrationStatusAndDataFlowMonitoringInterfacePort | supplier=dataManagementService, consumer=dashboard | Provides data to the dashboard for monitoring integration status and data flow with external job sites. | FR-103 |
| GovernmentDatabaseIntegrationInterface | GovernmentDatabaseIntegrationInterfacePort | supplier=dataManagementService, consumer=dataManagementService | Interface for the system to connect with external government databases for data verification and enrichment. | FR-104 |
| IntegrationWithMoLDatabaseSystem | IntegrationWithMoLDatabaseSystemPort | supplier=webApplicationInterface | Interface to connect with the MoL existing database and systems. | FR-105 |
| IntegrationWithPEFDatabaseSystem | IntegrationWithPEFDatabaseSystemPort | supplier=webApplicationInterface | Interface to connect with the PEF existing database and systems. | FR-105 |
| EducationalCredentialVerificationInterface | EducationalCredentialVerificationInterfacePort | supplier=dataManagementService, consumer=aiProcessingInfrastructure | Allows the system to verify educational credentials against external educational institution databases. | FR-106 |
| IdentityVerificationInterface | IdentityVerificationInterfacePort | supplier=webApplicationInterface | Allows the system to interact with external government ID verification systems. | FR-107 |
| AuditTrailLoggingForGovernmentDataExchanges | AuditTrailLoggingForGovernmentDataExchangesPort | supplier=dataManagementService, consumer=auditLog | Records all data exchanges occurring with external government systems for auditing purposes. | FR-108 |
| ExternalSystemIntegrationAPIFramework | ExternalSystemIntegrationAPIFrameworkPort | supplier=webApplicationInterface | Provides a comprehensive API framework for integration with external systems. | FR-110 |
| RESTfulAPIIntegrationInterface | RESTfulAPIIntegrationInterfacePort | supplier=webApplicationInterface, consumer=webApplicationInterface | Provides a standardized interface for all components to communicate using RESTful APIs and JSON data format. | FR-111 |
| APIDocumentationProvisionInterface | APIDocumentationProvisionInterfacePort | supplier=technicalDocumentationRepository, consumer=webApplicationInterface | Provides detailed API documentation, examples, and testing tools to users. | FR-112 |
| APIAuthenticationAndAuthorizationInterface | APIAuthenticationAndAuthorizationInterfacePort | supplier=webApplicationInterface, consumer=aiProcessingInfrastructure | Provides OAuth 2.0 mechanisms for authenticating and authorizing API access. | FR-113 |
| APIAuthenticationAndAuthorizationInterface | APIAuthenticationAndAuthorizationInterfacePort | supplier=webApplicationInterface, consumer=dataManagementService | Provides OAuth 2.0 mechanisms for authenticating and authorizing API access. | FR-113 |
| APIAuthenticationAndAuthorizationInterface | APIAuthenticationAndAuthorizationInterfacePort | supplier=webApplicationInterface, consumer=matcherService | Provides OAuth 2.0 mechanisms for authenticating and authorizing API access. | FR-113 |
| APIAuthenticationAndAuthorizationInterface | APIAuthenticationAndAuthorizationInterfacePort | supplier=webApplicationInterface, consumer=notificationCenter | Provides OAuth 2.0 mechanisms for authenticating and authorizing API access. | FR-113 |
| APIVersioningInterface | APIVersioningInterfacePort | supplier=webApplicationInterface, consumer=webApplicationInterface | Provides a mechanism for clients to specify and the system to handle different versions of the API. | FR-114 |
| ReportingFrameworkInterface | ReportingFrameworkInterfacePort | supplier=reportLibrary, consumer=webApplicationInterface | Provides a mechanism for generating custom reports that can be consumed by external reporting tools. | FR-135 |
| ReportGenerationInterface | ReportGenerationInterfacePort | supplier=reportLibrary, consumer=webApplicationInterface | Allows the system to request reports in various formats. | FR-137 |
| ReportExportInterface | ReportExportInterfacePort | supplier=reportLibrary, consumer=webApplicationInterface | Allows the system to export generated reports in common formats. | FR-139 |
| ReportBuildingInterface | ReportBuildingInterfacePort | supplier=reportLibrary, consumer=webApplicationInterface | Provides an interface for users to build reports based on system data. | FR-140 |
| EmailNotificationInterface | EmailNotificationInterfacePort | supplier=notificationCenter, consumer=emailTemplateManager | Allows the system to send email notifications for important events and updates. | FR-143 |
| EmailNotificationPreferenceConfigurationInterface | EmailNotificationPreferenceConfigurationInterfacePort | supplier=userProfile, consumer=emailTemplateManager | Allows users to configure their preferences for email notifications. | FR-145 |
| EmailNotificationInterface | EmailNotificationInterfacePort | supplier=notificationCenter, consumer=emailTemplateManager | Allows the system to send email notifications for important events and updates. | FR-146 |
| RealTimeNotificationDeliveryInterface | RealTimeNotificationDeliveryInterfacePort | supplier=notificationCenter, consumer=webApplicationInterface | This interface allows components to push real-time notifications to the user interface. | FR-150 |
| NotificationPreferenceConfigurationInterface | NotificationPreferenceConfigurationInterfacePort | supplier=userProfile, consumer=notificationCenter | Allows users to configure their in-app notification preferences. | FR-153 |
| NotificationManagementInterface | NotificationManagementInterfacePort | supplier=notificationCenter, consumer=userProfile | Allows users to manage their notifications (mark as read, delete, take action). | FR-155 |
| SMSNotificationInterface | SMSNotificationInterfacePort | supplier=notificationCenter, consumer=smsDeliveryTracker | Handles the sending of SMS notifications to users. | FR-156 |
| SMSNotificationOptInAndMobileNumberProvision | SMSNotificationOptInAndMobileNumberProvisionPort | supplier=userProfile, consumer=notificationCenter | Allows a user to opt-in to SMS notifications and provide their mobile number. | FR-157 |
| DisplayRelevantNewsAndUpdatesOnUserDashboards | DisplayRelevantNewsAndUpdatesOnUserDashboardsPort | supplier=dataManagementService, consumer=dashboard | The dashboard needs to receive relevant news and updates based on the user's profile. | FR-165 |
| ContextSensitiveHelpProvisionInterface | ContextSensitiveHelpProvisionInterfacePort | supplier=technicalDocumentationRepository, consumer=webApplicationInterface | Provides help documentation relevant to the current system function being used. | FR-170 |
| ThirdPartyAuthenticationInterface | ThirdPartyAuthenticationInterfacePort | supplier=webApplicationInterface, consumer=userProfile | Provides endpoints for OAuth 2.0 and OpenID Connect flows for external authentication. | NFR-28 |
| DataInTransitEncryptionInterface | DataInTransitEncryptionInterfacePort | supplier=networkInfrastructure, consumer=webApplicationInterface | Ensures all data flowing across network boundaries is encrypted using TLS 1.3 or higher. | NFR-30 |
| PersonalDataViewingAndExportInterface | PersonalDataViewingAndExportInterfacePort | supplier=userProfile, consumer=webApplicationInterface | Allows users to view and export their personal data. | NFR-37 |
| PersonalDataDeletionInterface | PersonalDataDeletionInterfacePort | supplier=userProfile, consumer=webApplicationInterface | Allows users to request the deletion of their personal data. | NFR-37 |
| MaintenanceNotificationInterface | MaintenanceNotificationInterfacePort | supplier=systemConfiguration, consumer=notificationCenter | Allows the system to notify all users about scheduled maintenance. | NFR-53 |
| InterfaceForConsistentTerminologyAndDesignPatterns | InterfaceForConsistentTerminologyAndDesignPatternsPort | supplier=webApplicationInterface, consumer=systemConfiguration | This requirement mandates adherence to consistent terminology and design patterns across all system interfaces. | NFR-74 |
| AccessibilityInterface | AccessibilityInterfacePort | supplier=webApplicationInterface | Provides necessary hooks or adherence to standards for assistive technologies to interact with the user interface. | NFR-79 |
| KeyboardNavigationInterface | KeyboardNavigationInterfacePort | supplier=webApplicationInterface, consumer=webApplicationInterface | Provides the mechanism for keyboard navigation across all system functions. | NFR-80 |
| TextAlternativeProvisionInterface | TextAlternativeProvisionInterfacePort | supplier=webApplicationInterface, consumer=userProfile | Provides text alternatives for non-text content within the system. | NFR-82 |
| LanguageSupportInterface | LanguageSupportInterfacePort | supplier=webApplicationInterface, consumer=webApplicationInterface | Allows components to specify and handle content in Arabic or English. | NFR-85 |
| RTLTextDirectionSupport | RTLTextDirectionSupportPort | supplier=webApplicationInterface, consumer=webApplicationInterface | The web application interface must support right-to-left text direction for Arabic content. | NFR-87 |
| LocalizationInterfaceForDataFormatting | LocalizationInterfaceForDataFormattingPort | supplier=webApplicationInterface, consumer=userProfile | Provides locale-aware formatting for dates, times, and numbers. | NFR-88 |
| TranslationQualityConsistencyInterface | TranslationQualityConsistencyInterfacePort | supplier=webApplicationInterface, consumer=dataManagementService | Ensures consistent translation quality across all elements interacting with the system. | NFR-89 |
| MultilingualContentProvisionForJobPostings | MultilingualContentProvisionForJobPostingsPort | supplier=jobPosting, consumer=webApplicationInterface | Allows the system to provide job posting content in multiple languages. | NFR-90 |
| MultilingualContentProvisionForUserProfiles | MultilingualContentProvisionForUserProfilesPort | supplier=userProfile, consumer=webApplicationInterface | Allows the system to provide user profile content in multiple languages. | NFR-90 |
| LanguageDetectionInterface | LanguageDetectionInterfacePort | supplier=webApplicationInterface, consumer=nlpEngine | Provides language detection capabilities based on user settings and location. | NFR-91 |
| DatabaseAbstractionInterface | DatabaseAbstractionInterfacePort | supplier=dataManagementService, consumer=dataManagementService | Provides a standardized way for components to interact with underlying database technologies. | NFR-109 |
| DeploymentProcedureDocumentationInterface | DeploymentProcedureDocumentationInterfacePort | supplier=technicalDocumentationRepository, consumer=systemConfiguration | Provides documented deployment procedures for different environments. | NFR-110 |
| WebBrowserCompatibilityInterface | WebBrowserCompatibilityInterfacePort | supplier=webApplicationInterface, consumer=containerizationTechnology | Defines the compatibility requirements for the web application interface with major web browsers. | NFR-112 |
| BrowserCompatibilityInterface | BrowserCompatibilityInterfacePort | supplier=webApplicationInterface, consumer=systemConfiguration | Defines the compatibility requirements for the web application interface across supported browsers. | NFR-113 |
| MobileBrowserCompatibilityInterface | MobileBrowserCompatibilityInterfacePort | supplier=webApplicationInterface, consumer=containerizationTechnology | Defines the necessary compatibility layer for the web application to function correctly on mobile browsers. | NFR-114 |
| EmailNotificationDeliveryInterface | EmailNotificationDeliveryInterfacePort | supplier=notificationCenter, consumer=emailTemplateManager | Allows the system to send notifications via standard email clients. | NFR-115 |
| DataImportExportInterface | DataImportExportInterfacePort | supplier=webApplicationInterface, consumer=dataManagementService | Allows the system to handle standard file formats (CSV, JSON, XML) for data import and export. | NFR-116 |
| ExternalSystemIntegrationInterface | ExternalSystemIntegrationInterfacePort | supplier=webApplicationInterface, consumer=networkInfrastructure | Provides a standardized boundary for integrating with external systems. | NFR-117 |
| ThirdPartyContentAttributionInterface | ThirdPartyContentAttributionInterfacePort | supplier=contentDeliveryService, consumer=dataManagementService | Provides mechanisms to attribute third-party content within the system. | NFR-125 |
| APIDocumentationProvisionInterface | APIDocumentationProvisionInterfacePort | supplier=webApplicationInterface, consumer=administratorAccount | Provides detailed API documentation, examples, and testing tools to users. | NFR-152 |
| ConfigurationParameterDocumentationInterface | ConfigurationParameterDocumentationInterfacePort | supplier=systemConfiguration, consumer=technicalDocumentationRepository | This interface is responsible for documenting all system configuration parameters and their effects. | NFR-153 |
| DateAndTimeFormattingInterface | DateAndTimeFormattingInterfacePort | supplier=webApplicationInterface, consumer=userProfile | Provides functionality to handle and format local date and time, including Hijri calendar references. | NFR-157 |

## Unresolved ends

- REQ-0017: The external job sites themselves are not represented as a KNOWN ELEMENT.
- REQ-0018: new_elements
- REQ-0018: interface GovernmentalDatabaseDataExchangeInterface names unknown consumer 'new_elements'
- REQ-0030: The requirement implies the existence of a user interface layer, but the specific components interacting with it (e.g., how it connects to backend services) are not fully defined.
- REQ-0031: The requirement implies a need for the web application interface to adapt its presentation based on the accessing device (smartphone/tablet), but there is no explicit element representing the device context or the rendering logic that consumes this responsiveness requirement.
- REQ-0036: The specific interfaces for integrating with 'existing MoL system' and 'existing PEF system' are not defined in KNOWN ELEMENTS.
- REQ-0036: interface IntegrationWithMoLSystem names unknown consumer 'new_elements'
- REQ-0036: interface IntegrationWithPEFSystem names unknown consumer 'new_elements'
- REQ-0050: The specific component responsible for *providing* the context-sensitive help content is not explicitly defined, only the need for it across system functions.
- REQ-0063: The specific mechanism for linking users from loginTracker to userProfile is not defined.
- REQ-0065: The requirement implies a general 'Registration and profile management interface', but the specific components involved in handling the registration/profile data flow (e.g., which service consumes the data from userProfile or employerRegistration) are not fully specified beyond the webApplicationInterface.
- REQ-0068: {'intent': 'Notification interface', 'description': 'The requirement implies a general notification interface, but the specific consumer for notifications (beyond the web application) is not fully defined.', 'supplier': 'part notificationCenter', 'consumer': 'unresolved'}
- REQ-0069: The requirement mentions 'Registration' which implies interaction with user/employer registration, but the specific interface boundary for this is not fully defined against the known elements.
- REQ-0070: The specific mechanism for identifying an 'unregistered (guest) user' within the system components is not defined.
- REQ-0071: {'intent': 'Authentication/Registration Prompting Mechanism', 'description': 'The mechanism that actually prompts the user (login/register) is not explicitly defined as a component.', 'supplier': 'webApplicationInterface', 'consumer': 'userProfile'}
- REQ-0073: {'intent': 'User-friendly UX/UI dynamic interface', 'description': "The requirement specifies a 'user-friendly UX/UI dynamic interface' which is the presentation layer, but no specific component is identified as the sole provider or consumer of this abstract concept beyond the general webApplicationInterface."}
- REQ-0075: The requirement implies that the AI functions and techniques must be tailored for both Arabic and English, but there is no explicit interface defined for how the 'part aiProcessingInfrastructure' consumes or dictates the specific AI techniques based on language, other than the general NLP engine interface.
- REQ-0078: {'intent': 'Layout/Presentation Logic', 'description': "The requirement implies a presentation layer that orchestrates the display, which is handled by part webApplicationInterface, but the specific logic for 'engaging and easy-to-navigate layout' is not defined as an interface.", 'supplier': 'part webApplicationInterface', 'consumer': 'new_elements'}
- REQ-0081: hardware components
- REQ-0084: The specific external job sites are not named, so the supplier/consumer relationship with them is unresolved.
- REQ-0087: The requirement mandates documentation for 'All software interfaces', but no specific component is named as the entity responsible for *providing* or *consuming* this documentation specification itself, other than potentially the webApplicationInterface or systemConfiguration.
- REQ-0090: The specific mechanism or component responsible for managing the WebSocket connection itself is not explicitly named, though part webApplicationInterface is the likely consumer.
- REQ-0091: The specific component responsible for initiating the SMTP communication (the consumer of the email sending capability) is not explicitly named, although part webApplicationInterface is a likely candidate for external communication.
- REQ-0092: The specific source component triggering the SMS notification is not explicitly named.
- REQ-0094: The requirement is very general and does not specify which components are exchanging data or what specific data needs to be exchanged, only that the format should be JSON.
- REQ-0097: The specific component that requires or provides the XML integration capability is not named.
- REQ-0097: interface LegacySystemIntegrationInterface names unknown consumer 'new_elements'
- REQ-0099: The requirement implies security mechanisms must be applied across all component interactions, but specific interfaces for data/control flow between internal components (e.g., between part dataManagementService and part aiProcessingInfrastructure) are not explicitly named or implied by the requirement alone.
- REQ-0101: MoL system interface
- REQ-0101: PEF system interface
- REQ-0109: The specific mechanism or service responsible for managing and serving translated text content is not explicitly defined in KNOWN ELEMENTS, although part contentDeliveryService might be involved.
- REQ-0114: The specific component responsible for managing or serving regional language variations is not explicitly defined.
- REQ-0115: The requirement implies a need for region-specific features, but no specific component is identified to provide or consume this feature set beyond the general content delivery.
- FR-02: The specific service responsible for handling the activation logic (e.g., sending OTP, verifying number) is not explicitly named.
- FR-03: {'intent': 'Mobile/Email communication interface', 'description': 'The requirement mentions collection via mobile/email, implying an interface for these channels, but no specific component is named to handle the input from these channels.', 'supplier': 'unresolved', 'consumer': 'jobSeekerProfile'}
- FR-04: The specific component responsible for handling the uploaded resume/CV content after reception from the webApplicationInterface is not explicitly defined, though dataManagementService is a likely candidate for storage/processing.
- FR-05: The mechanism for 'adding the extracted information to the profile' is implied but not fully defined in terms of data flow or specific component interaction beyond the profile itself.
- FR-06: The specific mechanism for 'popup prompts' is not defined in terms of a specific interface boundary.
- FR-11: The activation mechanism for generating the shareable profile URL/QR Code is not specified.
- FR-12: The specific mechanism for handling the uploaded document (e.g., storage, processing) is not explicitly defined as an interface boundary.
- FR-29: The specific component responsible for receiving the job push via the API is not explicitly named, although 'webApplicationInterface' is the entry point.
- FR-30: The requirement implies a mechanism to determine the 'source platform' and generate the 'backlink', which might involve other components not explicitly named as suppliers or consumers in this specific interaction.
- FR-31: The specific mechanism or component responsible for receiving and processing the external job site updates via the API is not explicitly named as a supplier or consumer, although 'webApplicationInterface' is implied as the entry point.
- FR-32: The specific data source or service providing the job status information (synced, failed, pending, archived) is not explicitly named as a supplier for the syncDashboard.
- FR-33: The requirement mentions 'periodic or real-time access', which implies a mechanism (like an API endpoint or a streaming interface) that is not explicitly defined as a known element.
- FR-34: {'intent': 'API endpoint for schema/validation access', 'description': 'The specific component that serves the API schema and validation rules is not explicitly named.', 'supplier': 'webApplicationInterface', 'consumer': 'jobPosting'}
- FR-35: The specific component responsible for reading and enforcing the visibility setting on the job posting itself is not explicitly named.
- FR-36: The specific mechanism or data structure for 'job level' audit trail recording is not fully defined.
- FR-46: {'intent': 'Report generation/download interface', 'description': 'The mechanism by which the administrator consumes the generated reports.', 'supplier': 'unresolved', 'consumer': 'part administratorAccount'}
- FR-49: The specific components responsible for managing the authentication state (e.g., user credentials storage, MFA logic) are not explicitly named, only the requirement for the mechanism is stated.
- FR-55: {'intent': 'File upload/copy-paste input handling', 'description': 'The mechanism for handling file uploads or copy/paste input for required skills is not fully defined.', 'supplier': 'part employerRegistration', 'consumer': 'part jobPosting'}
- FR-56: The specific mechanism or component responsible for validating and enforcing the Schema.org JobPosting standard on the input data is not explicitly named.
- FR-57: The specific entity representing the 'employer' performing the management action is not explicitly named as a known element, though it is implied by the requirement context.
- FR-59: The specific mechanism for 'comprehensive' search (e.g., filtering, ranking logic) is not fully defined in terms of required inputs/outputs beyond the general search interface.
- FR-60: The specific attributes defined by the employer for advanced search modes are not explicitly named as a known element.
- FR-62: {'intent': 'Job posting data retrieval interface', 'description': 'The matcherService needs to retrieve job posting data based on search criteria.', 'supplier': 'matcherService', 'consumer': 'jobPosting'}
- FR-63: {'intent': 'User login event trigger', 'description': "The requirement mentions 'when user login', implying a trigger event that needs to be defined for the system to initiate the recommendation display.", 'supplier': 'unresolved', 'consumer': 'part webApplicationInterface'}
- FR-75: The specific mechanism or component that consumes the match threshold from part administratorAccount is not explicitly named, though part matcherService is the logical consumer.
- FR-77: {'intent': 'Interface for displaying ranked results', 'description': 'The mechanism by which the ranked results from the matcher service are presented to the end-user (job seeker or employer).', 'supplier': 'part matcherService', 'consumer': 'part webApplicationInterface'}
- FR-78: The specific mechanism or component that consumes the configured matching parameters (beyond part matcherService) is not explicitly defined.
- FR-81: The specific component responsible for initiating the resume parsing process is not explicitly named, though it likely interacts with part dataManagementService.
- FR-83: The specific component responsible for 'extracted information' is not explicitly named, though 'part nlpEngine' is the most likely supplier.
- FR-89: matcherService
- FR-93: The specific interface for providing advanced filtering options to the search mechanism is not fully defined.
- FR-97: The specific mechanism or component responsible for receiving/acting upon 'recommendations by MoL and PEF' is not explicitly defined as a known element.
- FR-98: external job sites
- FR-98: interface ExternalJobDataSynchronizationAPI names unknown consumer 'external job sites'
- FR-99: The source of the different job postings is not explicitly named, only that they come from 'different sources'.
- FR-100: The specific external sites or integration endpoints are not named, so the counterpart to the integration mechanism is unresolved.
- FR-103: The specific external job sites integration mechanism is not defined, so the supplier providing the integration status/data flow is not explicitly named beyond the general data management service.
- FR-104: Government Database
- FR-105: new_elements
- FR-105: interface IntegrationWithMoLDatabaseSystem names unknown consumer 'new_elements'
- FR-105: interface IntegrationWithPEFDatabaseSystem names unknown consumer 'new_elements'
- FR-106: Educational institution databases
- FR-107: new_elements
- FR-107: interface IdentityVerificationInterface names unknown consumer 'new_elements'
- FR-108: Government Systems Interface
- FR-110: external systems
- FR-110: interface ExternalSystemIntegrationAPIFramework names unknown consumer 'external systems'
- FR-112: The consumer of the API documentation (e.g., a specific user role or component) is not explicitly named.
- FR-113: The specific components that consume the authentication/authorization provided by the webApplicationInterface are not fully specified beyond general service interactions.
- FR-135: Integration point for external reporting tools like Microsoft Power BI
- FR-140: The requirement mentions 'users with appropriate permissions', implying an authorization check, but no specific element handles this permission checking boundary.
- FR-143: The source of 'important events and updates' that trigger the notification.
- FR-145: The specific mechanism or component responsible for receiving and processing the configuration changes from the user interface is not explicitly named.
- FR-146: The specific mechanism or component responsible for triggering the 'immediate' vs 'digest' nature of the notification is not explicitly defined as a boundary.
- FR-150: The source of 'important events and updates' that trigger the notification is not explicitly defined as a supplier.
- FR-153: The specific mechanism or component that receives and processes the configuration change from the user interface is not explicitly named.
- FR-155: The specific mechanism for 'taking action' on a notification is not detailed, implying a potential interface between part notificationCenter and another component that handles the action.
- FR-156: The integration with SMS service providers (gateway) is mentioned but no specific known element represents this external service.
- FR-157: {'intent': 'SMS delivery tracking', 'description': 'The system needs to track SMS delivery status after the notification is sent.', 'supplier': 'part notificationCenter', 'consumer': 'part smsDeliveryTracker'}
- FR-165: {'intent': 'Determine relevant news/updates based on profile', 'description': 'The mechanism to filter news/updates based on the user profile is not explicitly defined.', 'supplier': 'part userProfile', 'consumer': 'part dataManagementService'}
- FR-170: The specific mechanism or component that triggers the context-sensitive help based on user context is not explicitly defined.
- NFR-28: The specific component responsible for handling the OAuth 2.0/OpenID Connect flow (beyond the webApplicationInterface) is not explicitly named.
- NFR-30: The requirement implies encryption for all data in transit, which affects all communication channels, but the specific endpoints (suppliers/consumers) for all data flows are not explicitly defined beyond the general network infrastructure.
- NFR-37: {'intent': 'Data protection regulation compliance mechanism', 'description': 'The specific mechanism ensuring compliance with data protection regulations is not fully defined.', 'supplier': 'userProfile', 'consumer': 'systemConfiguration'}
- NFR-53: part userProfile
- NFR-74: The requirement is a non-functional requirement about internal design quality and consistency, not a direct data or control flow boundary between two named components. The interface above is a conceptual representation of enforcing this constraint.
- NFR-79: new_elements
- NFR-79: interface AccessibilityInterface names unknown consumer 'new_elements'
- NFR-80: The specific components that implement or consume the keyboard navigation functionality are not explicitly named, although it is implied to be part of the user-facing interface.
- NFR-82: The requirement implies a mechanism to provide text alternatives, but it is not explicitly clear which component is responsible for *generating* or *storing* the non-text content that needs alternatives, or which component *consumes* this information for display.
- NFR-85: The requirement implies that various parts of the system must support multiple languages, but no specific element is identified as the central provider or consumer of language configuration across all components.
- NFR-88: The specific component responsible for *applying* the locale-aware formatting (beyond the presentation layer) is not explicitly defined, though it might be part of dataManagementService or systemConfiguration.
- NFR-89: The requirement implies a quality standard that must be enforced across various components, but it does not specify which components are responsible for *providing* or *consuming* this quality metric or standard. The interface is conceptual.
- NFR-91: The specific mechanism or component that consumes the language detection result to 'suggest the appropriate language' is not explicitly named.
- NFR-109: The specific abstraction layer implementation or component responsible for enforcing database portability is not explicitly named.
- NFR-110: The consumer of deployment procedures (e.g., an operations tool or deployment orchestrator) is not explicitly named.
- NFR-112: The specific mechanism or component responsible for enforcing or verifying browser compatibility is not explicitly named.
- NFR-113: The specific mechanism or component responsible for enforcing or reporting browser compatibility is not explicitly named.
- NFR-114: The specific mechanism or component responsible for enforcing or verifying mobile browser compatibility is not explicitly named.
- NFR-115: The specific mechanism or component responsible for interfacing with 'standard email clients' is not explicitly named in KNOWN ELEMENTS.
- NFR-116: The specific component responsible for handling the file format parsing/generation (e.g., a dedicated FileHandler component) is not explicitly named, though dataManagementService is the likely consumer/provider.
- NFR-117: The specific external systems to integrate with are not named, so the counterpart to the integration point is unresolved.
- NFR-125: The specific component responsible for *consuming* the attribution information (e.g., displaying it on the UI) is not explicitly defined, though part dashboard or part webApplicationInterface might be candidates.
- NFR-152: The specific entity or service responsible for *consuming* the API documentation (the integration partner representation) is not explicitly named in KNOWN ELEMENTS.
- NFR-157: The specific component responsible for implementing the date/time formatting logic (e.g., a dedicated service or library) is not explicitly named, although it is implied to interact with user profiles.
