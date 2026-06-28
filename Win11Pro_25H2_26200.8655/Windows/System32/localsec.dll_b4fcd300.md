# Binary Specification: localsec.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\localsec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b4fcd30039b016ac93977ffe1f23c98c891d92264a9f1a15801367cf79dcae67`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xE750` | 213 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xE860` | 134 | UnwindData |  |
