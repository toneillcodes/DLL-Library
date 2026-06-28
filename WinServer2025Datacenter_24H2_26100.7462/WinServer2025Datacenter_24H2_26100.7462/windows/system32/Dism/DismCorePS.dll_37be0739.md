# Binary Specification: DismCorePS.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\DismCorePS.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `37be0739fa92d26ed08fb41da75cfd490d5ea1cf3fa30ef4d0fb998244ce4d3d`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2D10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2D30` | 53 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x2DA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x2DD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetDismInterfaces` | `0x2E00` | 0 | Indeterminate |  |
