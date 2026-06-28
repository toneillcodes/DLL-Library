# Binary Specification: mmgaclient.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mmgaclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bb0a49a4de9f3e697be3279e20d175d9566c7d64713d7ef1f4a46ee464bae92f`
* **Total Exported Functions:** 82

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 139 | `FreePadrlist` | `0xB9C0` | 163 | UnwindData |  |
| 140 | `FreeProws` | `0xBA70` | 223 | UnwindData |  |
| 13 | `MAPIAllocateBuffer` | `0xBB60` | 95 | UnwindData |  |
| 15 | `MAPIAllocateMore` | `0xBBD0` | 168 | UnwindData |  |
| 17 | `MAPIFreeBuffer` | `0xBC80` | 111 | UnwindData |  |
| 59 | `MAPIGetDefaultMalloc` | `0xBD00` | 43 | UnwindData |  |
| 55 | `ChangeIdleRoutine` | `0x4F560` | 196 | UnwindData |  |
| 60 | `CreateIProp` | `0x4F630` | 201 | UnwindData |  |
| 61 | `CreateTable` | `0x4F700` | 246 | UnwindData |  |
| 34 | `DeinitMapiUtil` | `0x4F800` | 80 | UnwindData |  |
| 54 | `DeregisterIdleRoutine` | `0x4F860` | 121 | UnwindData |  |
| 53 | `EnableIdleRoutine` | `0x4F8E0` | 125 | UnwindData |  |
| 182 | `FBadColumnSet` | `0x4F970` | 127 | UnwindData |  |
| 190 | `FBadEntryList` | `0x4FA00` | 127 | UnwindData |  |
| 181 | `FBadProp` | `0x4FA90` | 127 | UnwindData |  |
| 179 | `FBadPropTag` | `0x4FB20` | 126 | UnwindData |  |
| 191 | `FBadRestriction` | `0x4FBB0` | 127 | UnwindData |  |
| 176 | `FBadRglpszW` | `0x4FC40` | 139 | UnwindData |  |
| 180 | `FBadRow` | `0x4FCE0` | 127 | UnwindData |  |
| 177 | `FBadRowSet` | `0x4FD70` | 127 | UnwindData |  |
| 189 | `FBadSortOrderSet` | `0x4FE00` | 127 | UnwindData |  |
| 72 | `FEqualNames` | `0x4FE90` | 140 | UnwindData |  |
| 79 | `FPropCompareProp` | `0x4FF30` | 161 | UnwindData |  |
| 78 | `FPropContainsProp` | `0x4FFE0` | 162 | UnwindData |  |
| 137 | `FPropExists` | `0x50090` | 139 | UnwindData |  |
| 259 | `ForceMmgaserverArchitecture` | `0x50130` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `FtgRegisterIdleRoutine` | `0x50160` | 198 | UnwindData |  |
| 200 | `GetAttribIMsgOnIStg` | `0x50230` | 162 | UnwindData |  |
| 153 | `GetTnefStreamCodepage` | `0x502E0` | 162 | UnwindData |  |
| 81 | `HrAddColumns` | `0x50390` | 172 | UnwindData |  |
| 82 | `HrAddColumnsEx` | `0x50450` | 195 | UnwindData |  |
| 143 | `HrComposeEID` | `0x50520` | 218 | UnwindData |  |
| 145 | `HrComposeMsgID` | `0x50600` | 200 | UnwindData |  |
| 144 | `HrDecomposeEID` | `0x506D0` | 218 | UnwindData |  |
| 146 | `HrDecomposeMsgID` | `0x507B0` | 201 | UnwindData |  |
| 239 | `HrDispatchNotifications` | `0x50880` | 126 | UnwindData |  |
| 142 | `HrEntryIDFromSz` | `0x50910` | 162 | UnwindData |  |
| 135 | `HrGetOneProp` | `0x509C0` | 161 | UnwindData |  |
| 194 | `HrIStorageFromStream` | `0x50A70` | 172 | UnwindData |  |
| 75 | `HrQueryAllRows` | `0x50B30` | 201 | UnwindData |  |
| 136 | `HrSetOneProp` | `0x50C00` | 140 | UnwindData |  |
| 141 | `HrSzFromEntryID` | `0x50CA0` | 161 | UnwindData |  |
| 195 | `HrValidateIPMSubtree` | `0x50D50` | 194 | UnwindData |  |
| 173 | `LpValFindProp` | `0x50E20` | 162 | UnwindData |  |
| 217 | `MAPIAddress` | `0x50ED0` | 270 | UnwindData |  |
| 19 | `MAPIAdminProfiles` | `0x50FF0` | 139 | UnwindData |  |
| 50 | `MAPIDeinitIdle` | `0x51090` | 80 | UnwindData |  |
| 215 | `MAPIDeleteMail` | `0x510F0` | 190 | UnwindData |  |
| 218 | `MAPIDetails` | `0x511C0` | 190 | UnwindData |  |
| 214 | `MAPIFindNext` | `0x51290` | 214 | UnwindData |  |
| 49 | `MAPIInitIdle` | `0x51370` | 127 | UnwindData |  |
| 21 | `MAPIInitialize` | `0x51400` | 211 | UnwindData |  |
| 210 | `MAPILogoff` | `0x514E0` | 167 | UnwindData |  |
| 209 | `MAPILogon` | `0x51590` | 196 | UnwindData |  |
| 11 | `MAPILogonEx` | `0x51660` | 190 | UnwindData |  |
| 30 | `MAPIOpenFormMgr` | `0x51730` | 140 | UnwindData |  |
| 32 | `MAPIOpenLocalFormContainer` | `0x517D0` | 127 | UnwindData |  |
| 213 | `MAPIReadMail` | `0x51860` | 196 | UnwindData |  |
| 219 | `MAPIResolveName` | `0x51930` | 196 | UnwindData |  |
| 212 | `MAPISaveMail` | `0x51A00` | 196 | UnwindData |  |
| 211 | `MAPISendMail` | `0x51AD0` | 190 | UnwindData |  |
| 208 | `MAPISendMailDocuments` | `0x51BA0` | 190 | UnwindData |  |
| 256 | `MAPISendMailW` | `0x51C70` | 190 | UnwindData |  |
| 23 | `MAPIUninitialize` | `0x51D40` | 137 | UnwindData |  |
| 201 | `MapStorageSCode` | `0x51DD0` | 126 | UnwindData |  |
| 198 | `OpenIMsgOnIStg` | `0x51E60` | 279 | UnwindData |  |
| 147 | `OpenStreamOnFile` | `0x51F80` | 201 | UnwindData |  |
| 149 | `OpenTnefStream` | `0x52050` | 219 | UnwindData |  |
| 151 | `OpenTnefStreamEx` | `0x52140` | 225 | UnwindData |  |
| 183 | `RTFSync` | `0x52230` | 161 | UnwindData |  |
| 171 | `ScCopyProps` | `0x522E0` | 171 | UnwindData |  |
| 170 | `ScCountProps` | `0x523A0` | 161 | UnwindData |  |
| 244 | `ScCreateConversationIndex` | `0x52450` | 171 | UnwindData |  |
| 174 | `ScDupPropset` | `0x52510` | 171 | UnwindData |  |
| 33 | `ScInitMapiUtil` | `0x525D0` | 126 | UnwindData |  |
| 199 | `SetAttribIMsgOnIStg` | `0x52660` | 172 | UnwindData |  |
| 257 | `SetUpForOutOfContainer` | `0x52720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `UlPropSize` | `0x52730` | 127 | UnwindData |  |
| 185 | `WrapCompressedRTFStream` | `0x527C0` | 161 | UnwindData |  |
| 73 | `WrapStoreEntryID` | `0x52870` | 200 | UnwindData |  |
| 138 | `PpropFindProp` | `0x52AE0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `PropCopyMore` | `0x52B30` | 1,432 | UnwindData |  |
