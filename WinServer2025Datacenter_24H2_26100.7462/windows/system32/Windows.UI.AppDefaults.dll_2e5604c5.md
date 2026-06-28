# Binary Specification: Windows.UI.AppDefaults.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.UI.AppDefaults.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2e5604c57aa9524ac712199d3c1a6c514d66256bf8c758951a8a185d1ca49650`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xD3C0` | 42 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xD3F0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xD430` | 65 | UnwindData |  |
| 4 | `GetSetting` | `0xD4A0` | 276,172 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
