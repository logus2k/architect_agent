# Traceability

| Requirement | Status | Text | Elements | Architecture elements |
|---|---|---|---|---|
| FR-01 | unreviewed | original | 1 | action def PromptRegistrationOrLogin |
| FR-02 | unreviewed | original | 3 | action def EnableUserAccount, interface def AccountActivationViaMobileNumber, port def AccountActivationViaMobileNumberPort |
| FR-03 | unreviewed | original | 8 | action def PromptRegistrationOrLogin, action def RegisterEmployer, interface def JobSeekerDetailedProfileUpdateInterface, interface def JobSeekerOnboardingDataCollectionInterface, interface def JobSeekerOptionalProfileEnrichmentInterface, port def JobSeekerDetailedProfileUpdateInterfacePort, port def JobSeekerOnboardingDataCollectionInterfacePort, port def JobSeekerOptionalProfileEnrichmentInterfacePort |
| FR-04 | unreviewed | original | 3 | action def AcceptResumeUpload, interface def ResumeCVUploadInterface, port def ResumeCVUploadInterfacePort |
| FR-05 | unreviewed | original | 6 | action def ExtractInformationFromResumes, action def UpdateUserProfileWithExtractedData, interface def CVInformationExtractionInterface, interface def ExtractedCVDataInterface, port def CVInformationExtractionInterfacePort, port def ExtractedCVDataInterfacePort |
| FR-06 | unreviewed | original | 15 | action def BuildUserProfile, action def InputEducationDetails, action def InputExperienceDetails, action def InputJobPreferences, action def InputSkills, attribute education, attribute experience, attribute preferences, attribute skills, interface def JobSeekerProfileBuildingInterface, part def JobSeekerProfile, part def WebApplicationInterface, part jobSeekerProfile, part webApplicationInterface, port def JobSeekerProfileBuildingInterfacePort |
| FR-07 | unreviewed | original | 5 | action def BuildUserProfile, action def InputEducationDetails, action def InputExperienceDetails, action def InputJobPreferences, action def InputSkills |
| FR-08 | unreviewed | original | 3 | action def DisplayContextSensitiveHelp, action def DisplayRecommendationInsights, state def JobSeekerProfileRecommendation |
| FR-09 | unreviewed | original | 8 | action def InputJobPreferences, attribute industry, attribute jobType, attribute location, attribute salaryExpectations, attribute workArrangements, part def JobSeekerProfile, part jobSeekerProfile |
| FR-10 | unreviewed | original | 4 | action def RequestAccountDeactivation, action def RequestAccountDeletion, action def SetProfileVisibilityPreferences, state def JobSeekerProfileVisibilityAndLifecycle |
| FR-100 | unreviewed | original | 4 | action def ReceiveRealTimeNotifications, action def SynchronizeJobData, interface def JobImportExportInterface, port def JobImportExportInterfacePort |
| FR-101 | unreviewed | original | 3 | action def MaintainAuditLog, action def QueueDataSynchronization, state def IntegrationSynchronizationLifecycle |
| FR-102 | unreviewed | original | 3 | action def QueueDataSynchronization, action def SynchronizeJobData, state def SynchronizationLifecycle |
| FR-103 | unreviewed | original | 9 | action def MonitorJobPostingSources, action def QueueDataSynchronization, action def SynchronizeJobData, attribute dataFlowStatus, attribute integrationStatus, interface def IntegrationStatusAndDataFlowMonitoringInterface, part dashboard, part def Dashboard, port def IntegrationStatusAndDataFlowMonitoringInterfacePort |
| FR-104 | unreviewed | original | 3 | action def VerifyExternalData, interface def GovernmentDatabaseIntegrationInterface, port def GovernmentDatabaseIntegrationInterfacePort |
| FR-105 | unreviewed | original | 6 | action def MigrateExistingData, action def VerifyExternalData, interface def IntegrationWithMoLDatabaseSystem, interface def IntegrationWithPEFDatabaseSystem, port def IntegrationWithMoLDatabaseSystemPort, port def IntegrationWithPEFDatabaseSystemPort |
| FR-106 | unreviewed | original | 3 | action def VerifyExternalData, interface def EducationalCredentialVerificationInterface, port def EducationalCredentialVerificationInterfacePort |
| FR-107 | unreviewed | original | 3 | action def VerifyExternalData, interface def IdentityVerificationInterface, port def IdentityVerificationInterfacePort |
| FR-108 | unreviewed | original | 3 | action def MaintainAuditLog, interface def AuditTrailLoggingForGovernmentDataExchanges, port def AuditTrailLoggingForGovernmentDataExchangesPort |
| FR-11 | unreviewed | original | 3 | action def GenerateShareableProfileURL, interface def ProfileURLQRCodeGenerationInterface, port def ProfileURLQRCodeGenerationInterfacePort |
| FR-110 | unreviewed | original | 4 | action def ProvideAPISchema, action def ProvideUserProfileLinks, interface def ExternalSystemIntegrationAPIFramework, port def ExternalSystemIntegrationAPIFrameworkPort |
| FR-111 | unreviewed | original | 4 | action def ProvideAPISchema, action def ProvideUserProfileLinks, interface def RESTfulAPIIntegrationInterface, port def RESTfulAPIIntegrationInterfacePort |
| FR-112 | unreviewed | original | 3 | action def ProvideAPISchema, interface def APIDocumentationProvisionInterface, port def APIDocumentationProvisionInterfacePort |
| FR-113 | unreviewed | original | 3 | action def ProvideAPISchema, interface def APIAuthenticationAndAuthorizationInterface, port def APIAuthenticationAndAuthorizationInterfacePort |
| FR-114 | unreviewed | original | 3 | interface def APIVersioningInterface, port def APIVersioningInterfacePort, state def APIVersioning |
| FR-115 | unreviewed | original | 10 | action def MaintainAuditLog, attribute actionRecord, attribute activityData, attribute loginEvent, part auditLog, part dataManagementService, part def AuditLog, part def DataManagementService, part def LoginTracker, part loginTracker |
| FR-116 | unreviewed | original | 9 | action def MonitorJobSeekerActivities, attribute applications, attribute interactions, attribute jobSearches, attribute profileViews, part def JobSeekerProfile, part def LoginTracker, part jobSeekerProfile, part loginTracker |
| FR-117 | unreviewed | original | 3 | action def MonitorJobPostingSources, action def MonitorJobSeekerActivities, action def SearchCandidateDatabase |
| FR-118 | unreviewed | original | 1 | action def MaintainAuditLog |
| FR-12 | unreviewed | original | 3 | action def AcceptResumeUpload, interface def DocumentUploadInterface, port def DocumentUploadInterfacePort |
| FR-120 | unreviewed | original | 5 | action def GenerateIndustryReports, action def GenerateRegionReports, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics |
| FR-121 | unreviewed | original | 10 | action def GenerateInteractionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSystemMetrics, attribute applicationRates, attribute hiringRates, attribute jobPostingTrends, attribute timeToFill, part def MetricsTracker, part metricsTracker |
| FR-122 | unreviewed | original | 2 | action def GenerateIndustryReports, action def GenerateSectorReports |
| FR-123 | unreviewed | original | 3 | action def GenerateSearchTrendReports, action def GenerateSectorReports, state def SkillTrendAnalysis |
| FR-124 | unreviewed | original | 1 | action def GenerateRegionReports |
| FR-125 | unreviewed | original | 3 | action def GenerateIndustryReports, action def GenerateRegionReports, action def GenerateSectorReports |
| FR-126 | unreviewed | original | 2 | action def MonitorJobSeekerActivities, action def TrackEmploymentOutcomes |
| FR-127 | unreviewed | original | 5 | action def GenerateIndustryReports, action def GenerateRegionReports, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics |
| FR-128 | unreviewed | original | 6 | action def GenerateSystemMetrics, attribute metricData, part dashboard, part def Dashboard, part def MetricsTracker, part metricsTracker |
| FR-129 | unreviewed | original | 2 | action def TrackMatchingAlgorithmPerformance, constraint def MatchingAlgorithmPerformanceTracking |
| FR-130 | unreviewed | original | 3 | action def GenerateSystemMetrics, action def MonitorJobSeekerActivities, state def SystemMonitoring |
| FR-131 | unreviewed | original | 2 | action def GenerateSystemMetrics, constraint def TechnicalPerformanceTracking |
| FR-132 | unreviewed | original | 8 | action def DisplayLoginStatistics, action def GenerateInteractionReports, action def GenerateSearchTrendReports, action def GenerateSystemMetrics, attribute systemHealthStatus, attribute systemPerformanceMetrics, part dashboard, part def Dashboard |
| FR-133 | unreviewed | original | 2 | action def GenerateSystemMetrics, state def AlertGenerationLifecycle |
| FR-134 | unreviewed | original | 5 | action def GenerateSystemMetrics, action def TrackMatchingAlgorithmPerformance, attribute historicalDataStorage, part def MetricsTracker, part metricsTracker |
| FR-135 | unreviewed | original | 9 | action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics, interface def ReportingFrameworkInterface, port def ReportingFrameworkInterfacePort |
| FR-136 | unreviewed | original | 8 | action def ConfigureReportTemplates, attribute administratorID, attribute reportTemplateDefinition, attribute templateParameters, part administratorAccount, part def AdministratorAccount, part def SystemConfiguration, part systemConfiguration |
| FR-137 | unreviewed | original | 9 | action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics, interface def ReportGenerationInterface, port def ReportGenerationInterfacePort |
| FR-138 | unreviewed | original | 6 | action def ConfigureReportTemplates, action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateSystemMetrics, state def ReportSchedulingLifecycle |
| FR-139 | unreviewed | original | 9 | action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics, interface def ReportExportInterface, port def ReportExportInterfacePort |
| FR-140 | unreviewed | original | 9 | action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics, interface def ReportBuildingInterface, port def ReportBuildingInterfacePort |
| FR-141 | unreviewed | original | 12 | action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics, attribute creationTimestamp, attribute reportData, attribute reportId, part def ReportLibrary, part reportLibrary |
| FR-142 | unreviewed | original | 2 | action def RestrictDataVisibilityByRole, constraint def RoleBasedAccessControlForReports |
| FR-143 | unreviewed | original | 3 | action def SendEmailNotifications, interface def EmailNotificationInterface, port def EmailNotificationInterfacePort |
| FR-144 | unreviewed | original | 5 | action def ConfigureReportTemplates, attribute templateContent, attribute templateId, part def EmailTemplateManager, part emailTemplateManager |
| FR-145 | unreviewed | original | 3 | action def ConfigureEmailNotificationPreferences, interface def EmailNotificationPreferenceConfigurationInterface, port def EmailNotificationPreferenceConfigurationInterfacePort |
| FR-146 | unreviewed | original | 4 | action def ConfigureEmailNotificationPreferences, action def SendEmailNotifications, interface def EmailNotificationInterface, port def EmailNotificationInterfacePort |
| FR-147 | unreviewed | original | 1 | action def LogEmailNotifications |
| FR-149 | unreviewed | original | 5 | action def ReceiveMatchingJobNotifications, action def ReceiveRealTimeNotifications, attribute notificationCount, part def NotificationCenter, part notificationCenter |
| FR-150 | unreviewed | original | 3 | action def ReceiveRealTimeNotifications, interface def RealTimeNotificationDeliveryInterface, port def RealTimeNotificationDeliveryInterfacePort |
| FR-151 | unreviewed | original | 3 | action def GeneratePersonalizedJobRecommendations, action def MonitorJobSeekerActivities, action def ReceiveMatchingJobNotifications |
| FR-152 | unreviewed | original | 4 | action def LogEmailNotifications, attribute notificationHistory, part def NotificationCenter, part notificationCenter |
| FR-153 | unreviewed | original | 3 | action def ConfigureEmailNotificationPreferences, interface def NotificationPreferenceConfigurationInterface, port def NotificationPreferenceConfigurationInterfacePort |
| FR-154 | unreviewed | original | 6 | action def ReceiveRealTimeNotifications, action def SendEmailNotifications, attribute notificationType, attribute visualIndicatorStatus, part def NotificationCenter, part notificationCenter |
| FR-155 | unreviewed | original | 3 | action def ManageUserNotifications, interface def NotificationManagementInterface, port def NotificationManagementInterfacePort |
| FR-156 | unreviewed | original | 3 | action def SendSMSNotifications, interface def SMSNotificationInterface, port def SMSNotificationInterfacePort |
| FR-157 | unreviewed | original | 4 | action def ConfigureEmailNotificationPreferences, action def ConfigureMatchingParameters, interface def SMSNotificationOptInAndMobileNumberProvision, port def SMSNotificationOptInAndMobileNumberProvisionPort |
| FR-158 | unreviewed | original | 3 | action def ConfigureEmailNotificationPreferences, action def ConfigureMatchingParameters, action def SendSMSNotifications |
| FR-159 | unreviewed | original | 4 | action def SendSMSNotifications, attribute deliveryStatus, part def SMSDeliveryTracker, part smsDeliveryTracker |
| FR-161 | unreviewed | original | 4 | action def PublishNewsContent, attribute contentSource, part contentDeliveryService, part def ContentDeliveryService |
| FR-162 | unreviewed | original | 3 | action def CreateAnnouncements, action def EditAnnouncements, action def PublishAnnouncements |
| FR-163 | unreviewed | original | 11 | action def EmbedMediaInContent, action def SupportRichTextFormatting, attribute supportsEmbeddedMedia, attribute supportsImages, attribute supportsRichText, part contentDeliveryService, part def ContentDeliveryService, part def JobPosting, part def UserProfile, part jobPosting, part userProfile |
| FR-164 | unreviewed | original | 1 | action def ClassifyJobPosting |
| FR-165 | unreviewed | original | 4 | action def DisplaySectorBasedNews, action def GeneratePersonalizedJobRecommendations, interface def DisplayRelevantNewsAndUpdatesOnUserDashboards, port def DisplayRelevantNewsAndUpdatesOnUserDashboardsPort |
| FR-166 | unreviewed | original | 7 | action def EditAnnouncements, action def PublishNewsContent, action def ViewAnnouncements, attribute archiveStorage, attribute searchCapability, part contentDeliveryService, part def ContentDeliveryService |
| FR-167 | unreviewed | original | 1 | action def DisplayContextSensitiveHelp |
| FR-168 | unreviewed | original | 5 | action def DisplayContextSensitiveHelp, attribute topic, attribute userRole, part def TrainingContent, part trainingContent |
| FR-169 | unreviewed | original | 1 | action def DisplayContextSensitiveHelp |
| FR-170 | unreviewed | original | 3 | action def DisplayContextSensitiveHelp, interface def ContextSensitiveHelpProvisionInterface, port def ContextSensitiveHelpProvisionInterfacePort |
| FR-171 | unreviewed | original | 1 | action def EditAnnouncements |
| FR-172 | unreviewed | original | 1 | action def CollectFeedbackOnHelpContent |
| FR-173 | unreviewed | original | 1 | action def DisplayContextSensitiveHelp |
| FR-174 | unreviewed | original | 5 | action def DisplayContextSensitiveHelp, action def EmbedMediaInContent, attribute contentType, part def TrainingContent, part trainingContent |
| FR-29 | unreviewed | original | 3 | action def CreateJobPosting, interface def JobSubmissionConfirmationInterface, port def JobSubmissionConfirmationInterfacePort |
| FR-30 | unreviewed | original | 3 | action def ClassifyJobPosting, interface def JobPostingTaggingAndLinkingInterface, port def JobPostingTaggingAndLinkingInterfacePort |
| FR-31 | unreviewed | original | 3 | action def SynchronizeJobData, interface def JobUpdateSynchronizationInterface, port def JobUpdateSynchronizationInterfacePort |
| FR-32 | unreviewed | original | 6 | action def ReviewJobPostingStatus, attribute statusIndicators, interface def JobStatusReviewInterface, part def SyncDashboard, part syncDashboard, port def JobStatusReviewInterfacePort |
| FR-33 | unreviewed | original | 3 | action def DisplayLoginStatistics, interface def IntegrationUsageStatisticsReportingInterface, port def IntegrationUsageStatisticsReportingInterfacePort |
| FR-34 | unreviewed | original | 4 | action def ProvideAPISchema, action def ValidateJobPostingStructure, interface def APISchemaAndValidationRuleProvision, port def APISchemaAndValidationRuleProvisionPort |
| FR-35 | unreviewed | original | 3 | action def ManageCompanyProfile, interface def SourcePlatformAttributionVisibilityConfigurationInterface, port def SourcePlatformAttributionVisibilityConfigurationInterfacePort |
| FR-36 | unreviewed | original | 11 | action def DisplayJobSourceTraceability, action def RecordJobPostingSource, attribute externalSiteIdentifier, interface def JobPostingAuditTrailInterface, interface def JobPostingTraceabilityDisplayInterface, part dashboard, part def Dashboard, part def JobPosting, part jobPosting, port def JobPostingAuditTrailInterfacePort, port def JobPostingTraceabilityDisplayInterfacePort |
| FR-37 | unreviewed | original | 15 | action def DeleteUserAccount, action def DisableUserAccount, action def DisplayCurrentLogins, action def DisplayLoginStatistics, action def EnableUserAccount, action def ManageSystemConfiguration, action def RecoverUserAccount, attribute credentials, attribute permissions, part administratorAccount, part def AdministratorAccount, part def SiteManagementAccount, part def WebApplicationInterface, part siteManagementAccount, part webApplicationInterface |
| FR-38 | unreviewed | original | 14 | action def BuildUserProfile, action def CreateJobPosting, action def RegisterEmployer, attribute isAuthorized, part administratorAccount, part dataManagementService, part def AdministratorAccount, part def DataManagementService, part def EmployerRegistration, part def JobPosting, part def JobSeekerProfile, part employerRegistration, part jobPosting, part jobSeekerProfile |
| FR-39 | unreviewed | original | 12 | action def DisableUserAccount, action def DisplayCurrentLogins, action def EnableUserAccount, action def ManageSystemConfiguration, action def RecoverUserAccount, attribute accountStatus, part administratorAccount, part def AdministratorAccount, part def SiteManagementAccount, part def UserProfile, part siteManagementAccount, part userProfile |
| FR-40 | unreviewed | original | 10 | action def RecoverUserAccount, action def RegisterEmployer, action def ReviewJobPostingStatus, attribute accountRecoveryTools, attribute approvalCapability, attribute pendingRegistrationView, part administratorAccount, part def AdministratorAccount, part def EmployerRegistration, part employerRegistration |
| FR-41 | unreviewed | original | 4 | action def MaintainAuditLog, attribute logEntries, part auditLog, part def AuditLog |
| FR-42 | unreviewed | original | 10 | action def ManageSystemConfiguration, attribute credentials, attribute permissions, attribute settings, part administratorAccount, part def AdministratorAccount, part def SystemConfiguration, part def WebApplicationInterface, part systemConfiguration, part webApplicationInterface |
| FR-43 | unreviewed | original | 8 | action def ManageSystemConfiguration, attribute isAuthorized, part administratorAccount, part dataManagementService, part def AdministratorAccount, part def DataManagementService, part def SystemConfiguration, part systemConfiguration |
| FR-44 | unreviewed | original | 8 | action def ManageSystemConfiguration, attribute credentials, attribute permissions, attribute taxonomies, part administratorAccount, part def AdministratorAccount, part def SystemConfiguration, part systemConfiguration |
| FR-45 | unreviewed | original | 5 | action def DeleteJobOfferings, action def ReviewJobPostingStatus, action def SuspendJobOfferings, action def ViewJobPostings, state def JobPostingLifecycle |
| FR-46 | unreviewed | original | 17 | action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateRegistrationStatistics, action def GenerateSearchTrendReports, action def GenerateSectorReports, action def GenerateSystemMetrics, interface def JobPostingStatisticsReportingInterface, interface def OverallSystemMetricsReportingInterface, interface def TopSearchesReportingInterface, interface def UserInteractionReportingInterface, interface def UserRegistrationStatisticsReportingInterface, port def JobPostingStatisticsReportingInterfacePort, port def OverallSystemMetricsReportingInterfacePort, port def TopSearchesReportingInterfacePort, port def UserInteractionReportingInterfacePort, port def UserRegistrationStatisticsReportingInterfacePort |
| FR-49 | unreviewed | original | 3 | action def PromptRegistrationOrLogin, interface def AuthenticationInterface, port def AuthenticationInterfacePort |
| FR-50 | unreviewed | original | 2 | action def ManageSystemConfiguration, constraint def PasswordPolicyEnforcement |
| FR-51 | unreviewed | original | 3 | action def RestrictDataVisibilityByRole, action def RestrictFeatureAccessByRole, constraint def RoleBasedAccessControl |
| FR-52 | unreviewed | original | 2 | action def ManageSystemConfiguration, constraint def SessionTimeout |
| FR-53 | unreviewed | original | 3 | action def MaintainAuditLog, part auditLog, part def AuditLog |
| FR-54 | unreviewed | original | 10 | action def CreateJobPosting, action def PublishJobPosting, action def ValidateJobPostingStructure, attribute jobDetails, part def EmployerRegistration, part def JobPosting, part def WebApplicationInterface, part employerRegistration, part jobPosting, part webApplicationInterface |
| FR-55 | unreviewed | original | 24 | action def CreateJobPosting, action def PublishJobPosting, action def ValidateJobPostingStructure, attribute applicationDeadline, attribute autoCloseFeature, attribute contractType, attribute gender, attribute jobLink, attribute jobTitle, attribute numberOfEmployees, attribute proficiencyLevels, attribute requiredEducationLevel, attribute requiredLanguages, attribute requiredSkills, attribute summary, attribute workFormatSelection, interface def JobPostingSubmissionInterface, part def EmployerRegistration, part def JobPosting, part def WebApplicationInterface, part employerRegistration, part jobPosting, part webApplicationInterface, port def JobPostingSubmissionInterfacePort |
| FR-56 | unreviewed | original | 5 | action def ClassifyJobPosting, action def ValidateJobPostingStructure, constraint def DataCompliance, interface def JobPostingDataInputInterface, port def JobPostingDataInputInterfacePort |
| FR-57 | unreviewed | original | 6 | action def CreateJobPosting, action def ManageCompanyProfile, action def PublishJobPosting, action def UpdateJobPostingDetails, interface def JobPostingManagementInterface, port def JobPostingManagementInterfacePort |
| FR-58 | unreviewed | original | 3 | action def RenewJobPosting, action def SetJobPostingExpiration, state def JobPostingLifecycle |
| FR-59 | unreviewed | original | 9 | action def BrowseJobListings, action def DisplayRecommendationInsights, action def MatchJobSeekersToPostings, interface def JobPostingDataAccess, interface def JobSearchInterface, interface def JobSearchResultsRetrieval, port def JobPostingDataAccessPort, port def JobSearchInterfacePort, port def JobSearchResultsRetrievalPort |
| FR-60 | unreviewed | original | 4 | action def BrowseJobListings, action def ViewJobPostings, interface def SearchInterfaceForBasicAndAdvancedSearchModes, port def SearchInterfaceForBasicAndAdvancedSearchModesPort |
| FR-61 | unreviewed | original | 1 | action def MatchJobSeekersToPostings |
| FR-62 | unreviewed | original | 3 | action def BrowseJobListings, interface def JobSearchInterface, port def JobSearchInterfacePort |
| FR-63 | unreviewed | original | 6 | action def DisplayRecommendationInsights, action def DisplaySearchResults, interface def DisplayRecommendedJobsUponLogin, interface def DisplaySearchResultsWithRankingAndSorting, port def DisplayRecommendedJobsUponLoginPort, port def DisplaySearchResultsWithRankingAndSortingPort |
| FR-64 | unreviewed | original | 10 | action def SaveJobToFavorites, action def ViewSavedFavorites, attribute jobId, attribute userId, part def FavoritesManager, part def JobPosting, part def JobSeekerProfile, part favoritesManager, part jobPosting, part jobSeekerProfile |
| FR-65 | unreviewed | original | 4 | action def MonitorJobPostings, action def ReceiveMatchingJobNotifications, action def SaveSearchCriteria, state def SavedSearchLifecycle |
| FR-66 | unreviewed | original | 8 | action def SaveJobToFavorites, action def SaveSearchCriteria, attribute savedJobsList, attribute savedSearchFilters, part def FavoritesManager, part def UserProfile, part favoritesManager, part userProfile |
| FR-67 | unreviewed | original | 4 | action def RenewJobPosting, action def SetJobPostingExpiration, action def SuspendJobOfferings, action def UpdateJobPostingDetails |
| FR-68 | unreviewed | original | 5 | action def SetJobPostingExpiration, action def SuspendJobOfferings, action def UpdateJobPostingDetails, action def ViewJobPostings, state def JobPostingLifecycle |
| FR-69 | unreviewed | original | 4 | action def MaintainAuditLog, attribute statusChangeHistory, part auditLog, part def AuditLog |
| FR-70 | unreviewed | original | 8 | action def MatchJobSeekersToPostings, attribute matchingAlgorithmType, part def JobPosting, part def JobSeekerProfile, part def MatcherService, part jobPosting, part jobSeekerProfile, part matcherService |
| FR-71 | unreviewed | original | 1 | action def MatchJobSeekersToPostings |
| FR-72 | unreviewed | original | 9 | action def GenerateShortlistsForPostings, action def MatchJobSeekersToPostings, attribute topNLimit, part def JobPosting, part def JobSeekerProfile, part def MatcherService, part jobPosting, part jobSeekerProfile, part matcherService |
| FR-73 | unreviewed | original | 6 | action def ClassifyJobPosting, action def ExtractInformationFromResumes, action def MatchJobSeekersToPostings, attribute processingMode, part def NLPEngine, part nlpEngine |
| FR-74 | unreviewed | original | 2 | action def ClassifyJobPosting, action def ExtractInformationFromResumes |
| FR-75 | unreviewed | original | 3 | action def ManageSystemConfiguration, interface def MatchThresholdConfigurationInterface, port def MatchThresholdConfigurationInterfacePort |
| FR-76 | unreviewed | original | 3 | action def DisplayRecommendationInsights, action def MatchJobSeekersToPostings, state def JobPostingRanking |
| FR-77 | unreviewed | original | 10 | action def GenerateShortlistsForPostings, action def MatchJobSeekersToPostings, interface def EmployerToMatcherServiceInterface, interface def JobSeekerToMatcherServiceInterface, interface def MatcherServiceToEmployerInterfaceInterface, interface def MatcherServiceToJobSeekerInterfaceInterface, port def EmployerToMatcherServiceInterfacePort, port def JobSeekerToMatcherServiceInterfacePort, port def MatcherServiceToEmployerInterfaceInterfacePort, port def MatcherServiceToJobSeekerInterfaceInterfacePort |
| FR-78 | unreviewed | original | 3 | action def ConfigureMatchingParameters, interface def MatchingParameterConfigurationInterface, port def MatchingParameterConfigurationInterfacePort |
| FR-79 | unreviewed | original | 7 | action def ExtractInformationFromResumes, action def UpdateUserProfileWithExtractedData, attribute parsingCapability, part def JobSeekerProfile, part def NLPEngine, part jobSeekerProfile, part nlpEngine |
| FR-80 | unreviewed | original | 11 | action def ExtractInformationFromResumes, action def UpdateUserProfileWithExtractedData, attribute extractedAchievements, attribute extractedCertifications, attribute extractedContactInformation, attribute extractedEducationHistory, attribute extractedPersonalDetails, attribute extractedSkills, attribute extractedWorkExperience, part def NLPEngine, part nlpEngine |
| FR-81 | unreviewed | original | 4 | action def SupportMultilingualInterface, action def UtilizeLanguageSpecificAIFunctions, interface def LanguageAwareResumeParsingInterface, port def LanguageAwareResumeParsingInterfacePort |
| FR-82 | unreviewed | original | 2 | action def ExtractInformationFromResumes, action def UpdateUserProfileWithExtractedData |
| FR-83 | unreviewed | original | 5 | action def ExtractInformationFromResumes, interface def ConfidenceScoreProvisionInterface, interface def ManualVerificationHighlightingInterface, port def ConfidenceScoreProvisionInterfacePort, port def ManualVerificationHighlightingInterfacePort |
| FR-84 | unreviewed | original | 7 | action def ReviewExtractedResumeData, action def UpdateUserProfileWithCorrections, attribute parsedInformation, part def JobSeekerProfile, part def WebApplicationInterface, part jobSeekerProfile, part webApplicationInterface |
| FR-85 | unreviewed | original | 2 | action def DisplayRecommendationInsights, action def MatchJobSeekersToPostings |
| FR-86 | unreviewed | original | 2 | action def GenerateShortlistsForPostings, action def MatchJobSeekersToPostings |
| FR-87 | unreviewed | original | 2 | action def DisplayRecommendationInsights, action def MatchJobSeekersToPostings |
| FR-88 | unreviewed | original | 11 | action def DisplayRecommendationInsights, action def MatchJobSeekersToPostings, attribute interestHistory, part dashboard, part def Dashboard, part def JobPosting, part def JobSeekerProfile, part def MatcherService, part jobPosting, part jobSeekerProfile, part matcherService |
| FR-89 | unreviewed | original | 5 | action def DisplayRecommendationInsights, action def InputJobPreferences, action def MatchJobSeekersToPostings, interface def RecommendationInputInterface, port def RecommendationInputInterfacePort |
| FR-90 | unreviewed | original | 1 | action def GenerateShortlistsForPostings |
| FR-91 | unreviewed | original | 11 | action def GenerateShortlistsForPostings, action def MatchJobSeekersToPostings, attribute matchQualityRanking, part def JobPosting, part def JobSeekerProfile, part def MatcherService, part def NLPEngine, part jobPosting, part jobSeekerProfile, part matcherService, part nlpEngine |
| FR-92 | unreviewed | original | 6 | action def ConfigureMatchingParameters, attribute minimumQualificationThresholds, part def EmployerRegistration, part def JobPosting, part employerRegistration, part jobPosting |
| FR-93 | unreviewed | original | 3 | action def SearchCandidateDatabase, interface def CandidateSearchInterface, port def CandidateSearchInterfacePort |
| FR-94 | unreviewed | original | 2 | action def MatchJobSeekersToPostings, action def RestrictDataVisibilityByRole |
| FR-95 | unreviewed | original | 2 | action def DisplayRecommendationInsights, action def MatchJobSeekersToPostings |
| FR-96 | unreviewed | original | 1 | action def GenerateShortlistsForPostings |
| FR-97 | unreviewed | original | 4 | action def RecordJobPostingSource, action def SynchronizeJobData, interface def ExternalJobSiteIntegrationInterface, port def ExternalJobSiteIntegrationInterfacePort |
| FR-98 | unreviewed | original | 4 | action def ProvideAPISchema, action def SynchronizeJobData, interface def ExternalJobDataSynchronizationAPI, port def ExternalJobDataSynchronizationAPIPort |
| FR-99 | unreviewed | original | 3 | action def StandardizeJobPostings, interface def JobPostingDataStandardizationInterface, port def JobPostingDataStandardizationInterfacePort |
| NFR-01 | unreviewed | original | 1 | constraint def PageLoadTime |
| NFR-02 | unreviewed | original | 2 | action def DisplaySearchResults, constraint def SearchResultLatency |
| NFR-03 | unreviewed | original | 2 | action def MatchJobSeekersToPostings, constraint def AIMatchingPerformance |
| NFR-04 | unreviewed | original | 2 | action def ProcessBatchOperations, constraint def BatchOperationProcessingTime |
| NFR-05 | unreviewed | original | 1 | constraint def ResponseTimeDegradation |
| NFR-06 | unreviewed | original | 1 | constraint def ConcurrentUserSupport |
| NFR-07 | unreviewed | original | 1 | constraint def ConcurrentUserSupport |
| NFR-08 | unreviewed | original | 2 | action def ProcessBatchOperations, constraint def JobApplicationProcessingRate |
| NFR-09 | unreviewed | original | 1 | constraint def JobPostingIngestionRate |
| NFR-10 | unreviewed | original | 1 | constraint def EmployerRegistrationThroughput |
| NFR-101 | unreviewed | original | 3 | attribute documentationVersion, part def TechnicalDocumentationRepository, part technicalDocumentationRepository |
| NFR-102 | unreviewed | original | 12 | action def DisplayCurrentLogins, action def MaintainAuditLog, action def MonitorSystemActivity, attribute alertStatus, attribute logEntries, attribute metricValue, part auditLog, part def AuditLog, part def IntrusionDetectionSystem, part def MetricsTracker, part intrusionDetectionSystem, part metricsTracker |
| NFR-103 | unreviewed | original | 5 | action def ConfigureMatchingParameters, action def ConfigureReportTemplates, action def ManageCompanyProfile, action def ManageSystemConfiguration, constraint def ConfigurationChangeSupport |
| NFR-104 | unreviewed | original | 2 | action def ExecuteAutomatedTests, constraint def CodeCoverage |
| NFR-105 | unreviewed | original | 4 | action def ManageSystemArtifactsVersions, attribute versionControlEnabled, part def SystemConfiguration, part systemConfiguration |
| NFR-106 | unreviewed | original | 4 | attribute hostingEnvironment, constraint def DeploymentFlexibility, part def SystemConfiguration, part systemConfiguration |
| NFR-107 | unreviewed | original | 4 | attribute deploymentConsistency, constraint def ConsistentDeployment, part containerizationTechnology, part def ContainerizationTechnology |
| NFR-109 | unreviewed | original | 5 | attribute databaseAbstractionLayer, interface def DatabaseAbstractionInterface, part dataManagementService, part def DataManagementService, port def DatabaseAbstractionInterfacePort |
| NFR-11 | unreviewed | original | 1 | constraint def CPUUtilization |
| NFR-110 | unreviewed | original | 5 | attribute documentationType, interface def DeploymentProcedureDocumentationInterface, part def TechnicalDocumentationRepository, part technicalDocumentationRepository, port def DeploymentProcedureDocumentationInterfacePort |
| NFR-111 | unreviewed | original | 3 | action def ExecuteAutomatedTests, action def ManageSystemConfiguration, state def DeploymentLifecycle |
| NFR-112 | unreviewed | original | 3 | constraint def BrowserCompatibility, interface def WebBrowserCompatibilityInterface, port def WebBrowserCompatibilityInterfacePort |
| NFR-113 | unreviewed | original | 3 | constraint def BrowserCompatibility, interface def BrowserCompatibilityInterface, port def BrowserCompatibilityInterfacePort |
| NFR-114 | unreviewed | original | 3 | constraint def MobileBrowserCompatibility, interface def MobileBrowserCompatibilityInterface, port def MobileBrowserCompatibilityInterfacePort |
| NFR-115 | unreviewed | original | 2 | interface def EmailNotificationDeliveryInterface, port def EmailNotificationDeliveryInterfacePort |
| NFR-116 | unreviewed | original | 4 | action def ExportDataToFiles, action def ImportDataFromFiles, interface def DataImportExportInterface, port def DataImportExportInterfacePort |
| NFR-117 | unreviewed | original | 2 | interface def ExternalSystemIntegrationInterface, port def ExternalSystemIntegrationInterfacePort |
| NFR-12 | unreviewed | original | 1 | constraint def MemoryUtilization |
| NFR-121 | unreviewed | original | 4 | action def MaintainAuditLog, action def MaintainSystemAvailability, action def PerformFullDataBackup, action def PerformIncrementalDataBackup |
| NFR-122 | unreviewed | original | 2 | action def ManageSystemConfiguration, action def UpdateRegulatoryPolicies |
| NFR-125 | unreviewed | original | 4 | action def DisplayJobSourceTraceability, action def RecordJobPostingSource, interface def ThirdPartyContentAttributionInterface, port def ThirdPartyContentAttributionInterfacePort |
| NFR-126 | unreviewed | original | 1 | action def DetectCopyrightInfringement |
| NFR-127 | unreviewed | original | 2 | action def DefineRecoveryTimeObjective, constraint def SystemAvailabilitySLA |
| NFR-128 | unreviewed | original | 3 | action def DefineEscalationProcedures, constraint def IncidentResolutionTime, constraint def IncidentResponseTime |
| NFR-129 | unreviewed | original | 2 | action def DefineEscalationProcedures, constraint def SLADefinitionAndDocumentation |
| NFR-13 | unreviewed | original | 1 | constraint def StorageCapacity |
| NFR-130 | unreviewed | original | 10 | action def DefineEscalationProcedures, action def GenerateSystemMetrics, attribute reportType, attribute slaMetric, part dashboard, part def Dashboard, part def MetricsTracker, part def ReportLibrary, part metricsTracker, part reportLibrary |
| NFR-131 | unreviewed | original | 2 | action def DefineEscalationProcedures, state def SLAViolationEscalation |
| NFR-132 | unreviewed | original | 18 | action def MaintainAuditLog, action def MaintainSystemAvailability, action def MonitorSystemActivity, attribute detectionLog, attribute logEntries, attribute loginEventLog, attribute metricData, attribute mitigationLog, part auditLog, part def AuditLog, part def IntrusionDetectionSystem, part def IntrusionPreventionSystem, part def LoginTracker, part def MetricsTracker, part intrusionDetectionSystem, part intrusionPreventionSystem, part loginTracker, part metricsTracker |
| NFR-133 | unreviewed | original | 2 | action def GenerateSystemMetrics, action def MonitorSystemActivity |
| NFR-134 | unreviewed | original | 4 | action def DetectSecurityThreats, action def GenerateSystemMetrics, action def MonitorSystemActivity, state def AlertGenerationLifecycle |
| NFR-136 | unreviewed | original | 7 | action def DisplayCurrentLogins, action def DisplayLoginStatistics, action def GenerateSystemMetrics, part dashboard, part def Dashboard, part def MetricsTracker, part metricsTracker |
| NFR-137 | unreviewed | original | 8 | action def MaintainAuditLog, action def MonitorSystemActivity, part auditLog, part def AuditLog, part def IntrusionDetectionSystem, part def MetricsTracker, part intrusionDetectionSystem, part metricsTracker |
| NFR-138 | unreviewed | original | 3 | action def PerformFullDataBackup, action def PerformIncrementalDataBackup, state def BackupLifecycle |
| NFR-139 | unreviewed | original | 2 | action def ExecuteAutomatedTests, state def BackupIntegrityVerification |
| NFR-14 | unreviewed | original | 1 | action def OptimizeDatabaseQueries |
| NFR-140 | unreviewed | original | 6 | action def DefineRecoveryPointObjective, action def DefineRecoveryTimeObjective, action def PerformFullDataBackup, action def PerformIncrementalDataBackup, action def ReplicateDatabase, state def DataRecoveryLifecycle |
| NFR-141 | unreviewed | original | 4 | action def DefineRecoveryPointObjective, action def DefineRecoveryTimeObjective, action def ExecuteAutomatedTests, state def RestorationProcedureDocumentationAndTesting |
| NFR-142 | unreviewed | original | 7 | action def MaintainAuditLog, action def PerformFullDataBackup, action def PerformIncrementalDataBackup, part auditLog, part backupService, part def AuditLog, part def BackupService |
| NFR-143 | unreviewed | original | 19 | action def ConfigureMatchingParameters, action def ConfigureReportTemplates, action def CreateAnnouncements, action def EditAnnouncements, action def GenerateIndustryReports, action def GenerateInteractionReports, action def GenerateRegionReports, action def GenerateSectorReports, action def GenerateSystemMetrics, action def ManageSystemConfiguration, attribute configurationSetting, part administratorAccount, part def AdministratorAccount, part def SiteManagementAccount, part def SystemConfiguration, part def WebApplicationInterface, part siteManagementAccount, part systemConfiguration, part webApplicationInterface |
| NFR-144 | unreviewed | original | 3 | action def RestrictDataVisibilityByRole, action def RestrictFeatureAccessByRole, constraint def RoleBasedAccessForAdministrativeFunctions |
| NFR-145 | unreviewed | original | 3 | action def ManageUserAccounts, action def ManageUserData, action def ProvideUserSupport |
| NFR-146 | unreviewed | original | 2 | action def ManageSystemArtifactsVersions, state def SystemModificationLifecycle |
| NFR-147 | unreviewed | original | 5 | action def DeleteJobOfferings, action def DetectCopyrightInfringement, action def DetectSecurityThreats, action def EditAnnouncements, action def PublishAnnouncements |
| NFR-148 | unreviewed | original | 10 | action def GenerateSystemMetrics, action def MonitorSystemActivity, attribute healthCheckStatus, attribute systemHealthMetrics, part dashboard, part def Dashboard, part def MetricsTracker, part def SystemConfiguration, part metricsTracker, part systemConfiguration |
| NFR-149 | unreviewed | original | 2 | action def DisplayContextSensitiveHelp, action def ProvideUserSupport |
| NFR-15 | unreviewed | original | 1 | action def CacheJobPostingData |
| NFR-150 | unreviewed | original | 3 | attribute documentationContent, part def TechnicalDocumentationRepository, part technicalDocumentationRepository |
| NFR-151 | unreviewed | original | 2 | part def TechnicalDocumentationRepository, part technicalDocumentationRepository |
| NFR-152 | unreviewed | original | 2 | interface def APIDocumentationProvisionInterface, port def APIDocumentationProvisionInterfacePort |
| NFR-153 | unreviewed | original | 7 | attribute configurationParameters, interface def ConfigurationParameterDocumentationInterface, part def SystemConfiguration, part def TechnicalDocumentationRepository, part systemConfiguration, part technicalDocumentationRepository, port def ConfigurationParameterDocumentationInterfacePort |
| NFR-154 | unreviewed | original | 1 | action def ProvideUserSupport |
| NFR-157 | unreviewed | original | 3 | action def DetectUserLanguage, interface def DateAndTimeFormattingInterface, port def DateAndTimeFormattingInterfacePort |
| NFR-16 | unreviewed | original | 3 | attribute maxInstanceCount, part def NetworkInfrastructure, part networkInfrastructure |
| NFR-161 | unreviewed | original | 1 | action def DetectCopyrightInfringement |
| NFR-162 | unreviewed | original | 2 | action def DetectUserLanguage, action def DisplayMeaningfulErrorMessages |
| NFR-17 | unreviewed | original | 6 | attribute bandwidthCapacity, attribute resourceCapacity, part aiProcessingInfrastructure, part def AIProcessingInfrastructure, part def NetworkInfrastructure, part networkInfrastructure |
| NFR-18 | unreviewed | original | 8 | attribute numberOfProfiles, constraint def JobSeekerCapacity, part dataManagementService, part def DataManagementService, part def JobSeekerProfile, part def NetworkInfrastructure, part jobSeekerProfile, part networkInfrastructure |
| NFR-19 | unreviewed | original | 6 | attribute employerCount, constraint def EmployerCapacity, part companyProfile, part dataManagementService, part def CompanyProfile, part def DataManagementService |
| NFR-20 | unreviewed | original | 4 | action def CacheJobPostingData, action def OptimizeDatabaseQueries, action def ProcessBatchOperations, constraint def JobPostingCapacity |
| NFR-22 | unreviewed | original | 4 | action def EnableMFAForUsers, action def EnforceMFAForAdministrators, constraint def MFAEnforcementForAdministrators, constraint def MFAOptionForUsers |
| NFR-23 | unreviewed | original | 5 | action def EnforcePasswordPolicy, action def ManagePasswordChanges, constraint def PasswordComplexityEnforcement, constraint def PasswordPolicyEnforcement, constraint def PasswordRotationPolicy |
| NFR-24 | unreviewed | original | 3 | action def RestrictDataVisibilityByRole, action def RestrictFeatureAccessByRole, constraint def RoleBasedAccessControl |
| NFR-25 | unreviewed | original | 7 | action def MaintainAuditLog, attribute logEntries, attribute loginEvent, part auditLog, part def AuditLog, part def LoginTracker, part loginTracker |
| NFR-26 | unreviewed | original | 3 | action def EnforceLoginAttemptLimits, constraint def AccountLockout, state def AccountLoginLifecycle |
| NFR-27 | unreviewed | original | 2 | action def ManageSessionTimeouts, constraint def SessionTimeout |
| NFR-28 | unreviewed | original | 3 | action def SupportThirdPartyAuthentication, interface def ThirdPartyAuthenticationInterface, port def ThirdPartyAuthenticationInterfacePort |
| NFR-29 | unreviewed | original | 2 | action def EncryptSensitiveDataAtRest, constraint def DataEncryptionAtRest |
| NFR-30 | unreviewed | original | 3 | constraint def DataInTransitEncryption, interface def DataInTransitEncryptionInterface, port def DataInTransitEncryptionInterfacePort |
| NFR-31 | unreviewed | original | 2 | action def MaskSensitiveDataInUI, constraint def DataMasking |
| NFR-32 | unreviewed | original | 1 | action def ManageEncryptionKeys |
| NFR-33 | unreviewed | original | 3 | action def DeleteJobOfferings, action def DeleteUserAccount, action def RequestAccountDeletion |
| NFR-34 | unreviewed | original | 2 | action def EncryptSensitiveDataAtRest, constraint def DatabaseEncryption |
| NFR-36 | unreviewed | original | 1 | constraint def DataProtectionCompliance |
| NFR-37 | unreviewed | original | 8 | action def DeletePersonalData, action def ExportPersonalData, action def ViewPersonalData, constraint def DataSubjectRights, interface def PersonalDataDeletionInterface, interface def PersonalDataViewingAndExportInterface, port def PersonalDataDeletionInterfacePort, port def PersonalDataViewingAndExportInterfacePort |
| NFR-38 | unreviewed | original | 2 | action def MaintainAuditLog, constraint def AuditTrail |
| NFR-39 | unreviewed | original | 2 | action def CollectNecessaryUserData, action def LimitDataRetention |
| NFR-40 | unreviewed | original | 2 | action def DisplayPrivacyNotices, action def ObtainDataCollectionConsent |
| NFR-41 | unreviewed | original | 1 | action def LimitDataRetention |
| NFR-42 | unreviewed | original | 1 | action def SupportDataProtectionImpactAssessments |
| NFR-43 | unreviewed | original | 2 | action def LogEmailNotifications, action def MaintainAuditLog |
| NFR-44 | unreviewed | original | 3 | action def MaintainAuditLog, action def MonitorJobSeekerActivities, action def ReceiveRealTimeNotifications |
| NFR-45 | unreviewed | original | 9 | action def DetectSecurityThreats, action def MonitorSystemActivity, action def PreventUnauthorizedAccess, attribute detectionThreshold, attribute preventionPolicy, part def IntrusionDetectionSystem, part def IntrusionPreventionSystem, part intrusionDetectionSystem, part intrusionPreventionSystem |
| NFR-46 | unreviewed | original | 2 | action def DetectSecurityThreats, state def SecurityScanLifecycle |
| NFR-47 | unreviewed | original | 4 | action def DetectSecurityThreats, action def MaintainAuditLog, action def PreventUnauthorizedAccess, state def SecurityIncidentResponse |
| NFR-48 | unreviewed | original | 3 | action def DetectSecurityThreats, action def EnforceLoginAttemptLimits, action def PreventUnauthorizedAccess |
| NFR-49 | unreviewed | original | 2 | action def ManageSystemConfiguration, state def SecurityPatchManagementLifecycle |
| NFR-50 | unreviewed | original | 2 | constraint def SystemAvailability2, state def SystemAvailability |
| NFR-51 | unreviewed | original | 1 | constraint def Availability |
| NFR-52 | unreviewed | original | 1 | state def MaintenanceScheduling |
| NFR-53 | unreviewed | original | 4 | action def CreateAnnouncements, action def PublishAnnouncements, interface def MaintenanceNotificationInterface, port def MaintenanceNotificationInterfacePort |
| NFR-54 | unreviewed | original | 10 | part aiProcessingInfrastructure, part dataManagementService, part def AIProcessingInfrastructure, part def DataManagementService, part def IntrusionDetectionSystem, part def IntrusionPreventionSystem, part def NetworkInfrastructure, part intrusionDetectionSystem, part intrusionPreventionSystem, part networkInfrastructure |
| NFR-55 | unreviewed | original | 1 | action def MaintainSystemAvailability |
| NFR-56 | unreviewed | original | 5 | action def ReplicateDatabase, attribute replicationStrategy, part dataManagementService, part def DataManagementService, state def DatabaseReplicationStatus |
| NFR-57 | unreviewed | original | 4 | action def DistributeTrafficAcrossServers, attribute serverCount, part def LoadBalancer, part loadBalancer |
| NFR-58 | unreviewed | original | 3 | action def MaintainSystemAvailability, action def ReplicateDatabase, state def SystemResilience |
| NFR-59 | unreviewed | original | 2 | action def ImplementCircuitBreakerPatterns, state def ExternalServiceDependencyHealth |
| NFR-60 | unreviewed | original | 4 | action def PerformFullDataBackup, action def PerformIncrementalDataBackup, constraint def DataBackupFrequency, state def DataBackupLifecycle |
| NFR-61 | unreviewed | original | 4 | attribute backupLocationStrategy, constraint def BackupLocationSeparation, part backupService, part def BackupService |
| NFR-62 | unreviewed | original | 3 | action def DefineRecoveryTimeObjective, constraint def RecoveryTimeObjectiveRTOForCriticalFunctions, constraint def RecoveryTimeObjectiveRTOForNonCriticalFunctions |
| NFR-63 | unreviewed | original | 2 | action def DefineRecoveryPointObjective, constraint def DataLossTolerance |
| NFR-64 | unreviewed | original | 2 | constraint def DisasterRecoveryPlan, state def DisasterRecoveryPlanStatus |
| NFR-65 | unreviewed | original | 2 | constraint def DisasterRecoveryDrillFrequency, state def DisasterRecoveryDrillScheduling |
| NFR-66 | unreviewed | original | 3 | action def DisplayMeaningfulErrorMessages, constraint def ErrorMessageContent, constraint def SensitiveInformationExposure |
| NFR-67 | unreviewed | original | 4 | action def MaintainAuditLog, attribute logDetails, part auditLog, part def AuditLog |
| NFR-68 | unreviewed | original | 2 | action def DisplayMeaningfulErrorMessages, state def UserInteractionLifecycle |
| NFR-69 | unreviewed | original | 2 | action def ImplementRetryMechanisms, state def ServiceOperationLifecycle |
| NFR-70 | unreviewed | original | 1 | state def SystemStability |
| NFR-71 | unreviewed | original | 3 | action def DisplayContextSensitiveHelp, action def DisplayMeaningfulErrorMessages, action def DisplayPrivacyNotices |
| NFR-72 | unreviewed | original | 1 | action def SupportMultilingualInterface |
| NFR-73 | unreviewed | original | 7 | action def DisplayContextSensitiveHelp, action def DisplayMeaningfulErrorMessages, action def DisplayPrivacyNotices, attribute informationArchitectureMap, attribute navigationStructure, part def WebApplicationInterface, part webApplicationInterface |
| NFR-74 | unreviewed | original | 2 | interface def InterfaceForConsistentTerminologyAndDesignPatterns, port def InterfaceForConsistentTerminologyAndDesignPatternsPort |
| NFR-75 | unreviewed | original | 3 | action def DisplayContextSensitiveHelp, action def DisplayMeaningfulErrorMessages, state def UserActionFeedback |
| NFR-76 | unreviewed | original | 1 | action def OptimizeUserWorkflows |
| NFR-77 | unreviewed | original | 2 | action def DisplayContextSensitiveHelp, state def HelpAndGuidanceAvailability |
| NFR-78 | unreviewed | original | 1 | constraint def WCAGCompliance |
| NFR-79 | unreviewed | original | 2 | interface def AccessibilityInterface, port def AccessibilityInterfacePort |
| NFR-80 | unreviewed | original | 3 | action def SupportKeyboardNavigation, interface def KeyboardNavigationInterface, port def KeyboardNavigationInterfacePort |
| NFR-82 | unreviewed | original | 3 | action def ProvideTextAlternativesForContent, interface def TextAlternativeProvisionInterface, port def TextAlternativeProvisionInterfacePort |
| NFR-83 | unreviewed | original | 5 | action def DisplayMeaningfulErrorMessages, attribute formElements, attribute labels, part def WebApplicationInterface, part webApplicationInterface |
| NFR-84 | unreviewed | original | 4 | action def HideMovingContent, action def PauseMovingContent, action def StopMovingContent, state def MovingContentVisibilityLifecycle |
| NFR-85 | unreviewed | original | 3 | action def SupportMultilingualInterface, interface def LanguageSupportInterface, port def LanguageSupportInterfacePort |
| NFR-86 | unreviewed | original | 2 | action def SupportMultilingualInterface, state def LanguageSwitching |
| NFR-87 | unreviewed | original | 3 | action def SupportMultilingualInterface, interface def RTLTextDirectionSupport, port def RTLTextDirectionSupportPort |
| NFR-88 | unreviewed | original | 3 | constraint def LocaleFormatting, interface def LocalizationInterfaceForDataFormatting, port def LocalizationInterfaceForDataFormattingPort |
| NFR-89 | unreviewed | original | 2 | interface def TranslationQualityConsistencyInterface, port def TranslationQualityConsistencyInterfacePort |
| NFR-90 | unreviewed | original | 5 | action def SupportMultilingualInterface, interface def MultilingualContentProvisionForJobPostings, interface def MultilingualContentProvisionForUserProfiles, port def MultilingualContentProvisionForJobPostingsPort, port def MultilingualContentProvisionForUserProfilesPort |
| NFR-91 | unreviewed | original | 3 | action def DetectUserLanguage, interface def LanguageDetectionInterface, port def LanguageDetectionInterfacePort |
| NFR-92 | unreviewed | original | 5 | action def DisplayRecommendationInsights, action def GeneratePersonalizedJobRecommendations, action def InputJobPreferences, action def MonitorJobSeekerActivities, state def UserExperiencePersonalization |
| NFR-93 | unreviewed | original | 2 | action def GuideUsersThroughComplexFeatures, state def FeatureVisibility |
| NFR-94 | unreviewed | original | 5 | action def BuildUserProfile, action def GuideUsersThroughComplexFeatures, action def InputEducationDetails, action def InputExperienceDetails, action def InputSkills |
| NFR-95 | unreviewed | original | 2 | action def CollectFeedbackOnHelpContent, state def UserFeedbackCollectionLifecycle |
| NFR-96 | unreviewed | original | 7 | action def GuideUsersThroughComplexFeatures, action def OptimizeUserWorkflows, attribute skillLevel, part def JobSeekerProfile, part def UserProfile, part jobSeekerProfile, part userProfile |
| NFR-97 | unreviewed | original | 2 | action def GuideUsersThroughComplexFeatures, action def OptimizeUserWorkflows |
| NFR-98 | unreviewed | original | 1 | action def ApplyDefaultSettings |
| NFR-99 | unreviewed | original | 3 | attribute configurationSetting, part def SystemConfiguration, part systemConfiguration |
| REQ-0005 | unreviewed | original | 9 | action def ManageCompanyProfile, action def RegisterEmployer, attribute companyName, attribute contactDetails, attribute registrationStatus, part companyProfile, part def CompanyProfile, part def EmployerRegistration, part employerRegistration |
| REQ-0006 | unreviewed | original | 5 | action def DeleteUserAccount, action def DisableUserAccount, action def EnableUserAccount, action def RecoverUserAccount, state def UserAccountLifecycle |
| REQ-0008 | unreviewed | original | 6 | attribute passwordHash, attribute username, part administratorAccount, part def AdministratorAccount, part def SiteManagementAccount, part siteManagementAccount |
| REQ-0009 | unreviewed | original | 2 | action def CreateJobPosting, action def PublishJobPosting |
| REQ-0010 | unreviewed | original | 1 | action def ClassifyJobPosting |
| REQ-0012 | unreviewed | original | 2 | action def DisableUserAccount, action def EnableUserAccount |
| REQ-0013 | unreviewed | original | 10 | action def MatchJobSeekersToPostings, attribute behavior, attribute education, attribute skills, part def JobPosting, part def JobSeekerProfile, part def MatcherService, part jobPosting, part jobSeekerProfile, part matcherService |
| REQ-0017 | unreviewed | original | 3 | action def SynchronizeJobData, interface def ExternalJobDataSynchronizationInterface, port def ExternalJobDataSynchronizationInterfacePort |
| REQ-0018 | unreviewed | original | 2 | interface def GovernmentalDatabaseDataExchangeInterface, port def GovernmentalDatabaseDataExchangeInterfacePort |
| REQ-0024 | unreviewed | original | 4 | action def ManageSystemConfiguration, attribute configurationData, part def SystemConfiguration, part systemConfiguration |
| REQ-0025 | unreviewed | original | 7 | action def SynchronizeJobData, attribute dataStore, attribute retentionPolicy, part backupService, part dataManagementService, part def BackupService, part def DataManagementService |
| REQ-0030 | unreviewed | original | 5 | attribute accessibility, interface def WebApplicationAccessInterface, part def WebApplicationInterface, part webApplicationInterface, port def WebApplicationAccessInterfacePort |
| REQ-0031 | unreviewed | original | 2 | interface def WebInterfacePresentation, port def WebInterfacePresentationPort |
| REQ-0032 | unreviewed | original | 3 | attribute processingCapacity, part aiProcessingInfrastructure, part def AIProcessingInfrastructure |
| REQ-0033 | unreviewed | original | 3 | attribute storageCapacity, part dataManagementService, part def DataManagementService |
| REQ-0034 | unreviewed | original | 7 | action def ManageSystemConfiguration, attribute autoScaling, attribute bandwidth, attribute highAvailability, attribute loadBalancing, part def NetworkInfrastructure, part networkInfrastructure |
| REQ-0036 | unreviewed | original | 5 | action def SynchronizeJobData, interface def IntegrationWithMoLSystem, interface def IntegrationWithPEFSystem, port def IntegrationWithMoLSystemPort, port def IntegrationWithPEFSystemPort |
| REQ-0038 | unreviewed | original | 3 | constraint def WebBrowserAccessibility, interface def WebAccessibilityInterface, port def WebAccessibilityInterfacePort |
| REQ-0039 | unreviewed | original | 2 | action def CacheJobPostingData, action def QueueDataSynchronization |
| REQ-0044 | unreviewed | original | 1 | state def ImplementationLifecycle |
| REQ-0050 | unreviewed | original | 3 | action def DisplayContextSensitiveHelp, interface def ContextSensitiveHelpProvisionInterface, port def ContextSensitiveHelpProvisionInterfacePort |
| REQ-0051 | unreviewed | original | 1 | action def DisplayContextSensitiveHelp |
| REQ-0052 | unreviewed | original | 5 | attribute profileData, part def JobSeekerProfile, part def WebApplicationInterface, part jobSeekerProfile, part webApplicationInterface |
| REQ-0053 | unreviewed | original | 3 | attribute userGuideContent, part def WebApplicationInterface, part webApplicationInterface |
| REQ-0054 | unreviewed | original | 6 | attribute credentials, attribute permissions, part administratorAccount, part def AdministratorAccount, part def WebApplicationInterface, part webApplicationInterface |
| REQ-0056 | unreviewed | original | 4 | attribute contentID, attribute version, part def TrainingContent, part trainingContent |
| REQ-0057 | unreviewed | original | 3 | attribute contentType, part def TrainingContent, part trainingContent |
| REQ-0058 | unreviewed | original | 3 | attribute materialType, part def SystemDemonstrationMaterials, part systemDemonstrationMaterials |
| REQ-0063 | unreviewed | original | 13 | action def DisplayCurrentLogins, action def DisplayLoginStatistics, action def ProvideUserProfileLinks, attribute currentLogins, attribute lastSessions, interface def LoginTrackingInterface, interface def UserProfileRetrievalInterface, part def LoginTracker, part def UserProfile, part loginTracker, part userProfile, port def LoginTrackingInterfacePort, port def UserProfileRetrievalInterfacePort |
| REQ-0064 | unreviewed | original | 4 | action def ManageCompanyProfile, action def RegisterEmployer, part def WebApplicationInterface, part webApplicationInterface |
| REQ-0065 | unreviewed | original | 11 | attribute userInterfaceView, interface def EmployerRegistrationInterface, interface def UserProfileManagementInterface, part def EmployerRegistration, part def UserProfile, part def WebApplicationInterface, part employerRegistration, part userProfile, part webApplicationInterface, port def EmployerRegistrationInterfacePort, port def UserProfileManagementInterfacePort |
| REQ-0067 | unreviewed | original | 6 | action def DisplayApplicationTracking, action def DisplayRecommendationInsights, attribute applicationStatus, attribute recommendationData, part dashboard, part def Dashboard |
| REQ-0068 | unreviewed | original | 4 | interface def MessagingInterface, interface def NotificationInterface, port def MessagingInterfacePort, port def NotificationInterfacePort |
| REQ-0069 | unreviewed | original | 4 | action def ManageCompanyProfile, action def RegisterEmployer, interface def CompanyProfileManagementInterface, port def CompanyProfileManagementInterfacePort |
| REQ-0070 | unreviewed | original | 3 | action def BrowseJobListings, interface def JobListingBrowsingInterface, port def JobListingBrowsingInterfacePort |
| REQ-0071 | unreviewed | original | 7 | action def PromptRegistrationOrLogin, interface def JobApplicationInitiationInterface, interface def ListingSavingInterface, interface def NotificationSubscriptionInterface, port def JobApplicationInitiationInterfacePort, port def ListingSavingInterfacePort, port def NotificationSubscriptionInterfacePort |
| REQ-0072 | unreviewed | original | 1 | action def DisplayContextSensitiveHelp |
| REQ-0073 | unreviewed | original | 9 | action def BrowseJobListings, action def DisplayContextSensitiveHelp, action def DisplayRecommendationInsights, interface def CareerAdviceNewsDisplayInterface, interface def FeaturedOpportunitiesDisplayInterface, interface def JobPostingDisplayInterface, port def CareerAdviceNewsDisplayInterfacePort, port def FeaturedOpportunitiesDisplayInterfacePort, port def JobPostingDisplayInterfacePort |
| REQ-0075 | unreviewed | original | 6 | action def SupportMultilingualInterface, action def UtilizeLanguageSpecificAIFunctions, interface def AIProcessingInterfaceForLanguageSpecificFunctions, interface def MultilingualContentProvisionInterface, port def AIProcessingInterfaceForLanguageSpecificFunctionsPort, port def MultilingualContentProvisionInterfacePort |
| REQ-0076 | unreviewed | original | 2 | action def SupportMultilingualInterface, constraint def WCAGCompliance |
| REQ-0078 | unreviewed | original | 18 | action def DisplayFeaturedOpportunities, action def DisplayLatestJobPostings, action def DisplaySectorBasedNews, attribute layoutStyle, interface def DisplayFeaturedOpportunitiesOnHomepage, interface def DisplayJobPostingsOnHomepage, interface def DisplaySectorBasedNewsAdviceOnHomepage, part contentDeliveryService, part dataManagementService, part def ContentDeliveryService, part def DataManagementService, part def JobPosting, part def WebApplicationInterface, part jobPosting, part webApplicationInterface, port def DisplayFeaturedOpportunitiesOnHomepagePort, port def DisplayJobPostingsOnHomepagePort, port def DisplaySectorBasedNewsAdviceOnHomepagePort |
| REQ-0080 | unreviewed | original | 1 | action def OptimizePublicPagesForSEO |
| REQ-0082 | unreviewed | original | 3 | attribute deviceCompatibility, part def WebApplicationInterface, part webApplicationInterface |
| REQ-0084 | unreviewed | original | 3 | action def SynchronizeJobData, interface def ExternalJobSiteIntegrationInterface, port def ExternalJobSiteIntegrationInterfacePort |
| REQ-0087 | unreviewed | original | 3 | constraint def InterfaceDocumentation, interface def InterfaceDocumentationSpecificationInterface, port def InterfaceDocumentationSpecificationInterfacePort |
| REQ-0089 | unreviewed | original | 2 | interface def WebAccessInterface, port def WebAccessInterfacePort |
| REQ-0090 | unreviewed | original | 3 | action def ReceiveRealTimeNotifications, interface def RealTimeNotificationInterface, port def RealTimeNotificationInterfacePort |
| REQ-0091 | unreviewed | original | 3 | action def SendEmailNotifications, interface def EmailSendingInterface, port def EmailSendingInterfacePort |
| REQ-0092 | unreviewed | original | 2 | interface def SMSNotificationInterface, port def SMSNotificationInterfacePort |
| REQ-0094 | unreviewed | original | 2 | interface def DataExchangeInterface, port def DataExchangeInterfacePort |
| REQ-0097 | unreviewed | original | 2 | interface def LegacySystemIntegrationInterface, port def LegacySystemIntegrationInterfacePort |
| REQ-0099 | unreviewed | original | 2 | interface def SecureCommunicationInterface, port def SecureCommunicationInterfacePort |
| REQ-0100 | unreviewed | original | 8 | attribute dataIsolationLevel, attribute environmentType, constraint def DataIsolation, constraint def EnvironmentSeparation, part dataManagementService, part def DataManagementService, part def SystemConfiguration, part systemConfiguration |
| REQ-0101 | unreviewed | original | 3 | action def MigrateExistingData, interface def DataMigrationInterfaceFromLegacySystems, port def DataMigrationInterfaceFromLegacySystemsPort |
| REQ-0107 | unreviewed | original | 2 | action def SupportMultilingualInterface, action def UtilizeLanguageSpecificAIFunctions |
| REQ-0108 | unreviewed | original | 4 | action def SupportMultilingualInterface, attribute supportedLanguages, part def SystemConfiguration, part systemConfiguration |
| REQ-0109 | unreviewed | original | 5 | attribute localizationData, interface def UITextProvisionInterface, part def WebApplicationInterface, part webApplicationInterface, port def UITextProvisionInterfacePort |
| REQ-0110 | unreviewed | original | 1 | action def SupportMultilingualInterface |
| REQ-0112 | unreviewed | original | 2 | action def SupportMultilingualInterface, action def UtilizeLanguageSpecificAIFunctions |
| REQ-0114 | unreviewed | original | 4 | action def SupportMultilingualInterface, action def UtilizeLanguageSpecificAIFunctions, interface def LanguageVariationSupportInterface, port def LanguageVariationSupportInterfacePort |
| REQ-0115 | unreviewed | original | 4 | action def SupportMultilingualInterface, action def UtilizeLanguageSpecificAIFunctions, interface def ContentDeliveryInterface, port def ContentDeliveryInterfacePort |
| REQ-0117 | unreviewed | original | 4 | action def ManageCompanyProfile, action def RegisterEmployer, part def TrainingContent, part trainingContent |
