# Binary Specification: upshared.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\upshared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `485f391234fba4cf8211d7a29e87d7898ed9d35c28212a16f56090df2b621910`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ConvertJsonValueToVariant` | `0x79A00` | 595 | UnwindData |  |
| 2 | `CreateQueryStringBuilder` | `0x79C60` | 340 | UnwindData |  |
| 3 | `ExpandCabFile` | `0x7A160` | 118 | UnwindData |  |
| 4 | `LoadJsonFromFile` | `0x7A1E0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MapExceptionToHResult` | `0x7A320` | 239 | UnwindData |  |
| 6 | `ParseJson` | `0x7A420` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SubmitRequestForData` | `0x7A540` | 3,668 | UnwindData |  |
| 8 | `SubmitRequestForSettings` | `0x7B3A0` | 3,323 | UnwindData |  |
| 9 | `ToBase64` | `0x7C0B0` | 983 | UnwindData |  |
| 10 | `VerifySelfSignedImageFile` | `0x7C490` | 549 | UnwindData |  |
