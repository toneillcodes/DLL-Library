# Binary Specification: lsaadt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\lsaadt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0774fcb8c75bdb6ae6c0e2cffa6eafb104d296c26c26af604fb3ba42ccaf2df4`
* **Total Exported Functions:** 133

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 21 | *Ordinal Only* | `0x90D0` | 443 | UnwindData |  |
| 22 | *Ordinal Only* | `0x92A0` | 145 | UnwindData |  |
| 75 | `LsapAdtLoadPolicySecurityDescriptor` | `0x9880` | 905 | UnwindData |  |
| 84 | `LsapAdtLookupCategoryName` | `0x9C10` | 65 | UnwindData |  |
| 85 | `LsapAdtLookupSubCategoryName` | `0x9C60` | 117 | UnwindData |  |
| 93 | `LsapAdtQueryAuditPolicy` | `0x9CE0` | 762 | UnwindData |  |
| 104 | `LsapAdtSetAuditPolicy` | `0x9FE0` | 1,311 | UnwindData |  |
| 117 | `LsapAuditQueryGlobalSacl` | `0xA510` | 56 | UnwindData |  |
| 118 | `LsapAuditSetGlobalSacl` | `0xA550` | 666 | UnwindData |  |
| 125 | `LsapQueryAuditSecurity` | `0xA7F0` | 452 | UnwindData |  |
| 130 | `LsapSetAuditSecurity` | `0xA9C0` | 454 | UnwindData |  |
| 12 | *Ordinal Only* | `0xCF20` | 118 | UnwindData |  |
| 13 | *Ordinal Only* | `0xCFA0` | 124 | UnwindData |  |
| 26 | `LsapAddClaimsToAdtParamsAt` | `0xD610` | 510 | UnwindData |  |
| 30 | `LsapAdtAuditCredentialsBackupRestore` | `0xD820` | 413 | UnwindData |  |
| 31 | `LsapAdtAuditCredentialsRead` | `0xD9D0` | 464 | UnwindData |  |
| 32 | `LsapAdtAuditGroupsInToken` | `0xDBB0` | 936 | UnwindData |  |
| 33 | `LsapAdtAuditLocalSystemAccessChange` | `0xDF60` | 420 | UnwindData |  |
| 34 | `LsapAdtAuditLogoff` | `0xE110` | 294 | UnwindData |  |
| 35 | `LsapAdtAuditLogon` | `0xE240` | 238 | UnwindData |  |
| 36 | `LsapAdtAuditLogonEx` | `0xE340` | 4,245 | UnwindData |  |
| 37 | `LsapAdtAuditLogonProcessRegistration` | `0xF3E0` | 528 | UnwindData |  |
| 38 | `LsapAdtAuditPackageLoad` | `0xF600` | 453 | UnwindData |  |
| 39 | `LsapAdtAuditPerUserTableCreation` | `0xF7D0` | 351 | UnwindData |  |
| 40 | `LsapAdtAuditSidFiltration` | `0xF940` | 1,040 | UnwindData |  |
| 41 | `LsapAdtAuditSpecialPrivileges` | `0xFD60` | 610 | UnwindData |  |
| 60 | `LsapAdtGenerateDomainPolicyChangeAuditEvent` | `0xFFD0` | 479 | UnwindData |  |
| 61 | `LsapAdtGenerateLsaAuditEvent` | `0x101C0` | 325 | UnwindData |  |
| 62 | `LsapAdtGenerateLsaAuditEventWithClientSid` | `0x10310` | 162 | UnwindData |  |
| 63 | `LsapAdtGenerateLsaAuditSystemAccessChange` | `0x103C0` | 313 | UnwindData |  |
| 64 | `LsapAdtGenerateObjectOperationAuditEvent` | `0x10500` | 743 | UnwindData |  |
| 78 | `LsapAdtLogAuditFailureEvent` | `0x107F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `LsapAdtLogAuditFailureEventWithCount` | `0x10810` | 242 | UnwindData |  |
| 92 | `LsapAdtPolicyChange` | `0x10910` | 316 | UnwindData |  |
| 106 | `LsapAdtSubCategoryPolicyChange` | `0x10A60` | 1,511 | UnwindData |  |
| 107 | `LsapAdtSystemRestart` | `0x11050` | 366 | UnwindData |  |
| 111 | `LsapAdtUserRightAssigned` | `0x111D0` | 605 | UnwindData |  |
| 116 | `LsapAuditLogonHelper` | `0x11440` | 844 | UnwindData |  |
| 120 | `LsapFreeClaimsInAdtParams` | `0x117A0` | 96 | UnwindData |  |
| 121 | `LsapFreeClaimsInfoFromToken` | `0x11810` | 66 | UnwindData |  |
| 123 | `LsapGetClaimsInToken` | `0x11860` | 801 | UnwindData |  |
| 129 | `LsapReserveSlotsForClaims` | `0x11B90` | 426 | UnwindData |  |
| 71 | `LsapAdtInitializeExtensibleAuditing` | `0x129E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `LsapAdtRegisterSecurityEventSource` | `0x12A20` | 760 | UnwindData |  |
| 102 | `LsapAdtReportSecurityEvent` | `0x12D20` | 647 | UnwindData |  |
| 103 | `LsapAdtRundownSecurityEventSource` | `0x12FB0` | 173 | UnwindData |  |
| 108 | `LsapAdtUnregisterSecurityEventSource` | `0x13070` | 66 | UnwindData |  |
| 11 | *Ordinal Only* | `0x136D0` | 480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `LsapAdtInitGenericAudits` | `0x138B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `LsapGenAuditEvent` | `0x138F0` | 614 | UnwindData |  |
| 126 | `LsapRegisterAuditEvent` | `0x13B60` | 121 | UnwindData |  |
| 132 | `LsapUnregisterAuditEvent` | `0x13BE0` | 59 | UnwindData |  |
| 69 | `LsapAdtInitialize` | `0x13C30` | 1,172 | UnwindData |  |
| 70 | `LsapAdtInitializeCrashOnAuditFail` | `0x140D0` | 622 | UnwindData |  |
| 72 | `LsapAdtInitializePerUserAuditingAndSD` | `0x14350` | 121 | UnwindData |  |
| 73 | `LsapAdtInitializeSpecialGroupsLogon` | `0x143D0` | 180 | UnwindData |  |
| 74 | `LsapAdtInitializeSpecializedProcessing` | `0x14490` | 168 | UnwindData |  |
| 89 | `LsapAdtOpenLog` | `0x15C90` | 542 | UnwindData |  |
| 1 | *Ordinal Only* | `0x15EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `LsapAdtWriteLogEx` | `0x15ED0` | 378 | UnwindData |  |
| 114 | `LsapAdtWriteLogWrkr` | `0x16050` | 68 | UnwindData |  |
| 119 | `LsapFlushSecurityLog` | `0x160A0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `LsapReportClaimsAtLogonEvent` | `0x16400` | 947 | UnwindData |  |
| 128 | `LsapReportGroupsAtLogonEvent` | `0x167C0` | 1,422 | UnwindData |  |
| 27 | `LsapAdtApplyGlobalSaclUpdate` | `0x16E40` | 215 | UnwindData |  |
| 28 | `LsapAdtApplyOldPublicPolicyOnStorage` | `0x16F20` | 166 | UnwindData |  |
| 29 | `LsapAdtApplySystemPolicyUpdates` | `0x16FD0` | 146 | UnwindData |  |
| 42 | `LsapAdtAuditingEnabledByLogonId` | `0x17070` | 195 | UnwindData |  |
| 43 | `LsapAdtAuditingEnabledByPolicy` | `0x17140` | 91 | UnwindData |  |
| 44 | `LsapAdtAuditingEnabledBySid` | `0x171B0` | 195 | UnwindData |  |
| 45 | `LsapAdtAuditingEnabledBySubCategory` | `0x17280` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `LsapAdtAuditingEnabledHint` | `0x172C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `LsapAdtAuditingEnabledHintByCategory` | `0x17300` | 173 | UnwindData |  |
| 50 | `LsapAdtConvertAuditPolicyToCurrentFormat` | `0x173C0` | 155 | UnwindData |  |
| 51 | `LsapAdtConvertSystemPolicyFromStorageToOldPublicFormat` | `0x17470` | 484 | UnwindData |  |
| 52 | `LsapAdtConvertTokenPolicyToStorageFormat` | `0x17660` | 176 | UnwindData |  |
| 53 | `LsapAdtCreateDefaultPolicy` | `0x17720` | 355 | UnwindData |  |
| 54 | `LsapAdtCreateEmptyPolicy` | `0x17890` | 78 | UnwindData |  |
| 56 | `LsapAdtDowngradeAuditPolicy` | `0x178F0` | 288 | UnwindData |  |
| 76 | `LsapAdtLoadProcessCreationParameters` | `0x17A20` | 173 | UnwindData |  |
| 86 | `LsapAdtMergeAuditPolicyOptions` | `0x17AE0` | 204 | UnwindData |  |
| 88 | `LsapAdtNotifySpecializedProcessingChange` | `0x17BC0` | 36 | UnwindData |  |
| 91 | `LsapAdtOpenSpecializedProcessingAuditingKey` | `0x17BF0` | 187 | UnwindData |  |
| 110 | `LsapAdtUpgradeAuditPolicy` | `0x17CC0` | 578 | UnwindData |  |
| 112 | `LsapAdtValidateAuditingPolicyInformation` | `0x17F10` | 155 | UnwindData |  |
| 3 | *Ordinal Only* | `0x17FC0` | 196 | UnwindData |  |
| 133 | `LsapUpdateSamAuditPolicy` | `0x18090` | 201 | UnwindData |  |
| 48 | `LsapAdtConstructPolicyPerUserAuditing` | `0x18160` | 261 | UnwindData |  |
| 49 | `LsapAdtConstructTablePerUserAuditing` | `0x18270` | 1,408 | UnwindData |  |
| 55 | `LsapAdtDecrementCountersPerUserAuditing` | `0x18800` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `LsapAdtEnumeratePerUserAuditing` | `0x18840` | 447 | UnwindData |  |
| 58 | `LsapAdtFilterAdminPerUserAuditing` | `0x18A10` | 325 | UnwindData |  |
| 59 | `LsapAdtFreeTablePerUserAuditing` | `0x18B60` | 115 | UnwindData |  |
| 80 | `LsapAdtLogoffPerUserAuditing` | `0x18BE0` | 151 | UnwindData |  |
| 82 | `LsapAdtLogonIncrementPerUserAuditing` | `0x18C80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `LsapAdtLogonPerUserAuditing` | `0x18CC0` | 304 | UnwindData |  |
| 90 | `LsapAdtOpenPerUserAuditingKey` | `0x18E00` | 110 | UnwindData |  |
| 94 | `LsapAdtQueryFullPerUserAuditingByLuid` | `0x18E80` | 26 | UnwindData |  |
| 95 | `LsapAdtQueryFullPerUserAuditingBySid` | `0x18EA0` | 26 | UnwindData |  |
| 96 | `LsapAdtQueryPerUserAuditingByLuid` | `0x18EC0` | 247 | UnwindData |  |
| 97 | `LsapAdtQueryPerUserAuditingBySid` | `0x18FC0` | 314 | UnwindData |  |
| 98 | `LsapAdtQuerySpecificPerUserAuditingByLuid` | `0x19100` | 28 | UnwindData |  |
| 99 | `LsapAdtQuerySpecificPerUserAuditingBySid` | `0x19130` | 28 | UnwindData |  |
| 101 | `LsapAdtRemoveLuidQueryPerUserAuditing` | `0x19160` | 155 | UnwindData |  |
| 105 | `LsapAdtStorePolicyByLuidPerUserAuditing` | `0x19210` | 254 | UnwindData |  |
| 109 | `LsapAdtUpdatePerUserCache` | `0x19320` | 416 | UnwindData |  |
| 115 | `LsapAdtWritePerUserPolicyToStore` | `0x194D0` | 343 | UnwindData |  |
| 65 | `LsapAdtGenerateSpecialGroupsLogonAudit` | `0x19B40` | 1,520 | UnwindData |  |
| 77 | `LsapAdtLoadSpecialGroups` | `0x1A140` | 863 | UnwindData |  |
| 87 | `LsapAdtNotifySpecialGroupLogonChange` | `0x1A4B0` | 27 | UnwindData |  |
| 20 | *Ordinal Only* | `0x1A4E0` | 83 | UnwindData |  |
| 16 | *Ordinal Only* | `0x1A540` | 352 | UnwindData |  |
| 24 | *Ordinal Only* | `0x1A6B0` | 113 | UnwindData |  |
| 14 | *Ordinal Only* | `0x1A790` | 292 | UnwindData |  |
| 15 | *Ordinal Only* | `0x1A930` | 305 | UnwindData |  |
| 23 | *Ordinal Only* | `0x1AA70` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | *Ordinal Only* | `0x1AAF0` | 196 | UnwindData |  |
| 17 | *Ordinal Only* | `0x1ABC0` | 342 | UnwindData |  |
| 19 | *Ordinal Only* | `0x1AD20` | 196 | UnwindData |  |
| 25 | *Ordinal Only* | `0x1ADF0` | 27 | UnwindData |  |
| 2 | *Ordinal Only* | `0x1AF50` | 405 | UnwindData |  |
| 67 | `LsapAdtInitParametersArray` | `0x1B0F0` | 49 | UnwindData |  |
| 68 | `LsapAdtInitParametersArrayWorker` | `0x1B130` | 823 | UnwindData |  |
| 81 | `LsapAdtLogonHoursSize` | `0x1B470` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `LsapGetImageNameFromProcessId` | `0x1B4B0` | 343 | UnwindData |  |
| 5 | *Ordinal Only* | `0x1B610` | 614 | UnwindData |  |
| 4 | *Ordinal Only* | `0x1B880` | 111 | UnwindData |  |
| 131 | `LsapStringListSize` | `0x1B900` | 83,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | *Ordinal Only* | `0x30010` | 4,768 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | *Ordinal Only* | `0x312B0` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | *Ordinal Only* | `0x315F0` | 1,128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | *Ordinal Only* | `0x31A58` | 332 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | *Ordinal Only* | `0x31BA4` | 0 | Indeterminate |  |
