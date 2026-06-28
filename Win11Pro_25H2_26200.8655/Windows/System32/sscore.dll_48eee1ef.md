# Binary Specification: sscore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sscore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `48eee1efbbdea081bc18f31c61803bf3fd1a8ed1af4a62a352ff3a985e7968f6`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `SsCoreOpenInstance` | `0x10F0` | 483 | UnwindData |  |
| 38 | `SsCoreShareAddForInstance` | `0x12E0` | 98 | UnwindData |  |
| 37 | `SsCoreShareAddEx` | `0x1510` | 111 | UnwindData |  |
| 39 | `SsCoreShareCleanup` | `0x22F0` | 55 | UnwindData |  |
| 18 | `SsCoreInitializeEx` | `0x2330` | 283 | UnwindData |  |
| 6 | `SsCoreCloseInstance` | `0x2580` | 7,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SsCoreAliasAdd` | `0x42D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SsCoreAliasAddEx` | `0x42E0` | 267 | UnwindData |  |
| 3 | `SsCoreAliasDel` | `0x4400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SsCoreAliasDelEx` | `0x4410` | 260 | UnwindData |  |
| 5 | `SsCoreCertificatesUpdate` | `0x4670` | 88 | UnwindData |  |
| 7 | `SsCoreCompleteCsvVolumeDrain` | `0x46D0` | 116 | UnwindData |  |
| 8 | `SsCoreDeregisterNetnameForMultichannel` | `0x4750` | 28 | UnwindData |  |
| 9 | `SsCoreEnumAlternativePort` | `0x4780` | 84 | UnwindData |  |
| 10 | `SsCoreFileDel` | `0x47E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SsCoreFileDelForInstance` | `0x4800` | 125 | UnwindData |  |
| 12 | `SsCoreFileEnum` | `0x4890` | 86 | UnwindData |  |
| 13 | `SsCoreFileEnumForInstance` | `0x48F0` | 508 | UnwindData |  |
| 14 | `SsCoreFileNotifyClose` | `0x4B00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SsCoreFileNotifyCloseForInstance` | `0x4B20` | 125 | UnwindData |  |
| 16 | `SsCoreFreeBuffer` | `0x4BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SsCoreInitialize` | `0x4BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `SsCoreInvalidationRequest` | `0x4BE0` | 248 | UnwindData |  |
| 20 | `SsCoreLockVolumes` | `0x4CE0` | 99 | UnwindData |  |
| 21 | `SsCoreMarkAsClusterSvc` | `0x4D50` | 102 | UnwindData |  |
| 22 | `SsCoreNodeResetInfo` | `0x4DC0` | 38 | UnwindData |  |
| 23 | `SsCoreNodeSetInfo` | `0x4DF0` | 138 | UnwindData |  |
| 25 | `SsCoreRefreshSrvCredentialHandle` | `0x4E80` | 74 | UnwindData |  |
| 26 | `SsCoreRegisterNetnameForMultichannel` | `0x4ED0` | 23 | UnwindData |  |
| 27 | `SsCoreServerTransportSetInfo` | `0x4EF0` | 28 | UnwindData |  |
| 28 | `SsCoreSessionDel` | `0x4FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `SsCoreSessionDelForInstance` | `0x4FE0` | 135 | UnwindData |  |
| 30 | `SsCoreSessionEnlist` | `0x5070` | 182 | UnwindData |  |
| 31 | `SsCoreSessionEnum` | `0x5130` | 68 | UnwindData |  |
| 32 | `SsCoreSessionEnumForInstance` | `0x5180` | 469 | UnwindData |  |
| 33 | `SsCoreSetInstanceProperties` | `0x5360` | 127 | UnwindData |  |
| 34 | `SsCoreSetMaxClusterDialect` | `0x53F0` | 113 | UnwindData |  |
| 35 | `SsCoreSetRdmaState` | `0x5470` | 107 | UnwindData |  |
| 36 | `SsCoreShareAdd` | `0x54F0` | 45 | UnwindData |  |
| 40 | `SsCoreShareDel` | `0x5530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `SsCoreShareDelForInstance` | `0x5550` | 197 | UnwindData |  |
| 42 | `SsCoreShareGetInfo` | `0x5620` | 36 | UnwindData |  |
| 43 | `SsCoreShareGetInfoForInstance` | `0x5650` | 358 | UnwindData |  |
| 44 | `SsCoreShareSetInfo` | `0x57C0` | 66 | UnwindData |  |
| 45 | `SsCoreShareSetInfoForInstance` | `0x5810` | 416 | UnwindData |  |
| 46 | `SsCoreShareShutdownForScope` | `0x59C0` | 199 | UnwindData |  |
| 47 | `SsCoreStartCsvVolumeDrain` | `0x5A90` | 116 | UnwindData |  |
| 48 | `SsCoreStartInstance` | `0x5B10` | 122 | UnwindData |  |
| 49 | `SsCoreStartInstanceEx` | `0x5B90` | 145 | UnwindData |  |
| 50 | `SsCoreStopInstance` | `0x5C30` | 122 | UnwindData |  |
| 51 | `SsCoreUninitialize` | `0x5CB0` | 131 | UnwindData |  |
| 52 | `SsCoreUnlockVolumes` | `0x5D40` | 104 | UnwindData |  |
| 53 | `SsCoreUpdateAlternativePort` | `0x5DB0` | 84 | UnwindData |  |
