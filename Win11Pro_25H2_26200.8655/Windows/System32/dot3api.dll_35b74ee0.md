# Binary Specification: dot3api.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dot3api.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `35b74ee0b14c3db46388c3c8a7751baccc92bcd433096d470e2946ae71ad8b59`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `Dot3CloseHandle` | `0x12CB0` | 536 | UnwindData |  |
| 3 | `Dot3CompleteMigration` | `0x12ED0` | 507 | UnwindData |  |
| 5 | `Dot3DeleteProfile` | `0x130E0` | 556 | UnwindData |  |
| 7 | `Dot3EnumInterfaces` | `0x13320` | 667 | UnwindData |  |
| 8 | `Dot3FreeMemory` | `0x135D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `Dot3GetCurrentProfile` | `0x135E0` | 618 | UnwindData |  |
| 10 | `Dot3GetInterfaceState` | `0x13850` | 749 | UnwindData |  |
| 11 | `Dot3GetProfile` | `0x13B50` | 580 | UnwindData |  |
| 14 | `Dot3OpenHandle` | `0x13DA0` | 892 | UnwindData |  |
| 15 | `Dot3QueryAutoConfigParameter` | `0x14130` | 728 | UnwindData |  |
| 17 | `Dot3QueryUIRequest` | `0x14410` | 619 | UnwindData |  |
| 18 | `Dot3ReConnect` | `0x14690` | 530 | UnwindData |  |
| 19 | `Dot3ReasonCodeToString` | `0x148B0` | 250 | UnwindData |  |
| 20 | `Dot3RegisterNotification` | `0x149B0` | 553 | UnwindData |  |
| 21 | `Dot3SetAutoConfigParameter` | `0x14BE0` | 578 | UnwindData |  |
| 22 | `Dot3SetInterface` | `0x14E30` | 546 | UnwindData |  |
| 23 | `Dot3SetProfile` | `0x15060` | 592 | UnwindData |  |
| 24 | `Dot3SetProfileEapUserData` | `0x152C0` | 625 | UnwindData |  |
| 25 | `Dot3SetProfileEapXmlUserData` | `0x15540` | 2,138 | UnwindData |  |
| 26 | `Dot3UIResponse` | `0x15DA0` | 651 | UnwindData |  |
| 27 | `QueryNetconStatus` | `0x167F0` | 911 | UnwindData |  |
| 1 | `Dot3CancelPlap` | `0x19510` | 217 | UnwindData |  |
| 4 | `Dot3DeinitPlapParams` | `0x195F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `Dot3DoPlap` | `0x19610` | 4,681 | UnwindData |  |
| 12 | `Dot3GetProfileEapUserDataInfo` | `0x1A860` | 267 | UnwindData |  |
| 13 | `Dot3InitPlapParams` | `0x1A980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `Dot3QueryPlapCredentials` | `0x1A9A0` | 366 | UnwindData |  |
