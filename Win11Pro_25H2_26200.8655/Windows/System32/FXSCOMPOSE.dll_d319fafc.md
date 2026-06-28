# Binary Specification: FXSCOMPOSE.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FXSCOMPOSE.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d319fafc81c7036fc316c5cb95f4aa620b9145e9a7806be355e5f783eb3a7195`
* **Total Exported Functions:** 15

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `FaxComposeFreeBuffer` | `0x9310` | 98 | UnwindData |  |
| 2 | `HrAddressBookPreTranslateAccelerator` | `0x9380` | 227 | UnwindData |  |
| 3 | `HrDeInitAddressBook` | `0x9470` | 149 | UnwindData |  |
| 4 | `HrDeinitComposeFormDll` | `0x9510` | 339 | UnwindData |  |
| 5 | `HrFaxComposePreTranslateAccelerator` | `0x9670` | 94 | UnwindData |  |
| 6 | `HrFreeDraftsListViewInfo` | `0x96E0` | 214 | UnwindData |  |
| 7 | `HrGetDraftsListViewInfo` | `0x97C0` | 1,010 | UnwindData |  |
| 8 | `HrInitAddressBook` | `0x9BC0` | 78 | UnwindData |  |
| 9 | `HrInitComposeFormDll` | `0x9C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `HrInvokeAddressBook` | `0x9C30` | 306 | UnwindData |  |
| 11 | `HrNewFaxComposeUI` | `0x9D70` | 163 | UnwindData |  |
| 12 | `HrNewFaxComposeUIFromFile` | `0x9E20` | 45 | UnwindData |  |
| 13 | `HrNewTiffViewUIFromFile` | `0x9E60` | 41 | UnwindData |  |
| 14 | `HrSelectEmailRecipient` | `0x9E90` | 328 | UnwindData |  |
| 15 | `DllMain` | `0xA050` | 1,369 | UnwindData |  |
