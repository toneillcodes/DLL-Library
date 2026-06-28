# Binary Specification: BootCriticalUpdatePlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BootCriticalUpdatePlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `307d62ab7203aa7d815570090b25e4d73f3bfe6377e64f5af54d607412ac8701`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x30BF0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x30C20` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x30D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x30D80` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x30EB0` | 152 | UnwindData |  |
