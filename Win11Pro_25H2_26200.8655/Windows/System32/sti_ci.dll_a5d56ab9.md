# Binary Specification: sti_ci.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\sti_ci.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a5d56ab9076e7b804f37ba314b1c4018e7a08d8393cd193460a6a94f1a397b5b`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 12 | `WiaCreatePortList` | `0x32B0` | 24,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddDevice` | `0x93D0` | 2,681 | UnwindData |  |
| 8 | `InstallWiaService` | `0x9E50` | 629 | UnwindData |  |
| 11 | `WiaAddDevice` | `0xA7F0` | 262 | UnwindData |  |
| 13 | `WiaDestroyPortList` | `0xA900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `WiaDeviceEnum` | `0xA910` | 709 | UnwindData |  |
| 15 | `WiaRemoveDevice` | `0xABE0` | 259 | UnwindData |  |
| 16 | `ClassInstall` | `0x15E60` | 301 | UnwindData |  |
| 17 | `CoinstallerEntry` | `0x15FA0` | 398 | UnwindData |  |
| 2 | `CreateWiaDeviceList` | `0x1E6A0` | 1,477 | UnwindData |  |
| 3 | `DestroyWiaDeviceList` | `0x1EC70` | 553 | UnwindData |  |
| 4 | `DisableWiaDevice` | `0x1EEA0` | 538 | UnwindData |  |
| 5 | `EnableWiaDevice` | `0x1F0C0` | 523 | UnwindData |  |
| 6 | `GetWiaDeviceProperty` | `0x1F500` | 889 | UnwindData |  |
| 7 | `InstallWiaDevice` | `0x1F880` | 3,729 | UnwindData |  |
| 9 | `SetWiaDeviceProperty` | `0x208A0` | 750 | UnwindData |  |
| 10 | `UninstallWiaDevice` | `0x20BA0` | 823 | UnwindData |  |
