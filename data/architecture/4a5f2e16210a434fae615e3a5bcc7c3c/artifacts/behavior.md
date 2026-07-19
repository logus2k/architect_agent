# Behavior

| State machine | Subject | States | Transitions | Requirement |
|---|---|---|---|---|
| UserAccountLifecycle | part userProfile | Enabled, Disabled, Deleted, Recoverable | Enabled->Disabled; Enabled->Deleted; Disabled->Enabled; Disabled->Recoverable; Recoverable->Enabled; Recoverable->Deleted | REQ-0006 |
| ImplementationLifecycle | systemConfiguration | basic_functionality_prioritized, full_functionality | basic_functionality_prioritized->full_functionality | REQ-0044 |
| SLAViolationEscalation | systemConfiguration | Normal_Operation, SLA_Violation_Detected, Escalation_Procedure_Active | Normal_Operation->SLA_Violation_Detected; SLA_Violation_Detected->Escalation_Procedure_Active | NFR-131 |
| JobSeekerProfileRecommendation | part jobSeekerProfile | profile_incomplete, profile_complete | profile_incomplete->profile_complete | FR-08 |
| JobSeekerProfileVisibilityAndLifecycle | part jobSeekerProfile | Active, PrivateParam, Deactivated, Deleted | Active->PrivateParam; Active->Deactivated; Active->Deleted | FR-10 |
| JobPostingLifecycle | part jobPosting | active, inactive | active->inactive; active->inactive | FR-45 |
| JobPostingLifecycle | part jobPosting | Active, Expired | Active->Expired; Expired->Active | FR-58 |
| SavedSearchLifecycle | part jobSeekerProfile | saved_search_configured | saved_search_configured->saved_search_configured | FR-65 |
| JobPostingLifecycle | part jobPosting | draft, active, paused, expired, archived | draft->active; active->paused; paused->active; active->expired; active->archived; paused->archived; expired->archived | FR-68 |
| JobPostingRanking | part jobPosting | unranked | — | FR-76 |
| IntegrationSynchronizationLifecycle | part dataManagementService | synchronized, synchronization_failed | synchronized->synchronization_failed | FR-101 |
| SynchronizationLifecycle | part dataManagementService | not_synchronized, scheduled_syncing, on_demand_syncing | not_synchronized->scheduled_syncing; not_synchronized->on_demand_syncing | FR-102 |
| APIVersioning | webApplicationInterface | Versioned | Versioned->Versioned | FR-114 |
| SkillTrendAnalysis | part dataManagementService | Idle | — | FR-123 |
| SkillTrendAnalysis | part matcherService | Idle | — | FR-123 |
| SystemMonitoring | part metricsTracker | monitoring | monitoring->monitoring; monitoring->monitoring; monitoring->monitoring; monitoring->monitoring | FR-130 |
| AlertGenerationLifecycle | part metricsTracker | monitoring | — | FR-133 |
| ReportSchedulingLifecycle | part reportLibrary | unscheduled, scheduled | unscheduled->scheduled | FR-138 |
| AccountLoginLifecycle | part administratorAccount | unlocked, locked | unlocked->locked | NFR-26 |
| SecurityScanLifecycle | part intrusionDetectionSystem | Idle, Scanning | Idle->Scanning | NFR-46 |
| SecurityIncidentResponse | part intrusionDetectionSystem | Normal_Operation | — | NFR-47 |
| SecurityIncidentResponse | part intrusionPreventionSystem | Normal_Operation | — | NFR-47 |
| SecurityPatchManagementLifecycle | part systemConfiguration | unpatched, patching | unpatched->patching; patching->unpatched | NFR-49 |
| SystemAvailability | systemConfiguration | Available_during_standard_operating_hours, Outside_standard_operating_hours | Outside_standard_operating_hours->Available_during_standard_operating_hours; Available_during_standard_operating_hours->Outside_standard_operating_hours | NFR-50 |
| MaintenanceScheduling | systemConfiguration | normal_operation, maintenance_window_scheduled | normal_operation->maintenance_window_scheduled | NFR-52 |
| DatabaseReplicationStatus | dataManagementService | Replicated | Replicated->Replicated | NFR-56 |
| SystemResilience | systemConfiguration | Operational | Operational->Operational | NFR-58 |
| ExternalServiceDependencyHealth | part aiProcessingInfrastructure | Operational, Tripped | Operational->Tripped; Tripped->Operational | NFR-59 |
| ExternalServiceDependencyHealth | part contentDeliveryService | Operational, Tripped | Operational->Tripped; Tripped->Operational | NFR-59 |
| ExternalServiceDependencyHealth | part dataManagementService | Operational, Tripped | Operational->Tripped; Tripped->Operational | NFR-59 |
| ExternalServiceDependencyHealth | part matcherService | Operational, Tripped | Operational->Tripped; Tripped->Operational | NFR-59 |
| ExternalServiceDependencyHealth | part nlpEngine | Operational, Tripped | Operational->Tripped; Tripped->Operational | NFR-59 |
| DataBackupLifecycle | part backupService | Data_Backup_State | Data_Backup_State->Data_Backup_State; Data_Backup_State->Data_Backup_State | NFR-60 |
| DisasterRecoveryPlanStatus | systemConfiguration | documented, tested | documented->tested | NFR-64 |
| DisasterRecoveryDrillScheduling | systemConfiguration | Scheduled | Scheduled->Scheduled | NFR-65 |
| UserInteractionLifecycle | webApplicationInterface | Awaiting_Input | Awaiting_Input->Awaiting_Input | NFR-68 |
| ServiceOperationLifecycle | part aiProcessingInfrastructure | Operational | Operational->Operational | NFR-69 |
| ServiceOperationLifecycle | part dataManagementService | Operational | Operational->Operational | NFR-69 |
| ServiceOperationLifecycle | part contentDeliveryService | Operational | Operational->Operational | NFR-69 |
| ServiceOperationLifecycle | part matcherService | Operational | Operational->Operational | NFR-69 |
| ServiceOperationLifecycle | part nlpEngine | Operational | Operational->Operational | NFR-69 |
| ServiceOperationLifecycle | part notificationCenter | Operational | Operational->Operational | NFR-69 |
| ServiceOperationLifecycle | part smsDeliveryTracker | Operational | Operational->Operational | NFR-69 |
| SystemStability | systemConfiguration | stable | stable->stable | NFR-70 |
| UserActionFeedback | webApplicationInterface | idle | idle->idle | NFR-75 |
| HelpAndGuidanceAvailability | webApplicationInterface | displaying_content | displaying_content->displaying_content | NFR-77 |
| MovingContentVisibilityLifecycle | part contentDeliveryService | moving, paused, stopped, hidden | moving->paused; moving->stopped; moving->hidden; paused->moving; paused->stopped; paused->hidden; stopped->moving; stopped->hidden; hidden->moving | NFR-84 |
| LanguageSwitching | webApplicationInterface | any_language_state | any_language_state->any_language_state | NFR-86 |
| UserExperiencePersonalization | part userProfile | has_preferences, has_behavioral_data | has_preferences->has_behavioral_data | NFR-92 |
| FeatureVisibility | webApplicationInterface | basic_view, advanced_view | basic_view->advanced_view | NFR-93 |
| UserFeedbackCollectionLifecycle | userProfile | feedback_available | feedback_available->feedback_available | NFR-95 |
| DeploymentLifecycle | part systemConfiguration | unconfigured, configured | unconfigured->configured | NFR-111 |
| AlertGenerationLifecycle | part intrusionDetectionSystem | monitoring | — | NFR-134 |
| AlertGenerationLifecycle | part metricsTracker | monitoring | — | NFR-134 |
| BackupLifecycle | part backupService | Scheduled | Scheduled->Scheduled | NFR-138 |
| BackupIntegrityVerification | part backupService | Backup_Integrity_Verified | Backup_Integrity_Verified->Backup_Integrity_Verified | NFR-139 |
| DataRecoveryLifecycle | part dataManagementService | Operational, Recovery | Operational->Recovery | NFR-140 |
| RestorationProcedureDocumentationAndTesting | part backupService | documented, tested | documented->tested | NFR-141 |
| SystemModificationLifecycle | systemConfiguration | unmodified, under_review, approved, implemented | unmodified->under_review; under_review->approved; approved->implemented | NFR-146 |

## Unresolved transitions

- FR-76: transition unranked->ranked references an undeclared state
- FR-123: transition Idle->Analyzing_Trends references an undeclared state
- FR-123: transition Idle->Identifying_Gaps references an undeclared state
- FR-133: transition monitoring->alerting references an undeclared state
- NFR-47: transition Normal_Operation->Incident_Detected references an undeclared state
- NFR-47: transition Normal_Operation->Incident_Detected references an undeclared state
- NFR-134: transition monitoring->alerting references an undeclared state
- NFR-134: transition monitoring->alerting references an undeclared state
- NFR-134: transition monitoring->alerting references an undeclared state
