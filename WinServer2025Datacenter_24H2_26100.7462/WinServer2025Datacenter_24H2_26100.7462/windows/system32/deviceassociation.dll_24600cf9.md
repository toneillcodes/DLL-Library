# Binary Specification: deviceassociation.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\deviceassociation.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `24600cf92919c2e595ee040fff8d80ca9de267e3ee58882722eda10f22d222fe`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `DafMemFree` | `0x30A0` | 130 | UnwindData |  |
| 4 | `DafCloseAssociationContext` | `0x9180` | 151 | UnwindData |  |
| 8 | `DafCreateAssociationContext` | `0x9220` | 41 | UnwindData |  |
| 9 | `DafCreateAssociationContextForApp` | `0x9250` | 273 | UnwindData |  |
| 10 | `DafCreateAssociationContextFromOobBlob` | `0x9370` | 327 | UnwindData |  |
| 11 | `DafCreateAssociationSetContextForAep` | `0x94C0` | 220 | UnwindData |  |
| 12 | `DafCreateAssociationSetContexts` | `0x95B0` | 1,198 | UnwindData |  |
| 23 | `DafSelectCeremony` | `0x9A70` | 287 | UnwindData |  |
| 26 | `DafStartDeviceStatusNotification` | `0x9BA0` | 343 | UnwindData |  |
| 27 | `DafStartEnumCeremonies` | `0x9D00` | 386 | UnwindData |  |
| 28 | `DafStartFinalize` | `0x9E90` | 343 | UnwindData |  |
| 30 | `DafStartReadCeremonyData` | `0x9FF0` | 361 | UnwindData |  |
| 31 | `DafStartRemoveAssociation` | `0xA160` | 331 | UnwindData |  |
| 32 | `DafStartWriteCeremonyData` | `0xA2C0` | 390 | UnwindData |  |
| 3 | `DafChallengeDevicePresence` | `0xA5B0` | 316 | UnwindData |  |
| 5 | `DafCloseChallengeContext` | `0xA700` | 151 | UnwindData |  |
| 13 | `DafCreateChallengeContext` | `0xA7A0` | 208 | UnwindData |  |
| 14 | `DafCreateDeviceChallengeContext` | `0xA880` | 985 | UnwindData |  |
| 15 | `DafCreateDeviceInterfaceChallengeContext` | `0xAC60` | 444 | UnwindData |  |
| 1 | `DafAepExport` | `0xB190` | 241 | UnwindData |  |
| 2 | `DafAepImport` | `0xB290` | 237 | UnwindData |  |
| 6 | `DafCloseImportExportContext` | `0xB390` | 151 | UnwindData |  |
| 16 | `DafCreateImportExportContext` | `0xB430` | 187 | UnwindData |  |
| 24 | `DafStartAepExport` | `0xB500` | 370 | UnwindData |  |
| 25 | `DafStartAepImport` | `0xB680` | 377 | UnwindData |  |
| 7 | `DafCloseInboundContext` | `0xBF20` | 151 | UnwindData |  |
| 17 | `DafCreateInboundContext` | `0xBFC0` | 187 | UnwindData |  |
| 19 | `DafGetInboundAssociationResultForAppActivation` | `0xC090` | 361 | UnwindData |  |
| 21 | `DafRegisterForInboundAssociationsAppActivation` | `0xC200` | 410 | UnwindData |  |
| 29 | `DafStartListenForInboundAssociations` | `0xC3A0` | 561 | UnwindData |  |
| 18 | `DafGenerateProvider` | `0xC730` | 586 | UnwindData |  |
| 22 | `DafRegisterProvider` | `0xC980` | 581 | UnwindData |  |
| 33 | `DafUnregisterProvider` | `0xCBD0` | 390 | UnwindData |  |
