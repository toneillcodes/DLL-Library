# Binary Specification: skci.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\skci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `19da8314d416eb5a8800e1c0a58665019b4c57fe933021c1f6fb537d2036353c`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `SkciInitialize` | `0xDD00` | 507 | UnwindData |  |
| 2 | `SkciCreateCodeCatalog` | `0xDF50` | 219 | UnwindData |  |
| 14 | `SkciValidateAmeCertChain` | `0xE070` | 377 | UnwindData |  |
| 15 | `SkciValidateCertChain` | `0xE1F0` | 401 | UnwindData |  |
| 3 | `SkciCreateSecureImage` | `0xE6E0` | 710 | UnwindData |  |
| 4 | `SkciFinalizeSecureImageHash` | `0xEC40` | 225 | UnwindData |  |
| 5 | `SkciFinishImageValidation` | `0xED30` | 1,471 | UnwindData |  |
| 6 | `SkciFreeImageContext` | `0xF300` | 110 | UnwindData |  |
| 8 | `SkciMatchHotPatch` | `0xF420` | 74 | UnwindData |  |
| 9 | `SkciQueryImageAuthorID` | `0xF470` | 42 | UnwindData |  |
| 10 | `SkciQueryImageUniqueID` | `0xF4A0` | 42 | UnwindData |  |
| 13 | `SkciTransferVersionResource` | `0xF5D0` | 521 | UnwindData |  |
| 16 | `SkciValidateDynamicCodePages` | `0xF7E0` | 60 | UnwindData |  |
| 17 | `SkciValidateImageData` | `0xF830` | 559 | UnwindData |  |
| 1 | `SkciCompareSigningLevels` | `0x3E340` | 35 | UnwindData |  |
| 11 | `SkciQueryInformation` | `0x42420` | 365 | UnwindData |  |
| 12 | `SkciSetCodeIntegrityPolicy` | `0x426D0` | 395 | UnwindData |  |
