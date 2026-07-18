# Traceability

| Requirement | Status | Text | Elements | Architecture elements |
|---|---|---|---|---|
| REQ-0005 | unreviewed | original | 9 | action def ManageCompanyProfile, action def RegisterEmployer, attribute companyName, attribute contactDetails, attribute registrationStatus, part companyProfile, part def CompanyProfile, part def EmployerRegistration, part employerRegistration |
| REQ-0006 | unreviewed | original | 5 | action def DeleteUserAccount, action def DisableUserAccount, action def EnableUserAccount, action def RecoverUserAccount, state def UserAccountLifecycle |
| REQ-0008 | unreviewed | original | 7 | attribute isActive, attribute passwordHash, attribute username, part administratorAccount, part def AdministratorAccount, part def SiteManagementAccount, part siteManagementAccount |
| REQ-0009 | unreviewed | original | 2 | action def CreateJobPosting, action def PublishJobPosting |
| REQ-0010 | unreviewed | original | 1 | action def ClassifyJobPosting |
| REQ-0012 | unreviewed | original | 2 | action def DisableUserAccount, action def EnableUserAccount |
| REQ-0013 | unreviewed | original | 7 | action def MatchJobSeekersToPostings, interface def JobPostingDataProvisionInterface, interface def JobSeekerProfileDataProvisionInterface, interface def MatchingResultProvisionInterface, port def JobPostingDataProvisionInterfacePort, port def JobSeekerProfileDataProvisionInterfacePort, port def MatchingResultProvisionInterfacePort |
| REQ-0017 | unreviewed | original | 3 | action def SynchronizeJobData, interface def JobDataSynchronizationInterface, port def JobDataSynchronizationInterfacePort |
| REQ-0018 | unreviewed | original | 2 | interface def APIBasedDataExchangeWithGovernmentalDatabases, port def APIBasedDataExchangeWithGovernmentalDatabasesPort |
| REQ-0024 | unreviewed | original | 4 | action def ManageSystemConfiguration, attribute configurationData, part def SystemConfiguration, part systemConfiguration |
| REQ-0025 | unreviewed | original | 7 | action def SynchronizeJobData, attribute dataStore, attribute retentionPolicy, part backupManager, part dataManagementService, part def BackupManager, part def DataManagementService |
| REQ-0030 | unreviewed | original | 5 | attribute accessibility, interface def WebApplicationAccessInterface, part def WebApplicationInterface, part webApplicationInterface, port def WebApplicationAccessInterfacePort |
