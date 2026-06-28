# Binary Specification: pla.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\pla.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4abd1e15c05ed883bf0045295e366a4ae9d217bd9320a19cd7812bbc4cdc5e25`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `PlaGetServerCapabilities` | `0x313B0` | 36 | UnwindData |  |
| 4 | `DllGetClassObject` | `0x33480` | 50 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x43E90` | 91,040 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllRegisterServer` | `0x5A230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0x5A230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `PlaServer` | `0x5A240` | 1,240 | UnwindData |  |
| 1 | `ServiceMain` | `0x5ABA0` | 1,185 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x5B050` | 10,896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `PlaUpgrade` | `0x5DAE0` | 1,076 | UnwindData |  |
| 10 | `PlaGetLegacyAlertActionsFlagsFromString` | `0xFE530` | 1,371 | UnwindData |  |
| 11 | `PlaGetLegacyAlertActionsStringFromFlags` | `0xFEAA0` | 1,377 | UnwindData |  |
| 8 | `PlaExpandTaskArguments` | `0x121E20` | 515 | UnwindData |  |
| 13 | `PlaHost` | `0x122F70` | 638 | UnwindData |  |
| 7 | `PlaDeleteReport` | `0x140EE0` | 322 | UnwindData |  |
| 9 | `PlaExtractCabinet` | `0x141030` | 35,420 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
