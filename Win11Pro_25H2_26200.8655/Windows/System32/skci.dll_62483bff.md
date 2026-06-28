# Binary Specification: skci.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\skci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `62483bff4d6961652914b4a4864176060f1dc49000356c98ed2490fde414ee46`
* **Total Exported Functions:** 18

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `SkciInitialize` | `0xDD40` | 507 | UnwindData |  |
| 2 | `SkciCreateCodeCatalog` | `0xDF90` | 219 | UnwindData |  |
| 15 | `SkciValidateAmeCertChain` | `0xE120` | 377 | UnwindData |  |
| 16 | `SkciValidateCertChain` | `0xE2A0` | 401 | UnwindData |  |
| 3 | `SkciCreateSecureImage` | `0xE910` | 710 | UnwindData |  |
| 4 | `SkciFinalizeSecureImageHash` | `0xEE70` | 225 | UnwindData |  |
| 5 | `SkciFinishImageValidation` | `0xEF60` | 1,422 | UnwindData |  |
| 6 | `SkciFreeImageContext` | `0xF500` | 158 | UnwindData |  |
| 8 | `SkciMatchHotPatch` | `0xF650` | 74 | UnwindData |  |
| 9 | `SkciQueryImageAttestationData` | `0xF6A0` | 364 | UnwindData |  |
| 10 | `SkciQueryImageAuthorID` | `0xF820` | 42 | UnwindData |  |
| 11 | `SkciQueryImageUniqueID` | `0xF850` | 42 | UnwindData |  |
| 14 | `SkciTransferVersionResource` | `0xF980` | 610 | UnwindData |  |
| 17 | `SkciValidateDynamicCodePages` | `0xFBF0` | 60 | UnwindData |  |
| 18 | `SkciValidateImageData` | `0xFC40` | 559 | UnwindData |  |
| 1 | `SkciCompareSigningLevels` | `0x403C0` | 35 | UnwindData |  |
| 12 | `SkciQueryInformation` | `0x44720` | 365 | UnwindData |  |
| 13 | `SkciSetCodeIntegrityPolicy` | `0x449D0` | 339 | UnwindData |  |
