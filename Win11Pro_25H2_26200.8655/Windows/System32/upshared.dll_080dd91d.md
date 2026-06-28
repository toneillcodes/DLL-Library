# Binary Specification: upshared.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\upshared.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `080dd91d32dd0c5c268adb2a206c3b5fb35f0fe14aed53dd4c5a03f9b459193a`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `ConvertJsonValueToVariant` | `0x79A10` | 595 | UnwindData |  |
| 2 | `CreateQueryStringBuilder` | `0x79C70` | 340 | UnwindData |  |
| 3 | `ExpandCabFile` | `0x7A170` | 118 | UnwindData |  |
| 4 | `LoadJsonFromFile` | `0x7A1F0` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MapExceptionToHResult` | `0x7A330` | 239 | UnwindData |  |
| 6 | `ParseJson` | `0x7A430` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `SubmitRequestForData` | `0x7A550` | 3,668 | UnwindData |  |
| 8 | `SubmitRequestForSettings` | `0x7B3B0` | 3,323 | UnwindData |  |
| 9 | `ToBase64` | `0x7C0C0` | 983 | UnwindData |  |
| 10 | `VerifySelfSignedImageFile` | `0x7C4A0` | 549 | UnwindData |  |
