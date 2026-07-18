# Behavior

| State machine | Subject | States | Transitions | Requirement |
|---|---|---|---|---|
| UserAccountLifecycle | part administratorAccount | Enabled, Disabled, Deleted, Recoverable | Enabled->Disabled; Disabled->Enabled; Enabled->Deleted; Disabled->Recoverable; Recoverable->Enabled; Recoverable->Deleted | REQ-0006 |
