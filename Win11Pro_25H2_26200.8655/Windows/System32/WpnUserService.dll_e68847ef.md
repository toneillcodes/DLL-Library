# Binary Specification: WpnUserService.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WpnUserService.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e68847efd454467ad079ab1f20e98e4b3f1db63d36a36449f38b85a95b152e1c`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xD9C0` | 70 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xDA10` | 232 | UnwindData |  |
| 3 | `ServiceMain` | `0xDB80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `SvchostPushServiceGlobals` | `0xDBA0` | 12,433 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
