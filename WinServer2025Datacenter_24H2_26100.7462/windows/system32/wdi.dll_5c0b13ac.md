# Binary Specification: wdi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wdi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5c0b13acf00267f6e4588869d0400ac67f88e8e8bfccf137125af7e8ecb3cc17`
* **Total Exported Functions:** 53

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 52 | `WdiSetResolution` | `0x1090` | 788 | UnwindData |  |
| 6 | `WdiAddParameter` | `0x4930` | 1,177 | UnwindData |  |
| 27 | `WdiGetProgress` | `0x5FC0` | 315 | UnwindData |  |
| 17 | `WdiGetInstanceId` | `0x63F0` | 144 | UnwindData |  |
| 15 | `WdiGetEvent` | `0x64C0` | 389 | UnwindData |  |
| 18 | `WdiGetLoggerSnapshotPath` | `0x6650` | 209 | UnwindData |  |
| 14 | `WdiGetDiagnosticModuleId` | `0x7B10` | 127 | UnwindData |  |
| 50 | `WdiSetProblemDetectionResult` | `0x7BA0` | 121 | UnwindData |  |
| 35 | `WdiGetScenarioInfo` | `0x7D70` | 269 | UnwindData |  |
| 19 | `WdiGetParameterByIndex` | `0x7E90` | 266 | UnwindData |  |
| 1 | `ServiceMain` | `0x7FA0` | 533 | UnwindData |  |
| 21 | `WdiGetParameterCount` | `0x8210` | 200 | UnwindData |  |
| 22 | `WdiGetParameterData` | `0x82E0` | 142 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x83D0` | 267 | UnwindData |  |
| 42 | `WdiImpersonateClient` | `0x84F0` | 231 | UnwindData |  |
| 49 | `WdiSetFeedback` | `0x8880` | 172 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x8940` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `WdiGetParameterName` | `0x89D0` | 325 | UnwindData |  |
| 53 | `WdipLaunchLocalHost` | `0x8EE0` | 86 | UnwindData |  |
| 20 | `WdiGetParameterByName` | `0x9170` | 583 | UnwindData |  |
| 5 | `WdiAddFileToInstance` | `0xBEA0` | 579 | UnwindData |  |
| 12 | `WdiGetClientActivityId` | `0xC0F0` | 144 | UnwindData |  |
| 13 | `WdiGetClientLCID` | `0xC190` | 152 | UnwindData |  |
| 16 | `WdiGetInstanceFilePath` | `0xC230` | 546 | UnwindData |  |
| 23 | `WdiGetParameterDataLength` | `0xC460` | 87 | UnwindData |  |
| 24 | `WdiGetParameterDiagnosticModuleId` | `0xC4C0` | 96 | UnwindData |  |
| 25 | `WdiGetParameterFlags` | `0xC530` | 87 | UnwindData |  |
| 33 | `WdiGetResult` | `0xC590` | 135 | UnwindData |  |
| 46 | `WdiQueueCurrentResolution` | `0xC620` | 234 | UnwindData |  |
| 48 | `WdiRevertToSelf` | `0xC710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `WdiSetProgress` | `0xC730` | 344 | UnwindData |  |
| 7 | `WdiCancel` | `0xD9D0` | 196 | UnwindData |  |
| 8 | `WdiCloseInstance` | `0xDAA0` | 415 | UnwindData |  |
| 9 | `WdiCreateInstance` | `0xDC50` | 704 | UnwindData |  |
| 10 | `WdiDeleteQueuedResolution` | `0xDF20` | 276 | UnwindData |  |
| 11 | `WdiDiagnose` | `0xE040` | 327 | UnwindData |  |
| 28 | `WdiGetQueuedResolutionAudience` | `0xE190` | 189 | UnwindData |  |
| 29 | `WdiGetQueuedResolutionExpirationDate` | `0xE260` | 224 | UnwindData |  |
| 30 | `WdiGetQueuedResolutionId` | `0xE350` | 196 | UnwindData |  |
| 31 | `WdiGetQueuedResolutionName` | `0xE420` | 669 | UnwindData |  |
| 32 | `WdiGetQueuedResolutionPriority` | `0xE6D0` | 189 | UnwindData |  |
| 34 | `WdiGetScenarioIcon` | `0xE7A0` | 638 | UnwindData |  |
| 36 | `WdiGetScenarioInstanceCreatedDate` | `0xEA30` | 190 | UnwindData |  |
| 37 | `WdiGetScenarioInstanceFilePath` | `0xEB00` | 530 | UnwindData |  |
| 38 | `WdiGetScenarioInstanceId` | `0xED20` | 192 | UnwindData |  |
| 39 | `WdiGetScenarioInstances` | `0xEDF0` | 213 | UnwindData |  |
| 40 | `WdiGetScenarioSourceName` | `0xEED0` | 669 | UnwindData |  |
| 41 | `WdiGetScenarioTypeName` | `0xF180` | 669 | UnwindData |  |
| 43 | `WdiIsQueuedResolutionAdmin` | `0xF430` | 189 | UnwindData |  |
| 44 | `WdiLaunchQueuedResolution` | `0xF500` | 276 | UnwindData |  |
| 45 | `WdiOpenInstance` | `0xF620` | 175 | UnwindData |  |
| 47 | `WdiResolve` | `0xF6E0` | 352 | UnwindData |  |
| 2 | `WdipLaunchRunDLLUserHost` | `0x10840` | 642 | UnwindData |  |
