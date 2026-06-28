# Binary Specification: hascsp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\hascsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `de0a412c2d6d1c63837bb9ed61c6cabbb596811b36da3091ba25c3cd7e033df2`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `PolicyManager_PreCheck` | `0x2C50` | 124 | UnwindData |  |
| 10 | `DllRegisterServer` | `0x4F40` | 73,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllUnregisterServer` | `0x4F40` | 73,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllCanUnloadNow` | `0x16CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllGetClassObject` | `0x16D10` | 214 | UnwindData |  |
| 9 | `DllMain` | `0x16DF0` | 235 | UnwindData |  |
| 1 | `GetForceRetrieve` | `0x172A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetHealthCert` | `0x172C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetNonce` | `0x172E0` | 574 | UnwindData |  |
| 5 | `SetForceRetrieve` | `0x17710` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SetNonce` | `0x17880` | 353 | UnwindData |  |
