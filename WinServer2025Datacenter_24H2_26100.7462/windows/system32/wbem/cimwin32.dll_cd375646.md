# Binary Specification: cimwin32.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\cimwin32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cd3756466b4bfcf5a87b5e6863a8bd9fa8bbe54c6e34d87c7016ee26015067a4`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllCanUnloadNow` | `0x48570` | 74 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x63BF0` | 78 | UnwindData |  |
| 4 | `??4CTcpMib@@QEAAAEAV0@AEBV0@@Z` | `0x89A80` | 14,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllRegisterServer` | `0x8D370` | 52 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x8D3B0` | 45 | UnwindData |  |
| 1 | `??0CTcpMib@@QEAA@AEBV0@@Z` | `0xD0D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CTcpMib@@QEAA@XZ` | `0xD0D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??1CTcpMib@@UEAA@XZ` | `0xD0D70` | 246,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetSDFromWin32SecurityDescriptor` | `0x10CF20` | 125 | UnwindData |  |
| 12 | `SetWin32SecurityDescriptorFromSD` | `0x10CFB0` | 141 | UnwindData |  |
| 5 | `??_7CTcpMib@@6B@` | `0x1429B0` | 469,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `?MySecurityDescriptor@@3VWin32SecurityDescriptor@@A` | `0x1B5250` | 0 | Indeterminate |  |
