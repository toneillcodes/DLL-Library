# Binary Specification: ResetEngine.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ResetEngine.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `af5f1c4ce4c4349419a5735661e660832dea01449794a32b1c17e568b238cbb6`
* **Total Exported Functions:** 60

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ResetApplyCloudPartitionLayout` | `0x85E0` | 432 | UnwindData |  |
| 2 | `ResetArmBootTrigger` | `0x87A0` | 408 | UnwindData |  |
| 3 | `ResetBareMetalResetAvailable` | `0x8940` | 1,550 | UnwindData |  |
| 4 | `ResetCBMREnabled` | `0x8F60` | 465 | UnwindData |  |
| 5 | `ResetCBMRLogCollect` | `0x9140` | 1,001 | UnwindData |  |
| 6 | `ResetCBMRPreparation` | `0x9530` | 843 | UnwindData |  |
| 7 | `ResetCancelCleanup` | `0x9890` | 961 | UnwindData |  |
| 8 | `ResetCancelImageDownload` | `0x9C60` | 432 | UnwindData |  |
| 9 | `ResetCleanPCBlocked` | `0x9E20` | 507 | UnwindData |  |
| 10 | `ResetClearSession` | `0xA030` | 411 | UnwindData |  |
| 11 | `ResetCloudEndpointAvailable` | `0xA1E0` | 522 | UnwindData |  |
| 12 | `ResetConnectCloud` | `0xA3F0` | 608 | UnwindData |  |
| 14 | `ResetCreateSession` | `0xA660` | 442 | UnwindData |  |
| 15 | `ResetDisabledByPolicy` | `0xA820` | 350 | UnwindData |  |
| 16 | `ResetDisarmBootTrigger` | `0xA990` | 92 | UnwindData |  |
| 17 | `ResetDownloadImage` | `0xAA00` | 458 | UnwindData |  |
| 18 | `ResetDownloadPayload` | `0xABD0` | 401 | UnwindData |  |
| 22 | `ResetExecute` | `0xAD70` | 460 | UnwindData |  |
| 23 | `ResetGetDataVolumes` | `0xAF50` | 937 | UnwindData |  |
| 24 | `ResetGetDiskSpaceRequired` | `0xB300` | 666 | UnwindData |  |
| 26 | `ResetGetRestoredApps` | `0xB5A0` | 1,350 | UnwindData |  |
| 27 | `ResetGetScenarioType` | `0xBAF0` | 433 | UnwindData |  |
| 29 | `ResetGetTelemetrySessionID` | `0xBCB0` | 435 | UnwindData |  |
| 30 | `ResetHasCustomizations` | `0xBE70` | 516 | UnwindData |  |
| 31 | `ResetLoadSession` | `0xC080` | 395 | UnwindData |  |
| 32 | `ResetNotifyAcknowledgeWarning` | `0xC220` | 508 | UnwindData |  |
| 33 | `ResetNotifyCancel` | `0xC430` | 329 | UnwindData |  |
| 34 | `ResetNotifyConfirm` | `0xC580` | 346 | UnwindData |  |
| 35 | `ResetNotifyExecutionStaged` | `0xC6E0` | 279 | UnwindData |  |
| 36 | `ResetPayloadConnection` | `0xC800` | 672 | UnwindData |  |
| 37 | `ResetPayloadEnabled` | `0xCAB0` | 408 | UnwindData |  |
| 38 | `ResetPrepareSession` | `0xCC50` | 1,404 | UnwindData |  |
| 41 | `ResetReleaseSession` | `0xD1E0` | 461 | UnwindData |  |
| 42 | `ResetResumeBitLockerProtection` | `0xD3C0` | 121 | UnwindData |  |
| 43 | `ResetResumeLog` | `0xD440` | 202 | UnwindData |  |
| 45 | `ResetSetDataPoint` | `0xD510` | 90 | UnwindData |  |
| 46 | `ResetSetStringPoint` | `0xD570` | 90 | UnwindData |  |
| 48 | `ResetSetUIDataPoint` | `0xD5D0` | 90 | UnwindData |  |
| 49 | `ResetSetUIStringPoint` | `0xD630` | 90 | UnwindData |  |
| 50 | `ResetStageOfflineBoot` | `0xD690` | 1,061 | UnwindData |  |
| 51 | `ResetSubmitTelemetry` | `0xDAC0` | 160 | UnwindData |  |
| 52 | `ResetSuspendSession` | `0xDB70` | 432 | UnwindData |  |
| 53 | `ResetTraceClientInfo` | `0xDD30` | 445 | UnwindData |  |
| 54 | `ResetUndo` | `0xDF00` | 1,083 | UnwindData |  |
| 55 | `ResetUnstageOfflineBoot` | `0xE350` | 582 | UnwindData |  |
| 56 | `ResetUploadDiagnosticData` | `0xE5A0` | 793 | UnwindData |  |
| 58 | `ResetValidateScenario` | `0xE8C0` | 1,371 | UnwindData |  |
| 59 | `ResetWillSuspendProtection` | `0xEE30` | 1,274 | UnwindData |  |
| 60 | `ResetWipeSystem` | `0xF330` | 695 | UnwindData |  |
| 13 | `ResetCreateMedia` | `0xF6F0` | 497 | UnwindData |  |
| 25 | `ResetGetMediaSize` | `0xF8F0` | 243 | UnwindData |  |
| 39 | `ResetProvisionMedia` | `0xF9F0` | 213 | UnwindData |  |
| 40 | `ResetReleaseMedia` | `0xFAD0` | 30 | UnwindData |  |
| 19 | `ResetEnterOOBE` | `0x10C40` | 1,197 | UnwindData |  |
| 20 | `ResetExecCleanup` | `0x11100` | 293 | UnwindData |  |
| 21 | `ResetExecOnline` | `0x11230` | 397 | UnwindData |  |
| 28 | `ResetGetTargetVolume` | `0x113D0` | 162 | UnwindData |  |
| 44 | `ResetReturnToOldOS` | `0x11480` | 2,539 | UnwindData |  |
| 47 | `ResetSetTestFlag` | `0x11E80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ResetUserLogon` | `0x11E90` | 1,043 | UnwindData |  |
