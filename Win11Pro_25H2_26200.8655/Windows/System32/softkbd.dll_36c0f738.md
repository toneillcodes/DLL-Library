# Binary Specification: softkbd.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\softkbd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `36c0f73816bec28396ee2ffa2bb742fb2d98740702cc5bee8f9d5c46e0d60081`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2B70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2C00` | 261 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x2D10` | 178 | UnwindData |  |
