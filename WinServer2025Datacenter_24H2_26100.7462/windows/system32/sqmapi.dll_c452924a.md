# Binary Specification: sqmapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sqmapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c452924a9ae08581d8e12e94722370af3a0594db8d5561f7ec8bfd8ec61382cd`
* **Total Exported Functions:** 62

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `SqmGetEscalationRuleStatus` | `0x13D0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `SqmIsNamespaceEnabled` | `0x13D0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SqmIsWindowsOptedIn` | `0x13D0` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `SqmSysprepCleanup` | `0x1F10` | 17 | UnwindData |  |
| 54 | `SqmSysprepGeneralize` | `0x1F30` | 418 | UnwindData |  |
| 59 | `SqmUnattendedSetup` | `0x20E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `SqmCheckEscalationAddToStreamDWord` | `0x2100` | 56 | UnwindData |  |
| 1 | `SqmCheckEscalationAddToStreamDWord64` | `0x2100` | 56 | UnwindData |  |
| 3 | `SqmCheckEscalationAddToStreamString` | `0x2100` | 56 | UnwindData |  |
| 5 | `SqmCheckEscalationSetDWord` | `0x2140` | 53 | UnwindData |  |
| 4 | `SqmCheckEscalationSetDWord64` | `0x2140` | 53 | UnwindData |  |
| 6 | `SqmCheckEscalationSetString` | `0x2140` | 53 | UnwindData |  |
| 8 | `SqmGetInstrumentationProperty` | `0x2180` | 52 | UnwindData |  |
| 12 | `SqmAddToAverage` | `0x21C0` | 29 | UnwindData |  |
| 14 | `SqmAddToStreamDWord` | `0x21C0` | 29 | UnwindData |  |
| 15 | `SqmAddToStreamDWord64` | `0x21C0` | 29 | UnwindData |  |
| 16 | `SqmAddToStreamString` | `0x21C0` | 29 | UnwindData |  |
| 17 | `SqmAddToStreamV` | `0x21C0` | 29 | UnwindData |  |
| 18 | `SqmCleanup` | `0x21C0` | 29 | UnwindData |  |
| 19 | `SqmClearFlags` | `0x21C0` | 29 | UnwindData |  |
| 21 | `SqmEndSession` | `0x21C0` | 29 | UnwindData |  |
| 22 | `SqmEndSessionEx` | `0x21C0` | 29 | UnwindData |  |
| 23 | `SqmFlushSession` | `0x21C0` | 29 | UnwindData |  |
| 28 | `SqmGetSession` | `0x21C0` | 29 | UnwindData |  |
| 31 | `SqmIncrement` | `0x21C0` | 29 | UnwindData |  |
| 9 | `SqmLoadEscalationManifest` | `0x21C0` | 29 | UnwindData |  |
| 36 | `SqmSet` | `0x21C0` | 29 | UnwindData |  |
| 37 | `SqmSetAppId` | `0x21C0` | 29 | UnwindData |  |
| 38 | `SqmSetAppVersion` | `0x21C0` | 29 | UnwindData |  |
| 39 | `SqmSetBits` | `0x21C0` | 29 | UnwindData |  |
| 40 | `SqmSetBool` | `0x21C0` | 29 | UnwindData |  |
| 41 | `SqmSetCurrentTimeAsUploadTime` | `0x21C0` | 29 | UnwindData |  |
| 42 | `SqmSetDWord64` | `0x21C0` | 29 | UnwindData |  |
| 43 | `SqmSetEnabled` | `0x21C0` | 29 | UnwindData |  |
| 10 | `SqmSetEscalationInfo` | `0x21C0` | 29 | UnwindData |  |
| 44 | `SqmSetFlags` | `0x21C0` | 29 | UnwindData |  |
| 45 | `SqmSetIfMax` | `0x21C0` | 29 | UnwindData |  |
| 46 | `SqmSetIfMin` | `0x21C0` | 29 | UnwindData |  |
| 47 | `SqmSetMachineId` | `0x21C0` | 29 | UnwindData |  |
| 48 | `SqmSetString` | `0x21C0` | 29 | UnwindData |  |
| 49 | `SqmSetUserId` | `0x21C0` | 29 | UnwindData |  |
| 50 | `SqmStartSession` | `0x21C0` | 29 | UnwindData |  |
| 55 | `SqmTimerAccumulate` | `0x21C0` | 29 | UnwindData |  |
| 56 | `SqmTimerAddToAverage` | `0x21C0` | 29 | UnwindData |  |
| 57 | `SqmTimerRecord` | `0x21C0` | 29 | UnwindData |  |
| 58 | `SqmTimerStart` | `0x21C0` | 29 | UnwindData |  |
| 11 | `SqmUnloadEscalationManifest` | `0x21C0` | 29 | UnwindData |  |
| 60 | `SqmWaitForUploadComplete` | `0x21C0` | 29 | UnwindData |  |
| 61 | `SqmWriteSharedMachineId` | `0x21C0` | 29 | UnwindData |  |
| 62 | `SqmWriteSharedUserId` | `0x21C0` | 29 | UnwindData |  |
| 13 | `SqmAddToStream` | `0x21F0` | 34 | UnwindData |  |
| 20 | `SqmCreateNewId` | `0x2220` | 41 | UnwindData |  |
| 34 | `SqmReadSharedMachineId` | `0x2220` | 41 | UnwindData |  |
| 35 | `SqmReadSharedUserId` | `0x2220` | 41 | UnwindData |  |
| 24 | `SqmGetEnabled` | `0x2250` | 26 | UnwindData |  |
| 29 | `SqmGetSessionStartTime` | `0x2250` | 26 | UnwindData |  |
| 51 | `SqmStartUpload` | `0x2250` | 26 | UnwindData |  |
| 52 | `SqmStartUploadEx` | `0x2250` | 26 | UnwindData |  |
| 25 | `SqmGetFlags` | `0x2270` | 37 | UnwindData |  |
| 26 | `SqmGetLastUploadTime` | `0x22A0` | 38 | UnwindData |  |
| 27 | `SqmGetMachineId` | `0x22D0` | 41 | UnwindData |  |
| 30 | `SqmGetUserId` | `0x22D0` | 41 | UnwindData |  |
