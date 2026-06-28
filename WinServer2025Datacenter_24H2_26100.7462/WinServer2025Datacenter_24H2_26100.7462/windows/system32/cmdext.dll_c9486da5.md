# Binary Specification: cmdext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cmdext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c9486da55900f2d029b6f81ef5fcb102f4303dcbfd6dd4823bf292a67a2efadb`
* **Total Exported Functions:** 14

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 10 | `SaferWorker` | `0x1140` | 183 | UnwindData |  |
| 1 | `CmdBatNotificationStub` | `0x1580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ShellExecuteWorker` | `0x15A0` | 261 | UnwindData |  |
| 2 | `DoSHChangeNotify` | `0x27F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `FindFirstStreamWStub` | `0x2810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `FindNextStreamWStub` | `0x2830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `GetBinaryTypeWStub` | `0x2850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetVDMCurrentDirectoriesStub` | `0x2870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `LookupAccountSidWStub` | `0x2890` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MessageBeepStub` | `0x28B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `QueryFullProcessImageNameWStub` | `0x28D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `WNetAddConnection2WStub` | `0x28F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `WNetCancelConnection2WStub` | `0x2910` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `WNetGetConnectionWStub` | `0x2930` | 17,452 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
