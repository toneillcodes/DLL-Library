# Binary Specification: deviceassociation.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\deviceassociation.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6fda99c0009b88e5a1cbeca32c4c699e6349d6c626ded1a19a77652a1ba26b0d`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `DafMemFree` | `0x30A0` | 130 | UnwindData |  |
| 4 | `DafCloseAssociationContext` | `0x9190` | 151 | UnwindData |  |
| 8 | `DafCreateAssociationContext` | `0x9230` | 41 | UnwindData |  |
| 9 | `DafCreateAssociationContextForApp` | `0x9260` | 273 | UnwindData |  |
| 10 | `DafCreateAssociationContextFromOobBlob` | `0x9380` | 327 | UnwindData |  |
| 11 | `DafCreateAssociationSetContextForAep` | `0x94D0` | 220 | UnwindData |  |
| 12 | `DafCreateAssociationSetContexts` | `0x95C0` | 1,198 | UnwindData |  |
| 23 | `DafSelectCeremony` | `0x9A80` | 287 | UnwindData |  |
| 26 | `DafStartDeviceStatusNotification` | `0x9BB0` | 343 | UnwindData |  |
| 27 | `DafStartEnumCeremonies` | `0x9D10` | 386 | UnwindData |  |
| 28 | `DafStartFinalize` | `0x9EA0` | 343 | UnwindData |  |
| 30 | `DafStartReadCeremonyData` | `0xA000` | 361 | UnwindData |  |
| 31 | `DafStartRemoveAssociation` | `0xA170` | 331 | UnwindData |  |
| 32 | `DafStartWriteCeremonyData` | `0xA2D0` | 390 | UnwindData |  |
| 3 | `DafChallengeDevicePresence` | `0xA5C0` | 316 | UnwindData |  |
| 5 | `DafCloseChallengeContext` | `0xA710` | 151 | UnwindData |  |
| 13 | `DafCreateChallengeContext` | `0xA7B0` | 208 | UnwindData |  |
| 14 | `DafCreateDeviceChallengeContext` | `0xA890` | 985 | UnwindData |  |
| 15 | `DafCreateDeviceInterfaceChallengeContext` | `0xAC70` | 444 | UnwindData |  |
| 1 | `DafAepExport` | `0xB1A0` | 241 | UnwindData |  |
| 2 | `DafAepImport` | `0xB2A0` | 237 | UnwindData |  |
| 6 | `DafCloseImportExportContext` | `0xB3A0` | 151 | UnwindData |  |
| 16 | `DafCreateImportExportContext` | `0xB440` | 187 | UnwindData |  |
| 24 | `DafStartAepExport` | `0xB510` | 370 | UnwindData |  |
| 25 | `DafStartAepImport` | `0xB690` | 377 | UnwindData |  |
| 7 | `DafCloseInboundContext` | `0xBF30` | 151 | UnwindData |  |
| 17 | `DafCreateInboundContext` | `0xBFD0` | 187 | UnwindData |  |
| 19 | `DafGetInboundAssociationResultForAppActivation` | `0xC0A0` | 361 | UnwindData |  |
| 21 | `DafRegisterForInboundAssociationsAppActivation` | `0xC210` | 410 | UnwindData |  |
| 29 | `DafStartListenForInboundAssociations` | `0xC3B0` | 561 | UnwindData |  |
| 18 | `DafGenerateProvider` | `0xC740` | 586 | UnwindData |  |
| 22 | `DafRegisterProvider` | `0xC990` | 581 | UnwindData |  |
| 33 | `DafUnregisterProvider` | `0xCBE0` | 390 | UnwindData |  |
