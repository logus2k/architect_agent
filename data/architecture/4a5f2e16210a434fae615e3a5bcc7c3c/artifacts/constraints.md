# Constraints

| Constraint | Category | Expression | Description | Requirement |
|---|---|---|---|---|
| WebBrowserAccessibility | resource | WebApplicationInterface.requiresSpecialPlugins == false | The WebApplicationInterface must be accessible via standard web browsers without requiring special plugins or settings. | REQ-0038 |
| WCAGCompliance | safety | WebApplicationInterface.meetsWCAG(2.1_or_later) | The WebApplicationInterface must adhere to WCAG 2.1 or a later standard for accessibility. | REQ-0076 |
| InterfaceDocumentation | resource | documentationExists == true | All software interfaces must be documented with detailed specifications covering data formats, protocols, and security requirements. | REQ-0087 |
| EnvironmentSeparation | resource | Environment == 'development' OR Environment == 'testing' OR Environment == 'production' | The system must maintain separate environments for development, testing, and production. | REQ-0100 |
| DataIsolation | resource | DataIsolation(Environment) == True | Data must be isolated between the development, testing, and production environments. | REQ-0100 |
| PasswordPolicyEnforcement | safety | passwordPolicyConfig.isEnabled == true | The system must enforce strong password policies with configurable parameters. | FR-50 |
| RoleBasedAccessControl | safety | access_control_mechanism == true | The system must restrict access to features and data based on defined user roles. | FR-51 |
| SessionTimeout | resource | sessionTimeoutConfigurable == true | The system shall provide session management with configurable timeout settings. | FR-52 |
| DataCompliance | resource | inputData.conformsTo(Schema.org.JobPosting) | All input data must comply with the Schema.org JobPosting standard for semantic compatibility and structured data integrity. | FR-56 |
| MatchingAlgorithmPerformanceTracking | performance | accuracy_metric == tracked_accuracy | The system must track the accuracy of the matching algorithm. | FR-129 |
| MatchingAlgorithmPerformanceTracking | performance | precision_metric == tracked_precision | The system must track the accuracy of the matching algorithm. | FR-129 |
| MatchingAlgorithmPerformanceTracking | performance | recall_metric == tracked_recall | The system must track the accuracy of the matching algorithm. | FR-129 |
| MatchingAlgorithmPerformanceTracking | performance | user_satisfaction_score == tracked_satisfaction | The system must track the accuracy of the matching algorithm. | FR-129 |
| TechnicalPerformanceTracking | performance | MetricsTracker.tracks(responseTimes, resourceUtilization, errorRates) | The system must track response times, resource utilization, and error rates. | FR-131 |
| RoleBasedAccessControlForReports | safety | user.role == report.allowedRoles | The system must restrict users from viewing reports unless their role permits access to that specific report. | FR-142 |
| PageLoadTime | performance | pageLoadTime < 3 | The system shall provide page load times of less than 3 seconds for standard operations under normal load conditions. | NFR-01 |
| SearchResultLatency | performance | search_result_time <= 2 | The system shall provide search results within 2 seconds for standard search queries. | NFR-02 |
| AIMatchingPerformance | performance | MatcherService.operationTime <= 5 | The system shall complete AI matching operations for individual job-candidate matches within 5 seconds. | NFR-03 |
| BatchOperationProcessingTime | performance | processingTime(batchOperation) <= 2 minutes | The system shall process batch operations within a timeframe proportional to the batch size, not exceeding 2 minutes for standard operations. | NFR-04 |
| ResponseTimeDegradation | performance | response_time_degradation <= 0.50 | The system's response time degradation must not exceed 50% during peak load periods. | NFR-05 |
| ConcurrentUserSupport | performance | concurrentUsers >= 1000 | The system must support at least 1,000 concurrent users during normal operations. | NFR-06 |
| ConcurrentUserSupport | performance | concurrentUsers >= 5000 | The system must support at least 1,000 concurrent users during normal operations. | NFR-07 |
| JobApplicationProcessingRate | performance | jobApplicationsProcessedPerMinute >= 100 | The system must process a minimum of 100 job applications per minute during peak periods. | NFR-08 |
| JobPostingIngestionRate | performance | dailyNewJobPostings >= 500 | The system must support a minimum rate of 500 new job postings per day. | NFR-09 |
| EmployerRegistrationThroughput | performance | dailyRegistrations >= 1000 | The system must support at least 1,000 new employer registrations per day. | NFR-10 |
| CPUUtilization | performance | cpu_utilization <= 0.80 | The system must not utilize more than 80% of the CPU capacity during normal operations. | NFR-11 |
| MemoryUtilization | resource | currentMemoryUsage <= 0.80 * availableMemory | The system shall utilize no more than 80% of available memory during normal operations. | NFR-12 |
| StorageCapacity | resource | DataManagementService.storageUsage <= 5TB | The system shall require no more than 5TB of storage for the first year of operation. | NFR-13 |
| JobSeekerCapacity | performance | JobSeekerProfile.count >= 100000 | The system must support a minimum number of registered job seekers without performance degradation. | NFR-18 |
| EmployerCapacity | performance | registeredEmployers >= 10000 | The system must support a minimum of 10,000 registered employers without performance degradation. | NFR-19 |
| JobPostingCapacity | performance | JobPosting.count >= 50000 | The system must support a minimum number of active job postings without performance degradation. | NFR-20 |
| MFAEnforcementForAdministrators | safety | MFA_enabled(AdministratorAccount) == true | The system must enforce multi-factor authentication for all AdministratorAccount. | NFR-22 |
| MFAOptionForUsers | safety | MFA_enabled(UserProfile) == optional | The system must allow users to optionally enable multi-factor authentication for their UserProfile. | NFR-22 |
| PasswordPolicyEnforcement | safety | passwordLength >= minLength | The system must enforce strong password policies with configurable parameters. | NFR-23 |
| PasswordComplexityEnforcement | safety | passwordComplexityCheck == true | The system must enforce password complexity rules. | NFR-23 |
| PasswordRotationPolicy | safety | passwordChangeInterval <= maxInterval | The system must enforce a regular password change frequency. | NFR-23 |
| RoleBasedAccessControl | safety | access_control_mechanism == RBAC | The system must restrict access to features and data based on defined user roles. | NFR-24 |
| AccountLockout | safety | failedLoginAttempts >= lockoutThreshold | The system shall automatically lock accounts after a specified number of failed login attempts. | NFR-26 |
| SessionTimeout | safety | sessionTimeout > 0 | The system shall provide session management with configurable timeout settings. | NFR-27 |
| DataEncryptionAtRest | safety | data_at_rest.encryption_algorithm == "AES-256" \|\| data_at_rest.encryption_algorithm == "equivalent" | All sensitive data must be encrypted when stored. | NFR-29 |
| DataInTransitEncryption | safety | TLS_version >= 1.3 | All data transmitted across the system must be encrypted using TLS 1.3 or a higher protocol version. | NFR-30 |
| DataMasking | safety | dataMaskingApplied == true | Sensitive information displayed in the WebApplicationInterface SHALL be masked. | NFR-31 |
| DatabaseEncryption | safety | database_encryption_enabled == true | The system shall implement database-level encryption for sensitive tables and columns. | NFR-34 |
| DataProtectionCompliance | safety | compliance(PalestinianDataProtectionRegulations) == true | The system must comply with Palestinian data protection regulations. | NFR-36 |
| DataProtectionCompliance | safety | compliance(GDPRPrinciples) == true | The system must comply with Palestinian data protection regulations. | NFR-36 |
| DataSubjectRights | safety | userProfile.canViewData == true | The system must provide mechanisms for users to view their personal data. | NFR-37 |
| DataSubjectRights | safety | userProfile.canExportData == true | The system must provide mechanisms for users to view their personal data. | NFR-37 |
| DataSubjectRights | safety | userProfile.canDeleteData == true | The system must provide mechanisms for users to view their personal data. | NFR-37 |
| AuditTrail | safety | AuditLog.recordsAllDataAccessAndModifications == true | The system shall maintain audit trails of all data access and modifications. | NFR-38 |
| SystemAvailability2 | performance | availability >= 0.995 | The system must maintain 99.5% availability during standard operating hours. | NFR-50 |
| Availability | performance | availability >= 0.99 | The system must maintain 99.0% availability during non-standard hours. | NFR-51 |
| DataBackupFrequency | resource | BackupService.fullBackupFrequency <= 7 days | The system must perform full data backups at least once per week. | NFR-60 |
| DataBackupFrequency | resource | BackupService.incrementalBackupFrequency <= 1 day | The system must perform full data backups at least once per week. | NFR-60 |
| BackupLocationSeparation | resource | BackupService.location != PrimarySystem.location | The system must store backups in locations geographically separate from the primary system. | NFR-61 |
| RecoveryTimeObjectiveRTOForCriticalFunctions | performance | RTO_critical <= 4 hours | The system must define and document a Recovery Time Objective (RTO) of 4 hours for critical functions. | NFR-62 |
| RecoveryTimeObjectiveRTOForNonCriticalFunctions | performance | RTO_non_critical <= 24 hours | The system must define and document a Recovery Time Objective (RTO) of 24 hours for non-critical functions. | NFR-62 |
| DataLossTolerance | resource | RPO <= 1 hour | The system must ensure that the Recovery Point Objective (RPO) does not exceed 1 hour in a disaster scenario. | NFR-63 |
| DisasterRecoveryPlan | safety | hasDocumentedPlan == true | The system must have a documented disaster recovery plan. | NFR-64 |
| DisasterRecoveryPlan | safety | hasTestedPlan == true | The system must have a documented disaster recovery plan. | NFR-64 |
| DisasterRecoveryDrillFrequency | safety | drillCount >= 2 | The system must conduct disaster recovery drills at least twice per year. | NFR-65 |
| ErrorMessageContent | safety | error_message.isMeaningful == true | The system shall provide error messages to users that are meaningful. | NFR-66 |
| SensitiveInformationExposure | safety | error_message.containsSensitiveInfo == false | The system shall not expose sensitive system information in error messages presented to users. | NFR-66 |
| WCAGCompliance | safety | WebApplicationInterface.accessibilityLevel == "WCAG 2.1 AA" | The WebApplicationInterface must adhere to WCAG 2.1 or a later standard for accessibility. | NFR-78 |
| LocaleFormatting | performance | locale_settings.date_format == selected_locale.date_format AND locale_settings.time_format == selected_locale.time_format AND locale_settings.number_format == selected_locale.number_format | The system must ensure that date, time, and number formats are appropriate for the selected language and locale. | NFR-88 |
| ConfigurationChangeSupport | resource | SystemConfiguration.isConfigurableWithoutCode == true | The system must allow configuration changes without requiring code modifications. | NFR-103 |
| CodeCoverage | performance | codeCoverage >= 0.80 | The system shall implement automated testing with a minimum of 80% code coverage. | NFR-104 |
| DeploymentFlexibility | resource | SystemConfiguration.supportedEnvironments == ["on-premises", "cloud", "hybrid"] | The system must be designed to operate across on-premises, cloud, or hybrid hosting environments. | NFR-106 |
| ConsistentDeployment | resource | ContainerizationTechnology.isUsed == true | The system must use ContainerizationTechnology to ensure consistent deployment across environments. | NFR-107 |
| BrowserCompatibility | performance | WebApplicationInterface.isCompatible(Chrome.latest) && WebApplicationInterface.isCompatible(Firefox.latest) && WebApplicationInterface.isCompatible(Safari.latest) && WebApplicationInterface.isCompatible(Edge.latest) | The WebApplicationInterface must function correctly with the latest versions of Chrome, Firefox, Safari, and Edge. | NFR-112 |
| BrowserCompatibility | performance | isCompatible(WebApplicationInterface, supportedBrowsers[i]) for i in 0..1 | The WebApplicationInterface must function correctly with the latest versions of Chrome, Firefox, Safari, and Edge. | NFR-113 |
| MobileBrowserCompatibility | performance | WebApplicationInterface.supports(iOS) | The WebApplicationInterface must function correctly on iOS mobile browsers. | NFR-114 |
| MobileBrowserCompatibility | performance | WebApplicationInterface.supports(Android) | The WebApplicationInterface must function correctly on iOS mobile browsers. | NFR-114 |
| SystemAvailabilitySLA | performance | SLA_Availability_Defined == true | The system must define and document service level agreements for system availability. | NFR-127 |
| IncidentResponseTime | performance | SLA_ResponseTime >= 0 | The system shall define a Service Level Agreement (SLA) for the time taken to respond to an incident. | NFR-128 |
| IncidentResolutionTime | performance | SLA_ResolutionTime >= 0 | The system shall define a Service Level Agreement (SLA) for the time taken to resolve an incident. | NFR-128 |
| SLADefinitionAndDocumentation | resource | SLA_defined == true && SLA_documented == true | The system must define and document Service Level Agreements (SLAs) for support services. | NFR-129 |
| RoleBasedAccessForAdministrativeFunctions | safety | hasRole(user, requiredRole) == true | The system must enforce role-based access control for all administrative functions. | NFR-144 |

## Unquantified

Requirements implying a limit with no measurable bound:

- REQ-0031: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0032: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- REQ-0033: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- REQ-0034: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0038: standard web browsers
- REQ-0039: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0040: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- REQ-0042: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0043: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- REQ-0044: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0046: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0047: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- REQ-0048: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0072: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0076: support for screen readers
- REQ-0076: appropriate color contrast
- REQ-0076: keyboard navigation
- REQ-0080: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0082: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0087: detailed specifications
- REQ-0099: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- REQ-0100: ['appropriate data isolation']
- REQ-0112: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- REQ-0116: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- FR-50: strong password policies
- FR-51: role-based access control
- FR-52: ['session management']
- FR-56: ['standardized job categories, skills, and qualifications']
- FR-94: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- FR-109: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- FR-118: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- FR-129: ['Matching algorithm performance tracking', 'The system SHOULD track matching algorithm performance including accuracy, precision, recall, and user satisfaction.']
- FR-131: technical performance metrics
- FR-142: ['view reports appropriate to their role']
- FR-148: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- FR-158: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- FR-160: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-01: normal load conditions
- NFR-02: ['standard search queries']
- NFR-03: individual job-candidate matches
- NFR-04: ['timeframe proportional to the batch size']
- NFR-05: ['peak load periods']
- NFR-07: peak periods
- NFR-08: peak periods
- NFR-09: N/A
- NFR-10: N/A
- NFR-11: ['normal operations']
- NFR-12: normal operations
- NFR-13: ['growth plan for subsequent years']
- NFR-14: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-15: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-16: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-17: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-18: ['performance degradation']
- NFR-19: ['performance degradation']
- NFR-20: ['performance degradation']
- NFR-21: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-22: multi-factor authentication
- NFR-23: ['strong password policies']
- NFR-24: role-based access control
- NFR-26: ['specified number of failed login attempts']
- NFR-27: ['appropriate timeout settings']
- NFR-29: industry-standard encryption algorithms
- NFR-30: SHALL
- NFR-31: sensitive information
- NFR-32: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-33: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-34: sensitive tables and columns
- NFR-36: incorporate GDPR principles as best practice
- NFR-37: ['data protection regulations']
- NFR-38: all data access and modifications
- NFR-39: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-40: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-41: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-43: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-44: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-48: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-50: Palestine time
- NFR-51: ['non-standard hours']
- NFR-52: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-54: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-55: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-60: {'intent': 'Data Backup Scope', 'description': 'The system must maintain regular backups of all data.', 'expression': 'true', 'parameters': [], 'category': 'resource'}
- NFR-61: geographically separate
- NFR-62: critical functions
- NFR-62: non-critical functions
- NFR-63: disaster scenario
- NFR-64: documented and tested
- NFR-65: disaster recovery drills
- NFR-66: ['meaningful error messages']
- NFR-70: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-71: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- NFR-72: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-74: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-76: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-78: WCAG 2.1 Level AA standards
- NFR-79: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-81: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-88: ['date, time, and number formats are appropriate for the selected language and locale']
- NFR-89: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-97: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- NFR-98: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-99: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-100: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-103: ['configuration changes']
- NFR-104: automated testing
- NFR-106: ['different hosting environments']
- NFR-107: consistent deployment across environments
- NFR-108: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-112: ['latest versions of major web browsers (Chrome, Firefox, Safari, Edge)']
- NFR-113: ['supported browsers']
- NFR-114: ['Mobile Browser Compatibility', 'The system SHALL be compatible with mobile browsers on iOS and Android platforms.']
- NFR-118: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-119: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-120: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-121: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-122: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-123: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- NFR-124: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-126: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-127: service level agreements (SLAs) for system availability
- NFR-128: ['SLAs for incident response and resolution times']
- NFR-129: SLAs for support services
- NFR-133: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-135: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-144: ['role-based access for administrative functions']
- NFR-151: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-155: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- NFR-156: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-158: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-159: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-160: states no measurable bound (C7=1) — upstream refinement needed; no constraint modelled
- NFR-161: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
- NFR-162: states no measurable bound (C7=2) — upstream refinement needed; no constraint modelled
