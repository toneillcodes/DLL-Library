# Binary Specification: cscobj.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cscobj.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a012eb3535475faefcd5b24c86041878a46b94e530569e6028ab4fa2960b6d56`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllGetClassObject` | `0x59B0` | 40 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0x60F0` | 57 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x105E0` | 63 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0x10630` | 63 | UnwindData |  |
| 1 | `ProcessGroupPolicy` | `0x12830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ProcessPolicy` | `0x12850` | 26 | UnwindData |  |
