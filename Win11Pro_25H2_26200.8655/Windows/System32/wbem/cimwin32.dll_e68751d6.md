# Binary Specification: cimwin32.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wbem\cimwin32.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e68751d64058a93ab8a7ece8a286e8214676931fe88e7166ff745c311260829b`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `DllCanUnloadNow` | `0x3E8C0` | 74 | UnwindData |  |
| 8 | `DllGetClassObject` | `0x64040` | 78 | UnwindData |  |
| 4 | `??4CTcpMib@@QEAAAEAV0@AEBV0@@Z` | `0x89AB0` | 14,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllRegisterServer` | `0x8D3C0` | 52 | UnwindData |  |
| 10 | `DllUnregisterServer` | `0x8D400` | 45 | UnwindData |  |
| 1 | `??0CTcpMib@@QEAA@AEBV0@@Z` | `0xD2540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CTcpMib@@QEAA@XZ` | `0xD2540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??1CTcpMib@@UEAA@XZ` | `0xD2560` | 246,192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `GetSDFromWin32SecurityDescriptor` | `0x10E710` | 125 | UnwindData |  |
| 12 | `SetWin32SecurityDescriptorFromSD` | `0x10E7A0` | 141 | UnwindData |  |
| 5 | `??_7CTcpMib@@6B@` | `0x143A00` | 469,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `?MySecurityDescriptor@@3VWin32SecurityDescriptor@@A` | `0x1B6250` | 0 | Indeterminate |  |
