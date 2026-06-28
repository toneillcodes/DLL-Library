# Binary Specification: Unistore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Unistore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `fde20af4650abbdfb40b6566df920fdb0f2313efa4946384a507d1c437d20fa7`
* **Total Exported Functions:** 42

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 42 | `USObjectTypeToEventMask` | `0x22C0` | 664 | UnwindData |  |
| 35 | `StartUnifiedStoreWorkForClient` | `0x6CB0` | 221 | UnwindData |  |
| 16 | `FindMaxSeenRevisionForAppInBlob` | `0x1AE10` | 212 | UnwindData |  |
| 37 | `USComparePropVals` | `0x24E30` | 853 | UnwindData |  |
| 41 | `USGetPropValsAncillaryBufferSize` | `0x283C0` | 351 | UnwindData |  |
| 38 | `USCopyPropVals` | `0x29540` | 773 | UnwindData |  |
| 10 | `CreateStoreManager` | `0x31BF0` | 446 | UnwindData |  |
| 11 | `CreateStoreManagerWithToken` | `0x31F00` | 215 | UnwindData |  |
| 30 | `RemoveStaleChangeTrackingDataOnStore` | `0x32FB0` | 2,433 | UnwindData |  |
| 8 | `AddDWORDPropertyRestrictions` | `0x37450` | 573 | UnwindData |  |
| 28 | `RegisterRundownProtectionForProcess` | `0x40240` | 60 | UnwindData |  |
| 15 | `EndUnifiedStoreWorkForClient` | `0x43BF0` | 45 | UnwindData |  |
| 2 | `GetDeviceStoreDefaultName` | `0x46490` | 264 | UnwindData |  |
| 12 | `DetectExistingCorruption` | `0x48D90` | 246 | UnwindData |  |
| 19 | `GetUSDeviceStoreCorruptedVolumeFolderPath` | `0x4A050` | 431 | UnwindData |  |
| 4 | `GetUSDeviceStoreFolderPath` | `0x4A210` | 449 | UnwindData |  |
| 3 | `GetUSDataFolderPath` | `0x4A3E0` | 524 | UnwindData |  |
| 39 | `USDeleteFileEx` | `0x4C040` | 688 | UnwindData |  |
| 6 | `USIsObjectHidden` | `0x58710` | 107 | UnwindData |  |
| 40 | `USEventMaskToObjectType` | `0x65D50` | 6,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `GetUnistoreJetInstance` | `0x675A0` | 262 | UnwindData |  |
| 25 | `IsUnistoreInProc` | `0x680A0` | 1,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ReleaseUnistoreJetInstance` | `0x68760` | 4,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `IsCEPropValPresent` | `0x69920` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `IsUSPropValPresent` | `0x69920` | 2,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `GetRealStoreManager` | `0x6A200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `SvchostPushServiceGlobals` | `0x6A210` | 5,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ServiceMain` | `0x6B5B0` | 2,640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `GetCurrentProcessRundownProtectionIdentifier` | `0x6C000` | 39,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AppRevisionBlobToUSBlob` | `0x75C00` | 590 | UnwindData |  |
| 5 | `USBlobToAppRevisionBlob` | `0x76580` | 425 | UnwindData |  |
| 32 | `SetMaxRevisionBlobSize` | `0x76C40` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `USIsSameObject` | `0x76D20` | 187 | UnwindData |  |
| 13 | `DisableLocalUnistore` | `0x76DF0` | 78 | UnwindData |  |
| 14 | `EnableLocalUnistore` | `0x76E50` | 175 | UnwindData |  |
| 21 | `GetUSFileStreamPath` | `0x76F10` | 225 | UnwindData |  |
| 26 | `IsUnistoreLocal` | `0x77000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `SetUnistoreProcessEventFilter` | `0x77010` | 226 | UnwindData |  |
| 34 | `SetUnistoreVersion` | `0x77100` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `GetUSDeviceStoreVolumePath` | `0x77270` | 225 | UnwindData |  |
| 9 | `ClearUSCache` | `0x78690` | 103 | UnwindData |  |
| 27 | `LowerRPCPriority` | `0x78700` | 327,996 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
