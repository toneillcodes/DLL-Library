# Binary Specification: mssph.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mssph.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4a8148ac5dfee29ff6d8bd6a46cfb5b82369c3a37e8aa9a5e8a0c87c9f79485b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x1C860` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1C890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x1C8B0` | 338 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x1CA10` | 200 | UnwindData |  |
