# Binary Specification: ntdsapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ntdsapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2c37c40b951c8ddb510722ffb394f6c27906fcc534a13a06c7b475830b0f9674`
* **Total Exported Functions:** 131

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `DsCrackSpn2A` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackSpn2A` |
| 24 | `DsCrackSpn2W` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackSpn2W` |
| 25 | `DsCrackSpn3W` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackSpn3W` |
| 26 | `DsCrackSpn4W` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackSpn4W` |
| 27 | `DsCrackSpnA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackSpnA` |
| 28 | `DsCrackSpnW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackSpnW` |
| 29 | `DsCrackUnquotedMangledRdnA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackUnquotedMangledRdnA` |
| 30 | `DsCrackUnquotedMangledRdnW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsCrackUnquotedMangledRdnW` |
| 53 | `DsGetRdnW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsGetRdnW` |
| 59 | `DsIsMangledDnA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsIsMangledDnA` |
| 60 | `DsIsMangledDnW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsIsMangledDnW` |
| 61 | `DsIsMangledRdnValueA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsIsMangledRdnValueA` |
| 62 | `DsIsMangledRdnValueW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsIsMangledRdnValueW` |
| 79 | `DsMakeSpnA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsMakeSpnA` |
| 80 | `DsMakeSpnW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsMakeSpnW` |
| 86 | `DsQuoteRdnValueA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsQuoteRdnValueA` |
| 87 | `DsQuoteRdnValueW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsQuoteRdnValueW` |
| 119 | `DsUnquoteRdnValueA` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsUnquoteRdnValueA` |
| 120 | `DsUnquoteRdnValueW` | `0x0` | - | Forwarded | Forwarded to: `DSPARSE.DsUnquoteRdnValueW` |
| 15 | `DsBindWithSpnExWWorker` | `0x3CF0` | 179 | UnwindData |  |
| 22 | `DsCrackNamesWWorker` | `0x4130` | 1,334 | UnwindData |  |
| 38 | `DsFreeNameResultWWorker` | `0x4B30` | 22 | UnwindData |  |
| 118 | `DsUnBindWWorker` | `0x4C10` | 346 | UnwindData |  |
| 19 | `DsClientMakeSpnForTargetServerW` | `0x4D70` | 306 | UnwindData |  |
| 55 | `DsGetSpnW` | `0x50A0` | 308 | UnwindData |  |
| 102 | `DsReplicaGetInfo2W` | `0x5640` | 744 | UnwindData |  |
| 9 | `DsBindW` | `0x5930` | 41 | UnwindData |  |
| 11 | `DsBindWithCredW` | `0x5960` | 38 | UnwindData |  |
| 16 | `DsBindWithSpnW` | `0x59F0` | 40 | UnwindData |  |
| 40 | `DsFreeNgcKeyWorker` | `0x5A20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `DsServerRegisterSpnW` | `0x5A40` | 150 | UnwindData |  |
| 2 | `DsAddSidHistoryA` | `0x7000` | 514 | UnwindData |  |
| 3 | `DsAddSidHistoryW` | `0x7210` | 1,385 | UnwindData |  |
| 56 | `DsInheritSecurityIdentityA` | `0x7780` | 232 | UnwindData |  |
| 57 | `DsInheritSecurityIdentityW` | `0x7870` | 390 | UnwindData |  |
| 4 | `DsBindA` | `0x7A00` | 31 | UnwindData |  |
| 10 | `DsBindWithCredA` | `0x7A30` | 28 | UnwindData |  |
| 12 | `DsBindWithSpnA` | `0x7A60` | 30 | UnwindData |  |
| 42 | `DsFreePasswordCredentialsWorker` | `0x7A90` | 152 | UnwindData |  |
| 76 | `DsMakePasswordCredentialsA` | `0x7B30` | 320 | UnwindData |  |
| 78 | `DsMakePasswordCredentialsWWorker` | `0x7C80` | 402 | UnwindData |  |
| 116 | `DsUnBindA` | `0x7E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `DsUnBindW` | `0x7E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DsBindByInstanceA` | `0x7E40` | 416 | UnwindData |  |
| 6 | `DsBindByInstanceW` | `0x7FF0` | 65 | UnwindData |  |
| 7 | `DsBindToISTGA` | `0x8040` | 126 | UnwindData |  |
| 8 | `DsBindToISTGW` | `0x80D0` | 1,096 | UnwindData |  |
| 13 | `DsBindWithSpnExA` | `0x8520` | 323 | UnwindData |  |
| 17 | `DsBindingSetTimeout` | `0x8670` | 99 | UnwindData |  |
| 47 | `DsGetBindAddrW` | `0x86E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `DsGetBindAnnotW` | `0x8710` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `DsGetBindInstGuid` | `0x8730` | 43 | UnwindData |  |
| 20 | `DsCrackNamesA` | `0x8A60` | 1,173 | UnwindData |  |
| 36 | `DsFreeNameResultA` | `0x8F00` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `DsFreeNameResultW` | `0x8F00` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `DsFreeDomainControllerInfoA` | `0x91A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `DsFreeDomainControllerInfoW` | `0x91A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `DsFreeDomainControllerInfoWWorker` | `0x91C0` | 525 | UnwindData |  |
| 50 | `DsGetDomainControllerInfoA` | `0x93E0` | 677 | UnwindData |  |
| 52 | `DsGetDomainControllerInfoWWorker` | `0x9690` | 481 | UnwindData |  |
| 107 | `DsReplicaSyncAllA` | `0xDB90` | 164 | UnwindData |  |
| 108 | `DsReplicaSyncAllW` | `0xE200` | 46 | UnwindData |  |
| 126 | `DsaopBind` | `0xE370` | 42 | UnwindData |  |
| 127 | `DsaopBindWithCred` | `0xE3A0` | 39 | UnwindData |  |
| 128 | `DsaopBindWithSpn` | `0xE3D0` | 840 | UnwindData |  |
| 129 | `DsaopExecuteScript` | `0xE720` | 133 | UnwindData |  |
| 130 | `DsaopPrepareScript` | `0xE7B0` | 109 | UnwindData |  |
| 131 | `DsaopUnBind` | `0xE830` | 42 | UnwindData |  |
| 31 | `DsFinishDemotionW` | `0xE860` | 359 | UnwindData |  |
| 58 | `DsInitDemotionW` | `0xE9D0` | 218 | UnwindData |  |
| 91 | `DsRemoveDsDomainA` | `0xEAB0` | 265 | UnwindData |  |
| 92 | `DsRemoveDsDomainW` | `0xEBC0` | 316 | UnwindData |  |
| 93 | `DsRemoveDsServerA` | `0xED10` | 419 | UnwindData |  |
| 94 | `DsRemoveDsServerW` | `0xEEC0` | 356 | UnwindData |  |
| 100 | `DsReplicaDemotionW` | `0xF030` | 384 | UnwindData |  |
| 1 | `DsAddCloneDCW` | `0xF1C0` | 394 | UnwindData |  |
| 32 | `DsFreeCloneDcResult` | `0xF350` | 27 | UnwindData |  |
| 85 | `DsQuerySitesFree` | `0xF350` | 27 | UnwindData |  |
| 95 | `DsReplicaAddA` | `0xF380` | 320 | UnwindData |  |
| 96 | `DsReplicaAddW` | `0xF4D0` | 1,015 | UnwindData |  |
| 97 | `DsReplicaConsistencyCheck` | `0xF8D0` | 202 | UnwindData |  |
| 98 | `DsReplicaDelA` | `0xF9A0` | 192 | UnwindData |  |
| 99 | `DsReplicaDelW` | `0xFA70` | 393 | UnwindData |  |
| 101 | `DsReplicaFreeInfo` | `0xFC00` | 777 | UnwindData |  |
| 103 | `DsReplicaGetInfoW` | `0xFF10` | 48 | UnwindData |  |
| 104 | `DsReplicaModifyA` | `0xFF50` | 291 | UnwindData |  |
| 105 | `DsReplicaModifyW` | `0x10080` | 791 | UnwindData |  |
| 106 | `DsReplicaSyncA` | `0x103A0` | 112 | UnwindData |  |
| 109 | `DsReplicaSyncW` | `0x10420` | 364 | UnwindData |  |
| 110 | `DsReplicaUpdateRefsA` | `0x105A0` | 188 | UnwindData |  |
| 111 | `DsReplicaUpdateRefsW` | `0x10670` | 476 | UnwindData |  |
| 112 | `DsReplicaVerifyObjectsA` | `0x10860` | 112 | UnwindData |  |
| 113 | `DsReplicaVerifyObjectsW` | `0x108E0` | 383 | UnwindData |  |
| 43 | `DsFreeSchemaGuidMapA` | `0x10AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `DsFreeSchemaGuidMapW` | `0x10AC0` | 51 | UnwindData |  |
| 81 | `DsMapSchemaGuidsA` | `0x10B00` | 31 | UnwindData |  |
| 82 | `DsMapSchemaGuidsW` | `0x10E90` | 34 | UnwindData |  |
| 63 | `DsListDomainsInSiteA` | `0x10FB0` | 91 | UnwindData |  |
| 64 | `DsListDomainsInSiteW` | `0x11020` | 98 | UnwindData |  |
| 65 | `DsListInfoForServerA` | `0x11090` | 54 | UnwindData |  |
| 66 | `DsListInfoForServerW` | `0x110D0` | 61 | UnwindData |  |
| 67 | `DsListRolesA` | `0x11120` | 61 | UnwindData |  |
| 68 | `DsListRolesW` | `0x11170` | 68 | UnwindData |  |
| 69 | `DsListServersForDomainInSiteA` | `0x111C0` | 99 | UnwindData |  |
| 70 | `DsListServersForDomainInSiteW` | `0x11230` | 97 | UnwindData |  |
| 71 | `DsListServersInSiteA` | `0x112A0` | 54 | UnwindData |  |
| 72 | `DsListServersInSiteW` | `0x112E0` | 61 | UnwindData |  |
| 73 | `DsListSitesA` | `0x11330` | 61 | UnwindData |  |
| 74 | `DsListSitesW` | `0x11380` | 68 | UnwindData |  |
| 83 | `DsQuerySitesByCostA` | `0x113D0` | 440 | UnwindData |  |
| 84 | `DsQuerySitesByCostW` | `0x11590` | 400 | UnwindData |  |
| 18 | `DsClientMakeSpnForTargetServerA` | `0x11730` | 376 | UnwindData |  |
| 45 | `DsFreeSpnArrayA` | `0x118B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `DsFreeSpnArrayW` | `0x118C0` | 94 | UnwindData |  |
| 54 | `DsGetSpnA` | `0x11930` | 611 | UnwindData |  |
| 114 | `DsServerRegisterSpnA` | `0x11BA0` | 168 | UnwindData |  |
| 121 | `DsWriteAccountSpnA` | `0x11C50` | 339 | UnwindData |  |
| 122 | `DsWriteAccountSpnW` | `0x11DB0` | 297 | UnwindData |  |
| 14 | `DsBindWithSpnExW` | `0x12220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `DsCrackNamesW` | `0x12240` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `DsFreePasswordCredentials` | `0x12260` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `DsGetDomainControllerInfoW` | `0x12280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `DsMakePasswordCredentialsW` | `0x122A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `DsLogEntry` | `0x122C0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `DsFreeNgcKey` | `0x12420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `DsReadNgcKeyW` | `0x12440` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `DsWriteNgcKeyW` | `0x12460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `DsReadNgcKeyA` | `0x12480` | 151 | UnwindData |  |
| 90 | `DsReadNgcKeyWWorker` | `0x12520` | 289 | UnwindData |  |
| 123 | `DsWriteNgcKeyA` | `0x12650` | 151 | UnwindData |  |
| 125 | `DsWriteNgcKeyWWorker` | `0x126F0` | 236 | UnwindData |  |
