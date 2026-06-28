# Binary Specification: wdi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wdi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8179aebabd33fcd715119b1c02bd7f306eec1af762feee526b2768520989cd02`
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
| 5 | `WdiAddFileToInstance` | `0xB410` | 579 | UnwindData |  |
| 12 | `WdiGetClientActivityId` | `0xB660` | 144 | UnwindData |  |
| 13 | `WdiGetClientLCID` | `0xB700` | 152 | UnwindData |  |
| 16 | `WdiGetInstanceFilePath` | `0xB7A0` | 546 | UnwindData |  |
| 23 | `WdiGetParameterDataLength` | `0xB9D0` | 87 | UnwindData |  |
| 24 | `WdiGetParameterDiagnosticModuleId` | `0xBA30` | 96 | UnwindData |  |
| 25 | `WdiGetParameterFlags` | `0xBAA0` | 87 | UnwindData |  |
| 33 | `WdiGetResult` | `0xBB00` | 135 | UnwindData |  |
| 46 | `WdiQueueCurrentResolution` | `0xBB90` | 234 | UnwindData |  |
| 48 | `WdiRevertToSelf` | `0xBC80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `WdiSetProgress` | `0xBCA0` | 344 | UnwindData |  |
| 7 | `WdiCancel` | `0xCF40` | 196 | UnwindData |  |
| 8 | `WdiCloseInstance` | `0xD010` | 415 | UnwindData |  |
| 9 | `WdiCreateInstance` | `0xD1C0` | 704 | UnwindData |  |
| 10 | `WdiDeleteQueuedResolution` | `0xD490` | 276 | UnwindData |  |
| 11 | `WdiDiagnose` | `0xD5B0` | 327 | UnwindData |  |
| 28 | `WdiGetQueuedResolutionAudience` | `0xD700` | 189 | UnwindData |  |
| 29 | `WdiGetQueuedResolutionExpirationDate` | `0xD7D0` | 224 | UnwindData |  |
| 30 | `WdiGetQueuedResolutionId` | `0xD8C0` | 196 | UnwindData |  |
| 31 | `WdiGetQueuedResolutionName` | `0xD990` | 669 | UnwindData |  |
| 32 | `WdiGetQueuedResolutionPriority` | `0xDC40` | 189 | UnwindData |  |
| 34 | `WdiGetScenarioIcon` | `0xDD10` | 638 | UnwindData |  |
| 36 | `WdiGetScenarioInstanceCreatedDate` | `0xDFA0` | 190 | UnwindData |  |
| 37 | `WdiGetScenarioInstanceFilePath` | `0xE070` | 530 | UnwindData |  |
| 38 | `WdiGetScenarioInstanceId` | `0xE290` | 192 | UnwindData |  |
| 39 | `WdiGetScenarioInstances` | `0xE360` | 213 | UnwindData |  |
| 40 | `WdiGetScenarioSourceName` | `0xE440` | 669 | UnwindData |  |
| 41 | `WdiGetScenarioTypeName` | `0xE6F0` | 669 | UnwindData |  |
| 43 | `WdiIsQueuedResolutionAdmin` | `0xE9A0` | 189 | UnwindData |  |
| 44 | `WdiLaunchQueuedResolution` | `0xEA70` | 276 | UnwindData |  |
| 45 | `WdiOpenInstance` | `0xEB90` | 175 | UnwindData |  |
| 47 | `WdiResolve` | `0xEC50` | 352 | UnwindData |  |
| 2 | `WdipLaunchRunDLLUserHost` | `0xFDB0` | 642 | UnwindData |  |
