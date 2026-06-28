# Binary Specification: softkbd.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\softkbd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ecd4253eaa1db051d049256bf85c546991accc3db93fab5f3e1501c613f3e000`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x2B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x2B70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x2C00` | 261 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x2D10` | 178 | UnwindData |  |
