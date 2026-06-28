# Binary Specification: ntmarta.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ntmarta.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f2bfd7121052ddfa5affae30efa070ac98052d76e6a5723f31ff75171c561974`
* **Total Exported Functions:** 50

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 47 | `GetSecurityInfo` | `0x21D0` | 42 | UnwindData |  |
| 36 | `AccRewriteGetHandleRights` | `0x24D0` | 67 | UnwindData |  |
| 46 | `GetNamedSecurityInfoW` | `0x26E0` | 42 | UnwindData |  |
| 37 | `AccRewriteGetNamedRights` | `0x29F0` | 67 | UnwindData |  |
| 38 | `AccRewriteSetEntriesInAcl` | `0x3610` | 2,934 | UnwindData |  |
| 50 | `SetSecurityInfo` | `0x8110` | 505 | UnwindData |  |
| 39 | `AccRewriteSetHandleRights` | `0x8310` | 84 | UnwindData |  |
| 49 | `SetNamedSecurityInfoW` | `0x8760` | 511 | UnwindData |  |
| 40 | `AccRewriteSetNamedRights` | `0x8970` | 83 | UnwindData |  |
| 35 | `AccRewriteGetExplicitEntriesFromAcl` | `0x94F0` | 96 | UnwindData |  |
| 42 | `AccTreeResetNamedSecurityInfo` | `0x9DB0` | 4,395 | UnwindData |  |
| 48 | `SetEntriesInAclW` | `0xB360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AccGetAccessForTrustee` | `0xB370` | 315 | UnwindData |  |
| 3 | `AccConvertAccessMaskToActrlAccess` | `0xD010` | 403 | UnwindData |  |
| 12 | `AccLookupAccountName` | `0xDE60` | 944 | UnwindData |  |
| 18 | `AccProvGetCapabilities` | `0xEDB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `GetExplicitEntriesFromAclW` | `0xEDD0` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetMartaExtensionInterface` | `0xF090` | 10,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `EventGuidToName` | `0x117A0` | 151 | UnwindData |  |
| 44 | `EventNameFree` | `0x11840` | 20,496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AccConvertAccessToSD` | `0x16850` | 444 | UnwindData |  |
| 5 | `AccConvertAccessToSecurityDescriptor` | `0x16A20` | 346 | UnwindData |  |
| 6 | `AccConvertAclToAccess` | `0x16B80` | 151 | UnwindData |  |
| 7 | `AccConvertSDToAccess` | `0x16C20` | 734 | UnwindData |  |
| 10 | `AccGetExplicitEntries` | `0x16F10` | 187 | UnwindData |  |
| 13 | `AccLookupAccountSid` | `0x16FE0` | 1,073 | UnwindData |  |
| 14 | `AccLookupAccountTrustee` | `0x17420` | 283 | UnwindData |  |
| 41 | `AccSetEntriesInAList` | `0x17550` | 344 | UnwindData |  |
| 1 | `AccProvHandleGrantAccessRights` | `0x1DBA0` | 287 | UnwindData |  |
| 15 | `AccProvCancelOperation` | `0x1E240` | 133 | UnwindData |  |
| 16 | `AccProvGetAccessInfoPerObjectType` | `0x1E2D0` | 168 | UnwindData |  |
| 17 | `AccProvGetAllRights` | `0x1E380` | 522 | UnwindData |  |
| 19 | `AccProvGetOperationResults` | `0x1E590` | 372 | UnwindData |  |
| 20 | `AccProvGetTrusteesAccess` | `0x1E710` | 271 | UnwindData |  |
| 21 | `AccProvGrantAccessRights` | `0x1E830` | 391 | UnwindData |  |
| 22 | `AccProvHandleGetAccessInfoPerObjectType` | `0x1E9C0` | 245 | UnwindData |  |
| 23 | `AccProvHandleGetAllRights` | `0x1EAC0` | 404 | UnwindData |  |
| 24 | `AccProvHandleGetTrusteesAccess` | `0x1EC60` | 129 | UnwindData |  |
| 25 | `AccProvHandleIsAccessAudited` | `0x1ECF0` | 154 | UnwindData |  |
| 26 | `AccProvHandleIsObjectAccessible` | `0x1ED90` | 388 | UnwindData |  |
| 27 | `AccProvHandleRevokeAccessRights` | `0x1EF20` | 215 | UnwindData |  |
| 28 | `AccProvHandleRevokeAuditRights` | `0x1F000` | 215 | UnwindData |  |
| 29 | `AccProvHandleSetAccessRights` | `0x1F0E0` | 250 | UnwindData |  |
| 30 | `AccProvIsAccessAudited` | `0x1F1E0` | 301 | UnwindData |  |
| 31 | `AccProvIsObjectAccessible` | `0x1F320` | 1,206 | UnwindData |  |
| 32 | `AccProvRevokeAccessRights` | `0x1F7E0` | 329 | UnwindData |  |
| 33 | `AccProvRevokeAuditRights` | `0x1F930` | 329 | UnwindData |  |
| 34 | `AccProvSetAccessRights` | `0x1FA80` | 250 | UnwindData |  |
| 8 | `AccFreeIndexArray` | `0x225E0` | 291 | UnwindData |  |
| 11 | `AccGetInheritanceSource` | `0x22710` | 1,672 | UnwindData |  |
