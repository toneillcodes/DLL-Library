# Binary Specification: StorSvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\StorSvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7ad9da276b33bdd18901aba2fac6472584ea17f989bd760cc1113a83a4a59f26`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x21800` | 32 | UnwindData |  |
| 4 | `DllGetActivationFactory` | `0x21830` | 45 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x21870` | 65 | UnwindData |  |
| 1 | `ServiceMain` | `0x40DC0` | 461 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x411B0` | 352,812 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
