# Binary Specification: plutonksp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\plutonksp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `056a5e3c0850e58879dea161838e19d4a3519de15dfd6fceddb2f3a0a26778e6`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0xBC80` | 565 | UnwindData |  |
| 2 | `DllUnregisterServer` | `0xBEC0` | 259 | UnwindData |  |
| 3 | `DllMain` | `0xCD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `GetKeyStorageInterface` | `0xCD80` | 129 | UnwindData |  |
