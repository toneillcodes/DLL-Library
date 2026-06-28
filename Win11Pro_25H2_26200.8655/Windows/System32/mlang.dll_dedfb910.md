# Binary Specification: mlang.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mlang.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dedfb9109824c1ccf2ac4e83cf85263e7f6df5ed0ee086ab8762041b1109fbd2`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 121 | `LcidToRfc1766W` | `0x46F0` | 317 | UnwindData |  |
| 123 | `Rfc1766ToLcidW` | `0x4D30` | 49 | UnwindData |  |
| 111 | `ConvertINetString` | `0x6A50` | 64 | UnwindData |  |
| 112 | `ConvertINetUnicodeToMultiByte` | `0x6B30` | 139 | UnwindData |  |
| 113 | `ConvertINetMultiByteToUnicode` | `0x6BD0` | 107 | UnwindData |  |
| 110 | `IsConvertINetStringAvailable` | `0x6C50` | 142 | UnwindData |  |
| 116 | `DllGetClassObject` | `0x12290` | 100 | UnwindData |  |
| 115 | `DllCanUnloadNow` | `0x13930` | 9,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ConvertINetReset` | `0x15C70` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `GetGlobalFontLinkObject` | `0x160D0` | 143 | UnwindData |  |
| 120 | `LcidToRfc1766A` | `0x17490` | 317 | UnwindData |  |
| 122 | `Rfc1766ToLcidA` | `0x1EB90` | 111 | UnwindData |  |
