package Architecture {
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
        attribute isActive : Boolean;
    }
    part def SiteManagementAccount {
        attribute username : String;
        attribute passwordHash : String;
        attribute isActive : Boolean;
    }
    part def SystemConfiguration {
        attribute configurationData : String;
    }
    part def DataManagementService {
        attribute dataStore : String;
    }
    part def BackupManager {
        attribute retentionPolicy : String;
    }
    part def WebApplicationInterface {
        attribute accessibility : Boolean;
    }

    part employerRegistration : EmployerRegistration;
    part companyProfile : CompanyProfile;
    part administratorAccount : AdministratorAccount;
    part siteManagementAccount : SiteManagementAccount;
    part systemConfiguration : SystemConfiguration;
    part dataManagementService : DataManagementService;
    part backupManager : BackupManager;
    part webApplicationInterface : WebApplicationInterface;

    // Interfaces
    port def JobSeekerProfileDataProvisionInterfacePort {
        attribute skill_data : String;
        attribute education_data : String;
        attribute behavior_data : String;
    }
    interface def JobSeekerProfileDataProvisionInterface {
        end supplier : JobSeekerProfileDataProvisionInterfacePort;
        end consumer : JobSeekerProfileDataProvisionInterfacePort;
    }
    port def JobPostingDataProvisionInterfacePort {
        attribute skill_data : String;
        attribute education_data : String;
        attribute behavior_data : String;
    }
    interface def JobPostingDataProvisionInterface {
        end supplier : JobPostingDataProvisionInterfacePort;
        end consumer : JobPostingDataProvisionInterfacePort;
    }
    port def MatchingResultProvisionInterfacePort {
        attribute match_score : Real;
    }
    interface def MatchingResultProvisionInterface {
        end supplier : MatchingResultProvisionInterfacePort;
        end consumer : MatchingResultProvisionInterfacePort;
    }
    port def JobDataSynchronizationInterfacePort {
        attribute Job_Data : String;
    }
    interface def JobDataSynchronizationInterface {
        end supplier : JobDataSynchronizationInterfacePort;
        end consumer : JobDataSynchronizationInterfacePort;
    }
    port def APIBasedDataExchangeWithGovernmentalDatabasesPort {
        attribute API_endpoint_details : String;
    }
    interface def APIBasedDataExchangeWithGovernmentalDatabases {
        end supplier : APIBasedDataExchangeWithGovernmentalDatabasesPort;
        end consumer : APIBasedDataExchangeWithGovernmentalDatabasesPort;
    }
    port def WebApplicationAccessInterfacePort {
        attribute Accessibility : Boolean;
    }
    interface def WebApplicationAccessInterface {
        end supplier : WebApplicationAccessInterfacePort;
        end consumer : WebApplicationAccessInterfacePort;
    }

    // Behavior
    state def UserAccountLifecycle {
        state Enabled;
        state Disabled;
        state Deleted;
        state Recoverable;
        transition Enabled then Disabled;
        transition Disabled then Enabled;
        transition Enabled then Deleted;
        transition Disabled then Recoverable;
        transition Recoverable then Enabled;
        transition Recoverable then Deleted;
    }

}
