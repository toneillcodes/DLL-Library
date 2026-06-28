# Binary Specification: samcli.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\samcli.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5d95f4cef8ca5d95ee86b6395a9895df0552efb4a6a24ba8b90c133dacebe3b2`
* **Total Exported Functions:** 36

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 25 | `NetUserDel` | `0x1250` | 424 | UnwindData |  |
| 20 | `NetLocalGroupSetInfo` | `0x1460` | 433 | UnwindData |  |
| 31 | `NetUserModalsGet` | `0x1620` | 122 | UnwindData |  |
| 7 | `NetGroupGetInfo` | `0x1DE0` | 8 | UnwindData |  |
| 30 | `NetUserGetLocalGroups` | `0x2000` | 2,403 | UnwindData |  |
| 28 | `NetUserGetInfo` | `0x3CE0` | 34 | UnwindData |  |
| 26 | `NetUserEnum` | `0x4400` | 2,313 | UnwindData |  |
| 19 | `NetLocalGroupGetMembers` | `0x6900` | 2,978 | UnwindData |  |
| 17 | `NetLocalGroupEnum` | `0x74B0` | 36 | UnwindData |  |
| 18 | `NetLocalGroupGetInfo` | `0x7E40` | 251 | UnwindData |  |
| 16 | `NetLocalGroupDelMembers` | `0x9090` | 31 | UnwindData |  |
| 13 | `NetLocalGroupAddMembers` | `0x90C0` | 31 | UnwindData |  |
| 11 | `NetLocalGroupAdd` | `0xAB10` | 439 | UnwindData |  |
| 12 | `NetLocalGroupAddMember` | `0xACD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `NetLocalGroupDel` | `0xACF0` | 186 | UnwindData |  |
| 15 | `NetLocalGroupDelMember` | `0xADB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `NetLocalGroupSetMembers` | `0xADC0` | 28 | UnwindData |  |
| 1 | `NetGetDisplayInformationIndex` | `0xB090` | 300 | UnwindData |  |
| 22 | `NetQueryDisplayInformation` | `0xB1D0` | 1,183 | UnwindData |  |
| 2 | `NetGroupAdd` | `0xB680` | 631 | UnwindData |  |
| 3 | `NetGroupAddUser` | `0xB900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `NetGroupDel` | `0xB920` | 34 | UnwindData |  |
| 5 | `NetGroupDelUser` | `0xB950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `NetGroupEnum` | `0xB960` | 1,587 | UnwindData |  |
| 8 | `NetGroupGetUsers` | `0xBFA0` | 924 | UnwindData |  |
| 9 | `NetGroupSetInfo` | `0xC350` | 572 | UnwindData |  |
| 10 | `NetGroupSetUsers` | `0xC5A0` | 28 | UnwindData |  |
| 29 | `NetUserGetInternetIdentityInfo` | `0xD1C0` | 461 | UnwindData |  |
| 35 | `NetValidatePasswordPolicy` | `0xD3A0` | 694 | UnwindData |  |
| 36 | `NetValidatePasswordPolicyFree` | `0xD660` | 111 | UnwindData |  |
| 23 | `NetUserAdd` | `0xE7F0` | 639 | UnwindData |  |
| 24 | `NetUserChangePassword` | `0xEA80` | 710 | UnwindData |  |
| 27 | `NetUserGetGroups` | `0xED50` | 870 | UnwindData |  |
| 32 | `NetUserModalsSet` | `0xF0C0` | 1,699 | UnwindData |  |
| 33 | `NetUserSetGroups` | `0xF770` | 1,403 | UnwindData |  |
| 34 | `NetUserSetInfo` | `0xFD00` | 360 | UnwindData |  |
