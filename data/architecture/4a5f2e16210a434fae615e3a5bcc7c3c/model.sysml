package JobMatchingPlatform {
    private import ScalarValues::*;

    // Functional decomposition
    action def RegisterEmployer;
    action def ManageCompanyProfile;
    action def EnableUserAccount;
    action def DisableUserAccount;
    action def DeleteUserAccount;
    action def RecoverUserAccount;
    action def CreateJobPosting;
    action def PublishJobPosting;
    action def ClassifyJobPosting;
    action def MatchJobSeekersToPostings;
    action def SynchronizeJobData;
    action def ManageSystemConfiguration;
    action def CacheJobPostingData;
    action def QueueDataSynchronization;
    action def DisplayContextSensitiveHelp;
    action def DisplayCurrentLogins;
    action def DisplayLoginStatistics;
    action def ProvideUserProfileLinks;
    action def DisplayApplicationTracking;
    action def DisplayRecommendationInsights;
    action def BrowseJobListings;
    action def PromptRegistrationOrLogin;
    action def SupportMultilingualInterface;
    action def UtilizeLanguageSpecificAIFunctions;
    action def DisplayLatestJobPostings;
    action def DisplayFeaturedOpportunities;
    action def DisplaySectorBasedNews;
    action def OptimizePublicPagesForSEO;
    action def ReceiveRealTimeNotifications;
    action def SendEmailNotifications;
    action def DefineEscalationProcedures;
    action def MigrateExistingData;
    action def AcceptResumeUpload;
    action def ExtractInformationFromResumes;
    action def UpdateUserProfileWithExtractedData;
    action def BuildUserProfile;
    action def InputEducationDetails;
    action def InputExperienceDetails;
    action def InputSkills;
    action def InputJobPreferences;
    action def SetProfileVisibilityPreferences;
    action def RequestAccountDeactivation;
    action def RequestAccountDeletion;
    action def GenerateShareableProfileURL;
    action def ReviewJobPostingStatus;
    action def ProvideAPISchema;
    action def ValidateJobPostingStructure;
    action def RecordJobPostingSource;
    action def DisplayJobSourceTraceability;
    action def MaintainAuditLog;
    action def ViewJobPostings;
    action def SuspendJobOfferings;
    action def DeleteJobOfferings;
    action def GenerateSectorReports;
    action def GenerateRegionReports;
    action def GenerateIndustryReports;
    action def GenerateRegistrationStatistics;
    action def GenerateSearchTrendReports;
    action def GenerateInteractionReports;
    action def GenerateSystemMetrics;
    action def RestrictFeatureAccessByRole;
    action def RestrictDataVisibilityByRole;
    action def UpdateJobPostingDetails;
    action def SetJobPostingExpiration;
    action def RenewJobPosting;
    action def DisplaySearchResults;
    action def SaveJobToFavorites;
    action def ViewSavedFavorites;
    action def SaveSearchCriteria;
    action def MonitorJobPostings;
    action def ReceiveMatchingJobNotifications;
    action def GenerateShortlistsForPostings;
    action def ConfigureMatchingParameters;
    action def ReviewExtractedResumeData;
    action def UpdateUserProfileWithCorrections;
    action def SearchCandidateDatabase;
    action def StandardizeJobPostings;
    action def MonitorJobPostingSources;
    action def VerifyExternalData;
    action def MonitorJobSeekerActivities;
    action def TrackEmploymentOutcomes;
    action def TrackMatchingAlgorithmPerformance;
    action def ConfigureReportTemplates;
    action def ConfigureEmailNotificationPreferences;
    action def LogEmailNotifications;
    action def GeneratePersonalizedJobRecommendations;
    action def ManageUserNotifications;
    action def SendSMSNotifications;
    action def PublishNewsContent;
    action def CreateAnnouncements;
    action def EditAnnouncements;
    action def PublishAnnouncements;
    action def SupportRichTextFormatting;
    action def EmbedMediaInContent;
    action def ViewAnnouncements;
    action def CollectFeedbackOnHelpContent;
    action def ProcessBatchOperations;
    action def OptimizeDatabaseQueries;
    action def EnforceMFAForAdministrators;
    action def EnableMFAForUsers;
    action def EnforcePasswordPolicy;
    action def ManagePasswordChanges;
    action def EnforceLoginAttemptLimits;
    action def ManageSessionTimeouts;
    action def SupportThirdPartyAuthentication;
    action def EncryptSensitiveDataAtRest;
    action def MaskSensitiveDataInUI;
    action def ManageEncryptionKeys;
    action def ViewPersonalData;
    action def ExportPersonalData;
    action def DeletePersonalData;
    action def CollectNecessaryUserData;
    action def LimitDataRetention;
    action def ObtainDataCollectionConsent;
    action def DisplayPrivacyNotices;
    action def SupportDataProtectionImpactAssessments;
    action def MonitorSystemActivity;
    action def DetectSecurityThreats;
    action def PreventUnauthorizedAccess;
    action def MaintainSystemAvailability;
    action def ReplicateDatabase;
    action def DistributeTrafficAcrossServers;
    action def ImplementCircuitBreakerPatterns;
    action def PerformFullDataBackup;
    action def PerformIncrementalDataBackup;
    action def DefineRecoveryTimeObjective;
    action def DefineRecoveryPointObjective;
    action def DisplayMeaningfulErrorMessages;
    action def ImplementRetryMechanisms;
    action def OptimizeUserWorkflows;
    action def SupportKeyboardNavigation;
    action def ProvideTextAlternativesForContent;
    action def PauseMovingContent;
    action def StopMovingContent;
    action def HideMovingContent;
    action def DetectUserLanguage;
    action def GuideUsersThroughComplexFeatures;
    action def ApplyDefaultSettings;
    action def ExecuteAutomatedTests;
    action def ManageSystemArtifactsVersions;
    action def ImportDataFromFiles;
    action def ExportDataToFiles;
    action def UpdateRegulatoryPolicies;
    action def DetectCopyrightInfringement;
    action def ManageUserAccounts;
    action def ManageUserData;
    action def ProvideUserSupport;

    // Logical architecture
    part def EmployerRegistration {
        attribute registrationStatus : String;
    }
    part def CompanyProfile {
        attribute companyName : String;
        attribute contactDetails : String;
    }
    part def AdministratorAccount {
        attribute username : String;
        attribute passwordHash : String;
    }
    part def SiteManagementAccount {
        attribute username : String;
        attribute passwordHash : String;
    }
    part def JobSeekerProfile {
        attribute skills : String;
        attribute education : String;
        attribute behavior : String;
    }
    part def JobPosting;
    part def MatcherService;
    part def SystemConfiguration {
        attribute configurationData : String;
    }
    part def DataManagementService {
        attribute dataStore : String;
    }
    part def BackupService {
        attribute retentionPolicy : String;
    }
    part def WebApplicationInterface {
        attribute accessibility : Boolean;
    }
    part def AIProcessingInfrastructure {
        attribute processingCapacity : String;
    }
    part def NetworkInfrastructure {
        attribute bandwidth : String;
        attribute highAvailability : Boolean;
        attribute loadBalancing : Boolean;
        attribute autoScaling : Boolean;
    }
    part def TrainingContent {
        attribute contentID : String;
        attribute version : String;
    }
    part def SystemDemonstrationMaterials {
        attribute materialType : String;
    }
    part def LoginTracker {
        attribute currentLogins : Integer;
        attribute lastSessions : Integer;
    }
    part def UserProfile;
    part def Dashboard {
        attribute applicationStatus : String;
        attribute recommendationData : String;
    }
    part def ContentDeliveryService;
    part def SyncDashboard {
        attribute statusIndicators : String;
    }
    part def AuditLog {
        attribute logEntries : Integer;
    }
    part def FavoritesManager {
        attribute userId : String;
        attribute jobId : String;
    }
    part def NLPEngine {
        attribute processingMode : String;
    }
    part def MetricsTracker {
        attribute jobPostingTrends : String;
        attribute applicationRates : Real;
        attribute hiringRates : Real;
        attribute timeToFill : Real;
    }
    part def ReportLibrary {
        attribute reportId : String;
        attribute reportData : String;
        attribute creationTimestamp : String;
    }
    part def EmailTemplateManager {
        attribute templateId : String;
        attribute templateContent : String;
    }
    part def NotificationCenter {
        attribute notificationCount : Integer;
    }
    part def SMSDeliveryTracker {
        attribute deliveryStatus : String;
    }
    part def IntrusionDetectionSystem {
        attribute detectionThreshold : Integer;
    }
    part def IntrusionPreventionSystem {
        attribute preventionPolicy : String;
    }
    part def LoadBalancer {
        attribute serverCount : Integer;
    }
    part def TechnicalDocumentationRepository {
        attribute documentationVersion : String;
    }
    part def ContainerizationTechnology {
        attribute deploymentConsistency : Boolean;
    }

    part employerRegistration : EmployerRegistration;
    part companyProfile : CompanyProfile;
    part administratorAccount : AdministratorAccount;
    part siteManagementAccount : SiteManagementAccount;
    part jobSeekerProfile : JobSeekerProfile;
    part jobPosting : JobPosting;
    part matcherService : MatcherService;
    part systemConfiguration : SystemConfiguration;
    part dataManagementService : DataManagementService;
    part backupService : BackupService;
    part webApplicationInterface : WebApplicationInterface;
    part aiProcessingInfrastructure : AIProcessingInfrastructure;
    part networkInfrastructure : NetworkInfrastructure;
    part trainingContent : TrainingContent;
    part systemDemonstrationMaterials : SystemDemonstrationMaterials;
    part loginTracker : LoginTracker;
    part userProfile : UserProfile;
    part dashboard : Dashboard;
    part contentDeliveryService : ContentDeliveryService;
    part syncDashboard : SyncDashboard;
    part auditLog : AuditLog;
    part favoritesManager : FavoritesManager;
    part nlpEngine : NLPEngine;
    part metricsTracker : MetricsTracker;
    part reportLibrary : ReportLibrary;
    part emailTemplateManager : EmailTemplateManager;
    part notificationCenter : NotificationCenter;
    part smsDeliveryTracker : SMSDeliveryTracker;
    part intrusionDetectionSystem : IntrusionDetectionSystem;
    part intrusionPreventionSystem : IntrusionPreventionSystem;
    part loadBalancer : LoadBalancer;
    part technicalDocumentationRepository : TechnicalDocumentationRepository;
    part containerizationTechnology : ContainerizationTechnology;

    // Interfaces
    port def ExternalJobDataSynchronizationInterfacePort {
        attribute Synchronization_Status : String;
    }
    interface def ExternalJobDataSynchronizationInterface {
        end supplier : ExternalJobDataSynchronizationInterfacePort;
        end consumer : ExternalJobDataSynchronizationInterfacePort;
    }
    port def GovernmentalDatabaseDataExchangeInterfacePort {
        attribute Data_payload : String;
    }
    interface def GovernmentalDatabaseDataExchangeInterface {
        end supplier : GovernmentalDatabaseDataExchangeInterfacePort;
        end consumer : GovernmentalDatabaseDataExchangeInterfacePort;
    }
    port def WebApplicationAccessInterfacePort {
        attribute Access_Protocol : String;
    }
    interface def WebApplicationAccessInterface {
        end supplier : WebApplicationAccessInterfacePort;
        end consumer : WebApplicationAccessInterfacePort;
    }
    port def WebInterfacePresentationPort {
        attribute Device_type : String;
    }
    interface def WebInterfacePresentation {
        end supplier : WebInterfacePresentationPort;
        end consumer : WebInterfacePresentationPort;
    }
    port def IntegrationWithMoLSystemPort;
    interface def IntegrationWithMoLSystem {
        end supplier : IntegrationWithMoLSystemPort;
        end consumer : IntegrationWithMoLSystemPort;
    }
    port def IntegrationWithPEFSystemPort;
    interface def IntegrationWithPEFSystem {
        end supplier : IntegrationWithPEFSystemPort;
        end consumer : IntegrationWithPEFSystemPort;
    }
    port def WebAccessibilityInterfacePort {
        attribute Browser_compatibility : String;
    }
    interface def WebAccessibilityInterface {
        end supplier : WebAccessibilityInterfacePort;
        end consumer : WebAccessibilityInterfacePort;
    }
    port def ContextSensitiveHelpProvisionInterfacePort {
        attribute Help_Content_Identifier : String;
    }
    interface def ContextSensitiveHelpProvisionInterface {
        end supplier : ContextSensitiveHelpProvisionInterfacePort;
        end consumer : ContextSensitiveHelpProvisionInterfacePort;
    }
    port def LoginTrackingInterfacePort {
        attribute current_logins_count : Integer;
        attribute number_of_current_logins : Integer;
        attribute last_sessions_list : String;
    }
    interface def LoginTrackingInterface {
        end supplier : LoginTrackingInterfacePort;
        end consumer : LoginTrackingInterfacePort;
    }
    port def UserProfileRetrievalInterfacePort {
        attribute user_profile_data : String;
    }
    interface def UserProfileRetrievalInterface {
        end supplier : UserProfileRetrievalInterfacePort;
        end consumer : UserProfileRetrievalInterfacePort;
    }
    port def UserProfileManagementInterfacePort {
        attribute Profile_data : String;
    }
    interface def UserProfileManagementInterface {
        end supplier : UserProfileManagementInterfacePort;
        end consumer : UserProfileManagementInterfacePort;
    }
    port def EmployerRegistrationInterfacePort;
    interface def EmployerRegistrationInterface {
        end supplier : EmployerRegistrationInterfacePort;
        end consumer : EmployerRegistrationInterfacePort;
    }
    port def NotificationInterfacePort {
        attribute notification_content : String;
    }
    interface def NotificationInterface {
        end supplier : NotificationInterfacePort;
        end consumer : NotificationInterfacePort;
    }
    port def MessagingInterfacePort {
        attribute message_payload : String;
    }
    interface def MessagingInterface {
        end supplier : MessagingInterfacePort;
        end consumer : MessagingInterfacePort;
    }
    port def CompanyProfileManagementInterfacePort {
        attribute Profile_Data : String;
    }
    interface def CompanyProfileManagementInterface {
        end supplier : CompanyProfileManagementInterfacePort;
        end consumer : CompanyProfileManagementInterfacePort;
    }
    port def JobListingBrowsingInterfacePort {
        attribute location : String;
        attribute sector : String;
        attribute datePosted : String;
    }
    interface def JobListingBrowsingInterface {
        end supplier : JobListingBrowsingInterfacePort;
        end consumer : JobListingBrowsingInterfacePort;
    }
    port def JobApplicationInitiationInterfacePort {
        attribute requires_authentication : Boolean;
    }
    interface def JobApplicationInitiationInterface {
        end supplier : JobApplicationInitiationInterfacePort;
        end consumer : JobApplicationInitiationInterfacePort;
    }
    port def ListingSavingInterfacePort {
        attribute requires_authentication : Boolean;
    }
    interface def ListingSavingInterface {
        end supplier : ListingSavingInterfacePort;
        end consumer : ListingSavingInterfacePort;
    }
    port def NotificationSubscriptionInterfacePort {
        attribute requires_authentication : Boolean;
    }
    interface def NotificationSubscriptionInterface {
        end supplier : NotificationSubscriptionInterfacePort;
        end consumer : NotificationSubscriptionInterfacePort;
    }
    port def JobPostingDisplayInterfacePort {
        attribute Job_Posting_Data : String;
    }
    interface def JobPostingDisplayInterface {
        end supplier : JobPostingDisplayInterfacePort;
        end consumer : JobPostingDisplayInterfacePort;
    }
    port def FeaturedOpportunitiesDisplayInterfacePort {
        attribute Featured_Opportunity_Data : String;
    }
    interface def FeaturedOpportunitiesDisplayInterface {
        end supplier : FeaturedOpportunitiesDisplayInterfacePort;
        end consumer : FeaturedOpportunitiesDisplayInterfacePort;
    }
    port def CareerAdviceNewsDisplayInterfacePort {
        attribute News_Advice_Content : String;
    }
    interface def CareerAdviceNewsDisplayInterface {
        end supplier : CareerAdviceNewsDisplayInterfacePort;
        end consumer : CareerAdviceNewsDisplayInterfacePort;
    }
    port def MultilingualContentProvisionInterfacePort {
        attribute LanguageCode : String;
    }
    interface def MultilingualContentProvisionInterface {
        end supplier : MultilingualContentProvisionInterfacePort;
        end consumer : MultilingualContentProvisionInterfacePort;
    }
    port def AIProcessingInterfaceForLanguageSpecificFunctionsPort {
        attribute LanguageCode : String;
    }
    interface def AIProcessingInterfaceForLanguageSpecificFunctions {
        end supplier : AIProcessingInterfaceForLanguageSpecificFunctionsPort;
        end consumer : AIProcessingInterfaceForLanguageSpecificFunctionsPort;
    }
    port def DisplayJobPostingsOnHomepagePort {
        attribute Job_Posting_Data : String;
    }
    interface def DisplayJobPostingsOnHomepage {
        end supplier : DisplayJobPostingsOnHomepagePort;
        end consumer : DisplayJobPostingsOnHomepagePort;
    }
    port def DisplayFeaturedOpportunitiesOnHomepagePort {
        attribute Featured_Opportunity_Data : String;
    }
    interface def DisplayFeaturedOpportunitiesOnHomepage {
        end supplier : DisplayFeaturedOpportunitiesOnHomepagePort;
        end consumer : DisplayFeaturedOpportunitiesOnHomepagePort;
    }
    port def DisplaySectorBasedNewsAdviceOnHomepagePort {
        attribute Content_Data : String;
    }
    interface def DisplaySectorBasedNewsAdviceOnHomepage {
        end supplier : DisplaySectorBasedNewsAdviceOnHomepagePort;
        end consumer : DisplaySectorBasedNewsAdviceOnHomepagePort;
    }
    port def ExternalJobSiteIntegrationInterfacePort {
        attribute External_Site_API_Endpoint : String;
    }
    interface def ExternalJobSiteIntegrationInterface {
        end supplier : ExternalJobSiteIntegrationInterfacePort;
        end consumer : ExternalJobSiteIntegrationInterfacePort;
    }
    port def InterfaceDocumentationSpecificationInterfacePort {
        attribute documentation_detail_level : String;
        attribute data_format_specification : String;
        attribute protocol_specification : String;
        attribute security_requirements : String;
    }
    interface def InterfaceDocumentationSpecificationInterface {
        end supplier : InterfaceDocumentationSpecificationInterfacePort;
        end consumer : InterfaceDocumentationSpecificationInterfacePort;
    }
    port def WebAccessInterfacePort {
        attribute Protocol : String;
    }
    interface def WebAccessInterface {
        end supplier : WebAccessInterfacePort;
        end consumer : WebAccessInterfacePort;
    }
    port def RealTimeNotificationInterfacePort {
        attribute Notification_payload : String;
    }
    interface def RealTimeNotificationInterface {
        end supplier : RealTimeNotificationInterfacePort;
        end consumer : RealTimeNotificationInterfacePort;
    }
    port def EmailSendingInterfacePort {
        attribute Email_content : String;
        attribute Recipient_address : String;
    }
    interface def EmailSendingInterface {
        end supplier : EmailSendingInterfacePort;
        end consumer : EmailSendingInterfacePort;
    }
    port def SMSNotificationInterfacePort {
        attribute messageContent : String;
    }
    interface def SMSNotificationInterface {
        end supplier : SMSNotificationInterfacePort;
        end consumer : SMSNotificationInterfacePort;
    }
    port def DataExchangeInterfacePort {
        attribute Data_format : String;
    }
    interface def DataExchangeInterface {
        end supplier : DataExchangeInterfacePort;
        end consumer : DataExchangeInterfacePort;
    }
    port def LegacySystemIntegrationInterfacePort {
        attribute XML_Data_Payload : String;
    }
    interface def LegacySystemIntegrationInterface {
        end supplier : LegacySystemIntegrationInterfacePort;
        end consumer : LegacySystemIntegrationInterfacePort;
    }
    port def SecureCommunicationInterfacePort {
        attribute Encryption_status : Boolean;
        attribute Authentication_mechanism_used : String;
    }
    interface def SecureCommunicationInterface {
        end supplier : SecureCommunicationInterfacePort;
        end consumer : SecureCommunicationInterfacePort;
    }
    port def DataMigrationInterfaceFromLegacySystemsPort {
        attribute Migrated_Data_Payload : String;
    }
    interface def DataMigrationInterfaceFromLegacySystems {
        end supplier : DataMigrationInterfaceFromLegacySystemsPort;
        end consumer : DataMigrationInterfaceFromLegacySystemsPort;
    }
    port def UITextProvisionInterfacePort {
        attribute Text_content : String;
    }
    interface def UITextProvisionInterface {
        end supplier : UITextProvisionInterfacePort;
        end consumer : UITextProvisionInterfacePort;
    }
    port def LanguageVariationSupportInterfacePort {
        attribute LanguageCode : String;
    }
    interface def LanguageVariationSupportInterface {
        end supplier : LanguageVariationSupportInterfacePort;
        end consumer : LanguageVariationSupportInterfacePort;
    }
    port def ContentDeliveryInterfacePort {
        attribute Region_identifier : String;
    }
    interface def ContentDeliveryInterface {
        end supplier : ContentDeliveryInterfacePort;
        end consumer : ContentDeliveryInterfacePort;
    }
    port def AccountActivationViaMobileNumberPort {
        attribute mobileNumber : String;
    }
    interface def AccountActivationViaMobileNumber {
        end supplier : AccountActivationViaMobileNumberPort;
        end consumer : AccountActivationViaMobileNumberPort;
    }
    port def JobSeekerOnboardingDataCollectionInterfacePort {
        attribute First_and_last_name : String;
        attribute Email : String;
        attribute Mobile_number : String;
        attribute Password : String;
        attribute Gender : String;
    }
    interface def JobSeekerOnboardingDataCollectionInterface {
        end supplier : JobSeekerOnboardingDataCollectionInterfacePort;
        end consumer : JobSeekerOnboardingDataCollectionInterfacePort;
    }
    port def JobSeekerDetailedProfileUpdateInterfacePort {
        attribute Education_details : String;
        attribute Work_experience_details : String;
        attribute Skills_list : String;
        attribute Training_details : String;
        attribute Certificates_list : String;
        attribute Recent_salary : Real;
        attribute Current_address : String;
        attribute Permanent_address_residence : String;
    }
    interface def JobSeekerDetailedProfileUpdateInterface {
        end supplier : JobSeekerDetailedProfileUpdateInterfacePort;
        end consumer : JobSeekerDetailedProfileUpdateInterfacePort;
    }
    port def JobSeekerOptionalProfileEnrichmentInterfacePort {
        attribute Social_media_links : String;
        attribute Personal_statement : String;
        attribute Bio : String;
    }
    interface def JobSeekerOptionalProfileEnrichmentInterface {
        end supplier : JobSeekerOptionalProfileEnrichmentInterfacePort;
        end consumer : JobSeekerOptionalProfileEnrichmentInterfacePort;
    }
    port def ResumeCVUploadInterfacePort {
        attribute file_content : String;
        attribute file_format : String;
    }
    interface def ResumeCVUploadInterface {
        end supplier : ResumeCVUploadInterfacePort;
        end consumer : ResumeCVUploadInterfacePort;
    }
    port def CVInformationExtractionInterfacePort {
        attribute CV_document : String;
    }
    interface def CVInformationExtractionInterface {
        end supplier : CVInformationExtractionInterfacePort;
        end consumer : CVInformationExtractionInterfacePort;
    }
    port def ExtractedCVDataInterfacePort {
        attribute Extracted_data : String;
    }
    interface def ExtractedCVDataInterface {
        end supplier : ExtractedCVDataInterfacePort;
        end consumer : ExtractedCVDataInterfacePort;
    }
    port def JobSeekerProfileBuildingInterfacePort {
        attribute Education_details : String;
        attribute Experience_details : String;
        attribute Skills_details : String;
        attribute Preferences_details : String;
    }
    interface def JobSeekerProfileBuildingInterface {
        end supplier : JobSeekerProfileBuildingInterfacePort;
        end consumer : JobSeekerProfileBuildingInterfacePort;
    }
    port def ProfileURLQRCodeGenerationInterfacePort {
        attribute Profile_URL_QR_Code : String;
    }
    interface def ProfileURLQRCodeGenerationInterface {
        end supplier : ProfileURLQRCodeGenerationInterfacePort;
        end consumer : ProfileURLQRCodeGenerationInterfacePort;
    }
    port def DocumentUploadInterfacePort {
        attribute document_file : String;
    }
    interface def DocumentUploadInterface {
        end supplier : DocumentUploadInterfacePort;
        end consumer : DocumentUploadInterfacePort;
    }
    port def JobSubmissionConfirmationInterfacePort {
        attribute unique_job_ID : String;
    }
    interface def JobSubmissionConfirmationInterface {
        end supplier : JobSubmissionConfirmationInterfacePort;
        end consumer : JobSubmissionConfirmationInterfacePort;
    }
    port def JobPostingTaggingAndLinkingInterfacePort {
        attribute Source_Platform_Tag : String;
        attribute Original_Advertisement_Backlink : String;
    }
    interface def JobPostingTaggingAndLinkingInterface {
        end supplier : JobPostingTaggingAndLinkingInterfacePort;
        end consumer : JobPostingTaggingAndLinkingInterfacePort;
    }
    port def JobUpdateSynchronizationInterfacePort {
        attribute jobId : String;
        attribute jobDetailsUpdate : String;
    }
    interface def JobUpdateSynchronizationInterface {
        end supplier : JobUpdateSynchronizationInterfacePort;
        end consumer : JobUpdateSynchronizationInterfacePort;
    }
    port def JobStatusReviewInterfacePort {
        attribute Job_status_indicator : String;
    }
    interface def JobStatusReviewInterface {
        end supplier : JobStatusReviewInterfacePort;
        end consumer : JobStatusReviewInterfacePort;
    }
    port def IntegrationUsageStatisticsReportingInterfacePort {
        attribute Number_of_jobs_submitted : Integer;
        attribute Number_of_jobs_matched : Integer;
        attribute Number_of_jobs_viewed : Integer;
    }
    interface def IntegrationUsageStatisticsReportingInterface {
        end supplier : IntegrationUsageStatisticsReportingInterfacePort;
        end consumer : IntegrationUsageStatisticsReportingInterfacePort;
    }
    port def APISchemaAndValidationRuleProvisionPort {
        attribute API_Schema : String;
        attribute Validation_Rules : String;
    }
    interface def APISchemaAndValidationRuleProvision {
        end supplier : APISchemaAndValidationRuleProvisionPort;
        end consumer : APISchemaAndValidationRuleProvisionPort;
    }
    port def SourcePlatformAttributionVisibilityConfigurationInterfacePort {
        attribute Attribution_visibility_setting : Boolean;
    }
    interface def SourcePlatformAttributionVisibilityConfigurationInterface {
        end supplier : SourcePlatformAttributionVisibilityConfigurationInterfacePort;
        end consumer : SourcePlatformAttributionVisibilityConfigurationInterfacePort;
    }
    port def JobPostingAuditTrailInterfacePort {
        attribute external_job_site_identifier : String;
    }
    interface def JobPostingAuditTrailInterface {
        end supplier : JobPostingAuditTrailInterfacePort;
        end consumer : JobPostingAuditTrailInterfacePort;
    }
    port def JobPostingTraceabilityDisplayInterfacePort;
    interface def JobPostingTraceabilityDisplayInterface {
        end supplier : JobPostingTraceabilityDisplayInterfacePort;
        end consumer : JobPostingTraceabilityDisplayInterfacePort;
    }
    port def JobPostingStatisticsReportingInterfacePort {
        attribute Sector_filter : String;
        attribute Region_filter : String;
        attribute Industry_filter : String;
    }
    interface def JobPostingStatisticsReportingInterface {
        end supplier : JobPostingStatisticsReportingInterfacePort;
        end consumer : JobPostingStatisticsReportingInterfacePort;
    }
    port def UserRegistrationStatisticsReportingInterfacePort;
    interface def UserRegistrationStatisticsReportingInterface {
        end supplier : UserRegistrationStatisticsReportingInterfacePort;
        end consumer : UserRegistrationStatisticsReportingInterfacePort;
    }
    port def TopSearchesReportingInterfacePort {
        attribute Search_type : String;
    }
    interface def TopSearchesReportingInterface {
        end supplier : TopSearchesReportingInterfacePort;
        end consumer : TopSearchesReportingInterfacePort;
    }
    port def UserInteractionReportingInterfacePort;
    interface def UserInteractionReportingInterface {
        end supplier : UserInteractionReportingInterfacePort;
        end consumer : UserInteractionReportingInterfacePort;
    }
    port def OverallSystemMetricsReportingInterfacePort;
    interface def OverallSystemMetricsReportingInterface {
        end supplier : OverallSystemMetricsReportingInterfacePort;
        end consumer : OverallSystemMetricsReportingInterfacePort;
    }
    port def AuthenticationInterfacePort {
        attribute Username_Password_credentials : String;
        attribute Email_verification_token : String;
        attribute MFA_token : String;
    }
    interface def AuthenticationInterface {
        end supplier : AuthenticationInterfacePort;
        end consumer : AuthenticationInterfacePort;
    }
    port def JobPostingSubmissionInterfacePort {
        attribute Job_title : String;
        attribute Summary : String;
        attribute Required_skills : String;
        attribute Contract_type : String;
        attribute Required_education_level : String;
        attribute Application_deadline : String;
        attribute Work_format_selection : String;
        attribute Gender : String;
        attribute Number_of_employees : Integer;
        attribute Required_languages_and_proficiency_levels : String;
        attribute Job_link : String;
    }
    interface def JobPostingSubmissionInterface {
        end supplier : JobPostingSubmissionInterfacePort;
        end consumer : JobPostingSubmissionInterfacePort;
    }
    port def JobPostingDataInputInterfacePort {
        attribute JobPosting_data : String;
    }
    interface def JobPostingDataInputInterface {
        end supplier : JobPostingDataInputInterfacePort;
        end consumer : JobPostingDataInputInterfacePort;
    }
    port def JobPostingManagementInterfacePort {
        attribute job_details : String;
        attribute application_deadline : String;
        attribute visibility_setting : String;
    }
    interface def JobPostingManagementInterface {
        end supplier : JobPostingManagementInterfacePort;
        end consumer : JobPostingManagementInterfacePort;
    }
    port def JobSearchInterfacePort {
        attribute searchQuery : String;
    }
    interface def JobSearchInterface {
        end supplier : JobSearchInterfacePort;
        end consumer : JobSearchInterfacePort;
    }
    port def JobSearchResultsRetrievalPort {
        attribute searchCriteria : String;
    }
    interface def JobSearchResultsRetrieval {
        end supplier : JobSearchResultsRetrievalPort;
        end consumer : JobSearchResultsRetrievalPort;
    }
    port def JobPostingDataAccessPort;
    interface def JobPostingDataAccess {
        end supplier : JobPostingDataAccessPort;
        end consumer : JobPostingDataAccessPort;
    }
    port def SearchInterfaceForBasicAndAdvancedSearchModesPort {
        attribute Search_Query : String;
        attribute Search_Mode : String;
    }
    interface def SearchInterfaceForBasicAndAdvancedSearchModes {
        end supplier : SearchInterfaceForBasicAndAdvancedSearchModesPort;
        end consumer : SearchInterfaceForBasicAndAdvancedSearchModesPort;
    }
    port def JobSearchInterfacePort {
        attribute Keywords : String;
        attribute Location : String;
        attribute Salary_range : String;
        attribute Employment_type : String;
        attribute Date_posted : String;
        attribute Application_deadline : String;
        attribute Job_specific_requirements : String;
        attribute Company_sector_industry : String;
    }
    interface def JobSearchInterface {
        end supplier : JobSearchInterfacePort;
        end consumer : JobSearchInterfacePort;
    }
    port def DisplaySearchResultsWithRankingAndSortingPort {
        attribute search_results : String;
        attribute ranking_criteria : String;
        attribute sorting_options : String;
    }
    interface def DisplaySearchResultsWithRankingAndSorting {
        end supplier : DisplaySearchResultsWithRankingAndSortingPort;
        end consumer : DisplaySearchResultsWithRankingAndSortingPort;
    }
    port def DisplayRecommendedJobsUponLoginPort {
        attribute recommended_jobs : String;
    }
    interface def DisplayRecommendedJobsUponLogin {
        end supplier : DisplayRecommendedJobsUponLoginPort;
        end consumer : DisplayRecommendedJobsUponLoginPort;
    }
    port def MatchThresholdConfigurationInterfacePort {
        attribute minimum_match_threshold : Real;
    }
    interface def MatchThresholdConfigurationInterface {
        end supplier : MatchThresholdConfigurationInterfacePort;
        end consumer : MatchThresholdConfigurationInterfacePort;
    }
    port def JobSeekerToMatcherServiceInterfacePort {
        attribute profileData : String;
    }
    interface def JobSeekerToMatcherServiceInterface {
        end supplier : JobSeekerToMatcherServiceInterfacePort;
        end consumer : JobSeekerToMatcherServiceInterfacePort;
    }
    port def MatcherServiceToJobSeekerInterfaceInterfacePort {
        attribute rankedJobOpportunities : String;
    }
    interface def MatcherServiceToJobSeekerInterfaceInterface {
        end supplier : MatcherServiceToJobSeekerInterfaceInterfacePort;
        end consumer : MatcherServiceToJobSeekerInterfaceInterfacePort;
    }
    port def EmployerToMatcherServiceInterfacePort {
        attribute postingData : String;
    }
    interface def EmployerToMatcherServiceInterface {
        end supplier : EmployerToMatcherServiceInterfacePort;
        end consumer : EmployerToMatcherServiceInterfacePort;
    }
    port def MatcherServiceToEmployerInterfaceInterfacePort {
        attribute rankedJobSeekers : String;
    }
    interface def MatcherServiceToEmployerInterfaceInterface {
        end supplier : MatcherServiceToEmployerInterfaceInterfacePort;
        end consumer : MatcherServiceToEmployerInterfaceInterfacePort;
    }
    port def MatchingParameterConfigurationInterfacePort {
        attribute Matching_parameters : String;
    }
    interface def MatchingParameterConfigurationInterface {
        end supplier : MatchingParameterConfigurationInterfacePort;
        end consumer : MatchingParameterConfigurationInterfacePort;
    }
    port def LanguageAwareResumeParsingInterfacePort {
        attribute Language_Code : String;
    }
    interface def LanguageAwareResumeParsingInterface {
        end supplier : LanguageAwareResumeParsingInterfacePort;
        end consumer : LanguageAwareResumeParsingInterfacePort;
    }
    port def ConfidenceScoreProvisionInterfacePort {
        attribute Confidence_Score : Real;
    }
    interface def ConfidenceScoreProvisionInterface {
        end supplier : ConfidenceScoreProvisionInterfacePort;
        end consumer : ConfidenceScoreProvisionInterfacePort;
    }
    port def ManualVerificationHighlightingInterfacePort {
        attribute Verification_Flag : Boolean;
    }
    interface def ManualVerificationHighlightingInterface {
        end supplier : ManualVerificationHighlightingInterfacePort;
        end consumer : ManualVerificationHighlightingInterfacePort;
    }
    port def RecommendationInputInterfacePort {
        attribute location : String;
        attribute salaryExpectations : Integer;
        attribute workArrangementPreferences : String;
    }
    interface def RecommendationInputInterface {
        end supplier : RecommendationInputInterfacePort;
        end consumer : RecommendationInputInterfacePort;
    }
    port def CandidateSearchInterfacePort {
        attribute search_criteria : String;
    }
    interface def CandidateSearchInterface {
        end supplier : CandidateSearchInterfacePort;
        end consumer : CandidateSearchInterfacePort;
    }
    port def ExternalJobSiteIntegrationInterfacePort {
        attribute External_Job_Site_Data : String;
    }
    interface def ExternalJobSiteIntegrationInterface {
        end supplier : ExternalJobSiteIntegrationInterfacePort;
        end consumer : ExternalJobSiteIntegrationInterfacePort;
    }
    port def ExternalJobDataSynchronizationAPIPort {
        attribute Job_data_payload : String;
    }
    interface def ExternalJobDataSynchronizationAPI {
        end supplier : ExternalJobDataSynchronizationAPIPort;
        end consumer : ExternalJobDataSynchronizationAPIPort;
    }
    port def JobPostingDataStandardizationInterfacePort {
        attribute standardized_job_posting_data : String;
    }
    interface def JobPostingDataStandardizationInterface {
        end supplier : JobPostingDataStandardizationInterfacePort;
        end consumer : JobPostingDataStandardizationInterfacePort;
    }
    port def JobImportExportInterfacePort {
        attribute Job_data_payload : String;
    }
    interface def JobImportExportInterface {
        end supplier : JobImportExportInterfacePort;
        end consumer : JobImportExportInterfacePort;
    }
    port def IntegrationStatusAndDataFlowMonitoringInterfacePort {
        attribute Integration_status_data : String;
        attribute Data_flow_metrics : Real;
    }
    interface def IntegrationStatusAndDataFlowMonitoringInterface {
        end supplier : IntegrationStatusAndDataFlowMonitoringInterfacePort;
        end consumer : IntegrationStatusAndDataFlowMonitoringInterfacePort;
    }
    port def GovernmentDatabaseIntegrationInterfacePort {
        attribute VerificationRequest : String;
        attribute VerificationResponse : String;
    }
    interface def GovernmentDatabaseIntegrationInterface {
        end supplier : GovernmentDatabaseIntegrationInterfacePort;
        end consumer : GovernmentDatabaseIntegrationInterfacePort;
    }
    port def IntegrationWithMoLDatabaseSystemPort;
    interface def IntegrationWithMoLDatabaseSystem {
        end supplier : IntegrationWithMoLDatabaseSystemPort;
        end consumer : IntegrationWithMoLDatabaseSystemPort;
    }
    port def IntegrationWithPEFDatabaseSystemPort;
    interface def IntegrationWithPEFDatabaseSystem {
        end supplier : IntegrationWithPEFDatabaseSystemPort;
        end consumer : IntegrationWithPEFDatabaseSystemPort;
    }
    port def EducationalCredentialVerificationInterfacePort {
        attribute Credential_Data : String;
    }
    interface def EducationalCredentialVerificationInterface {
        end supplier : EducationalCredentialVerificationInterfacePort;
        end consumer : EducationalCredentialVerificationInterfacePort;
    }
    port def IdentityVerificationInterfacePort {
        attribute VerificationRequest : String;
        attribute VerificationResult : String;
    }
    interface def IdentityVerificationInterface {
        end supplier : IdentityVerificationInterfacePort;
        end consumer : IdentityVerificationInterfacePort;
    }
    port def AuditTrailLoggingForGovernmentDataExchangesPort {
        attribute exchange_details : String;
    }
    interface def AuditTrailLoggingForGovernmentDataExchanges {
        end supplier : AuditTrailLoggingForGovernmentDataExchangesPort;
        end consumer : AuditTrailLoggingForGovernmentDataExchangesPort;
    }
    port def ExternalSystemIntegrationAPIFrameworkPort {
        attribute API_endpoint_definition : String;
    }
    interface def ExternalSystemIntegrationAPIFramework {
        end supplier : ExternalSystemIntegrationAPIFrameworkPort;
        end consumer : ExternalSystemIntegrationAPIFrameworkPort;
    }
    port def RESTfulAPIIntegrationInterfacePort {
        attribute Data_Format : String;
    }
    interface def RESTfulAPIIntegrationInterface {
        end supplier : RESTfulAPIIntegrationInterfacePort;
        end consumer : RESTfulAPIIntegrationInterfacePort;
    }
    port def APIDocumentationProvisionInterfacePort {
        attribute documentation_content : String;
        attribute examples_available : Boolean;
        attribute testing_tools_available : Boolean;
    }
    interface def APIDocumentationProvisionInterface {
        end supplier : APIDocumentationProvisionInterfacePort;
        end consumer : APIDocumentationProvisionInterfacePort;
    }
    port def APIAuthenticationAndAuthorizationInterfacePort {
        attribute Authentication_Token : String;
    }
    interface def APIAuthenticationAndAuthorizationInterface {
        end supplier : APIAuthenticationAndAuthorizationInterfacePort;
        end consumer : APIAuthenticationAndAuthorizationInterfacePort;
    }
    port def APIAuthenticationAndAuthorizationInterfacePort {
        attribute Authentication_Token : String;
    }
    interface def APIAuthenticationAndAuthorizationInterface {
        end supplier : APIAuthenticationAndAuthorizationInterfacePort;
        end consumer : APIAuthenticationAndAuthorizationInterfacePort;
    }
    port def APIAuthenticationAndAuthorizationInterfacePort {
        attribute Authentication_Token : String;
    }
    interface def APIAuthenticationAndAuthorizationInterface {
        end supplier : APIAuthenticationAndAuthorizationInterfacePort;
        end consumer : APIAuthenticationAndAuthorizationInterfacePort;
    }
    port def APIAuthenticationAndAuthorizationInterfacePort {
        attribute Authentication_Token : String;
    }
    interface def APIAuthenticationAndAuthorizationInterface {
        end supplier : APIAuthenticationAndAuthorizationInterfacePort;
        end consumer : APIAuthenticationAndAuthorizationInterfacePort;
    }
    port def APIVersioningInterfacePort {
        attribute API_Version : String;
    }
    interface def APIVersioningInterface {
        end supplier : APIVersioningInterfacePort;
        end consumer : APIVersioningInterfacePort;
    }
    port def ReportingFrameworkInterfacePort {
        attribute Report_Data : String;
    }
    interface def ReportingFrameworkInterface {
        end supplier : ReportingFrameworkInterfacePort;
        end consumer : ReportingFrameworkInterfacePort;
    }
    port def ReportGenerationInterfacePort {
        attribute Report_format : String;
    }
    interface def ReportGenerationInterface {
        end supplier : ReportGenerationInterfacePort;
        end consumer : ReportGenerationInterfacePort;
    }
    port def ReportExportInterfacePort {
        attribute Report_format : String;
    }
    interface def ReportExportInterface {
        end supplier : ReportExportInterfacePort;
        end consumer : ReportExportInterfacePort;
    }
    port def ReportBuildingInterfacePort {
        attribute Report_definition : String;
    }
    interface def ReportBuildingInterface {
        end supplier : ReportBuildingInterfacePort;
        end consumer : ReportBuildingInterfacePort;
    }
    port def EmailNotificationInterfacePort {
        attribute Email_content : String;
    }
    interface def EmailNotificationInterface {
        end supplier : EmailNotificationInterfacePort;
        end consumer : EmailNotificationInterfacePort;
    }
    port def EmailNotificationPreferenceConfigurationInterfacePort {
        attribute Notification_preference_settings : String;
    }
    interface def EmailNotificationPreferenceConfigurationInterface {
        end supplier : EmailNotificationPreferenceConfigurationInterfacePort;
        end consumer : EmailNotificationPreferenceConfigurationInterfacePort;
    }
    port def EmailNotificationInterfacePort {
        attribute Email_content : String;
    }
    interface def EmailNotificationInterface {
        end supplier : EmailNotificationInterfacePort;
        end consumer : EmailNotificationInterfacePort;
    }
    port def RealTimeNotificationDeliveryInterfacePort {
        attribute Notification_payload : String;
    }
    interface def RealTimeNotificationDeliveryInterface {
        end supplier : RealTimeNotificationDeliveryInterfacePort;
        end consumer : RealTimeNotificationDeliveryInterfacePort;
    }
    port def NotificationPreferenceConfigurationInterfacePort {
        attribute Notification_preferences : String;
    }
    interface def NotificationPreferenceConfigurationInterface {
        end supplier : NotificationPreferenceConfigurationInterfacePort;
        end consumer : NotificationPreferenceConfigurationInterfacePort;
    }
    port def NotificationManagementInterfacePort {
        attribute Notification_ID : String;
    }
    interface def NotificationManagementInterface {
        end supplier : NotificationManagementInterfacePort;
        end consumer : NotificationManagementInterfacePort;
    }
    port def SMSNotificationInterfacePort {
        attribute message_content : String;
        attribute recipient_phone_number : String;
    }
    interface def SMSNotificationInterface {
        end supplier : SMSNotificationInterfacePort;
        end consumer : SMSNotificationInterfacePort;
    }
    port def SMSNotificationOptInAndMobileNumberProvisionPort {
        attribute mobile_number : String;
        attribute opt_in_status : Boolean;
    }
    interface def SMSNotificationOptInAndMobileNumberProvision {
        end supplier : SMSNotificationOptInAndMobileNumberProvisionPort;
        end consumer : SMSNotificationOptInAndMobileNumberProvisionPort;
    }
    port def DisplayRelevantNewsAndUpdatesOnUserDashboardsPort {
        attribute News_Update_Data : String;
    }
    interface def DisplayRelevantNewsAndUpdatesOnUserDashboards {
        end supplier : DisplayRelevantNewsAndUpdatesOnUserDashboardsPort;
        end consumer : DisplayRelevantNewsAndUpdatesOnUserDashboardsPort;
    }
    port def ContextSensitiveHelpProvisionInterfacePort {
        attribute Help_Content : String;
    }
    interface def ContextSensitiveHelpProvisionInterface {
        end supplier : ContextSensitiveHelpProvisionInterfacePort;
        end consumer : ContextSensitiveHelpProvisionInterfacePort;
    }
    port def ThirdPartyAuthenticationInterfacePort {
        attribute Authentication_Token : String;
    }
    interface def ThirdPartyAuthenticationInterface {
        end supplier : ThirdPartyAuthenticationInterfacePort;
        end consumer : ThirdPartyAuthenticationInterfacePort;
    }
    port def DataInTransitEncryptionInterfacePort {
        attribute EncryptionProtocol : String;
    }
    interface def DataInTransitEncryptionInterface {
        end supplier : DataInTransitEncryptionInterfacePort;
        end consumer : DataInTransitEncryptionInterfacePort;
    }
    port def PersonalDataViewingAndExportInterfacePort {
        attribute Data_payload : String;
    }
    interface def PersonalDataViewingAndExportInterface {
        end supplier : PersonalDataViewingAndExportInterfacePort;
        end consumer : PersonalDataViewingAndExportInterfacePort;
    }
    port def PersonalDataDeletionInterfacePort;
    interface def PersonalDataDeletionInterface {
        end supplier : PersonalDataDeletionInterfacePort;
        end consumer : PersonalDataDeletionInterfacePort;
    }
    port def MaintenanceNotificationInterfacePort {
        attribute MaintenanceStartTime : String;
        attribute MaintenanceEndTime : String;
        attribute MaintenanceDescription : String;
    }
    interface def MaintenanceNotificationInterface {
        end supplier : MaintenanceNotificationInterfacePort;
        end consumer : MaintenanceNotificationInterfacePort;
    }
    port def InterfaceForConsistentTerminologyAndDesignPatternsPort {
        attribute Design_Pattern_Adherence : Boolean;
        attribute Terminology_Consistency_Level : String;
    }
    interface def InterfaceForConsistentTerminologyAndDesignPatterns {
        end supplier : InterfaceForConsistentTerminologyAndDesignPatternsPort;
        end consumer : InterfaceForConsistentTerminologyAndDesignPatternsPort;
    }
    port def AccessibilityInterfacePort {
        attribute Accessibility_Compliance_Level : String;
    }
    interface def AccessibilityInterface {
        end supplier : AccessibilityInterfacePort;
        end consumer : AccessibilityInterfacePort;
    }
    port def KeyboardNavigationInterfacePort {
        attribute Navigation_Support : Boolean;
    }
    interface def KeyboardNavigationInterface {
        end supplier : KeyboardNavigationInterfacePort;
        end consumer : KeyboardNavigationInterfacePort;
    }
    port def TextAlternativeProvisionInterfacePort {
        attribute Text_alternative_content : String;
    }
    interface def TextAlternativeProvisionInterface {
        end supplier : TextAlternativeProvisionInterfacePort;
        end consumer : TextAlternativeProvisionInterfacePort;
    }
    port def LanguageSupportInterfacePort {
        attribute Language_Code : String;
    }
    interface def LanguageSupportInterface {
        end supplier : LanguageSupportInterfacePort;
        end consumer : LanguageSupportInterfacePort;
    }
    port def RTLTextDirectionSupportPort {
        attribute Text_Direction : String;
    }
    interface def RTLTextDirectionSupport {
        end supplier : RTLTextDirectionSupportPort;
        end consumer : RTLTextDirectionSupportPort;
    }
    port def LocalizationInterfaceForDataFormattingPort {
        attribute LocaleParam : String;
    }
    interface def LocalizationInterfaceForDataFormatting {
        end supplier : LocalizationInterfaceForDataFormattingPort;
        end consumer : LocalizationInterfaceForDataFormattingPort;
    }
    port def TranslationQualityConsistencyInterfacePort {
        attribute TranslationQualityMetric : Real;
    }
    interface def TranslationQualityConsistencyInterface {
        end supplier : TranslationQualityConsistencyInterfacePort;
        end consumer : TranslationQualityConsistencyInterfacePort;
    }
    port def MultilingualContentProvisionForJobPostingsPort {
        attribute LanguageCode : String;
    }
    interface def MultilingualContentProvisionForJobPostings {
        end supplier : MultilingualContentProvisionForJobPostingsPort;
        end consumer : MultilingualContentProvisionForJobPostingsPort;
    }
    port def MultilingualContentProvisionForUserProfilesPort {
        attribute LanguageCode : String;
    }
    interface def MultilingualContentProvisionForUserProfiles {
        end supplier : MultilingualContentProvisionForUserProfilesPort;
        end consumer : MultilingualContentProvisionForUserProfilesPort;
    }
    port def LanguageDetectionInterfacePort {
        attribute User_settings : String;
        attribute Location : String;
    }
    interface def LanguageDetectionInterface {
        end supplier : LanguageDetectionInterfacePort;
        end consumer : LanguageDetectionInterfacePort;
    }
    port def DatabaseAbstractionInterfacePort {
        attribute Database_connection_details : String;
    }
    interface def DatabaseAbstractionInterface {
        end supplier : DatabaseAbstractionInterfacePort;
        end consumer : DatabaseAbstractionInterfacePort;
    }
    port def DeploymentProcedureDocumentationInterfacePort {
        attribute Environment_type : String;
    }
    interface def DeploymentProcedureDocumentationInterface {
        end supplier : DeploymentProcedureDocumentationInterfacePort;
        end consumer : DeploymentProcedureDocumentationInterfacePort;
    }
    port def WebBrowserCompatibilityInterfacePort {
        attribute SupportedBrowsers : String;
    }
    interface def WebBrowserCompatibilityInterface {
        end supplier : WebBrowserCompatibilityInterfacePort;
        end consumer : WebBrowserCompatibilityInterfacePort;
    }
    port def BrowserCompatibilityInterfacePort {
        attribute SupportedBrowserVersions : String;
    }
    interface def BrowserCompatibilityInterface {
        end supplier : BrowserCompatibilityInterfacePort;
        end consumer : BrowserCompatibilityInterfacePort;
    }
    port def MobileBrowserCompatibilityInterfacePort {
        attribute Supported_Platforms : String;
    }
    interface def MobileBrowserCompatibilityInterface {
        end supplier : MobileBrowserCompatibilityInterfacePort;
        end consumer : MobileBrowserCompatibilityInterfacePort;
    }
    port def EmailNotificationDeliveryInterfacePort {
        attribute Email_content : String;
    }
    interface def EmailNotificationDeliveryInterface {
        end supplier : EmailNotificationDeliveryInterfacePort;
        end consumer : EmailNotificationDeliveryInterfacePort;
    }
    port def DataImportExportInterfacePort {
        attribute File_Format : String;
    }
    interface def DataImportExportInterface {
        end supplier : DataImportExportInterfacePort;
        end consumer : DataImportExportInterfacePort;
    }
    port def ExternalSystemIntegrationInterfacePort {
        attribute Protocol_specification : String;
    }
    interface def ExternalSystemIntegrationInterface {
        end supplier : ExternalSystemIntegrationInterfacePort;
        end consumer : ExternalSystemIntegrationInterfacePort;
    }
    port def ThirdPartyContentAttributionInterfacePort {
        attribute Attribution_Metadata : String;
    }
    interface def ThirdPartyContentAttributionInterface {
        end supplier : ThirdPartyContentAttributionInterfacePort;
        end consumer : ThirdPartyContentAttributionInterfacePort;
    }
    port def APIDocumentationProvisionInterfacePort {
        attribute Documentation_Access : Boolean;
    }
    interface def APIDocumentationProvisionInterface {
        end supplier : APIDocumentationProvisionInterfacePort;
        end consumer : APIDocumentationProvisionInterfacePort;
    }
    port def ConfigurationParameterDocumentationInterfacePort {
        attribute Configuration_Parameter : String;
        attribute Parameter_Value : String;
        attribute Effect_Description : String;
    }
    interface def ConfigurationParameterDocumentationInterface {
        end supplier : ConfigurationParameterDocumentationInterfacePort;
        end consumer : ConfigurationParameterDocumentationInterfacePort;
    }
    port def DateAndTimeFormattingInterfacePort {
        attribute Date_Time_Value : String;
    }
    interface def DateAndTimeFormattingInterface {
        end supplier : DateAndTimeFormattingInterfacePort;
        end consumer : DateAndTimeFormattingInterfacePort;
    }

    // Behavior
    state def UserAccountLifecycle {
        state Enabled;
        state Disabled;
        state Deleted;
        state Recoverable;
        transition Enabled then Disabled;
        transition Enabled then Deleted;
        transition Disabled then Enabled;
        transition Disabled then Recoverable;
        transition Recoverable then Enabled;
        transition Recoverable then Deleted;
    }
    state def ImplementationLifecycle {
        state basic_functionality_prioritized;
        state full_functionality;
        transition basic_functionality_prioritized then full_functionality;
    }
    state def SLAViolationEscalation {
        state Normal_Operation;
        state SLA_Violation_Detected;
        state Escalation_Procedure_Active;
        transition Normal_Operation then SLA_Violation_Detected;
        transition SLA_Violation_Detected then Escalation_Procedure_Active;
    }
    state def JobSeekerProfileRecommendation {
        state profile_incomplete;
        state profile_complete;
        transition profile_incomplete then profile_complete;
    }
    state def JobSeekerProfileVisibilityAndLifecycle {
        state Active;
        state PrivateParam;
        state Deactivated;
        state Deleted;
        transition Active then PrivateParam;
        transition Active then Deactivated;
        transition Active then Deleted;
    }
    state def JobPostingLifecycle {
        state active;
        state inactive;
        transition active then inactive;
        transition active then inactive;
    }
    state def JobPostingLifecycle {
        state Active;
        state Expired;
        transition Active then Expired;
        transition Expired then Active;
    }
    state def SavedSearchLifecycle {
        state saved_search_configured;
        transition saved_search_configured then saved_search_configured;
    }
    state def JobPostingLifecycle {
        state draft;
        state active;
        state paused;
        state expired;
        state archived;
        transition draft then active;
        transition active then paused;
        transition paused then active;
        transition active then expired;
        transition active then archived;
        transition paused then archived;
        transition expired then archived;
    }
    state def JobPostingRanking {
        state unranked;
    }
    state def IntegrationSynchronizationLifecycle {
        state synchronized;
        state synchronization_failed;
        transition synchronized then synchronization_failed;
    }
    state def SynchronizationLifecycle {
        state not_synchronized;
        state scheduled_syncing;
        state on_demand_syncing;
        transition not_synchronized then scheduled_syncing;
        transition not_synchronized then on_demand_syncing;
    }
    state def APIVersioning {
        state Versioned;
        transition Versioned then Versioned;
    }
    state def SkillTrendAnalysis {
        state Idle;
    }
    state def SkillTrendAnalysis {
        state Idle;
    }
    state def SystemMonitoring {
        state monitoring;
        transition monitoring then monitoring;
        transition monitoring then monitoring;
        transition monitoring then monitoring;
        transition monitoring then monitoring;
    }
    state def AlertGenerationLifecycle {
        state monitoring;
    }
    state def ReportSchedulingLifecycle {
        state unscheduled;
        state scheduled;
        transition unscheduled then scheduled;
    }
    state def AccountLoginLifecycle {
        state unlocked;
        state locked;
        transition unlocked then locked;
    }
    state def SecurityScanLifecycle {
        state Idle;
        state Scanning;
        transition Idle then Scanning;
    }
    state def SecurityIncidentResponse {
        state Normal_Operation;
    }
    state def SecurityIncidentResponse {
        state Normal_Operation;
    }
    state def SecurityPatchManagementLifecycle {
        state unpatched;
        state patching;
        transition unpatched then patching;
        transition patching then unpatched;
    }
    state def SystemAvailability {
        state Available_during_standard_operating_hours;
        state Outside_standard_operating_hours;
        transition Outside_standard_operating_hours then Available_during_standard_operating_hours;
        transition Available_during_standard_operating_hours then Outside_standard_operating_hours;
    }
    state def MaintenanceScheduling {
        state normal_operation;
        state maintenance_window_scheduled;
        transition normal_operation then maintenance_window_scheduled;
    }
    state def DatabaseReplicationStatus {
        state Replicated;
        transition Replicated then Replicated;
    }
    state def SystemResilience {
        state Operational;
        transition Operational then Operational;
    }
    state def ExternalServiceDependencyHealth {
        state Operational;
        state Tripped;
        transition Operational then Tripped;
        transition Tripped then Operational;
    }
    state def ExternalServiceDependencyHealth {
        state Operational;
        state Tripped;
        transition Operational then Tripped;
        transition Tripped then Operational;
    }
    state def ExternalServiceDependencyHealth {
        state Operational;
        state Tripped;
        transition Operational then Tripped;
        transition Tripped then Operational;
    }
    state def ExternalServiceDependencyHealth {
        state Operational;
        state Tripped;
        transition Operational then Tripped;
        transition Tripped then Operational;
    }
    state def ExternalServiceDependencyHealth {
        state Operational;
        state Tripped;
        transition Operational then Tripped;
        transition Tripped then Operational;
    }
    state def DataBackupLifecycle {
        state Data_Backup_State;
        transition Data_Backup_State then Data_Backup_State;
        transition Data_Backup_State then Data_Backup_State;
    }
    state def DisasterRecoveryPlanStatus {
        state documented;
        state tested;
        transition documented then tested;
    }
    state def DisasterRecoveryDrillScheduling {
        state Scheduled;
        transition Scheduled then Scheduled;
    }
    state def UserInteractionLifecycle {
        state Awaiting_Input;
        transition Awaiting_Input then Awaiting_Input;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def ServiceOperationLifecycle {
        state Operational;
        transition Operational then Operational;
    }
    state def SystemStability {
        state stable;
        transition stable then stable;
    }
    state def UserActionFeedback {
        state idle;
        transition idle then idle;
    }
    state def HelpAndGuidanceAvailability {
        state displaying_content;
        transition displaying_content then displaying_content;
    }
    state def MovingContentVisibilityLifecycle {
        state moving;
        state paused;
        state stopped;
        state hidden;
        transition moving then paused;
        transition moving then stopped;
        transition moving then hidden;
        transition paused then moving;
        transition paused then stopped;
        transition paused then hidden;
        transition stopped then moving;
        transition stopped then hidden;
        transition hidden then moving;
    }
    state def LanguageSwitching {
        state any_language_state;
        transition any_language_state then any_language_state;
    }
    state def UserExperiencePersonalization {
        state has_preferences;
        state has_behavioral_data;
        transition has_preferences then has_behavioral_data;
    }
    state def FeatureVisibility {
        state basic_view;
        state advanced_view;
        transition basic_view then advanced_view;
    }
    state def UserFeedbackCollectionLifecycle {
        state feedback_available;
        transition feedback_available then feedback_available;
    }
    state def DeploymentLifecycle {
        state unconfigured;
        state configured;
        transition unconfigured then configured;
    }
    state def AlertGenerationLifecycle {
        state monitoring;
    }
    state def AlertGenerationLifecycle {
        state monitoring;
    }
    state def BackupLifecycle {
        state Scheduled;
        transition Scheduled then Scheduled;
    }
    state def BackupIntegrityVerification {
        state Backup_Integrity_Verified;
        transition Backup_Integrity_Verified then Backup_Integrity_Verified;
    }
    state def DataRecoveryLifecycle {
        state Operational;
        state Recovery;
        transition Operational then Recovery;
    }
    state def RestorationProcedureDocumentationAndTesting {
        state documented;
        state tested;
        transition documented then tested;
    }
    state def SystemModificationLifecycle {
        state unmodified;
        state under_review;
        state approved;
        state implemented;
        transition unmodified then under_review;
        transition under_review then approved;
        transition approved then implemented;
    }

    // Constraints
    constraint def WebBrowserAccessibility {
        true
    }
    constraint def WCAGCompliance {
        in WCAG_Version : Real;
        true
    }
    constraint def InterfaceDocumentation {
        true
    }
    constraint def EnvironmentSeparation {
        in Environment : String;
        true
    }
    constraint def DataIsolation {
        in Environment : String;
        true
    }
    constraint def PasswordPolicyEnforcement {
        in passwordPolicyConfig : Integer;
        true
    }
    constraint def RoleBasedAccessControl {
        in user_roles : String;
        true
    }
    constraint def SessionTimeout {
        in sessionTimeout : Integer;
        true
    }
    constraint def DataCompliance {
        in inputData : Real;
        true
    }
    constraint def MatchingAlgorithmPerformanceTracking {
        in accuracy_metric : Real;
        true
    }
    constraint def TechnicalPerformanceTracking {
        in responseTimes : Real;
        in resourceUtilization : Real;
        in errorRates : Real;
        true
    }
    constraint def RoleBasedAccessControlForReports {
        in user_role : String;
        in report_allowedRoles : String;
        true
    }
    constraint def PageLoadTime {
        in pageLoadTime : Real;
        pageLoadTime < 3
    }
    constraint def SearchResultLatency {
        in search_result_time : Real;
        search_result_time <= 2
    }
    constraint def AIMatchingPerformance {
        in individual_job_candidate_matches : Integer;
        true
    }
    constraint def BatchOperationProcessingTime {
        in batchOperation : Integer;
        true
    }
    constraint def ResponseTimeDegradation {
        in Peak_Load_Period : Boolean;
        true
    }
    constraint def ConcurrentUserSupport {
        in concurrentUsers : Integer;
        concurrentUsers >= 1000
    }
    constraint def JobApplicationProcessingRate {
        in jobApplicationsProcessedPerMinute : Integer;
        jobApplicationsProcessedPerMinute >= 100
    }
    constraint def JobPostingIngestionRate {
        in dailyNewJobPostings : Integer;
        dailyNewJobPostings >= 500
    }
    constraint def EmployerRegistrationThroughput {
        in dailyRegistrations : Integer;
        dailyRegistrations >= 1000
    }
    constraint def CPUUtilization {
        in cpu_utilization : Real;
        cpu_utilization <= 0.80
    }
    constraint def MemoryUtilization {
        in availableMemory : Real;
        true
    }
    constraint def StorageCapacity {
        in Storage_capacity : Real;
        true
    }
    constraint def JobSeekerCapacity {
        in JobSeekerProfile : Integer;
        true
    }
    constraint def EmployerCapacity {
        in registeredEmployers : Integer;
        registeredEmployers >= 10000
    }
    constraint def JobPostingCapacity {
        in JobPosting : Integer;
        true
    }
    constraint def MFAEnforcementForAdministrators {
        true
    }
    constraint def MFAOptionForUsers {
        true
    }
    constraint def PasswordComplexityEnforcement {
        true
    }
    constraint def PasswordRotationPolicy {
        in maxInterval : Integer;
        true
    }
    constraint def AccountLockout {
        in lockoutThreshold : Integer;
        true
    }
    constraint def DataEncryptionAtRest {
        in data_at_rest_encryption_algorithm : String;
        true
    }
    constraint def DataInTransitEncryption {
        in TLS_version : Real;
        TLS_version >= 1.3
    }
    constraint def DataMasking {
        true
    }
    constraint def DatabaseEncryption {
        true
    }
    constraint def DataProtectionCompliance {
        true
    }
    constraint def DataSubjectRights {
        in UserProfile : String;
        true
    }
    constraint def AuditTrail {
        true
    }
    constraint def SystemAvailability2 {
        in Standard_Operating_Hours : String;
        true
    }
    constraint def Availability {
        in availability : Real;
        availability >= 0.99
    }
    constraint def DataBackupFrequency {
        in BackupService : Integer;
        true
    }
    constraint def BackupLocationSeparation {
        in PrimarySystem : String;
        true
    }
    constraint def RecoveryTimeObjectiveRTOForCriticalFunctions {
        in RTO_critical : Integer;
        true
    }
    constraint def RecoveryTimeObjectiveRTOForNonCriticalFunctions {
        in RTO_non_critical : Integer;
        true
    }
    constraint def DataLossTolerance {
        in RPO : Integer;
        true
    }
    constraint def DisasterRecoveryPlan {
        true
    }
    constraint def DisasterRecoveryDrillFrequency {
        in drillCount : Integer;
        drillCount >= 2
    }
    constraint def ErrorMessageContent {
        true
    }
    constraint def SensitiveInformationExposure {
        true
    }
    constraint def LocaleFormatting {
        in selected_locale : String;
        true
    }
    constraint def ConfigurationChangeSupport {
        true
    }
    constraint def CodeCoverage {
        in codeCoverage : Real;
        codeCoverage >= 0.80
    }
    constraint def DeploymentFlexibility {
        true
    }
    constraint def ConsistentDeployment {
        true
    }
    constraint def BrowserCompatibility {
        in Chrome : String;
        in Firefox : String;
        in Safari : String;
        in Edge : String;
        true
    }
    constraint def MobileBrowserCompatibility {
        in iOS : String;
        true
    }
    constraint def SystemAvailabilitySLA {
        true
    }
    constraint def IncidentResponseTime {
        in SLA_ResponseTime : Real;
        SLA_ResponseTime >= 0
    }
    constraint def IncidentResolutionTime {
        in SLA_ResolutionTime : Real;
        SLA_ResolutionTime >= 0
    }
    constraint def SLADefinitionAndDocumentation {
        true
    }
    constraint def RoleBasedAccessForAdministrativeFunctions {
        in user : String;
        in requiredRole : String;
        true
    }

}
