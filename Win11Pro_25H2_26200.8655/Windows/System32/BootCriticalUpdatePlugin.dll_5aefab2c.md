# Binary Specification: BootCriticalUpdatePlugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BootCriticalUpdatePlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5aefab2cb66e4f258ae10a84930a324ed662e6f3fe4438d5d822619e37b0a2cf`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x30A60` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x30A90` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x30BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x30BF0` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x30D20` | 152 | UnwindData |  |
