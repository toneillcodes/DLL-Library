# Binary Specification: mspatchc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mspatchc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e671f5e786b80ac41a270fe6cf88993288ba9a0dab089adee686d550ecb5a92e`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreatePatchFileA` | `0x1F00` | 87 | UnwindData |  |
| 2 | `CreatePatchFileByHandles` | `0x1F60` | 97 | UnwindData |  |
| 3 | `CreatePatchFileByHandlesEx` | `0x1FD0` | 70 | UnwindData |  |
| 4 | `CreatePatchFileExA` | `0x4130` | 616 | UnwindData |  |
| 5 | `CreatePatchFileExW` | `0x43A0` | 616 | UnwindData |  |
| 6 | `CreatePatchFileW` | `0x4610` | 87 | UnwindData |  |
| 7 | `ExtractPatchHeaderToFileA` | `0x5560` | 216 | UnwindData |  |
| 8 | `ExtractPatchHeaderToFileByHandles` | `0x5640` | 515 | UnwindData |  |
| 9 | `ExtractPatchHeaderToFileW` | `0x5850` | 216 | UnwindData |  |
| 10 | `GetFilePatchSignatureA` | `0x5930` | 209 | UnwindData |  |
| 11 | `GetFilePatchSignatureByBuffer` | `0x5A10` | 412 | UnwindData |  |
| 12 | `GetFilePatchSignatureByHandle` | `0x5BC0` | 222 | UnwindData |  |
| 13 | `GetFilePatchSignatureW` | `0x5CB0` | 362 | UnwindData |  |
| 14 | `NormalizeFileForPatchSignature` | `0x5E20` | 420 | UnwindData |  |
