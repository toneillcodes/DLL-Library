# Binary Specification: dwmredir.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dwmredir.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `18acd924755aae0fb27d8912c70bb7d3996a13aaca6915ab0ccb094d1975b4b0`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DwmInitializePort` | `0xB530` | 36 | UnwindData |  |
| 1 | `DwmRedirectionManagerInitialize` | `0x1AA60` | 82 | UnwindData |  |
| 2 | `DwmRedirectionManagerShutdown` | `0x1AAC0` | 50 | UnwindData |  |
| 3 | `DwmRegisterWindowNotificationHandler` | `0x20E00` | 11,564 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
