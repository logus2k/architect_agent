package RestaurantMenuManager {
    private import ScalarValues::*;

    // Functional decomposition
    action def GenerateFoodDescription;
    action def DisplayItemImages;
    action def SwitchInterfaceLanguage;
    action def DiscardContactFormSubmission;
    action def SetRestaurantWorkingHours;
    action def RequireGoogleAuthentication;
    action def RenderResponsiveUserInterface;
    action def ManageMenu;
    action def AllowUserToUploadImage;
    action def ConfirmReservation;
    action def ResolveTenantIdentity;
    action def AssociateImageIDWithPathMetadata;
    action def DisplayContactForm;
    action def DisplayMapInterface;
    action def DisplayConfigurationSettingsDashboard;

    // Logical architecture
    part def Category {
        attribute id : String;
        attribute name : String;
        attribute description : String;
        attribute order : Integer;
    }
    part def Image {
        attribute description : String;
        attribute itemId : String;
        attribute languageElement : String;
        attribute generatedText : String;
        attribute approvedFlag : Boolean;
        attribute timestamp : String;
    }
    part def Reservation {
        attribute id : String;
        attribute userGoogleId : String;
        attribute tenantId : String;
        attribute dateTime : String;
        attribute numberOfPeople : Integer;
        attribute status : String;
        attribute timestamp : String;
        attribute notes : String;
    }
    part def Tenant;
    part def ContactForm;

    part category : Category;
    part image : Image;
    part reservation : Reservation;
    part tenant : Tenant;
    part contactForm : ContactForm;

    // Interfaces
    port def LanguageSwitchingInterfacePort {
        attribute Language_code : String;
    }
    interface def LanguageSwitchingInterface {
        end supplier : LanguageSwitchingInterfacePort;
        end consumer : LanguageSwitchingInterfacePort;
    }
    port def WorkingHoursSettingInterfacePort {
        attribute Working_hours : String;
    }
    interface def WorkingHoursSettingInterface {
        end supplier : WorkingHoursSettingInterfacePort;
        end consumer : WorkingHoursSettingInterfacePort;
    }
    port def MapInterfacePort {
        attribute Map_data : String;
    }
    interface def MapInterface {
        end supplier : MapInterfacePort;
        end consumer : MapInterfacePort;
    }
    port def AuthenticationInterfacePort {
        attribute Authentication_token : String;
    }
    interface def AuthenticationInterface {
        end supplier : AuthenticationInterfacePort;
        end consumer : AuthenticationInterfacePort;
    }
    port def UserInterfaceRenderingInterfacePort {
        attribute Layout_Size : String;
    }
    interface def UserInterfaceRenderingInterface {
        end supplier : UserInterfaceRenderingInterfacePort;
        end consumer : UserInterfaceRenderingInterfacePort;
    }
    port def UserAuthenticationInterfacePort {
        attribute Authentication_token : String;
    }
    interface def UserAuthenticationInterface {
        end supplier : UserAuthenticationInterfacePort;
        end consumer : UserAuthenticationInterfacePort;
    }
    port def TenantConfigurationManagementInterfacePort {
        attribute Configuration_data : String;
    }
    interface def TenantConfigurationManagementInterface {
        end supplier : TenantConfigurationManagementInterfacePort;
        end consumer : TenantConfigurationManagementInterfacePort;
    }
    port def ImageUploadInterfacePort {
        attribute image_file : String;
    }
    interface def ImageUploadInterface {
        end supplier : ImageUploadInterfacePort;
        end consumer : ImageUploadInterfacePort;
    }
    port def AIDescriptionGenerationInterfacePort {
        attribute specified_language : String;
    }
    interface def AIDescriptionGenerationInterface {
        end supplier : AIDescriptionGenerationInterfacePort;
        end consumer : AIDescriptionGenerationInterfacePort;
    }
    port def TenantIdentityResolutionInterfacePort {
        attribute Path_prefix : String;
    }
    interface def TenantIdentityResolutionInterface {
        end supplier : TenantIdentityResolutionInterfacePort;
        end consumer : TenantIdentityResolutionInterfacePort;
    }
    port def RequestRoutingInterfacePort {
        attribute Request_data : String;
    }
    interface def RequestRoutingInterface {
        end supplier : RequestRoutingInterfacePort;
        end consumer : RequestRoutingInterfacePort;
    }
    port def OAuth2AuthenticationInterfacePort {
        attribute authentication_token : String;
    }
    interface def OAuth2AuthenticationInterface {
        end supplier : OAuth2AuthenticationInterfacePort;
        end consumer : OAuth2AuthenticationInterfacePort;
    }
    port def LanguageSelectionInterfacePort {
        attribute Language_code : String;
    }
    interface def LanguageSelectionInterface {
        end supplier : LanguageSelectionInterfacePort;
        end consumer : LanguageSelectionInterfacePort;
    }
    port def HTTPSEnforcementInterfacePort {
        attribute Protocol : String;
    }
    interface def HTTPSEnforcementInterface {
        end supplier : HTTPSEnforcementInterfacePort;
        end consumer : HTTPSEnforcementInterfacePort;
    }
    port def ReservationInitiationInterfacePort {
        attribute authentication_status : Boolean;
    }
    interface def ReservationInitiationInterface {
        end supplier : ReservationInitiationInterfacePort;
        end consumer : ReservationInitiationInterfacePort;
    }
    port def AuthenticationInterfacePort {
        attribute Authentication_credentials : String;
    }
    interface def AuthenticationInterface {
        end supplier : AuthenticationInterfacePort;
        end consumer : AuthenticationInterfacePort;
    }
    port def RestaurantNameManagementInterfacePort {
        attribute restaurant_name : String;
    }
    interface def RestaurantNameManagementInterface {
        end supplier : RestaurantNameManagementInterfacePort;
        end consumer : RestaurantNameManagementInterfacePort;
    }
    port def LogoManagementInterfacePort {
        attribute logo : String;
    }
    interface def LogoManagementInterface {
        end supplier : LogoManagementInterfacePort;
        end consumer : LogoManagementInterfacePort;
    }
    port def ContactInformationManagementInterfacePort;
    interface def ContactInformationManagementInterface {
        end supplier : ContactInformationManagementInterfacePort;
        end consumer : ContactInformationManagementInterfacePort;
    }
    port def WorkhoursManagementInterfacePort;
    interface def WorkhoursManagementInterface {
        end supplier : WorkhoursManagementInterfacePort;
        end consumer : WorkhoursManagementInterfacePort;
    }
    port def CategoryDataProvisionInterfacePort {
        attribute id : String;
        attribute name : String;
        attribute description : String;
        attribute order : Integer;
    }
    interface def CategoryDataProvisionInterface {
        end supplier : CategoryDataProvisionInterfacePort;
        end consumer : CategoryDataProvisionInterfacePort;
    }
    port def MenuDisplayInterfacePort {
        attribute tenant_id : String;
    }
    interface def MenuDisplayInterface {
        end supplier : MenuDisplayInterfacePort;
        end consumer : MenuDisplayInterfacePort;
    }
    port def LanguageSwitchingInterfacePort {
        attribute Target_Language : String;
    }
    interface def LanguageSwitchingInterface {
        end supplier : LanguageSwitchingInterfacePort;
        end consumer : LanguageSwitchingInterfacePort;
    }
    port def MapDisplayInterfacePort {
        attribute Map_data_source : String;
    }
    interface def MapDisplayInterface {
        end supplier : MapDisplayInterfacePort;
        end consumer : MapDisplayInterfacePort;
    }
    port def ReservationSubmissionInterfacePort {
        attribute reservation_data : String;
    }
    interface def ReservationSubmissionInterface {
        end supplier : ReservationSubmissionInterfacePort;
        end consumer : ReservationSubmissionInterfacePort;
    }
    port def GoogleOAuthAuthenticationInterfacePort {
        attribute authentication_token : String;
    }
    interface def GoogleOAuthAuthenticationInterface {
        end supplier : GoogleOAuthAuthenticationInterfacePort;
        end consumer : GoogleOAuthAuthenticationInterfacePort;
    }
    port def ConfigurationSettingsDashboardAccessInterfacePort {
        attribute Administrator_role : Boolean;
    }
    interface def ConfigurationSettingsDashboardAccessInterface {
        end supplier : ConfigurationSettingsDashboardAccessInterfacePort;
        end consumer : ConfigurationSettingsDashboardAccessInterfacePort;
    }
    port def MenuEntityManagementInterfacePort {
        attribute Menu_entity_data : String;
    }
    interface def MenuEntityManagementInterface {
        end supplier : MenuEntityManagementInterfacePort;
        end consumer : MenuEntityManagementInterfacePort;
    }
    port def ImageUploadInterfacePort {
        attribute image_data : String;
    }
    interface def ImageUploadInterface {
        end supplier : ImageUploadInterfacePort;
        end consumer : ImageUploadInterfacePort;
    }
    port def ReservationSubmissionInterfacePort {
        attribute reservation_details : String;
    }
    interface def ReservationSubmissionInterface {
        end supplier : ReservationSubmissionInterfacePort;
        end consumer : ReservationSubmissionInterfacePort;
    }
    port def TenantConfigurationInterfacePort {
        attribute configuration_settings : String;
    }
    interface def TenantConfigurationInterface {
        end supplier : TenantConfigurationInterfacePort;
        end consumer : TenantConfigurationInterfacePort;
    }
    port def UserAuthenticationInterfacePort {
        attribute Authentication_token : String;
    }
    interface def UserAuthenticationInterface {
        end supplier : UserAuthenticationInterfacePort;
        end consumer : UserAuthenticationInterfacePort;
    }
    port def ManualMenuImageDescriptionInputInterfacePort {
        attribute description_text : String;
    }
    interface def ManualMenuImageDescriptionInputInterface {
        end supplier : ManualMenuImageDescriptionInputInterfacePort;
        end consumer : ManualMenuImageDescriptionInputInterfacePort;
    }

    // Constraints
    constraint def AssetStorageLocation {
        in Tenant : Integer;
        true
    }
    constraint def HTTPSEnforcement {
        true
    }
    constraint def ReservationAccessControl {
        in Reservation : Integer;
        true
    }
    constraint def UniqueIdentifier {
        in menuItem : Integer;
        true
    }
    constraint def UniqueIdentifierStorage {
        true
    }
    constraint def ConcurrentUsers {
        in concurrentUsers : Integer;
        concurrentUsers >= 5
    }

    // Allocations

}
