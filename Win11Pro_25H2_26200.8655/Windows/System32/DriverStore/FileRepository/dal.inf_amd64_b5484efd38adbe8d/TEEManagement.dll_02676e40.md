# Binary Specification: TEEManagement.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\dal.inf_amd64_b5484efd38adbe8d\TEEManagement.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `02676e4006528a529364eb435ff5e09acd5ad160457eedf0a373f33d493b1f1d`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `TEE_OpenSDSession` | `0x8660` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `TEE_CloseSDSession` | `0x8890` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `TEE_SendAdminCmdPkg` | `0x89C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `TEE_ListInstalledTAs` | `0x8B30` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `TEE_ListInstalledSDs` | `0x8BD0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `TEE_QueryTEEMetadata` | `0x8C70` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `TEE_ProvisionOemMasterKey` | `0x8E10` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `TEE_SetTAEncryptionKey` | `0x8F60` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `TEE_DEALLOC` | `0x90B0` | 120,234 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
