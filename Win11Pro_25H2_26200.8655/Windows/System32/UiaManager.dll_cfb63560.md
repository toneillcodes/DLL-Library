# Binary Specification: UiaManager.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\UiaManager.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cfb6356001ac7b1fb51e2224fecfdd57acf384fa8b3dfdc4b3c295fbcc787be6`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllGetClassObject` | `0xC9C0` | 689 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0xD480` | 75 | UnwindData |  |
| 5 | `GetProxyDllInfo` | `0x27440` | 238,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `UiaInitCrossMachineConnection` | `0x617A0` | 362 | UnwindData |  |
| 2 | `UiaInitCrossMachineConnectionW` | `0x617A0` | 362 | UnwindData |  |
