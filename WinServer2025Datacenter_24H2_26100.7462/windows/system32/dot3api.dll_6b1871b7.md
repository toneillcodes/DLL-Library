# Binary Specification: dot3api.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dot3api.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6b1871b7ae04873a5b95651d58e647753595395e2bc6afc55a5b828697fc5335`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `Dot3CloseHandle` | `0x12B90` | 536 | UnwindData |  |
| 4 | `Dot3DeleteProfile` | `0x12DB0` | 556 | UnwindData |  |
| 6 | `Dot3EnumInterfaces` | `0x12FF0` | 667 | UnwindData |  |
| 7 | `Dot3FreeMemory` | `0x132A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `Dot3GetCurrentProfile` | `0x132B0` | 618 | UnwindData |  |
| 9 | `Dot3GetInterfaceState` | `0x13520` | 749 | UnwindData |  |
| 10 | `Dot3GetProfile` | `0x13820` | 580 | UnwindData |  |
| 13 | `Dot3OpenHandle` | `0x13A70` | 892 | UnwindData |  |
| 14 | `Dot3QueryAutoConfigParameter` | `0x13E00` | 728 | UnwindData |  |
| 16 | `Dot3QueryUIRequest` | `0x140E0` | 619 | UnwindData |  |
| 17 | `Dot3ReConnect` | `0x14360` | 530 | UnwindData |  |
| 18 | `Dot3ReasonCodeToString` | `0x14580` | 250 | UnwindData |  |
| 19 | `Dot3RegisterNotification` | `0x14680` | 553 | UnwindData |  |
| 20 | `Dot3SetAutoConfigParameter` | `0x148B0` | 578 | UnwindData |  |
| 21 | `Dot3SetInterface` | `0x14B00` | 546 | UnwindData |  |
| 22 | `Dot3SetProfile` | `0x14D30` | 592 | UnwindData |  |
| 23 | `Dot3SetProfileEapUserData` | `0x14F90` | 625 | UnwindData |  |
| 24 | `Dot3SetProfileEapXmlUserData` | `0x15210` | 2,138 | UnwindData |  |
| 25 | `Dot3UIResponse` | `0x15A70` | 651 | UnwindData |  |
| 26 | `QueryNetconStatus` | `0x164C0` | 911 | UnwindData |  |
| 1 | `Dot3CancelPlap` | `0x191E0` | 217 | UnwindData |  |
| 3 | `Dot3DeinitPlapParams` | `0x192C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `Dot3DoPlap` | `0x192E0` | 4,681 | UnwindData |  |
| 11 | `Dot3GetProfileEapUserDataInfo` | `0x1A530` | 267 | UnwindData |  |
| 12 | `Dot3InitPlapParams` | `0x1A650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `Dot3QueryPlapCredentials` | `0x1A670` | 366 | UnwindData |  |
