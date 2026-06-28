# Binary Specification: cemapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cemapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `145a2a3f81558d7ae70f5402527e362cb2c1300b6fba3bafe7e7c660b8d1a024`
* **Total Exported Functions:** 34

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 54 | `GetMAPIStorePropTags` | `0x8410` | 85 | UnwindData |  |
| 55 | `GetMsgClassEnum` | `0x85C0` | 112 | UnwindData |  |
| 56 | `GetMsgClassEnumFromMsg` | `0x8640` | 111 | UnwindData |  |
| 58 | `IsMessageClassDeviceGenerated` | `0x86C0` | 83 | UnwindData |  |
| 59 | `IsMessageClassReadRequest` | `0x8720` | 191 | UnwindData |  |
| 60 | `IsMessageClassSPlusV2` | `0x87F0` | 101 | UnwindData |  |
| 62 | `TranslateSPlusV1MessageClassToV2` | `0x8890` | 140 | UnwindData |  |
| 57 | `InitializeServiceProps` | `0x8930` | 6,304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `MAPI_CompareEntryIDs` | `0xA1D0` | 185 | UnwindData |  |
| 65 | `FlushMailStore` | `0xA970` | 163 | UnwindData |  |
| 67 | `GetEntryIDType` | `0xAA20` | 154 | UnwindData |  |
| 68 | `GetMsgStoreFromMessage` | `0xAAC0` | 207 | UnwindData |  |
| 69 | `GetNamedPropTag` | `0xABA0` | 231 | UnwindData |  |
| 74 | `MAPIDeleteMessageById` | `0xAC90` | 544 | UnwindData |  |
| 75 | `MAPIDupString` | `0xAEC0` | 205 | UnwindData |  |
| 77 | `MAPIGetContext` | `0xAFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `MAPI_GetStoreByName` | `0xAFB0` | 578 | UnwindData |  |
| 82 | `ReadMailVolumeNameEx` | `0xB200` | 59 | UnwindData |  |
| 83 | `SetConversationId` | `0xB250` | 198 | UnwindData |  |
| 84 | `USOIDfromCEENTRYID` | `0xB320` | 121 | UnwindData |  |
| 85 | `USOIDtoCEENTRYID` | `0xB3A0` | 126 | UnwindData |  |
| 63 | `CreateMAPITableWalker` | `0xBC40` | 31 | UnwindData |  |
| 64 | `CreateMAPITableWalkerEx` | `0xBC70` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `FreeProws` | `0xBE40` | 178 | UnwindData |  |
| 72 | `MAPIAllocateBuffer` | `0xBF00` | 158 | UnwindData |  |
| 52 | `MAPIAllocateBuffer_dbg` | `0xBFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `MAPIAllocateMore` | `0xBFC0` | 271 | UnwindData |  |
| 53 | `MAPIAllocateMore_dbg` | `0xC0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `MAPIFreeBuffer` | `0xC0F0` | 168 | UnwindData |  |
| 70 | `HrGetOneProp` | `0xDB70` | 239 | UnwindData |  |
| 71 | `HrSetOneProp` | `0xDC70` | 89 | UnwindData |  |
| 78 | `MAPIInitialize` | `0xDF00` | 56 | UnwindData |  |
| 79 | `MAPILogonEx` | `0xDF40` | 326 | UnwindData |  |
| 80 | `MAPIUninitialize` | `0xE090` | 145 | UnwindData |  |
