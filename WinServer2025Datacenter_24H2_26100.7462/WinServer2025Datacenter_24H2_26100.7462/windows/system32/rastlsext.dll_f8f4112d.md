# Binary Specification: rastlsext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rastlsext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f8f4112d2b34cf31cd64a9bebe0be93472962e45155890713e1d4369d3b94a25`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `RasTlsExt_FreeMemory` | `0x3E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `RasTlsExt_GetConfigCacheOnlyCertValidation` | `0x3E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RasTlsExt_GetConfigForceNotDomainJoined` | `0x3E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `RasTlsExt_ShowHelp` | `0x3E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RasTlsExt_GetPinUserBlob` | `0x3E30` | 318 | UnwindData |  |
| 9 | `RasTlsExt_GetServerCertDetails` | `0x3F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `RasTlsExt_SelectCertificate` | `0x3F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `RasTlsExt_ValidateServer` | `0x3F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `RasTlsExt_PackUserBlob` | `0x3F90` | 201 | UnwindData |  |
| 13 | `RasTlsExt_UnpackUserBlob` | `0x4060` | 371 | UnwindData |  |
| 15 | `RasTlsExt_ValidateServerDialogProc` | `0x41E0` | 313 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x91B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x91D0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x93D0` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x9440` | 17 | UnwindData |  |
