# Binary Specification: rastlsext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\rastlsext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `913a248d083ac1e286eb0f0217deae236fb9fe28e5ad16f8c26fac78d0e4f07a`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `RasTlsExt_FreeMemory` | `0x3E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `RasTlsExt_GetConfigCacheOnlyCertValidation` | `0x3E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `RasTlsExt_GetConfigForceNotDomainJoined` | `0x3E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `RasTlsExt_ShowHelp` | `0x3E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `RasTlsExt_GetPinUserBlob` | `0x3E40` | 318 | UnwindData |  |
| 9 | `RasTlsExt_GetServerCertDetails` | `0x3F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `RasTlsExt_SelectCertificate` | `0x3F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `RasTlsExt_ValidateServer` | `0x3F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `RasTlsExt_PackUserBlob` | `0x3FA0` | 201 | UnwindData |  |
| 13 | `RasTlsExt_UnpackUserBlob` | `0x4070` | 371 | UnwindData |  |
| 15 | `RasTlsExt_ValidateServerDialogProc` | `0x41F0` | 313 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x91C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x91E0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x93E0` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x9450` | 17 | UnwindData |  |
