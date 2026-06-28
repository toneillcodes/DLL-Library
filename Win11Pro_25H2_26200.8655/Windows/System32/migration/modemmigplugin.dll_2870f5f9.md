# Binary Specification: modemmigplugin.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\migration\modemmigplugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2870f5f95416b65222fb8ee8a68448b667845c55609812b7819bc3034734fad2`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x66B0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x66E0` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x6820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x6840` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6970` | 151 | UnwindData |  |
