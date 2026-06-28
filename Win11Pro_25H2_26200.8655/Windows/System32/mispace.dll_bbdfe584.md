# Binary Specification: mispace.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mispace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bbdfe584e7dbed07fef0eff5bcc72429d5ef50d2a725418941888887b5d825c3`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0xB110` | 47 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xB150` | 119 | UnwindData |  |
| 4 | `DllMain` | `0xB1D0` | 162 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xB280` | 72 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0xB2D0` | 65 | UnwindData |  |
| 7 | `GetProviderClassID` | `0xB320` | 8,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MI_Main` | `0xD2A0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PreShutdown` | `0xD360` | 27 | UnwindData |  |
| 10 | `SetShutdownCallback` | `0xD390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SmpUnload` | `0xD3A0` | 4,688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WspCheckMinimumSubsystemVersion` | `0xE5F0` | 27 | UnwindData |  |
| 12 | `WspCompleteMethod` | `0xF610` | 295 | UnwindData |  |
| 13 | `WspCreateJob` | `0xF7C0` | 499 | UnwindData |  |
| 14 | `WspEnumerateRemoteInstances` | `0xF9C0` | 333 | UnwindData |  |
| 15 | `WspFreeString` | `0xFB20` | 20 | UnwindData |  |
| 16 | `WspGetClassName` | `0xFB40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `WspGetRemoteInstance` | `0xFB70` | 333 | UnwindData |  |
| 18 | `WspGetSubsystemFilter` | `0xFCD0` | 40 | UnwindData |  |
| 19 | `WspGuidToString` | `0xFE10` | 251 | UnwindData |  |
| 20 | `WspInvokeRemoteMethod` | `0xFF20` | 378 | UnwindData |  |
| 21 | `WspIsAutomaticClusteringEnabled` | `0x100A0` | 221 | UnwindData |  |
| 22 | `WspIsRemoteInstance` | `0x10190` | 269 | UnwindData |  |
| 23 | `WspIsRemoteRequest` | `0x102B0` | 149 | UnwindData |  |
| 24 | `WspPackObjectId` | `0x10350` | 1,026 | UnwindData |  |
| 25 | `WspPostAssociation` | `0x10760` | 395 | UnwindData |  |
| 26 | `WspPostSubsystemAssociationReferenceObject` | `0x10900` | 413 | UnwindData |  |
| 27 | `WspProviderEnter` | `0x10AB0` | 357 | UnwindData |  |
| 28 | `WspProviderExit` | `0x10C20` | 26 | UnwindData |  |
| 29 | `WspReferencesOfRemoteInstance` | `0x10C40` | 455 | UnwindData |  |
| 30 | `WspRunMethodAsJob` | `0x10E10` | 734 | UnwindData |  |
| 31 | `WspSendIndication` | `0x11100` | 382 | UnwindData |  |
| 32 | `WspUnpackObjectId` | `0x11290` | 692 | UnwindData |  |
| 33 | `WspUpdateMethod` | `0x11550` | 218 | UnwindData |  |
