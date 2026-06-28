# Binary Specification: lsaadt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\lsaadt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1a797c2fdfa2c01e6d8502539a79c426cf149e4cc8f1330b4cb87165f65997b9`
* **Total Exported Functions:** 133

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | *Ordinal Only* | `0x9010` | 443 | UnwindData |  |
| 22 | *Ordinal Only* | `0x91E0` | 145 | UnwindData |  |
| 75 | `LsapAdtLoadPolicySecurityDescriptor` | `0x97C0` | 905 | UnwindData |  |
| 84 | `LsapAdtLookupCategoryName` | `0x9B50` | 65 | UnwindData |  |
| 85 | `LsapAdtLookupSubCategoryName` | `0x9BA0` | 117 | UnwindData |  |
| 93 | `LsapAdtQueryAuditPolicy` | `0x9C20` | 762 | UnwindData |  |
| 104 | `LsapAdtSetAuditPolicy` | `0x9F20` | 1,311 | UnwindData |  |
| 117 | `LsapAuditQueryGlobalSacl` | `0xA450` | 56 | UnwindData |  |
| 118 | `LsapAuditSetGlobalSacl` | `0xA490` | 666 | UnwindData |  |
| 125 | `LsapQueryAuditSecurity` | `0xA730` | 452 | UnwindData |  |
| 130 | `LsapSetAuditSecurity` | `0xA900` | 454 | UnwindData |  |
| 12 | *Ordinal Only* | `0xD5F0` | 118 | UnwindData |  |
| 13 | *Ordinal Only* | `0xD670` | 124 | UnwindData |  |
| 26 | `LsapAddClaimsToAdtParamsAt` | `0xDF30` | 510 | UnwindData |  |
| 30 | `LsapAdtAuditCredentialsBackupRestore` | `0xE140` | 413 | UnwindData |  |
| 31 | `LsapAdtAuditCredentialsRead` | `0xE2F0` | 464 | UnwindData |  |
| 32 | `LsapAdtAuditGroupsInToken` | `0xE4D0` | 936 | UnwindData |  |
| 33 | `LsapAdtAuditLocalSystemAccessChange` | `0xE880` | 420 | UnwindData |  |
| 34 | `LsapAdtAuditLogoff` | `0xEA30` | 294 | UnwindData |  |
| 35 | `LsapAdtAuditLogon` | `0xEB60` | 238 | UnwindData |  |
| 36 | `LsapAdtAuditLogonEx` | `0xEC60` | 4,245 | UnwindData |  |
| 37 | `LsapAdtAuditLogonProcessRegistration` | `0xFD00` | 528 | UnwindData |  |
| 38 | `LsapAdtAuditPackageLoad` | `0xFF20` | 453 | UnwindData |  |
| 39 | `LsapAdtAuditPerUserTableCreation` | `0x100F0` | 351 | UnwindData |  |
| 40 | `LsapAdtAuditSidFiltration` | `0x10260` | 1,040 | UnwindData |  |
| 41 | `LsapAdtAuditSpecialPrivileges` | `0x10680` | 610 | UnwindData |  |
| 60 | `LsapAdtGenerateDomainPolicyChangeAuditEvent` | `0x108F0` | 479 | UnwindData |  |
| 61 | `LsapAdtGenerateLsaAuditEvent` | `0x10AE0` | 325 | UnwindData |  |
| 62 | `LsapAdtGenerateLsaAuditEventWithClientSid` | `0x10C30` | 162 | UnwindData |  |
| 63 | `LsapAdtGenerateLsaAuditSystemAccessChange` | `0x10CE0` | 313 | UnwindData |  |
| 64 | `LsapAdtGenerateObjectOperationAuditEvent` | `0x10E20` | 743 | UnwindData |  |
| 78 | `LsapAdtLogAuditFailureEvent` | `0x11110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `LsapAdtLogAuditFailureEventWithCount` | `0x11130` | 242 | UnwindData |  |
| 92 | `LsapAdtPolicyChange` | `0x11230` | 316 | UnwindData |  |
| 106 | `LsapAdtSubCategoryPolicyChange` | `0x11380` | 1,511 | UnwindData |  |
| 107 | `LsapAdtSystemRestart` | `0x11970` | 366 | UnwindData |  |
| 111 | `LsapAdtUserRightAssigned` | `0x11AF0` | 605 | UnwindData |  |
| 116 | `LsapAuditLogonHelper` | `0x11D60` | 844 | UnwindData |  |
| 120 | `LsapFreeClaimsInAdtParams` | `0x120C0` | 96 | UnwindData |  |
| 121 | `LsapFreeClaimsInfoFromToken` | `0x12130` | 66 | UnwindData |  |
| 123 | `LsapGetClaimsInToken` | `0x12180` | 801 | UnwindData |  |
| 129 | `LsapReserveSlotsForClaims` | `0x124B0` | 426 | UnwindData |  |
| 71 | `LsapAdtInitializeExtensibleAuditing` | `0x13300` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `LsapAdtRegisterSecurityEventSource` | `0x13340` | 760 | UnwindData |  |
| 102 | `LsapAdtReportSecurityEvent` | `0x13640` | 647 | UnwindData |  |
| 103 | `LsapAdtRundownSecurityEventSource` | `0x138D0` | 173 | UnwindData |  |
| 108 | `LsapAdtUnregisterSecurityEventSource` | `0x13990` | 66 | UnwindData |  |
| 11 | *Ordinal Only* | `0x13FF0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `LsapAdtInitGenericAudits` | `0x141D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `LsapGenAuditEvent` | `0x14210` | 614 | UnwindData |  |
| 126 | `LsapRegisterAuditEvent` | `0x14480` | 121 | UnwindData |  |
| 132 | `LsapUnregisterAuditEvent` | `0x14500` | 59 | UnwindData |  |
| 69 | `LsapAdtInitialize` | `0x14550` | 1,172 | UnwindData |  |
| 70 | `LsapAdtInitializeCrashOnAuditFail` | `0x149F0` | 622 | UnwindData |  |
| 72 | `LsapAdtInitializePerUserAuditingAndSD` | `0x14C70` | 121 | UnwindData |  |
| 73 | `LsapAdtInitializeSpecialGroupsLogon` | `0x14CF0` | 180 | UnwindData |  |
| 74 | `LsapAdtInitializeSpecializedProcessing` | `0x14DB0` | 168 | UnwindData |  |
| 89 | `LsapAdtOpenLog` | `0x165B0` | 542 | UnwindData |  |
| 1 | *Ordinal Only* | `0x167E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `LsapAdtWriteLogEx` | `0x167F0` | 378 | UnwindData |  |
| 114 | `LsapAdtWriteLogWrkr` | `0x16970` | 68 | UnwindData |  |
| 119 | `LsapFlushSecurityLog` | `0x169C0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `LsapReportClaimsAtLogonEvent` | `0x16D20` | 947 | UnwindData |  |
| 128 | `LsapReportGroupsAtLogonEvent` | `0x170E0` | 1,422 | UnwindData |  |
| 27 | `LsapAdtApplyGlobalSaclUpdate` | `0x17760` | 215 | UnwindData |  |
| 28 | `LsapAdtApplyOldPublicPolicyOnStorage` | `0x17840` | 166 | UnwindData |  |
| 29 | `LsapAdtApplySystemPolicyUpdates` | `0x178F0` | 146 | UnwindData |  |
| 42 | `LsapAdtAuditingEnabledByLogonId` | `0x17990` | 195 | UnwindData |  |
| 43 | `LsapAdtAuditingEnabledByPolicy` | `0x17A60` | 91 | UnwindData |  |
| 44 | `LsapAdtAuditingEnabledBySid` | `0x17AD0` | 195 | UnwindData |  |
| 45 | `LsapAdtAuditingEnabledBySubCategory` | `0x17BA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LsapAdtAuditingEnabledHint` | `0x17BE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `LsapAdtAuditingEnabledHintByCategory` | `0x17C20` | 173 | UnwindData |  |
| 50 | `LsapAdtConvertAuditPolicyToCurrentFormat` | `0x17CE0` | 155 | UnwindData |  |
| 51 | `LsapAdtConvertSystemPolicyFromStorageToOldPublicFormat` | `0x17D90` | 484 | UnwindData |  |
| 52 | `LsapAdtConvertTokenPolicyToStorageFormat` | `0x17F80` | 176 | UnwindData |  |
| 53 | `LsapAdtCreateDefaultPolicy` | `0x18040` | 355 | UnwindData |  |
| 54 | `LsapAdtCreateEmptyPolicy` | `0x181B0` | 78 | UnwindData |  |
| 56 | `LsapAdtDowngradeAuditPolicy` | `0x18210` | 288 | UnwindData |  |
| 76 | `LsapAdtLoadProcessCreationParameters` | `0x18340` | 173 | UnwindData |  |
| 86 | `LsapAdtMergeAuditPolicyOptions` | `0x18400` | 204 | UnwindData |  |
| 88 | `LsapAdtNotifySpecializedProcessingChange` | `0x184E0` | 36 | UnwindData |  |
| 91 | `LsapAdtOpenSpecializedProcessingAuditingKey` | `0x18510` | 187 | UnwindData |  |
| 110 | `LsapAdtUpgradeAuditPolicy` | `0x185E0` | 578 | UnwindData |  |
| 112 | `LsapAdtValidateAuditingPolicyInformation` | `0x18830` | 155 | UnwindData |  |
| 3 | *Ordinal Only* | `0x188E0` | 196 | UnwindData |  |
| 133 | `LsapUpdateSamAuditPolicy` | `0x189B0` | 201 | UnwindData |  |
| 48 | `LsapAdtConstructPolicyPerUserAuditing` | `0x18A80` | 261 | UnwindData |  |
| 49 | `LsapAdtConstructTablePerUserAuditing` | `0x18B90` | 1,408 | UnwindData |  |
| 55 | `LsapAdtDecrementCountersPerUserAuditing` | `0x19120` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `LsapAdtEnumeratePerUserAuditing` | `0x19160` | 447 | UnwindData |  |
| 58 | `LsapAdtFilterAdminPerUserAuditing` | `0x19330` | 325 | UnwindData |  |
| 59 | `LsapAdtFreeTablePerUserAuditing` | `0x19480` | 115 | UnwindData |  |
| 80 | `LsapAdtLogoffPerUserAuditing` | `0x19500` | 151 | UnwindData |  |
| 82 | `LsapAdtLogonIncrementPerUserAuditing` | `0x195A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `LsapAdtLogonPerUserAuditing` | `0x195E0` | 304 | UnwindData |  |
| 90 | `LsapAdtOpenPerUserAuditingKey` | `0x19720` | 110 | UnwindData |  |
| 94 | `LsapAdtQueryFullPerUserAuditingByLuid` | `0x197A0` | 26 | UnwindData |  |
| 95 | `LsapAdtQueryFullPerUserAuditingBySid` | `0x197C0` | 26 | UnwindData |  |
| 96 | `LsapAdtQueryPerUserAuditingByLuid` | `0x197E0` | 247 | UnwindData |  |
| 97 | `LsapAdtQueryPerUserAuditingBySid` | `0x198E0` | 314 | UnwindData |  |
| 98 | `LsapAdtQuerySpecificPerUserAuditingByLuid` | `0x19A20` | 28 | UnwindData |  |
| 99 | `LsapAdtQuerySpecificPerUserAuditingBySid` | `0x19A50` | 28 | UnwindData |  |
| 101 | `LsapAdtRemoveLuidQueryPerUserAuditing` | `0x19A80` | 155 | UnwindData |  |
| 105 | `LsapAdtStorePolicyByLuidPerUserAuditing` | `0x19B30` | 254 | UnwindData |  |
| 109 | `LsapAdtUpdatePerUserCache` | `0x19C40` | 416 | UnwindData |  |
| 115 | `LsapAdtWritePerUserPolicyToStore` | `0x19DF0` | 343 | UnwindData |  |
| 65 | `LsapAdtGenerateSpecialGroupsLogonAudit` | `0x1A460` | 1,520 | UnwindData |  |
| 77 | `LsapAdtLoadSpecialGroups` | `0x1AA60` | 863 | UnwindData |  |
| 87 | `LsapAdtNotifySpecialGroupLogonChange` | `0x1ADD0` | 27 | UnwindData |  |
| 20 | *Ordinal Only* | `0x1AE00` | 83 | UnwindData |  |
| 16 | *Ordinal Only* | `0x1AE60` | 352 | UnwindData |  |
| 24 | *Ordinal Only* | `0x1AFD0` | 113 | UnwindData |  |
| 14 | *Ordinal Only* | `0x1B0B0` | 292 | UnwindData |  |
| 15 | *Ordinal Only* | `0x1B250` | 305 | UnwindData |  |
| 23 | *Ordinal Only* | `0x1B390` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | *Ordinal Only* | `0x1B410` | 196 | UnwindData |  |
| 17 | *Ordinal Only* | `0x1B4E0` | 342 | UnwindData |  |
| 19 | *Ordinal Only* | `0x1B640` | 196 | UnwindData |  |
| 25 | *Ordinal Only* | `0x1B710` | 27 | UnwindData |  |
| 2 | *Ordinal Only* | `0x1B870` | 405 | UnwindData |  |
| 67 | `LsapAdtInitParametersArray` | `0x1BA10` | 49 | UnwindData |  |
| 68 | `LsapAdtInitParametersArrayWorker` | `0x1BA50` | 823 | UnwindData |  |
| 81 | `LsapAdtLogonHoursSize` | `0x1BD90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `LsapGetImageNameFromProcessId` | `0x1BDD0` | 343 | UnwindData |  |
| 5 | *Ordinal Only* | `0x1BF30` | 614 | UnwindData |  |
| 4 | *Ordinal Only* | `0x1C1A0` | 111 | UnwindData |  |
| 131 | `LsapStringListSize` | `0x1C220` | 81,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | *Ordinal Only* | `0x30010` | 4,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | *Ordinal Only* | `0x31320` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | *Ordinal Only* | `0x31660` | 1,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | *Ordinal Only* | `0x31AC8` | 372 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | *Ordinal Only* | `0x31C3C` | 0 | Indeterminate |  |
