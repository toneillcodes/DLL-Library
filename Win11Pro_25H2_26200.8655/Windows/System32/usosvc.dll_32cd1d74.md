# Binary Specification: usosvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\usosvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `32cd1d74b05f28579f1f9930db8f4c8f6bac93e0e65c58c07ef2601d3727ddf2`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `ServiceMain` | `0x9FA0` | 178 | UnwindData |  |
| 3 | `SvchostPushServiceGlobals` | `0xA060` | 261 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xAC40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0xAC60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllMain` | `0xAC80` | 32 | UnwindData |  |
| 1 | `GeneralizeForImaging` | `0xC330` | 313 | UnwindData |  |
