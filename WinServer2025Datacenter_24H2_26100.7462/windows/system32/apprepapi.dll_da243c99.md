# Binary Specification: apprepapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\apprepapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da243c99734ee3b9fd62e9d76f477b9113bdbed7840e871b848685acf8a1d631`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `AppRepComputeImageHash` | `0x1F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `AppRepComputeImageHashWithOffset` | `0x1F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `AppRepComputeSignatureInfo` | `0x1F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `AppRepInitializeAttributeLib` | `0x1F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AppRepFreeAttributeLib` | `0x1F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `AppRepParameterCleanup` | `0x1F50` | 0 | Indeterminate |  |
| 7 | `AppRepPartialTelemetryCleanup` | `0x1F50` | 0 | Indeterminate |  |
| 8 | `RepGetFileInformation` | `0x1F50` | 0 | Indeterminate |  |
| 9 | `RepInformUserAction` | `0x1F50` | 0 | Indeterminate |  |
| 10 | `ReputationInfoCleanup` | `0x1F50` | 0 | Indeterminate |  |
