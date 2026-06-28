# Binary Specification: EsdSip.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\EsdSip.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ce5198c32e3b6ca0c47fbb51445b1ad09df4ba668493e09f25988013b22a1d98`
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
| 8 | `DllCanUnloadNow` | `0x8870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllMain` | `0x8880` | 32 | UnwindData |  |
| 10 | `DllRegisterServer` | `0x88B0` | 310 | UnwindData |  |
| 11 | `DllUnregisterServer` | `0x89F0` | 31 | UnwindData |  |
