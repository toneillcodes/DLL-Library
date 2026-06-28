# Binary Specification: lenovo.certificatevalidation.native.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\AddOnPlugins\618bf3cf-e6b6-4f49-a338-d564c832d07f\x64\x64\lenovo.certificatevalidation.native.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `119d9adf4d20858f17a214e9544bcf98e5fd0d6bf2d6d245701d393812cd8e0c`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `ValidateAssembly` | `0xA5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `ValidateCertFile` | `0xA5D0` | 81 | UnwindData |  |
| 6 | `ValidateXmlContent` | `0xA740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `ValidateXmlFile` | `0xA750` | 78 | UnwindData |  |
| 8 | `ValidateXmlString` | `0xA8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddValidThumbPrints` | `0xA8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `IsCatalogSigned` | `0xA900` | 253 | UnwindData |  |
| 2 | `IsCatSigned` | `0xAA00` | 219 | UnwindData |  |
