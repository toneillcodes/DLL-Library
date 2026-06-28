# Binary Specification: WsUpgrade.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\WsUpgrade.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `edfe056696e6394d33802200ba26f8750a1fbd5f0c79aa9bc60583709d5faeae`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1A590` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1A5C0` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x1A700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x1A720` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1A850` | 151 | UnwindData |  |
