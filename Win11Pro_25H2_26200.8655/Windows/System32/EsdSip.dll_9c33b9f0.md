# Binary Specification: EsdSip.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\EsdSip.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9c33b9f04da94d91c23f8a39c79c8380670af33762eb3f7a9063ee42c3ed9637`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `EsdSipCreateHash` | `0x3A00` | 1,056 | UnwindData |  |
| 2 | `EsdSipDelSignature` | `0x3E30` | 304 | UnwindData |  |
| 3 | `EsdSipGetCaps` | `0x3F70` | 60 | UnwindData |  |
| 4 | `EsdSipGetSignature` | `0x3FC0` | 346 | UnwindData |  |
| 5 | `EsdSipIsMyFileType` | `0x4120` | 704 | UnwindData |  |
| 6 | `EsdSipPutSignature` | `0x43F0` | 320 | UnwindData |  |
| 7 | `EsdSipVerifyHash` | `0x4540` | 543 | UnwindData |  |
| 8 | `DllCanUnloadNow` | `0x8880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllMain` | `0x8890` | 32 | UnwindData |  |
| 10 | `DllRegisterServer` | `0x88C0` | 310 | UnwindData |  |
| 11 | `DllUnregisterServer` | `0x8A00` | 31 | UnwindData |  |
