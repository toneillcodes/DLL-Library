# Binary Specification: TEEManagement64.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\dal.inf_amd64_b5484efd38adbe8d\TEEManagement64.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4740035101e18eaf5085d808907280c5e30fe7d69f9caacae9ab9f1c55823859`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `TEE_OpenSDSession` | `0x98B0` | 485 | UnwindData |  |
| 1 | `TEE_CloseSDSession` | `0x9AA0` | 131 | UnwindData |  |
| 8 | `TEE_SendAdminCmdPkg` | `0x9D20` | 331 | UnwindData |  |
| 4 | `TEE_ListInstalledTAs` | `0x9E70` | 322 | UnwindData |  |
| 3 | `TEE_ListInstalledSDs` | `0x9FC0` | 322 | UnwindData |  |
| 7 | `TEE_QueryTEEMetadata` | `0xA110` | 306 | UnwindData |  |
| 6 | `TEE_ProvisionOemMasterKey` | `0xA250` | 203 | UnwindData |  |
| 9 | `TEE_SetTAEncryptionKey` | `0xA530` | 203 | UnwindData |  |
| 2 | `TEE_DEALLOC` | `0xA820` | 143,420 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
