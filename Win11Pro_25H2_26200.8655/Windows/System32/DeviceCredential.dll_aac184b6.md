# Binary Specification: DeviceCredential.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DeviceCredential.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `aac184b6f55b418afea5a4797df3c318352c60e85e2647351595fa7db7b5b940`
* **Total Exported Functions:** 31

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `DeviceCredentialFreeBuffer` | `0x6DD0` | 9,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DeviceCredentialAbortAuthentication` | `0x9120` | 155 | UnwindData |  |
| 2 | `DeviceCredentialAbortProvisioning` | `0x91D0` | 153 | UnwindData |  |
| 3 | `DeviceCredentialCompleteAuthentication` | `0x9270` | 170 | UnwindData |  |
| 4 | `DeviceCredentialCompleteProvisioning` | `0x9320` | 168 | UnwindData |  |
| 5 | `DeviceCredentialDeprovision` | `0x93D0` | 369 | UnwindData |  |
| 6 | `DeviceCredentialFindClose` | `0x9550` | 150 | UnwindData |  |
| 7 | `DeviceCredentialFindFirst` | `0x95F0` | 390 | UnwindData |  |
| 8 | `DeviceCredentialFindNext` | `0x9780` | 132 | UnwindData |  |
| 10 | `DeviceCredentialGetAuthStageData` | `0x9810` | 328 | UnwindData |  |
| 11 | `DeviceCredentialGetDeviceInfo` | `0x9960` | 183 | UnwindData |  |
| 12 | `DeviceCredentialInitializeAuthentication` | `0x9A20` | 478 | UnwindData |  |
| 13 | `DeviceCredentialInitializeProvisioning` | `0x9C10` | 482 | UnwindData |  |
| 14 | `DeviceCredentialMgrBeginAuthentication` | `0x9E00` | 393 | UnwindData |  |
| 15 | `DeviceCredentialMgrCheckIfUserSessionIsRequired` | `0x9F90` | 372 | UnwindData |  |
| 17 | `DeviceCredentialMgrCheckProvisionedDevice` | `0xA110` | 389 | UnwindData |  |
| 18 | `DeviceCredentialMgrGetAuthenticationData` | `0xA2A0` | 373 | UnwindData |  |
| 19 | `DeviceCredentialMgrHasLogonSession` | `0xA420` | 372 | UnwindData |  |
| 20 | `DeviceCredentialMgrProtectData` | `0xA5A0` | 453 | UnwindData |  |
| 21 | `DeviceCredentialMgrUnprotectData` | `0xA770` | 468 | UnwindData |  |
| 22 | `DeviceCredentialMgrUpdateAuthenticationStage` | `0xA950` | 460 | UnwindData |  |
| 25 | `DeviceCredentialScanDeploymentData` | `0xAB30` | 316 | UnwindData |  |
| 26 | `DeviceCredentialSetFriendlyName` | `0xAC80` | 398 | UnwindData |  |
| 27 | `DeviceCredentialSetOpaqueBlob` | `0xAE20` | 477 | UnwindData |  |
| 28 | `DeviceCredentialShowNotificationMessage` | `0xB010` | 392 | UnwindData |  |
| 30 | `DeviceCredentialUpdateDeploymentData` | `0xB1A0` | 318 | UnwindData |  |
| 16 | `DeviceCredentialMgrCheckPresence` | `0xB9A0` | 316 | UnwindData |  |
| 23 | `DeviceCredentialRegisterPresenceMonitoring` | `0xBAF0` | 394 | UnwindData |  |
| 24 | `DeviceCredentialRegisterPresenceMonitoringOnExistingDevice` | `0xBC80` | 457 | UnwindData |  |
| 29 | `DeviceCredentialUnregisterPresenceMonitoring` | `0xBE50` | 320 | UnwindData |  |
| 31 | `DeviceCredentialUpdatePresenceState` | `0xBFA0` | 386 | UnwindData |  |
