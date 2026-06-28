# Binary Specification: mmgaclient.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mmgaclient.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c1bfa6d00ff96d1771a6b2fbcac03856a72ef1b67767c0d06d91bc3eaa16eef8`
* **Total Exported Functions:** 82

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 139 | `FreePadrlist` | `0xB9A0` | 163 | UnwindData |  |
| 140 | `FreeProws` | `0xBA50` | 223 | UnwindData |  |
| 13 | `MAPIAllocateBuffer` | `0xBB40` | 95 | UnwindData |  |
| 15 | `MAPIAllocateMore` | `0xBBB0` | 168 | UnwindData |  |
| 17 | `MAPIFreeBuffer` | `0xBC60` | 111 | UnwindData |  |
| 59 | `MAPIGetDefaultMalloc` | `0xBCE0` | 43 | UnwindData |  |
| 55 | `ChangeIdleRoutine` | `0x4F540` | 196 | UnwindData |  |
| 60 | `CreateIProp` | `0x4F610` | 201 | UnwindData |  |
| 61 | `CreateTable` | `0x4F6E0` | 246 | UnwindData |  |
| 34 | `DeinitMapiUtil` | `0x4F7E0` | 80 | UnwindData |  |
| 54 | `DeregisterIdleRoutine` | `0x4F840` | 121 | UnwindData |  |
| 53 | `EnableIdleRoutine` | `0x4F8C0` | 125 | UnwindData |  |
| 182 | `FBadColumnSet` | `0x4F950` | 127 | UnwindData |  |
| 190 | `FBadEntryList` | `0x4F9E0` | 127 | UnwindData |  |
| 181 | `FBadProp` | `0x4FA70` | 127 | UnwindData |  |
| 179 | `FBadPropTag` | `0x4FB00` | 126 | UnwindData |  |
| 191 | `FBadRestriction` | `0x4FB90` | 127 | UnwindData |  |
| 176 | `FBadRglpszW` | `0x4FC20` | 139 | UnwindData |  |
| 180 | `FBadRow` | `0x4FCC0` | 127 | UnwindData |  |
| 177 | `FBadRowSet` | `0x4FD50` | 127 | UnwindData |  |
| 189 | `FBadSortOrderSet` | `0x4FDE0` | 127 | UnwindData |  |
| 72 | `FEqualNames` | `0x4FE70` | 140 | UnwindData |  |
| 79 | `FPropCompareProp` | `0x4FF10` | 161 | UnwindData |  |
| 78 | `FPropContainsProp` | `0x4FFC0` | 162 | UnwindData |  |
| 137 | `FPropExists` | `0x50070` | 139 | UnwindData |  |
| 259 | `ForceMmgaserverArchitecture` | `0x50110` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `FtgRegisterIdleRoutine` | `0x50140` | 198 | UnwindData |  |
| 200 | `GetAttribIMsgOnIStg` | `0x50210` | 162 | UnwindData |  |
| 153 | `GetTnefStreamCodepage` | `0x502C0` | 162 | UnwindData |  |
| 81 | `HrAddColumns` | `0x50370` | 172 | UnwindData |  |
| 82 | `HrAddColumnsEx` | `0x50430` | 195 | UnwindData |  |
| 143 | `HrComposeEID` | `0x50500` | 218 | UnwindData |  |
| 145 | `HrComposeMsgID` | `0x505E0` | 200 | UnwindData |  |
| 144 | `HrDecomposeEID` | `0x506B0` | 218 | UnwindData |  |
| 146 | `HrDecomposeMsgID` | `0x50790` | 201 | UnwindData |  |
| 239 | `HrDispatchNotifications` | `0x50860` | 126 | UnwindData |  |
| 142 | `HrEntryIDFromSz` | `0x508F0` | 162 | UnwindData |  |
| 135 | `HrGetOneProp` | `0x509A0` | 161 | UnwindData |  |
| 194 | `HrIStorageFromStream` | `0x50A50` | 172 | UnwindData |  |
| 75 | `HrQueryAllRows` | `0x50B10` | 201 | UnwindData |  |
| 136 | `HrSetOneProp` | `0x50BE0` | 140 | UnwindData |  |
| 141 | `HrSzFromEntryID` | `0x50C80` | 161 | UnwindData |  |
| 195 | `HrValidateIPMSubtree` | `0x50D30` | 194 | UnwindData |  |
| 173 | `LpValFindProp` | `0x50E00` | 162 | UnwindData |  |
| 217 | `MAPIAddress` | `0x50EB0` | 270 | UnwindData |  |
| 19 | `MAPIAdminProfiles` | `0x50FD0` | 139 | UnwindData |  |
| 50 | `MAPIDeinitIdle` | `0x51070` | 80 | UnwindData |  |
| 215 | `MAPIDeleteMail` | `0x510D0` | 190 | UnwindData |  |
| 218 | `MAPIDetails` | `0x511A0` | 190 | UnwindData |  |
| 214 | `MAPIFindNext` | `0x51270` | 214 | UnwindData |  |
| 49 | `MAPIInitIdle` | `0x51350` | 127 | UnwindData |  |
| 21 | `MAPIInitialize` | `0x513E0` | 211 | UnwindData |  |
| 210 | `MAPILogoff` | `0x514C0` | 167 | UnwindData |  |
| 209 | `MAPILogon` | `0x51570` | 196 | UnwindData |  |
| 11 | `MAPILogonEx` | `0x51640` | 190 | UnwindData |  |
| 30 | `MAPIOpenFormMgr` | `0x51710` | 140 | UnwindData |  |
| 32 | `MAPIOpenLocalFormContainer` | `0x517B0` | 127 | UnwindData |  |
| 213 | `MAPIReadMail` | `0x51840` | 196 | UnwindData |  |
| 219 | `MAPIResolveName` | `0x51910` | 196 | UnwindData |  |
| 212 | `MAPISaveMail` | `0x519E0` | 196 | UnwindData |  |
| 211 | `MAPISendMail` | `0x51AB0` | 190 | UnwindData |  |
| 208 | `MAPISendMailDocuments` | `0x51B80` | 190 | UnwindData |  |
| 256 | `MAPISendMailW` | `0x51C50` | 190 | UnwindData |  |
| 23 | `MAPIUninitialize` | `0x51D20` | 137 | UnwindData |  |
| 201 | `MapStorageSCode` | `0x51DB0` | 126 | UnwindData |  |
| 198 | `OpenIMsgOnIStg` | `0x51E40` | 279 | UnwindData |  |
| 147 | `OpenStreamOnFile` | `0x51F60` | 201 | UnwindData |  |
| 149 | `OpenTnefStream` | `0x52030` | 219 | UnwindData |  |
| 151 | `OpenTnefStreamEx` | `0x52120` | 225 | UnwindData |  |
| 183 | `RTFSync` | `0x52210` | 161 | UnwindData |  |
| 171 | `ScCopyProps` | `0x522C0` | 171 | UnwindData |  |
| 170 | `ScCountProps` | `0x52380` | 161 | UnwindData |  |
| 244 | `ScCreateConversationIndex` | `0x52430` | 171 | UnwindData |  |
| 174 | `ScDupPropset` | `0x524F0` | 171 | UnwindData |  |
| 33 | `ScInitMapiUtil` | `0x525B0` | 126 | UnwindData |  |
| 199 | `SetAttribIMsgOnIStg` | `0x52640` | 172 | UnwindData |  |
| 257 | `SetUpForOutOfContainer` | `0x52700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `UlPropSize` | `0x52710` | 127 | UnwindData |  |
| 185 | `WrapCompressedRTFStream` | `0x527A0` | 161 | UnwindData |  |
| 73 | `WrapStoreEntryID` | `0x52850` | 200 | UnwindData |  |
| 138 | `PpropFindProp` | `0x52AC0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `PropCopyMore` | `0x52B10` | 1,432 | UnwindData |  |
