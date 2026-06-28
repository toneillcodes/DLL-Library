# Binary Specification: localsec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\localsec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5c914da309d224254a060826ef3dfecaffa17cdf739c0ad203bc759192d363d6`
* **Total Exported Functions:** 3

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE720` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xE750` | 213 | UnwindData |  |
| 3 | `DllRegisterServer` | `0xE860` | 134 | UnwindData |  |
