# Binary Specification: cemapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\cemapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b417acac10b87f25cb734d5097d3ebcb750b64977f63522596fd73e6b2620457`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 54 | `GetMAPIStorePropTags` | `0x8400` | 85 | UnwindData |  |
| 55 | `GetMsgClassEnum` | `0x85B0` | 112 | UnwindData |  |
| 56 | `GetMsgClassEnumFromMsg` | `0x8630` | 111 | UnwindData |  |
| 58 | `IsMessageClassDeviceGenerated` | `0x86B0` | 83 | UnwindData |  |
| 59 | `IsMessageClassReadRequest` | `0x8710` | 191 | UnwindData |  |
| 60 | `IsMessageClassSPlusV2` | `0x87E0` | 101 | UnwindData |  |
| 62 | `TranslateSPlusV1MessageClassToV2` | `0x8880` | 140 | UnwindData |  |
| 57 | `InitializeServiceProps` | `0x8920` | 6,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MAPI_CompareEntryIDs` | `0xA1C0` | 185 | UnwindData |  |
| 65 | `FlushMailStore` | `0xA960` | 163 | UnwindData |  |
| 67 | `GetEntryIDType` | `0xAA10` | 154 | UnwindData |  |
| 68 | `GetMsgStoreFromMessage` | `0xAAB0` | 207 | UnwindData |  |
| 69 | `GetNamedPropTag` | `0xAB90` | 231 | UnwindData |  |
| 74 | `MAPIDeleteMessageById` | `0xAC80` | 544 | UnwindData |  |
| 75 | `MAPIDupString` | `0xAEB0` | 205 | UnwindData |  |
| 77 | `MAPIGetContext` | `0xAF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `MAPI_GetStoreByName` | `0xAFA0` | 578 | UnwindData |  |
| 82 | `ReadMailVolumeNameEx` | `0xB1F0` | 59 | UnwindData |  |
| 83 | `SetConversationId` | `0xB240` | 198 | UnwindData |  |
| 84 | `USOIDfromCEENTRYID` | `0xB310` | 121 | UnwindData |  |
| 85 | `USOIDtoCEENTRYID` | `0xB390` | 126 | UnwindData |  |
| 63 | `CreateMAPITableWalker` | `0xBC30` | 31 | UnwindData |  |
| 64 | `CreateMAPITableWalkerEx` | `0xBC60` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `FreeProws` | `0xBE30` | 178 | UnwindData |  |
| 72 | `MAPIAllocateBuffer` | `0xBEF0` | 158 | UnwindData |  |
| 52 | `MAPIAllocateBuffer_dbg` | `0xBFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `MAPIAllocateMore` | `0xBFB0` | 271 | UnwindData |  |
| 53 | `MAPIAllocateMore_dbg` | `0xC0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `MAPIFreeBuffer` | `0xC0E0` | 168 | UnwindData |  |
| 70 | `HrGetOneProp` | `0xDB60` | 239 | UnwindData |  |
| 71 | `HrSetOneProp` | `0xDC60` | 89 | UnwindData |  |
| 78 | `MAPIInitialize` | `0xDEF0` | 56 | UnwindData |  |
| 79 | `MAPILogonEx` | `0xDF30` | 326 | UnwindData |  |
| 80 | `MAPIUninitialize` | `0xE080` | 145 | UnwindData |  |
