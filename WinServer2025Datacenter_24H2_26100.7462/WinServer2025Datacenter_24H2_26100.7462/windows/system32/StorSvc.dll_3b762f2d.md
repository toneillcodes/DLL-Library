# Binary Specification: StorSvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\StorSvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3b762f2d87d7226fdff1499cd443f1033418b45750ce7717460e8b543fe5fa10`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x21750` | 32 | UnwindData |  |
| 4 | `DllGetActivationFactory` | `0x21780` | 45 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x217C0` | 65 | UnwindData |  |
| 1 | `ServiceMain` | `0x45850` | 461 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x45C40` | 347,068 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
