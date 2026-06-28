# Binary Specification: sti_ci.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\sti_ci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3ef5304f78191f80f134fe7a34c38a82c53eeabbdea911485c1c9e50dd82463f`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `WiaCreatePortList` | `0x3300` | 24,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddDevice` | `0x9420` | 2,681 | UnwindData |  |
| 8 | `InstallWiaService` | `0x9EA0` | 629 | UnwindData |  |
| 11 | `WiaAddDevice` | `0xA840` | 262 | UnwindData |  |
| 13 | `WiaDestroyPortList` | `0xA950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `WiaDeviceEnum` | `0xA960` | 709 | UnwindData |  |
| 15 | `WiaRemoveDevice` | `0xAC30` | 259 | UnwindData |  |
| 16 | `ClassInstall` | `0x18900` | 301 | UnwindData |  |
| 17 | `CoinstallerEntry` | `0x18A40` | 398 | UnwindData |  |
| 2 | `CreateWiaDeviceList` | `0x21640` | 1,477 | UnwindData |  |
| 3 | `DestroyWiaDeviceList` | `0x21C10` | 553 | UnwindData |  |
| 4 | `DisableWiaDevice` | `0x21E40` | 538 | UnwindData |  |
| 5 | `EnableWiaDevice` | `0x22060` | 523 | UnwindData |  |
| 6 | `GetWiaDeviceProperty` | `0x224A0` | 889 | UnwindData |  |
| 7 | `InstallWiaDevice` | `0x22820` | 3,729 | UnwindData |  |
| 9 | `SetWiaDeviceProperty` | `0x23840` | 750 | UnwindData |  |
| 10 | `UninstallWiaDevice` | `0x23B40` | 823 | UnwindData |  |
