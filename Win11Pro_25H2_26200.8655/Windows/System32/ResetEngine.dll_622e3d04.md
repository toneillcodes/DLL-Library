# Binary Specification: ResetEngine.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ResetEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `622e3d04fd7d431703b70203237baa8ba3e99667687ef33ee8cca449f662e37c`
* **Total Exported Functions:** 60

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ResetApplyCloudPartitionLayout` | `0x8620` | 432 | UnwindData |  |
| 2 | `ResetArmBootTrigger` | `0x87E0` | 408 | UnwindData |  |
| 3 | `ResetBareMetalResetAvailable` | `0x8980` | 1,550 | UnwindData |  |
| 4 | `ResetCBMREnabled` | `0x8FA0` | 465 | UnwindData |  |
| 5 | `ResetCBMRLogCollect` | `0x9180` | 1,001 | UnwindData |  |
| 6 | `ResetCBMRPreparation` | `0x9570` | 843 | UnwindData |  |
| 7 | `ResetCancelCleanup` | `0x98D0` | 961 | UnwindData |  |
| 8 | `ResetCancelImageDownload` | `0x9CA0` | 432 | UnwindData |  |
| 9 | `ResetCleanPCBlocked` | `0x9E60` | 507 | UnwindData |  |
| 10 | `ResetClearSession` | `0xA070` | 411 | UnwindData |  |
| 11 | `ResetCloudEndpointAvailable` | `0xA220` | 522 | UnwindData |  |
| 12 | `ResetConnectCloud` | `0xA430` | 608 | UnwindData |  |
| 14 | `ResetCreateSession` | `0xA6A0` | 442 | UnwindData |  |
| 15 | `ResetDisabledByPolicy` | `0xA860` | 350 | UnwindData |  |
| 16 | `ResetDisarmBootTrigger` | `0xA9D0` | 92 | UnwindData |  |
| 17 | `ResetDownloadImage` | `0xAA40` | 458 | UnwindData |  |
| 18 | `ResetDownloadPayload` | `0xAC10` | 401 | UnwindData |  |
| 22 | `ResetExecute` | `0xADB0` | 460 | UnwindData |  |
| 23 | `ResetGetDataVolumes` | `0xAF90` | 937 | UnwindData |  |
| 24 | `ResetGetDiskSpaceRequired` | `0xB340` | 666 | UnwindData |  |
| 26 | `ResetGetRestoredApps` | `0xB5E0` | 1,350 | UnwindData |  |
| 27 | `ResetGetScenarioType` | `0xBB30` | 433 | UnwindData |  |
| 29 | `ResetGetTelemetrySessionID` | `0xBCF0` | 435 | UnwindData |  |
| 30 | `ResetHasCustomizations` | `0xBEB0` | 516 | UnwindData |  |
| 31 | `ResetLoadSession` | `0xC0C0` | 395 | UnwindData |  |
| 32 | `ResetNotifyAcknowledgeWarning` | `0xC260` | 508 | UnwindData |  |
| 33 | `ResetNotifyCancel` | `0xC470` | 329 | UnwindData |  |
| 34 | `ResetNotifyConfirm` | `0xC5C0` | 346 | UnwindData |  |
| 35 | `ResetNotifyExecutionStaged` | `0xC720` | 279 | UnwindData |  |
| 36 | `ResetPayloadConnection` | `0xC840` | 672 | UnwindData |  |
| 37 | `ResetPayloadEnabled` | `0xCAF0` | 408 | UnwindData |  |
| 38 | `ResetPrepareSession` | `0xCC90` | 1,404 | UnwindData |  |
| 41 | `ResetReleaseSession` | `0xD220` | 461 | UnwindData |  |
| 42 | `ResetResumeBitLockerProtection` | `0xD400` | 121 | UnwindData |  |
| 43 | `ResetResumeLog` | `0xD480` | 202 | UnwindData |  |
| 45 | `ResetSetDataPoint` | `0xD550` | 90 | UnwindData |  |
| 46 | `ResetSetStringPoint` | `0xD5B0` | 90 | UnwindData |  |
| 48 | `ResetSetUIDataPoint` | `0xD610` | 90 | UnwindData |  |
| 49 | `ResetSetUIStringPoint` | `0xD670` | 90 | UnwindData |  |
| 50 | `ResetStageOfflineBoot` | `0xD6D0` | 1,061 | UnwindData |  |
| 51 | `ResetSubmitTelemetry` | `0xDB00` | 160 | UnwindData |  |
| 52 | `ResetSuspendSession` | `0xDBB0` | 432 | UnwindData |  |
| 53 | `ResetTraceClientInfo` | `0xDD70` | 445 | UnwindData |  |
| 54 | `ResetUndo` | `0xDF40` | 1,083 | UnwindData |  |
| 55 | `ResetUnstageOfflineBoot` | `0xE390` | 582 | UnwindData |  |
| 56 | `ResetUploadDiagnosticData` | `0xE5E0` | 793 | UnwindData |  |
| 58 | `ResetValidateScenario` | `0xE900` | 1,371 | UnwindData |  |
| 59 | `ResetWillSuspendProtection` | `0xEE70` | 1,274 | UnwindData |  |
| 60 | `ResetWipeSystem` | `0xF370` | 695 | UnwindData |  |
| 13 | `ResetCreateMedia` | `0xF730` | 497 | UnwindData |  |
| 25 | `ResetGetMediaSize` | `0xF930` | 243 | UnwindData |  |
| 39 | `ResetProvisionMedia` | `0xFA30` | 213 | UnwindData |  |
| 40 | `ResetReleaseMedia` | `0xFB10` | 30 | UnwindData |  |
| 19 | `ResetEnterOOBE` | `0x18630` | 1,216 | UnwindData |  |
| 20 | `ResetExecCleanup` | `0x18B00` | 293 | UnwindData |  |
| 21 | `ResetExecOnline` | `0x18C30` | 397 | UnwindData |  |
| 28 | `ResetGetTargetVolume` | `0x18DD0` | 162 | UnwindData |  |
| 44 | `ResetReturnToOldOS` | `0x18E80` | 2,634 | UnwindData |  |
| 47 | `ResetSetTestFlag` | `0x198D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ResetUserLogon` | `0x198E0` | 1,144 | UnwindData |  |
