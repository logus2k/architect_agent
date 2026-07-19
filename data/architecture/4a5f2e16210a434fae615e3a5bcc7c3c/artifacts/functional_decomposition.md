# Functional Decomposition

| Function | Parent | Description | Requirement |
|---|---|---|---|
| RegisterEmployer | — | Allows a new employer to register within the system. | REQ-0005 |
| ManageCompanyProfile | — | Enables employers to view and update their company profile information. | REQ-0005 |
| EnableUserAccount | — | Activates a user account within the system. | REQ-0006 |
| DisableUserAccount | — | Deactivates a user account within the system. | REQ-0006 |
| DeleteUserAccount | — | Permanently removes a user account from the system. | REQ-0006 |
| RecoverUserAccount | — | Restores a disabled or deleted user account. | REQ-0006 |
| CreateJobPosting | — | Allows users to create a new job posting. | REQ-0009 |
| PublishJobPosting | Create job posting | Makes a created job posting visible to the public. | REQ-0009 |
| ClassifyJobPosting | null | Assigns categories and classifications to a job posting. | REQ-0010 |
| DisableUserAccount | — | Deactivates a user account within the system. | REQ-0012 |
| EnableUserAccount | — | Activates a user account within the system. | REQ-0012 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | REQ-0013 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | REQ-0017 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | REQ-0024 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | REQ-0025 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | REQ-0034 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | REQ-0036 |
| CacheJobPostingData | — | Stores job posting information locally for offline access. | REQ-0039 |
| QueueDataSynchronization | — | Saves updates to be synchronized when connectivity is restored. | REQ-0039 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | REQ-0050 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | REQ-0051 |
| DisplayCurrentLogins | — | Shows a list of users currently logged into the system. | REQ-0063 |
| DisplayLoginStatistics | — | Provides the total count of current logins and historical session data. | REQ-0063 |
| ProvideUserProfileLinks | Display current logins | Offers direct links to the profiles of currently logged-in users. | REQ-0063 |
| RegisterEmployer | — | Allows a new employer to register within the system. | REQ-0064 |
| ManageCompanyProfile | — | Enables employers to view and update their company profile information. | REQ-0064 |
| DisplayApplicationTracking | — | Shows users a dashboard to track the status of their job applications. | REQ-0067 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | REQ-0067 |
| RegisterEmployer | — | Allows a new employer to register within the system. | REQ-0069 |
| ManageCompanyProfile | — | Enables employers to view and update their company profile information. | REQ-0069 |
| BrowseJobListings | — | Allows unregistered users to view available job postings using basic filters. | REQ-0070 |
| PromptRegistrationOrLogin | — | Prompts guest users to register or log in when attempting actions like applying, saving, or subscribing. | REQ-0071 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | REQ-0072 |
| BrowseJobListings | — | Allows unregistered users to view available job postings using basic filters. | REQ-0073 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | REQ-0073 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | REQ-0073 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0075 |
| UtilizeLanguageSpecificAIFunctions | Support multilingual interface | Applies different AI functions and techniques tailored for Arabic language processing. | REQ-0075 |
| UtilizeLanguageSpecificAIFunctions | Support multilingual interface | Applies different AI functions and techniques tailored for Arabic language processing. | REQ-0075 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0076 |
| DisplayLatestJobPostings | — | Shows the most recently added job postings on the homepage. | REQ-0078 |
| DisplayFeaturedOpportunities | — | Highlights specific, promoted job postings on the homepage. | REQ-0078 |
| DisplaySectorBasedNews | — | Presents relevant news or career advice categorized by industry. | REQ-0078 |
| OptimizePublicPagesForSEO | — | Ensures all publicly accessible pages are optimized according to Search Engine Optimization standards. | REQ-0080 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | REQ-0084 |
| ReceiveRealTimeNotifications | — | Establishes a persistent connection to push immediate updates to the user interface. | REQ-0090 |
| SendEmailNotifications | — | Handles the sending of emails for various system communications. | REQ-0091 |
| DefineEscalationProcedures | ManageSystemConfiguration | Establishes the workflow for handling Service Level Agreement violations. | NFR-131 |
| MigrateExistingData | — | Handles the process of transferring data from legacy MoL and PEF systems into the new platform. | REQ-0101 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0107 |
| UtilizeLanguageSpecificAIFunctions | Support Multilingual Interface | Applies different AI functions and techniques tailored for Arabic language processing. | REQ-0107 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0108 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0110 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0112 |
| UtilizeLanguageSpecificAIFunctions | SupportMultilingualInterface | Applies different AI functions and techniques tailored for Arabic language processing. | REQ-0112 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0114 |
| UtilizeLanguageSpecificAIFunctions | Support Multilingual Interface | Applies different AI functions and techniques tailored for Arabic language processing. | REQ-0114 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | REQ-0115 |
| UtilizeLanguageSpecificAIFunctions | SupportMultilingualInterface | Applies different AI functions and techniques tailored for Arabic language processing. | REQ-0115 |
| ManageCompanyProfile | — | Enables employers to view and update their company profile information. | REQ-0117 |
| RegisterEmployer | — | Allows a new employer to register within the system. | REQ-0117 |
| PromptRegistrationOrLogin | — | Prompts guest users to register or log in when attempting actions like applying, saving, or subscribing. | FR-01 |
| EnableUserAccount | — | Activates a user account within the system. | FR-02 |
| PromptRegistrationOrLogin | — | Prompts guest users to register or log in when attempting actions like applying, saving, or subscribing. | FR-03 |
| RegisterEmployer | — | Allows a new employer to register within the system. | FR-03 |
| AcceptResumeUpload | — | Allows users to upload resumes in supported formats like PDF, DOCX, or TXT. | FR-04 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-05 |
| UpdateUserProfileWithExtractedData | Extract information from resumes | Adds the information extracted from the resume to the user's profile. | FR-05 |
| BuildUserProfile | — | Guides job seekers through a staged form to build their profile information. | FR-06 |
| InputEducationDetails | Build user profile | Allows users to enter their educational background, including degree and institution. | FR-06 |
| InputExperienceDetails | Build user profile | Allows users to enter their work history, including company, role, and duration. | FR-06 |
| InputSkills | Build user profile | Allows users to specify their skills, differentiating between primary/secondary and soft/hard skills. | FR-06 |
| InputJobPreferences | Build user profile | Allows users to define their job preferences such as job type, desired salary, and preferred location. | FR-06 |
| BuildUserProfile | — | Guides job seekers through a staged form to build their profile information. | FR-07 |
| InputEducationDetails | BuildUserProfile | Allows users to enter their educational background, including degree and institution. | FR-07 |
| InputExperienceDetails | BuildUserProfile | Allows users to enter their work history, including company, role, and duration. | FR-07 |
| InputSkills | BuildUserProfile | Allows users to specify their skills, differentiating between primary/secondary and soft/hard skills. | FR-07 |
| InputJobPreferences | BuildUserProfile | Allows users to define their job preferences such as job type, desired salary, and preferred location. | FR-07 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-08 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-08 |
| InputJobPreferences | — | Allows users to define their job preferences such as job type, desired salary, and preferred location. | FR-09 |
| SetProfileVisibilityPreferences | — | Allows job seekers to control whether their profile information is publicly visible or private. | FR-10 |
| RequestAccountDeactivation | — | Allows job seekers to request that their account be temporarily deactivated. | FR-10 |
| RequestAccountDeletion | — | Allows job seekers to request the permanent removal of their account. | FR-10 |
| GenerateShareableProfileURL | — | Creates a public, shareable URL for a job seeker's profile. | FR-11 |
| AcceptResumeUpload | — | Allows users to upload resumes in supported formats like PDF, DOCX, or TXT. | FR-12 |
| CreateJobPosting | — | Allows users to create a new job posting. | FR-29 |
| ClassifyJobPosting | — | Assigns categories and classifications to a job posting. | FR-30 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | FR-31 |
| ReviewJobPostingStatus | — | Allows partners to view the status of jobs posted via the API. | FR-32 |
| DisplayLoginStatistics | — | Provides the total count of current logins and historical session data. | FR-33 |
| ProvideAPISchema | — | Makes the current API schema available to external consumers. | FR-34 |
| ValidateJobPostingStructure | — | Checks submitted job postings against defined field validation rules. | FR-34 |
| ManageCompanyProfile | — | Enables employers to view and update their company profile information. | FR-35 |
| RecordJobPostingSource | — | Logs the external job site responsible for creating or modifying a job posting. | FR-36 |
| DisplayJobSourceTraceability | — | Shows the origin of a job posting within the MoL admin dashboard. | FR-36 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-37 |
| DisplayCurrentLogins | — | Shows a list of users currently logged into the system. | FR-37 |
| DisplayLoginStatistics | — | Provides the total count of current logins and historical session data. | FR-37 |
| DisableUserAccount | — | Deactivates a user account within the system. | FR-37 |
| EnableUserAccount | — | Activates a user account within the system. | FR-37 |
| DeleteUserAccount | — | Permanently removes a user account from the system. | FR-37 |
| RecoverUserAccount | — | Restores a disabled or deleted user account. | FR-37 |
| RegisterEmployer | — | Allows a new employer to register within the system. | FR-38 |
| CreateJobPosting | — | Allows users to create a new job posting. | FR-38 |
| BuildUserProfile | — | Guides job seekers through a staged form to build their profile information. | FR-38 |
| DisplayCurrentLogins | — | Shows a list of users currently logged into the system. | FR-39 |
| DisableUserAccount | — | Deactivates a user account within the system. | FR-39 |
| EnableUserAccount | — | Activates a user account within the system. | FR-39 |
| RecoverUserAccount | — | Restores a disabled or deleted user account. | FR-39 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-39 |
| RecoverUserAccount | — | Restores a disabled or deleted user account. | FR-40 |
| ReviewJobPostingStatus | — | Allows partners to view the status of jobs posted via the API. | FR-40 |
| RegisterEmployer | — | Allows a new employer to register within the system. | FR-40 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-41 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-42 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-43 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-44 |
| ViewJobPostings | — | Allows administrators to view both active and inactive job postings. | FR-45 |
| ReviewJobPostingStatus | View job postings | Allows partners to view the status of jobs posted via the API. | FR-45 |
| SuspendJobOfferings | View job postings | Allows administrators to temporarily disable job postings that violate policies. | FR-45 |
| DeleteJobOfferings | View job postings | Allows administrators to permanently remove inappropriate job postings from the system. | FR-45 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-46 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-46 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-46 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-46 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-46 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-46 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-46 |
| PromptRegistrationOrLogin | — | Prompts guest users to register or log in when attempting actions like applying, saving, or subscribing. | FR-49 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-50 |
| RestrictFeatureAccessByRole | — | Controls which features users can access based on their assigned role. | FR-51 |
| RestrictDataVisibilityByRole | — | Ensures users can only view data appropriate for their assigned role. | FR-51 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-52 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-53 |
| CreateJobPosting | — | Allows users to create a new job posting. | FR-54 |
| ValidateJobPostingStructure | CreateJobPosting | Checks submitted job postings against defined field validation rules. | FR-54 |
| PublishJobPosting | CreateJobPosting | Makes a created job posting visible to the public. | FR-54 |
| CreateJobPosting | — | Allows users to create a new job posting. | FR-55 |
| ValidateJobPostingStructure | CreateJobPosting | Checks submitted job postings against defined field validation rules. | FR-55 |
| PublishJobPosting | CreateJobPosting | Makes a created job posting visible to the public. | FR-55 |
| ValidateJobPostingStructure | — | Checks submitted job postings against defined field validation rules. | FR-56 |
| ClassifyJobPosting | — | Assigns categories and classifications to a job posting. | FR-56 |
| ManageCompanyProfile | — | Enables employers to view and update their company profile information. | FR-57 |
| CreateJobPosting | — | Allows users to create a new job posting. | FR-57 |
| PublishJobPosting | — | Makes a created job posting visible to the public. | FR-57 |
| UpdateJobPostingDetails | — | Allows employers to modify the details of an existing job posting. | FR-57 |
| SetJobPostingExpiration | null | Allows employers to set an expiration date for a job posting. | FR-58 |
| RenewJobPosting | null | Allows employers to extend the active period of an existing job posting. | FR-58 |
| BrowseJobListings | — | Allows unregistered users to view available job postings using basic filters. | FR-59 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-59 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-59 |
| BrowseJobListings | — | Allows unregistered users to view available job postings using basic filters. | FR-60 |
| ViewJobPostings | — | Allows administrators to view both active and inactive job postings. | FR-60 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-61 |
| BrowseJobListings | — | Allows unregistered users to view available job postings using basic filters. | FR-62 |
| DisplaySearchResults | — | Shows job postings based on search criteria, including relevance and sorting options. | FR-63 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-63 |
| SaveJobToFavorites | — | Allows users to mark a job posting as a favorite for later review. | FR-64 |
| ViewSavedFavorites | — | Allows users to view a list of job postings they have saved to their favorites. | FR-64 |
| SaveSearchCriteria | — | Allows users to save specific search parameters for future use. | FR-65 |
| MonitorJobPostings | Save search criteria | Continuously checks for new job postings that match saved search criteria. | FR-65 |
| ReceiveMatchingJobNotifications | Monitor job postings | Alerts the user when a new job posting matches their saved search criteria. | FR-65 |
| SaveJobToFavorites | — | Allows users to mark a job posting as a favorite for later review. | FR-66 |
| SaveSearchCriteria | — | Allows users to save specific search parameters for future use. | FR-66 |
| UpdateJobPostingDetails | — | Allows employers to modify the details of an existing job posting. | FR-67 |
| SetJobPostingExpiration | — | Allows employers to set an expiration date for a job posting. | FR-67 |
| RenewJobPosting | — | Allows employers to extend the active period of an existing job posting. | FR-67 |
| SuspendJobOfferings | — | Allows administrators to temporarily disable job postings that violate policies. | FR-67 |
| SetJobPostingExpiration | — | Allows employers to set an expiration date for a job posting. | FR-68 |
| UpdateJobPostingDetails | — | Allows employers to modify the details of an existing job posting. | FR-68 |
| SuspendJobOfferings | — | Allows administrators to temporarily disable job postings that violate policies. | FR-68 |
| ViewJobPostings | — | Allows administrators to view both active and inactive job postings. | FR-68 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-69 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-70 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-71 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-72 |
| GenerateShortlistsForPostings | MatchJobSeekersToPostings | Generates shortlists of top-matching candidates for each job posting to assist employers. | FR-72 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-73 |
| ClassifyJobPosting | — | Assigns categories and classifications to a job posting. | FR-73 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-73 |
| ClassifyJobPosting | — | Assigns categories and classifications to a job posting. | FR-74 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-74 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | FR-75 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-76 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-76 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-77 |
| GenerateShortlistsForPostings | MatchJobSeekersToPostings | Generates shortlists of top-matching candidates for each job posting to assist employers. | FR-77 |
| ConfigureMatchingParameters | — | Allows administrators to adjust the importance of different factors used in job matching. | FR-78 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-79 |
| UpdateUserProfileWithExtractedData | ExtractInformationFromResumes | Adds the information extracted from the resume to the user's profile. | FR-79 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-80 |
| UpdateUserProfileWithExtractedData | Extract information from resumes | Adds the information extracted from the resume to the user's profile. | FR-80 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | FR-81 |
| UtilizeLanguageSpecificAIFunctions | Support Multilingual Interface | Applies different AI functions and techniques tailored for Arabic language processing. | FR-81 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-82 |
| UpdateUserProfileWithExtractedData | ExtractInformationFromResumes | Adds the information extracted from the resume to the user's profile. | FR-82 |
| ExtractInformationFromResumes | — | Uses AI parsing technology to extract data from uploaded resumes. | FR-83 |
| ReviewExtractedResumeData | — | Allows job seekers to review the data extracted from their uploaded resumes. | FR-84 |
| UpdateUserProfileWithCorrections | Review extracted resume data | Allows job seekers to correct and update their profile using the parsed and reviewed data. | FR-84 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-85 |
| MatchJobSeekersToPostings | DisplayRecommendationInsights | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-85 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-86 |
| GenerateShortlistsForPostings | MatchJobSeekersToPostings | Generates shortlists of top-matching candidates for each job posting to assist employers. | FR-86 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-87 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-87 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-88 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-88 |
| InputJobPreferences | — | Allows users to define their job preferences such as job type, desired salary, and preferred location. | FR-89 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-89 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-89 |
| GenerateShortlistsForPostings | — | Generates shortlists of top-matching candidates for each job posting to assist employers. | FR-90 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-91 |
| GenerateShortlistsForPostings | MatchJobSeekersToPostings | Generates shortlists of top-matching candidates for each job posting to assist employers. | FR-91 |
| ConfigureMatchingParameters | — | Allows administrators to adjust the importance of different factors used in job matching. | FR-92 |
| SearchCandidateDatabase | — | Allows employers to search the candidate database using advanced filtering options. | FR-93 |
| RestrictDataVisibilityByRole | — | Ensures users can only view data appropriate for their assigned role. | FR-94 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-94 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | FR-95 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | FR-95 |
| GenerateShortlistsForPostings | — | Generates shortlists of top-matching candidates for each job posting to assist employers. | FR-96 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | FR-97 |
| RecordJobPostingSource | SynchronizeJobData | Logs the external job site responsible for creating or modifying a job posting. | FR-97 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | FR-98 |
| ProvideAPISchema | — | Makes the current API schema available to external consumers. | FR-98 |
| StandardizeJobPostings | — | The system transforms job postings from various sources into a consistent format. | FR-99 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | FR-100 |
| ReceiveRealTimeNotifications | — | Establishes a persistent connection to push immediate updates to the user interface. | FR-100 |
| QueueDataSynchronization | — | Saves updates to be synchronized when connectivity is restored. | FR-101 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-101 |
| QueueDataSynchronization | — | Saves updates to be synchronized when connectivity is restored. | FR-102 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | FR-102 |
| MonitorJobPostingSources | — | Shows the origin of a job posting within the MoL admin dashboard. | FR-103 |
| SynchronizeJobData | — | Updates job posting information from external job sites in real-time. | FR-103 |
| QueueDataSynchronization | — | Saves updates to be synchronized when connectivity is restored. | FR-103 |
| VerifyExternalData | — | Integrates with government databases to verify and enrich data. | FR-104 |
| MigrateExistingData | — | Handles the process of transferring data from legacy MoL and PEF systems into the new platform. | FR-105 |
| VerifyExternalData | — | Integrates with government databases to verify and enrich data. | FR-105 |
| VerifyExternalData | — | Integrates with government databases to verify and enrich data. | FR-106 |
| VerifyExternalData | — | Integrates with government databases to verify and enrich data. | FR-107 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-108 |
| ProvideAPISchema | — | Makes the current API schema available to external consumers. | FR-110 |
| ProvideUserProfileLinks | — | Offers direct links to the profiles of currently logged-in users. | FR-110 |
| ProvideAPISchema | — | Makes the current API schema available to external consumers. | FR-111 |
| ProvideUserProfileLinks | — | Offers direct links to the profiles of currently logged-in users. | FR-111 |
| ProvideAPISchema | — | Makes the current API schema available to external consumers. | FR-112 |
| ProvideAPISchema | — | Makes the current API schema available to external consumers. | FR-113 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-115 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | FR-116 |
| MonitorJobPostingSources | — | Shows the origin of a job posting within the MoL admin dashboard. | FR-117 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | FR-117 |
| SearchCandidateDatabase | — | Allows employers to search the candidate database using advanced filtering options. | FR-117 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | FR-118 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-120 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-120 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-120 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-120 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-120 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-121 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-121 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-121 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-121 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-122 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-122 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-123 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-123 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-124 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-124 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-125 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-125 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-125 |
| TrackEmploymentOutcomes | — | The system tracks the final employment status of job seekers after application. | FR-126 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | FR-126 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-127 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-127 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-127 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-127 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-127 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-128 |
| TrackMatchingAlgorithmPerformance | — | Records and monitors the performance metrics of the job matching algorithm. | FR-129 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | FR-130 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-130 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-131 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-132 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-132 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-132 |
| DisplayLoginStatistics | — | Provides the total count of current logins and historical session data. | FR-132 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-133 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-134 |
| TrackMatchingAlgorithmPerformance | — | Records and monitors the performance metrics of the job matching algorithm. | FR-134 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-135 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-135 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-135 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-135 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-135 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-135 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-135 |
| ConfigureReportTemplates | — | Allows administrators to define and configure templates for system reports. | FR-136 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-137 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-137 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-137 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-137 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-137 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-137 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-137 |
| ConfigureReportTemplates | — | Allows administrators to define and configure templates for system reports. | FR-138 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-138 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-138 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-138 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-138 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-139 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-139 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-139 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-139 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-139 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-139 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-139 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-140 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-140 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-140 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-140 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-140 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-140 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-140 |
| GenerateIndustryReports | — | Allows administrators to generate reports on job postings categorized by industry. | FR-141 |
| GenerateInteractionReports | — | Allows administrators to generate reports on user interactions with job offers. | FR-141 |
| GenerateRegionReports | — | Allows administrators to generate reports on job postings categorized by region. | FR-141 |
| GenerateRegistrationStatistics | — | Allows administrators to generate reports on user registrations. | FR-141 |
| GenerateSearchTrendReports | — | Allows administrators to generate reports on top searches from job seekers and employers. | FR-141 |
| GenerateSectorReports | — | Allows administrators to generate reports on job postings categorized by sector. | FR-141 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | FR-141 |
| RestrictDataVisibilityByRole | — | Ensures users can only view data appropriate for their assigned role. | FR-142 |
| SendEmailNotifications | — | Handles the sending of emails for various system communications. | FR-143 |
| ConfigureReportTemplates | — | Allows administrators to define and configure templates for system reports. | FR-144 |
| ConfigureEmailNotificationPreferences | — | Allows users to set their preferences for receiving email notifications from the system. | FR-145 |
| ConfigureEmailNotificationPreferences | — | Allows users to set their preferences for receiving email notifications from the system. | FR-146 |
| SendEmailNotifications | ConfigureEmailNotificationPreferences | Handles the sending of emails for various system communications. | FR-146 |
| LogEmailNotifications | — | Records all outgoing email notifications sent by the system. | FR-147 |
| ReceiveRealTimeNotifications | — | Establishes a persistent connection to push immediate updates to the user interface. | FR-149 |
| ReceiveMatchingJobNotifications | — | Alerts the user when a new job posting matches their saved search criteria. | FR-149 |
| ReceiveRealTimeNotifications | — | Establishes a persistent connection to push immediate updates to the user interface. | FR-150 |
| GeneratePersonalizedJobRecommendations | — | Presents personalized job recommendations and insights to the user. | FR-151 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | FR-151 |
| ReceiveMatchingJobNotifications | — | Alerts the user when a new job posting matches their saved search criteria. | FR-151 |
| LogEmailNotifications | — | Records all outgoing email notifications sent by the system. | FR-152 |
| ConfigureEmailNotificationPreferences | — | Allows users to set their preferences for receiving email notifications from the system. | FR-153 |
| ReceiveRealTimeNotifications | — | Establishes a persistent connection to push immediate updates to the user interface. | FR-154 |
| SendEmailNotifications | — | Handles the sending of emails for various system communications. | FR-154 |
| ManageUserNotifications | — | Allows users to manage their received notifications, including marking them as read or deleting them. | FR-155 |
| SendSMSNotifications | — | Sends SMS messages for critical updates, including registration and password resets. | FR-156 |
| ConfigureEmailNotificationPreferences | — | Allows users to set their preferences for receiving email notifications from the system. | FR-157 |
| ConfigureMatchingParameters | — | Allows administrators to adjust the importance of different factors used in job matching. | FR-157 |
| ConfigureEmailNotificationPreferences | — | Allows users to set their preferences for receiving email notifications from the system. | FR-158 |
| ConfigureMatchingParameters | — | Allows administrators to adjust the importance of different factors used in job matching. | FR-158 |
| SendSMSNotifications | — | Sends SMS messages for critical updates, including registration and password resets. | FR-158 |
| SendSMSNotifications | — | Sends SMS messages for critical updates, including registration and password resets. | FR-159 |
| PublishNewsContent | — | Allows the system to publish news and updates to the platform. | FR-161 |
| CreateAnnouncements | — | Allows administrators to create new articles or announcements. | FR-162 |
| EditAnnouncements | — | Allows administrators to modify existing articles or announcements. | FR-162 |
| PublishAnnouncements | — | Allows administrators to make created or edited articles and announcements visible to users. | FR-162 |
| SupportRichTextFormatting | — | The system must allow content to be formatted using rich text capabilities. | FR-163 |
| EmbedMediaInContent | — | The system must allow users to include images and other media within content. | FR-163 |
| ClassifyJobPosting | — | Assigns categories and classifications to a job posting. | FR-164 |
| DisplaySectorBasedNews | — | Presents relevant news or career advice categorized by industry. | FR-165 |
| GeneratePersonalizedJobRecommendations | — | Presents personalized job recommendations and insights to the user. | FR-165 |
| PublishNewsContent | — | Allows the system to publish news and updates to the platform. | FR-166 |
| EditAnnouncements | — | Allows administrators to modify existing articles or announcements. | FR-166 |
| ViewAnnouncements | — | Allows users to view archived news and updates with search functionality. | FR-166 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-167 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-167 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-168 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-169 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-170 |
| EditAnnouncements | — | Allows administrators to modify existing articles or announcements. | FR-171 |
| CollectFeedbackOnHelpContent | — | Allows users to provide feedback regarding the effectiveness of the help content displayed. | FR-172 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-173 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | FR-174 |
| EmbedMediaInContent | — | The system must allow users to include images and other media within content. | FR-174 |
| DisplaySearchResults | — | Shows job postings based on search criteria, including relevance and sorting options. | NFR-02 |
| MatchJobSeekersToPostings | — | Compares job seeker profiles against job posting requirements using vector-based matching. | NFR-03 |
| ProcessBatchOperations | — | Handles the execution of batch processes, such as bulk candidate matching, within defined time constraints. | NFR-04 |
| ProcessBatchOperations | — | Handles the execution of batch processes, such as bulk candidate matching, within defined time constraints. | NFR-08 |
| OptimizeDatabaseQueries | — | The system optimizes database queries to minimize I/O operations and response times. | NFR-14 |
| CacheJobPostingData | — | Stores job posting information locally for offline access. | NFR-15 |
| OptimizeDatabaseQueries | — | The system optimizes database queries to minimize I/O operations and response times. | NFR-20 |
| CacheJobPostingData | — | Stores job posting information locally for offline access. | NFR-20 |
| ProcessBatchOperations | — | Handles the execution of batch processes, such as bulk candidate matching, within defined time constraints. | NFR-20 |
| EnforceMFAForAdministrators | — | The system must enforce multi-factor authentication for all administrative accounts. | NFR-22 |
| EnableMFAForUsers | — | The system must allow all users to optionally enable multi-factor authentication. | NFR-22 |
| EnforcePasswordPolicy | — | The system enforces rules regarding password strength, such as minimum length and complexity. | NFR-23 |
| ManagePasswordChanges | Enforce password policy | The system manages the requirement for users to periodically change their passwords. | NFR-23 |
| RestrictFeatureAccessByRole | — | Controls which features users can access based on their assigned role. | NFR-24 |
| RestrictDataVisibilityByRole | — | Ensures users can only view data appropriate for their assigned role. | NFR-24 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-25 |
| EnforceLoginAttemptLimits | — | The system enforces a limit on failed login attempts before locking an account. | NFR-26 |
| ManageSessionTimeouts | — | The system manages the duration after which a user session will automatically expire. | NFR-27 |
| SupportThirdPartyAuthentication | — | The system must support OAuth 2.0 and OpenID Connect for third-party authentication. | NFR-28 |
| EncryptSensitiveDataAtRest | — | The system must encrypt all sensitive data stored in the database using industry-standard algorithms. | NFR-29 |
| MaskSensitiveDataInUI | — | The system masks sensitive information before displaying it in the user interface. | NFR-31 |
| ManageEncryptionKeys | — | The system manages the secure lifecycle of encryption keys used by the platform. | NFR-32 |
| RequestAccountDeletion | — | Allows job seekers to request the permanent removal of their account. | NFR-33 |
| DeleteUserAccount | — | Permanently removes a user account from the system. | NFR-33 |
| DeleteJobOfferings | — | Allows administrators to permanently remove inappropriate job postings from the system. | NFR-33 |
| EncryptSensitiveDataAtRest | — | The system must encrypt all sensitive data stored in the database using industry-standard algorithms. | NFR-34 |
| ViewPersonalData | — | Allows users to view their personal data stored in the system. | NFR-37 |
| ExportPersonalData | — | Allows users to download a copy of their personal data. | NFR-37 |
| DeletePersonalData | — | Allows users to request the deletion of their personal data from the system. | NFR-37 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-38 |
| CollectNecessaryUserData | — | The system collects only the information required for core system functionalities. | NFR-39 |
| LimitDataRetention | — | The system ensures data is not kept longer than necessary for its intended purpose. | NFR-39 |
| ObtainDataCollectionConsent | — | The system must obtain appropriate consent from users regarding data collection and processing. | NFR-40 |
| DisplayPrivacyNotices | — | The system must provide clear privacy notices to users. | NFR-40 |
| LimitDataRetention | — | The system ensures data is not kept longer than necessary for its intended purpose. | NFR-41 |
| SupportDataProtectionImpactAssessments | — | The system must provide functionality to support data protection impact assessments for high-risk processing activities. | NFR-42 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-43 |
| LogEmailNotifications | — | Records all outgoing email notifications sent by the system. | NFR-43 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-44 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | NFR-44 |
| ReceiveRealTimeNotifications | — | Establishes a persistent connection to push immediate updates to the user interface. | NFR-44 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-45 |
| DetectSecurityThreats | Monitor system activity | Identifies potential intrusions or malicious activities within the system. | NFR-45 |
| PreventUnauthorizedAccess | Detect security threats | Takes automated actions to block or mitigate detected security threats. | NFR-45 |
| DetectSecurityThreats | — | Identifies potential intrusions or malicious activities within the system. | NFR-46 |
| DetectSecurityThreats | — | Identifies potential intrusions or malicious activities within the system. | NFR-47 |
| PreventUnauthorizedAccess | DetectSecurityThreats | Takes automated actions to block or mitigate detected security threats. | NFR-47 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-47 |
| EnforceLoginAttemptLimits | — | The system enforces a limit on failed login attempts before locking an account. | NFR-48 |
| DetectSecurityThreats | — | Identifies potential intrusions or malicious activities within the system. | NFR-48 |
| PreventUnauthorizedAccess | — | Takes automated actions to block or mitigate detected security threats. | NFR-48 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | NFR-49 |
| CreateAnnouncements | — | Allows administrators to create new articles or announcements. | NFR-53 |
| PublishAnnouncements | CreateAnnouncements | Allows administrators to make created or edited articles and announcements visible to users. | NFR-53 |
| MaintainSystemAvailability | — | Ensures the system remains operational even when individual components fail. | NFR-55 |
| ReplicateDatabase | — | The system implements database replication to prevent data loss during database failures. | NFR-56 |
| DistributeTrafficAcrossServers | — | The system distributes incoming traffic across multiple servers to prevent any single server from becoming overloaded. | NFR-57 |
| MaintainSystemAvailability | — | Ensures the system remains operational even when individual components fail. | NFR-58 |
| ReplicateDatabase | MaintainSystemAvailability | The system implements database replication to prevent data loss during database failures. | NFR-58 |
| ImplementCircuitBreakerPatterns | — | The system implements circuit breaker patterns for external service dependencies to prevent cascading failures. | NFR-59 |
| PerformFullDataBackup | — | The system performs complete backups of all stored data on a weekly schedule. | NFR-60 |
| PerformIncrementalDataBackup | — | The system performs incremental backups of all stored data daily. | NFR-60 |
| DefineRecoveryTimeObjective | — | The system defines and documents the Recovery Time Objective (RTO) for critical functions. | NFR-62 |
| DefineRecoveryTimeObjective | — | The system defines and documents the Recovery Time Objective (RTO) for critical functions. | NFR-62 |
| DefineRecoveryPointObjective | — | The system defines and documents the Recovery Point Objective (RPO) for data loss tolerance. | NFR-63 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-66 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-67 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-68 |
| ImplementRetryMechanisms | — | The system must implement retry mechanisms to handle transient errors during operations. | NFR-69 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-71 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | NFR-71 |
| DisplayPrivacyNotices | — | The system must provide clear privacy notices to users. | NFR-71 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | NFR-72 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | NFR-73 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-73 |
| DisplayPrivacyNotices | — | The system must provide clear privacy notices to users. | NFR-73 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-75 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | NFR-75 |
| OptimizeUserWorkflows | — | The system streamlines common tasks to reduce the number of steps required for users. | NFR-76 |
| DisplayContextSensitiveHelp | — | Provides relevant help information based on the current system function being used. | NFR-77 |
| SupportKeyboardNavigation | — | Ensures that all system functions are accessible and operable using only keyboard inputs. | NFR-80 |
| ProvideTextAlternativesForContent | — | The system must provide text alternatives for non-text content to ensure accessibility. | NFR-82 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-83 |
| PauseMovingContent | — | Allows users to pause any moving content displayed within the system. | NFR-84 |
| StopMovingContent | — | Allows users to stop any moving content displayed within the system. | NFR-84 |
| HideMovingContent | — | Allows users to hide moving content from the user interface. | NFR-84 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | NFR-85 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | NFR-86 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | NFR-87 |
| SupportMultilingualInterface | — | Provides the system with the capability to operate in multiple languages, specifically Arabic and English. | NFR-90 |
| DetectUserLanguage | — | The system detects the appropriate language based on user settings and location. | NFR-91 |
| GeneratePersonalizedJobRecommendations | — | Presents personalized job recommendations and insights to the user. | NFR-92 |
| DisplayRecommendationInsights | — | Presents personalized job recommendations and insights to the user. | NFR-92 |
| InputJobPreferences | — | Allows users to define their job preferences such as job type, desired salary, and preferred location. | NFR-92 |
| MonitorJobSeekerActivities | — | Tracks various actions performed by job seekers within the system. | NFR-92 |
| GuideUsersThroughComplexFeatures | — | The system presents complex features in manageable steps to prevent user overload. | NFR-93 |
| GuideUsersThroughComplexFeatures | — | The system presents complex features in manageable steps to prevent user overload. | NFR-94 |
| BuildUserProfile | Guide users through complex features | Guides job seekers through a staged form to build their profile information. | NFR-94 |
| InputSkills | Build user profile | Allows users to specify their skills, differentiating between primary/secondary and soft/hard skills. | NFR-94 |
| InputExperienceDetails | Build user profile | Allows users to enter their work history, including company, role, and duration. | NFR-94 |
| InputEducationDetails | Build user profile | Allows users to enter their educational background, including degree and institution. | NFR-94 |
| CollectFeedbackOnHelpContent | — | Allows users to provide feedback regarding the effectiveness of the help content displayed. | NFR-95 |
| GuideUsersThroughComplexFeatures | — | The system presents complex features in manageable steps to prevent user overload. | NFR-96 |
| OptimizeUserWorkflows | — | The system streamlines common tasks to reduce the number of steps required for users. | NFR-96 |
| GuideUsersThroughComplexFeatures | — | The system presents complex features in manageable steps to prevent user overload. | NFR-97 |
| OptimizeUserWorkflows | — | The system streamlines common tasks to reduce the number of steps required for users. | NFR-97 |
| ApplyDefaultSettings | — | The system applies predefined settings to reduce the need for user configuration. | NFR-98 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-102 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-102 |
| DisplayCurrentLogins | — | Shows a list of users currently logged into the system. | NFR-102 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | NFR-103 |
| ConfigureMatchingParameters | ManageSystemConfiguration | Allows administrators to adjust the importance of different factors used in job matching. | NFR-103 |
| ConfigureReportTemplates | ManageSystemConfiguration | Allows administrators to define and configure templates for system reports. | NFR-103 |
| ManageCompanyProfile | ManageSystemConfiguration | Enables employers to view and update their company profile information. | NFR-103 |
| ExecuteAutomatedTests | — | The system runs automated tests to verify functionality. | NFR-104 |
| ManageSystemArtifactsVersions | — | The system must support version control for all system artifacts. | NFR-105 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | NFR-111 |
| ExecuteAutomatedTests | — | The system runs automated tests to verify functionality. | NFR-111 |
| ImportDataFromFiles | — | Allows the system to import data from standard file formats like CSV, JSON, or XML. | NFR-116 |
| ExportDataToFiles | — | Allows the system to export data into standard file formats like CSV, JSON, or XML. | NFR-116 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-121 |
| MaintainSystemAvailability | — | Ensures the system remains operational even when individual components fail. | NFR-121 |
| PerformFullDataBackup | — | The system performs complete backups of all stored data on a weekly schedule. | NFR-121 |
| PerformIncrementalDataBackup | — | The system performs incremental backups of all stored data daily. | NFR-121 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | NFR-122 |
| UpdateRegulatoryPolicies | ManageSystemConfiguration | Allows the system to incorporate and enforce changes in external regulatory requirements. | NFR-122 |
| DisplayJobSourceTraceability | — | Shows the origin of a job posting within the MoL admin dashboard. | NFR-125 |
| RecordJobPostingSource | — | Logs the external job site responsible for creating or modifying a job posting. | NFR-125 |
| DetectCopyrightInfringement | — | The system monitors user content to identify potential copyright violations. | NFR-126 |
| DefineRecoveryTimeObjective | — | The system defines and documents the Recovery Time Objective (RTO) for critical functions. | NFR-127 |
| DefineEscalationProcedures | — | Establishes the workflow for handling Service Level Agreement violations. | NFR-128 |
| DefineEscalationProcedures | — | Establishes the workflow for handling Service Level Agreement violations. | NFR-129 |
| DefineEscalationProcedures | — | Establishes the workflow for handling Service Level Agreement violations. | NFR-130 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | NFR-130 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-132 |
| MaintainSystemAvailability | — | Ensures the system remains operational even when individual components fail. | NFR-132 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-132 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-133 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | NFR-133 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-134 |
| DetectSecurityThreats | MonitorSystemActivity | Identifies potential intrusions or malicious activities within the system. | NFR-134 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | NFR-134 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | NFR-136 |
| DisplayLoginStatistics | — | Provides the total count of current logins and historical session data. | NFR-136 |
| DisplayCurrentLogins | — | Shows a list of users currently logged into the system. | NFR-136 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-137 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-137 |
| PerformFullDataBackup | — | The system performs complete backups of all stored data on a weekly schedule. | NFR-138 |
| PerformIncrementalDataBackup | — | The system performs incremental backups of all stored data daily. | NFR-138 |
| ExecuteAutomatedTests | — | The system runs automated tests to verify functionality. | NFR-139 |
| DefineRecoveryPointObjective | — | The system defines and documents the Recovery Point Objective (RPO) for data loss tolerance. | NFR-140 |
| DefineRecoveryTimeObjective | — | The system defines and documents the Recovery Time Objective (RTO) for critical functions. | NFR-140 |
| PerformFullDataBackup | — | The system performs complete backups of all stored data on a weekly schedule. | NFR-140 |
| PerformIncrementalDataBackup | — | The system performs incremental backups of all stored data daily. | NFR-140 |
| ReplicateDatabase | — | The system implements database replication to prevent data loss during database failures. | NFR-140 |
| DefineRecoveryTimeObjective | — | The system defines and documents the Recovery Time Objective (RTO) for critical functions. | NFR-141 |
| DefineRecoveryPointObjective | — | The system defines and documents the Recovery Point Objective (RPO) for data loss tolerance. | NFR-141 |
| ExecuteAutomatedTests | — | The system runs automated tests to verify functionality. | NFR-141 |
| PerformFullDataBackup | — | The system performs complete backups of all stored data on a weekly schedule. | NFR-142 |
| PerformIncrementalDataBackup | — | The system performs incremental backups of all stored data daily. | NFR-142 |
| MaintainAuditLog | — | Records all administrative actions performed within the system for security and accountability. | NFR-142 |
| ManageSystemConfiguration | — | Allows administrators to configure the overall settings of the system. | NFR-143 |
| ConfigureMatchingParameters | ManageSystemConfiguration | Allows administrators to adjust the importance of different factors used in job matching. | NFR-143 |
| ConfigureReportTemplates | ManageSystemConfiguration | Allows administrators to define and configure templates for system reports. | NFR-143 |
| CreateAnnouncements | ManageSystemConfiguration | Allows administrators to create new articles or announcements. | NFR-143 |
| EditAnnouncements | ManageSystemConfiguration | Allows administrators to modify existing articles or announcements. | NFR-143 |
| GenerateIndustryReports | ManageSystemConfiguration | Allows administrators to generate reports on job postings categorized by industry. | NFR-143 |
| GenerateInteractionReports | ManageSystemConfiguration | Allows administrators to generate reports on user interactions with job offers. | NFR-143 |
| GenerateRegionReports | ManageSystemConfiguration | Allows administrators to generate reports on job postings categorized by region. | NFR-143 |
| GenerateSectorReports | ManageSystemConfiguration | Allows administrators to generate reports on job postings categorized by sector. | NFR-143 |
| GenerateSystemMetrics | ManageSystemConfiguration | Allows administrators to generate reports on overall system metrics. | NFR-143 |
| RestrictFeatureAccessByRole | — | Controls which features users can access based on their assigned role. | NFR-144 |
| RestrictDataVisibilityByRole | — | Ensures users can only view data appropriate for their assigned role. | NFR-144 |
| ManageUserAccounts | — | Allows users and administrators to manage the lifecycle and access rights of user accounts. | NFR-145 |
| ManageUserData | — | Provides mechanisms for users to control and manage their personal and profile information. | NFR-145 |
| ProvideUserSupport | — | Offers various tools and information to assist users with system usage and issues. | NFR-145 |
| ManageSystemArtifactsVersions | — | The system must support version control for all system artifacts. | NFR-146 |
| DetectCopyrightInfringement | — | The system monitors user content to identify potential copyright violations. | NFR-147 |
| DetectSecurityThreats | — | Identifies potential intrusions or malicious activities within the system. | NFR-147 |
| DeleteJobOfferings | — | Allows administrators to permanently remove inappropriate job postings from the system. | NFR-147 |
| EditAnnouncements | — | Allows administrators to modify existing articles or announcements. | NFR-147 |
| PublishAnnouncements | — | Allows administrators to make created or edited articles and announcements visible to users. | NFR-147 |
| MonitorSystemActivity | — | Continuously monitors system operations for suspicious patterns. | NFR-148 |
| GenerateSystemMetrics | — | Allows administrators to generate reports on overall system metrics. | NFR-148 |
| ProvideUserSupport | — | Offers various tools and information to assist users with system usage and issues. | NFR-149 |
| DisplayContextSensitiveHelp | ProvideUserSupport | Provides relevant help information based on the current system function being used. | NFR-149 |
| ProvideUserSupport | — | Offers various tools and information to assist users with system usage and issues. | NFR-154 |
| DetectUserLanguage | — | The system detects the appropriate language based on user settings and location. | NFR-157 |
| DetectCopyrightInfringement | — | The system monitors user content to identify potential copyright violations. | NFR-161 |
| DetectUserLanguage | — | The system detects the appropriate language based on user settings and location. | NFR-162 |
| DisplayMeaningfulErrorMessages | — | The system must present clear and helpful error messages to users. | NFR-162 |
