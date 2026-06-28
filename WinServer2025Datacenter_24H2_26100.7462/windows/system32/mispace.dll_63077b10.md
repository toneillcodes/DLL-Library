# Binary Specification: mispace.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mispace.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `63077b10dfde99b498c9944ad21fd26ef58a3ab72619f6d74c50c129bf742f2c`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0xB100` | 47 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xB140` | 119 | UnwindData |  |
| 4 | `DllMain` | `0xB1C0` | 162 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xB270` | 72 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0xB2C0` | 65 | UnwindData |  |
| 7 | `GetProviderClassID` | `0xB310` | 8,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MI_Main` | `0xD290` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `PreShutdown` | `0xD350` | 27 | UnwindData |  |
| 10 | `SetShutdownCallback` | `0xD380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `SmpUnload` | `0xD390` | 32,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WspCheckMinimumSubsystemVersion` | `0x15170` | 27 | UnwindData |  |
| 12 | `WspCompleteMethod` | `0x161A0` | 295 | UnwindData |  |
| 13 | `WspCreateJob` | `0x16350` | 499 | UnwindData |  |
| 14 | `WspEnumerateRemoteInstances` | `0x16550` | 333 | UnwindData |  |
| 15 | `WspFreeString` | `0x166B0` | 20 | UnwindData |  |
| 16 | `WspGetClassName` | `0x166D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `WspGetRemoteInstance` | `0x16700` | 333 | UnwindData |  |
| 18 | `WspGetSubsystemFilter` | `0x16860` | 40 | UnwindData |  |
| 19 | `WspGuidToString` | `0x169A0` | 251 | UnwindData |  |
| 20 | `WspInvokeRemoteMethod` | `0x16AB0` | 378 | UnwindData |  |
| 21 | `WspIsAutomaticClusteringEnabled` | `0x16C30` | 221 | UnwindData |  |
| 22 | `WspIsRemoteInstance` | `0x16D20` | 269 | UnwindData |  |
| 23 | `WspIsRemoteRequest` | `0x16E40` | 149 | UnwindData |  |
| 24 | `WspPackObjectId` | `0x16EE0` | 1,026 | UnwindData |  |
| 25 | `WspPostAssociation` | `0x172F0` | 395 | UnwindData |  |
| 26 | `WspPostSubsystemAssociationReferenceObject` | `0x17490` | 413 | UnwindData |  |
| 27 | `WspProviderEnter` | `0x17640` | 357 | UnwindData |  |
| 28 | `WspProviderExit` | `0x177B0` | 26 | UnwindData |  |
| 29 | `WspReferencesOfRemoteInstance` | `0x177D0` | 455 | UnwindData |  |
| 30 | `WspRunMethodAsJob` | `0x179A0` | 734 | UnwindData |  |
| 31 | `WspSendIndication` | `0x17C90` | 382 | UnwindData |  |
| 32 | `WspUnpackObjectId` | `0x17E20` | 744 | UnwindData |  |
| 33 | `WspUpdateMethod` | `0x18110` | 218 | UnwindData |  |
