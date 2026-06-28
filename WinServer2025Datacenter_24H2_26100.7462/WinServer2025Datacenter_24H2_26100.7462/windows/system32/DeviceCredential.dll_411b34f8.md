# Binary Specification: DeviceCredential.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\DeviceCredential.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `411b34f8aca603fa53890a51defc821cd56e0067f3591d8c9ab93b9bb65f8ea1`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `DeviceCredentialFreeBuffer` | `0x6DC0` | 9,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DeviceCredentialAbortAuthentication` | `0x9110` | 155 | UnwindData |  |
| 2 | `DeviceCredentialAbortProvisioning` | `0x91C0` | 153 | UnwindData |  |
| 3 | `DeviceCredentialCompleteAuthentication` | `0x9260` | 170 | UnwindData |  |
| 4 | `DeviceCredentialCompleteProvisioning` | `0x9310` | 168 | UnwindData |  |
| 5 | `DeviceCredentialDeprovision` | `0x93C0` | 369 | UnwindData |  |
| 6 | `DeviceCredentialFindClose` | `0x9540` | 150 | UnwindData |  |
| 7 | `DeviceCredentialFindFirst` | `0x95E0` | 390 | UnwindData |  |
| 8 | `DeviceCredentialFindNext` | `0x9770` | 132 | UnwindData |  |
| 10 | `DeviceCredentialGetAuthStageData` | `0x9800` | 328 | UnwindData |  |
| 11 | `DeviceCredentialGetDeviceInfo` | `0x9950` | 183 | UnwindData |  |
| 12 | `DeviceCredentialInitializeAuthentication` | `0x9A10` | 478 | UnwindData |  |
| 13 | `DeviceCredentialInitializeProvisioning` | `0x9C00` | 482 | UnwindData |  |
| 14 | `DeviceCredentialMgrBeginAuthentication` | `0x9DF0` | 393 | UnwindData |  |
| 15 | `DeviceCredentialMgrCheckIfUserSessionIsRequired` | `0x9F80` | 372 | UnwindData |  |
| 17 | `DeviceCredentialMgrCheckProvisionedDevice` | `0xA100` | 389 | UnwindData |  |
| 18 | `DeviceCredentialMgrGetAuthenticationData` | `0xA290` | 373 | UnwindData |  |
| 19 | `DeviceCredentialMgrHasLogonSession` | `0xA410` | 372 | UnwindData |  |
| 20 | `DeviceCredentialMgrProtectData` | `0xA590` | 453 | UnwindData |  |
| 21 | `DeviceCredentialMgrUnprotectData` | `0xA760` | 468 | UnwindData |  |
| 22 | `DeviceCredentialMgrUpdateAuthenticationStage` | `0xA940` | 460 | UnwindData |  |
| 25 | `DeviceCredentialScanDeploymentData` | `0xAB20` | 316 | UnwindData |  |
| 26 | `DeviceCredentialSetFriendlyName` | `0xAC70` | 398 | UnwindData |  |
| 27 | `DeviceCredentialSetOpaqueBlob` | `0xAE10` | 477 | UnwindData |  |
| 28 | `DeviceCredentialShowNotificationMessage` | `0xB000` | 392 | UnwindData |  |
| 30 | `DeviceCredentialUpdateDeploymentData` | `0xB190` | 318 | UnwindData |  |
| 16 | `DeviceCredentialMgrCheckPresence` | `0xB990` | 316 | UnwindData |  |
| 23 | `DeviceCredentialRegisterPresenceMonitoring` | `0xBAE0` | 394 | UnwindData |  |
| 24 | `DeviceCredentialRegisterPresenceMonitoringOnExistingDevice` | `0xBC70` | 457 | UnwindData |  |
| 29 | `DeviceCredentialUnregisterPresenceMonitoring` | `0xBE40` | 320 | UnwindData |  |
| 31 | `DeviceCredentialUpdatePresenceState` | `0xBF90` | 386 | UnwindData |  |
