# Binary Specification: WsUpgrade.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\WsUpgrade.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7706f8aac6d30d76d90a1c9d6dbfaa7e6f867bab60d07bf3418ad34eba09487d`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1A580` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1A5B0` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x1A6F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x1A710` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1A840` | 151 | UnwindData |  |
